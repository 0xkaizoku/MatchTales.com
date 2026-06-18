#!/usr/bin/env python3
"""
MatchTales Backend API Test Suite
Tests all backend endpoints for the MatchTales World Cup 2026 app
"""
import requests
import sys
import time
from datetime import datetime

# Handle Windows emoji stdout printing
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

class MatchTalesAPITester:
    def __init__(self, base_url="https://whycare-fc.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []

    def log_result(self, test_name, passed, expected, actual, details=""):
        """Log test result"""
        self.tests_run += 1
        if passed:
            self.tests_passed += 1
        
        result = {
            "test": test_name,
            "passed": passed,
            "expected": expected,
            "actual": actual,
            "details": details
        }
        self.test_results.append(result)
        
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"\n{status} - {test_name}")
        if not passed:
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")
            if details:
                print(f"  Details: {details}")

    def run_test(self, name, method, endpoint, expected_status, data=None, params=None):
        """Run a single API test"""
        url = f"{self.base_url}{endpoint}"
        headers = {'Content-Type': 'application/json'}

        print(f"\n🔍 Testing {name}...")
        print(f"   {method} {endpoint}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers, timeout=10)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=10)

            success = response.status_code == expected_status
            
            try:
                response_data = response.json()
            except:
                response_data = response.text

            self.log_result(
                name,
                success,
                f"Status {expected_status}",
                f"Status {response.status_code}",
                str(response_data)[:200]
            )

            return success, response_data, response.status_code

        except requests.exceptions.Timeout:
            self.log_result(name, False, f"Status {expected_status}", "Timeout", "Request timed out after 10s")
            return False, {}, 0
        except Exception as e:
            self.log_result(name, False, f"Status {expected_status}", "Exception", str(e))
            return False, {}, 0

    def test_root(self):
        """Test API root endpoint"""
        success, data, status = self.run_test(
            "API Root",
            "GET",
            "/api/",
            200
        )
        if success and isinstance(data, dict):
            if data.get('service') == 'matchtales':
                print("   ✓ Service identifier correct")
            else:
                print(f"   ⚠ Unexpected service: {data.get('service')}")
        return success

    def test_newsletter_valid_email(self):
        """Test newsletter subscription with valid email"""
        test_email = f"test_{int(time.time())}@example.com"
        success, data, status = self.run_test(
            "Newsletter - Valid Email",
            "POST",
            "/api/newsletter",
            200,
            data={"email": test_email, "name": "Test User"}
        )
        if success and isinstance(data, dict):
            if data.get('ok') and not data.get('already'):
                print("   ✓ New subscription successful")
                return test_email
            else:
                print(f"   ⚠ Unexpected response: {data}")
        return None

    def test_newsletter_duplicate_email(self, email):
        """Test newsletter subscription with duplicate email"""
        success, data, status = self.run_test(
            "Newsletter - Duplicate Email",
            "POST",
            "/api/newsletter",
            200,
            data={"email": email}
        )
        if success and isinstance(data, dict):
            if data.get('already') == True:
                print("   ✓ Duplicate detection working")
                return True
            else:
                print(f"   ⚠ Expected already=True, got: {data}")
        return False

    def test_newsletter_invalid_email(self):
        """Test newsletter subscription with invalid email"""
        success, data, status = self.run_test(
            "Newsletter - Invalid Email",
            "POST",
            "/api/newsletter",
            422,
            data={"email": "not-an-email"}
        )
        if success:
            print("   ✓ Invalid email rejected correctly")
        return success

    def test_hype_note_create(self):
        """Test creating a hype note"""
        success, data, status = self.run_test(
            "Hype Note - Create",
            "POST",
            "/api/hype-notes",
            200,
            data={
                "name": "Test Fan",
                "text": "This is a test hype note for the match!",
                "matchSlug": "test-match",
                "matchLabel": "Test vs Match"
            }
        )
        if success and isinstance(data, dict):
            note_id = data.get('id')
            if note_id:
                print(f"   ✓ Note created with ID: {note_id}")
                return note_id
            else:
                print(f"   ⚠ No ID in response: {data}")
        return None

    def test_hype_note_with_url(self):
        """Test creating a hype note with URL (should fail)"""
        success, data, status = self.run_test(
            "Hype Note - With URL (should fail)",
            "POST",
            "/api/hype-notes",
            400,
            data={
                "name": "Spammer",
                "text": "Check out http://spam.com for more info!"
            }
        )
        if success:
            print("   ✓ URL in text rejected correctly")
        return success

    def test_hype_note_too_short(self):
        """Test creating a hype note with text too short"""
        success, data, status = self.run_test(
            "Hype Note - Too Short (should fail)",
            "POST",
            "/api/hype-notes",
            422,
            data={
                "name": "Test",
                "text": "Hi"
            }
        )
        if success:
            print("   ✓ Short text rejected correctly")
        return success

    def test_hype_notes_list(self):
        """Test listing hype notes"""
        success, data, status = self.run_test(
            "Hype Notes - List",
            "GET",
            "/api/hype-notes",
            200,
            params={"limit": 30}
        )
        if success and isinstance(data, list):
            print(f"   ✓ Retrieved {len(data)} notes")
            return True
        return False

    def test_hype_notes_filter_by_match(self):
        """Test filtering hype notes by matchSlug"""
        success, data, status = self.run_test(
            "Hype Notes - Filter by Match",
            "GET",
            "/api/hype-notes",
            200,
            params={"matchSlug": "england-vs-croatia-md2", "limit": 30}
        )
        if success and isinstance(data, list):
            print(f"   ✓ Retrieved {len(data)} notes for match")
            # Verify all notes have the correct matchSlug
            if data:
                all_match = all(note.get('matchSlug') == 'england-vs-croatia-md2' for note in data)
                if all_match:
                    print("   ✓ All notes match the filter")
                else:
                    print("   ⚠ Some notes don't match the filter")
            return True
        return False

    def test_hype_note_like(self, note_id):
        """Test liking a hype note"""
        if not note_id:
            print("\n⚠️  Skipping like test - no note ID available")
            return False
        
        success, data, status = self.run_test(
            "Hype Note - Like",
            "POST",
            f"/api/hype-notes/{note_id}/like",
            200
        )
        if success and isinstance(data, dict):
            likes = data.get('likes', 0)
            print(f"   ✓ Note now has {likes} like(s)")
            return True
        return False

    def test_live_scores(self):
        """Test live scores endpoint (Football-Data.org proxy)"""
        success, data, status = self.run_test(
            "Live Scores - Competitions",
            "GET",
            "/api/live-scores",
            200
        )
        if success and isinstance(data, dict):
            competitions = data.get('competitions', [])
            if isinstance(competitions, list):
                print(f"   ✓ Retrieved {len(competitions)} competitions")
                if competitions:
                    print(f"   ✓ Sample: {competitions[0].get('name', 'N/A')}")
                return True
            else:
                print(f"   ⚠ Unexpected competitions format: {type(competitions)}")
        return False

    def test_poll_vote(self):
        """Test poll voting"""
        test_slug = "test-match-poll"
        success, data, status = self.run_test(
            "Poll - Vote (home)",
            "POST",
            "/api/poll/vote",
            200,
            data={
                "matchSlug": test_slug,
                "option": "home"
            }
        )
        if success and isinstance(data, dict):
            votes = data.get('votes', {})
            if 'home' in votes:
                print(f"   ✓ Vote recorded. Home votes: {votes.get('home', 0)}")
                return test_slug
            else:
                print(f"   ⚠ Unexpected votes format: {votes}")
        return None

    def test_poll_results(self, match_slug):
        """Test getting poll results"""
        if not match_slug:
            print("\n⚠️  Skipping poll results test - no match slug available")
            return False
        
        success, data, status = self.run_test(
            "Poll - Get Results",
            "GET",
            f"/api/poll/{match_slug}",
            200
        )
        if success and isinstance(data, dict):
            votes = data.get('votes', {})
            total = votes.get('home', 0) + votes.get('draw', 0) + votes.get('away', 0)
            print(f"   ✓ Total votes: {total} (home: {votes.get('home', 0)}, draw: {votes.get('draw', 0)}, away: {votes.get('away', 0)})")
            return True
        return False

    def test_poll_invalid_option(self):
        """Test poll voting with invalid option"""
        success, data, status = self.run_test(
            "Poll - Invalid Option (should fail)",
            "POST",
            "/api/poll/vote",
            400,
            data={
                "matchSlug": "test-match",
                "option": "invalid"
            }
        )
        if success:
            print("   ✓ Invalid option rejected correctly")
        return success

    def run_all_tests(self):
        """Run all backend tests"""
        print("=" * 70)
        print("MatchTales Backend API Test Suite")
        print("=" * 70)
        print(f"Base URL: {self.base_url}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)

        # Test API root
        self.test_root()

        # Newsletter tests
        print("\n" + "=" * 70)
        print("NEWSLETTER TESTS")
        print("=" * 70)
        email = self.test_newsletter_valid_email()
        if email:
            time.sleep(0.5)
            self.test_newsletter_duplicate_email(email)
        self.test_newsletter_invalid_email()

        # Hype notes tests
        print("\n" + "=" * 70)
        print("HYPE NOTES TESTS")
        print("=" * 70)
        note_id = self.test_hype_note_create()
        time.sleep(0.5)
        self.test_hype_note_with_url()
        self.test_hype_note_too_short()
        self.test_hype_notes_list()
        self.test_hype_notes_filter_by_match()
        if note_id:
            time.sleep(0.5)
            self.test_hype_note_like(note_id)

        # Live scores test
        print("\n" + "=" * 70)
        print("LIVE SCORES TESTS")
        print("=" * 70)
        self.test_live_scores()

        # Poll tests
        print("\n" + "=" * 70)
        print("POLL TESTS")
        print("=" * 70)
        match_slug = self.test_poll_vote()
        if match_slug:
            time.sleep(0.5)
            self.test_poll_results(match_slug)
        self.test_poll_invalid_option()

        # Print summary
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print(f"Total tests run: {self.tests_run}")
        print(f"Tests passed: {self.tests_passed}")
        print(f"Tests failed: {self.tests_run - self.tests_passed}")
        print(f"Success rate: {(self.tests_passed / self.tests_run * 100):.1f}%")
        print("=" * 70)

        # Print failed tests
        failed_tests = [r for r in self.test_results if not r['passed']]
        if failed_tests:
            print("\n❌ FAILED TESTS:")
            for test in failed_tests:
                print(f"\n  • {test['test']}")
                print(f"    Expected: {test['expected']}")
                print(f"    Actual: {test['actual']}")
                if test['details']:
                    print(f"    Details: {test['details'][:150]}")

        return 0 if self.tests_passed == self.tests_run else 1

def main():
    base_url = "https://whycare-fc.preview.emergentagent.com"
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    tester = MatchTalesAPITester(base_url=base_url)
    exit_code = tester.run_all_tests()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
