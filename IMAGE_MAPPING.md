# Image URL to Demographics Mapping Guide

This document helps you verify that each image URL matches the correct demographic profile.

## How to Verify Images

1. Open each URL in a browser
2. Check if the person's appearance matches the race/age specified
3. Update the URL in `stimuly.py` if it doesn't match

## Male Profiles - Required Demographics

| Index | Profile ID | Age | Race | Current URL Photo ID | Status |
|-------|------------|-----|------|---------------------|--------|
| 0 | m1 | 24 | White | photo-1507003211169-0a1dd7228f2d | ⚠️ Verify |
| 1 | m2 | 25 | Black | photo-1506277886164-e25aa3f4ef7f | ⚠️ Verify |
| 2 | m3 | 26 | Asian | photo-1506794778202-cad84cf45f1d | ⚠️ Verify |
| 3 | m4 | 27 | Latino | photo-1500648767791-00dcc994a43e | ⚠️ Verify |
| 4 | m5 | 28 | White | photo-1507591064344-4c6ce005b128 | ⚠️ Verify |
| 5 | m6 | 29 | Mixed Race | photo-1472099645785-5658abf4ff4e | ⚠️ Verify |
| 6 | m7 | 30 | Black | photo-1519085360753-af0119f7cbe7 | ⚠️ Verify |
| 7 | m8 | 31 | Asian | photo-1521119989659-a83eee488004 | ⚠️ Verify |
| 8 | m9 | 24 | Latino | photo-1508341591423-4347099e1f19 | ⚠️ Verify |
| 9 | m10 | 25 | Other | photo-1519345182560-3f2917c472ef | ⚠️ Verify |

## Female Profiles - Required Demographics

| Index | Profile ID | Age | Race | Current URL Photo ID | Status |
|-------|------------|-----|------|---------------------|--------|
| 0 | w1 | 24 | White | photo-1494790108377-be9c29b29330 | ⚠️ Verify |
| 1 | w2 | 25 | Black | photo-1531123897727-8f129e1688ce | ⚠️ Verify |
| 2 | w3 | 26 | Asian | photo-1531746020798-e6953c6e8e04 | ⚠️ Verify |
| 3 | w4 | 27 | Latino | photo-1544005313-94ddf0286df2 | ⚠️ Verify |
| 4 | w5 | 28 | White | photo-1438761681033-6461ffad8d80 | ⚠️ Verify |
| 5 | w6 | 29 | Mixed Race | photo-1488426862026-3ee34a7d66df | ⚠️ Verify |
| 6 | w7 | 30 | Black | photo-1508214751196-bcfd4ca60f91 | ⚠️ Verify |
| 7 | w8 | 31 | Asian | photo-1529626455594-4ff0802cfb7e | ⚠️ Verify |
| 8 | w9 | 24 | Latino | photo-1487412720507-e7ab37603c6f | ⚠️ Verify |
| 9 | w10 | 25 | Other | photo-1534528741775-53994a69daeb | ⚠️ Verify |

## How to Find Matching Images on Unsplash

### For Men:
- White men: https://unsplash.com/s/photos/portrait-white-man
- Black men: https://unsplash.com/s/photos/portrait-black-man
- Asian men: https://unsplash.com/s/photos/portrait-asian-man
- Latino/Hispanic men: https://unsplash.com/s/photos/portrait-latino-man

### For Women:
- White women: https://unsplash.com/s/photos/portrait-white-woman
- Black women: https://unsplash.com/s/photos/portrait-black-woman
- Asian women: https://unsplash.com/s/photos/portrait-asian-woman
- Latino/Hispanic women: https://unsplash.com/s/photos/portrait-latino-woman

### Steps to Get Correct Image URL:
1. Go to the appropriate Unsplash search page above
2. Find an image that matches the age and race
3. Click on the image
4. Right-click the image → "Copy image address"
5. Add `?w=400&h=400&fit=crop&crop=faces` to the end of the URL
6. Replace the URL in `stimuly.py` at the corresponding index

## Alternative: Use This Person Does Not Exist Style Services

For more control over demographics, consider:
- **Generated Photos**: https://generated.photos/ (has demographic filters)
- **This Person Does Not Exist**: https://thispersondoesnotexist.com/ (random, but diverse)
- **Pexels**: https://www.pexels.com/search/portrait/ (has diverse collections)

## Important Notes

- All images must be free to use (Unsplash, Pexels licenses)
- Images should look professional and appropriate for dating profiles
- Age should appear to be in the 20s-30s range
- Race/ethnicity should clearly match the specified demographic


