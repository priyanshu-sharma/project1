# Yelp Dataset

## Documentation

Link - https://www.yelp.com/dataset/documentation/main

## Dataset

Link - https://www.yelp.com/dataset

## Components of the Yelp Dataset:

1. Business Data:

Information about businesses including name, address, coordinates, categories, hours of operation, and attributes (e.g., wheelchair accessible, accepts credit cards).

2. Review Data:

User reviews of businesses, including the review text, star rating, date, and votes for usefulness, funny, and cool.

3. User Data:

Information about users who write reviews, including user ID, name, review count, average star rating, and various other user activity statistics.

4. Check-in Data:

Information about check-ins at businesses, which can be used to analyze foot traffic trends.

5. Photo Data:

Photos associated with businesses, including the photo ID, business ID, and labels.

## Schemas

### Business

Contains business data including location data, attributes, and categories.

```
{
    // string, 22 character unique string business id
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg",

    // string, the business's name
    "name": "Garaje",

    // string, the full address of the business
    "address": "475 3rd St",

    // string, the city
    "city": "San Francisco",

    // string, 2 character state code, if applicable
    "state": "CA",

    // string, the postal code
    "postal code": "94107",

    // float, latitude
    "latitude": 37.7817529521,

    // float, longitude
    "longitude": -122.39612197,

    // float, star rating, rounded to half-stars
    "stars": 4.5,

    // integer, number of reviews
    "review_count": 1198,

    // integer, 0 or 1 for closed or open, respectively
    "is_open": 1,

    // object, business attributes to values. note: some attribute values might be objects
    "attributes": {
        "RestaurantsTakeOut": true,
        "BusinessParking": {
            "garage": false,
            "street": true,
            "validated": false,
            "lot": false,
            "valet": false
        },
    },

    // an array of strings of business categories
    "categories": [
        "Mexican",
        "Burgers",
        "Gastropubs"
    ],

    // an object of key day to value hours, hours are using a 24hr clock
    "hours": {
        "Monday": "10:00-21:00",
        "Tuesday": "10:00-21:00",
        "Friday": "10:00-21:00",
        "Wednesday": "10:00-21:00",
        "Thursday": "10:00-21:00",
        "Sunday": "11:00-18:00",
        "Saturday": "10:00-21:00"
    }
}
```

### Review

Contains full review text data including the user_id that wrote the review and the business_id the review is written for.

```
{
    // string, 22 character unique review id
    "review_id": "zdSx_SD6obEhz9VrW9uAWA",

    // string, 22 character unique user id, maps to the user in user.json
    "user_id": "Ha3iJu77CxlrFm-vQRs_8g",

    // string, 22 character business id, maps to business in business.json
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg",

    // integer, star rating
    "stars": 4,

    // string, date formatted YYYY-MM-DD
    "date": "2016-03-09",

    // string, the review itself
    "text": "Great place to hang out after work: the prices are decent, and the ambience is fun. It's a bit loud, but very lively. The staff is friendly, and the food is good. They have a good selection of drinks.",

    // integer, number of useful votes received
    "useful": 0,

    // integer, number of funny votes received
    "funny": 0,

    // integer, number of cool votes received
    "cool": 0
}
```

### User

User data including the user's friend mapping and all the metadata associated with the user.

```
{
    // string, 22 character unique user id, maps to the user in user.json
    "user_id": "Ha3iJu77CxlrFm-vQRs_8g",

    // string, the user's first name
    "name": "Sebastien",

    // integer, the number of reviews they've written
    "review_count": 56,

    // string, when the user joined Yelp, formatted like YYYY-MM-DD
    "yelping_since": "2011-01-01",

    // array of strings, an array of the user's friend as user_ids
    "friends": [
        "wqoXYLWmpkEH0YvTmHBsJQ",
        "KUXLLiJGrjtSsapmxmpvTA",
        "6e9rJKQC3n0RSKyHLViL-Q"
    ],

    // integer, number of useful votes sent by the user
    "useful": 21,

    // integer, number of funny votes sent by the user
    "funny": 88,

    // integer, number of cool votes sent by the user
    "cool": 15,

    // integer, number of fans the user has
    "fans": 1032,

    // array of integers, the years the user was elite
    "elite": [
        2012,
        2013
    ],

    // float, average rating of all reviews
    "average_stars": 4.31,

    // integer, number of hot compliments received by the user
    "compliment_hot": 339,

    // integer, number of more compliments received by the user
    "compliment_more": 668,

    // integer, number of profile compliments received by the user
    "compliment_profile": 42,

    // integer, number of cute compliments received by the user
    "compliment_cute": 62,

    // integer, number of list compliments received by the user
    "compliment_list": 37,

    // integer, number of note compliments received by the user
    "compliment_note": 356,

    // integer, number of plain compliments received by the user
    "compliment_plain": 68,

    // integer, number of cool compliments received by the user
    "compliment_cool": 91,

    // integer, number of funny compliments received by the user
    "compliment_funny": 99,

    // integer, number of writer compliments received by the user
    "compliment_writer": 95,

    // integer, number of photo compliments received by the user
    "compliment_photos": 50
}
```

### Checkin 

Checkins on a business.

```
{
    // string, 22 character business id, maps to business in business.json
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg"

    // string which is a comma-separated list of timestamps for each checkin, each with format YYYY-MM-DD HH:MM:SS
    "date": "2016-04-26 19:49:16, 2016-08-30 18:36:57, 2016-10-15 02:45:18, 2016-11-18 01:54:50, 2017-04-20 18:39:06, 2017-05-03 17:58:02"
}
```

### Tip

Tips written by a user on a business. Tips are shorter than reviews and tend to convey quick suggestions.

```
{
    // string, text of the tip
    "text": "Secret menu - fried chicken sando is da bombbbbbb Their zapatos are good too.",

    // string, when the tip was written, formatted like YYYY-MM-DD
    "date": "2013-09-20",

    // integer, how many compliments it has
    "compliment_count": 172,

    // string, 22 character business id, maps to business in business.json
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg",

    // string, 22 character unique user id, maps to the user in user.json
    "user_id": "49JhAJh8vSQ-vM4Aourl0g"
}
```

### Photo

Contains photo data including the caption and classification (one of "food", "drink", "menu", "inside" or "outside").

```
{
    // string, 22 character unique photo id
    "photo_id": "_nN_DhLXkfwEkwPNxne9hw",
    // string, 22 character business id, maps to business in business.json
    "business_id" : "tnhfDv5Il8EaGSXZGiuQGg",
    // string, the photo caption, if any
    "caption" : "carne asada fries",
    // string, the category the photo belongs to, if any
    "label" : "food"
}
```

## Business Metrics

1. Customer Metrics:

```
1. Average Rating: Average star rating for a business.
2. Review Count: Total number of reviews a business has received.
3. Sentiment Analysis: Overall sentiment derived from review text (positive, negative, neutral).
4. Review Distribution: Distribution of star ratings (e.g., how many 1-star, 2-star, etc. reviews).
5. Customer Demographics: Information about the reviewers (age, location, review count, etc.).
```
2. Operational Metrics:

```
1. Business Hours: Hours of operation and patterns of busy times.
2. Check-ins: Number of check-ins over time, indicating foot traffic and peak times.
3. Service Attributes: Analysis of business attributes (e.g., delivery options, wheelchair accessibility).
```

3. Performance Metrics:

```
1. Review Velocity: Rate at which new reviews are received over time.
2. Rating Trends: Changes in average rating over time.
3. Top Keywords: Frequent keywords and phrases in reviews that indicate common praises or complaints.
4. Year-over-Year Growth: Changes in review count, ratings, and check-ins over time.
5. Review Length: Average length of reviews, which can indicate the level of detail and customer effort in providing feedback.
```

4. Competitive Metrics:

```
1. Category Performance: Comparison of ratings and review counts within business categories.
2. Market Position: Relative performance compared to competitors in the same area or category.
3. Customer Loyalty: Analysis of repeat reviews and long-term customer engagement.
4. Geographical Analysis: Performance metrics broken down by location (city, neighborhood) to identify regional trends.
5. Competitor Ratings and Reviews: Tracking competitors' ratings and reviews to benchmark performance.
6. Market Share: Estimating market share within a category or region based on review count and check-ins.
```

5. Financial Metrics:

```
1. Price Range: Analysis of the price level and its correlation with ratings and reviews.
2. Value for Money: Customer perception of value based on review content.
```

6. Geographical Metrics:

```
1. Location Analysis: Performance based on geographical location, including trends in different areas.
2. Heatmaps: Visualization of customer activity and business density in different regions.
```

7. Engagement Metrics:

```
1. Useful/Funny/Cool Votes: Engagement levels of reviews based on user votes.
2. Response Rate: Analysis of business responses to reviews (if available).
3. Review Frequency: The rate at which new reviews are being posted over time. Indicates current customer engagement.
4. Check-ins: Number of check-ins at a business location. Shows foot traffic and customer visits.
```

8. Customer Demographics:

```
1. User Activity: Analyzing user data to understand the demographics and behavior patterns of reviewers.
2. Top Reviewers: Identifying users who contribute the most reviews and their impact on business ratings.
```

9. Photo Engagement:

```
1. Photo Count and Quality: Number of photos posted and their quality (labels, user votes) to assess visual engagement.
2. Photo Sentiment: Sentiment analysis of photo labels and comments.
```

10. User Loyalty:

```
1. Repeat Reviews: Tracking the number of repeat reviews from the same users to measure customer loyalty.
```

## Note - I will select any of the 5-6 different metrics to track.