# OpenCage API Reference

## OpenCage API Reference for Reverse Geocoding

### Reverse Geocoding

**Endpoint:** `https://api.opencagedata.com/geocode/v1/json?`

**Parameters:**

- `key`: Your API key
- `q`: A comma-separated string representing the latitude and longitude coordinates. Use `.`, not `,`.

**Response:**

```
{
  "documentation": "https://opencagedata.com/api",
  "licenses": [
    {
      "name": "see attribution guide",
      "url": "https://opencagedata.com/credits"
    }
  ],
  "rate": {
    "limit": 2500,
    "remaining": 2499,
    "reset": 1725494400
  },
  "results": [
    {
      "annotations": {
        "DMS": {
          "lat": "37° 46' 29.81316'' N",
          "lng": "122° 25' 9.98076'' W"
        },
        "FIPS": {
          "state": "06"
        },
        "MGRS": "10SEG5112781004",
        "Maidenhead": "CM87ss95qx",
        "Mercator": {
          "x": -13627669.624,
          "y": 4521505.245
        },
        "OSM": {
          "edit_url": "https://www.openstreetmap.org/edit?way=228228520#map=17/37.77495/-122.41944",
          "note_url": "https://www.openstreetmap.org/note/new#map=17/37.77495/-122.41944&layers=N",
          "url": "https://www.openstreetmap.org/?mlat=37.77495&mlon=-122.41944#map=17/37.77495/-122.41944"
        },
        "UN_M49": {
          "regions": {
            "AMERICAS": "019",
            "NORTHERN_AMERICA": "021",
            "US": "840",
            "WORLD": "001"
          },
          "statistical_groupings": [
            "MEDC"
          ]
        },
        "callingcode": 1,
        "currency": {
          "alternate_symbols": [
            "US$"
          ],
          "decimal_mark": ".",
          "disambiguate_symbol": "US$",
          "html_entity": "$",
          "iso_code": "USD",
          "iso_numeric": "840",
          "name": "United States Dollar",
          "smallest_denomination": 1,
          "subunit": "Cent",
          "subunit_to_unit": 100,
          "symbol": "$",
          "symbol_first": 1,
          "thousands_separator": ","
        },
        "flag": "🇺🇸",
        "geohash": "9q8yyk8zh2dnev2rh2p5",
        "qibla": 18.84,
        "roadinfo": {
          "drive_on": "right",
          "road": "Market Street",
          "road_type": "primary",
          "speed_in": "mph"
        },
        "sun": {
          "rise": {
            "apparent": 1725457440,
            "astronomical": 1725452040,
            "civil": 1725455880,
            "nautical": 1725453960
          },
          "set": {
            "apparent": 1725417120,
            "astronomical": 1725422520,
            "civil": 1725418680,
            "nautical": 1725420600
          }
        },
        "timezone": {
          "name": "America/Los_Angeles",
          "now_in_dst": 1,
          "offset_sec": -25200,
          "offset_string": "-0700",
          "short_name": "PDT"
        },
        "what3words": {
          "words": "oppose.noses.wells"
        }
      },
      "bounds": {
        "northeast": {
          "lat": 37.77502,
          "lng": -122.4193403
        },
        "southwest": {
          "lat": 37.7746586,
          "lng": -122.4197953
        }
      },
      "components": {
        "ISO_3166-1_alpha-2": "US",
        "ISO_3166-1_alpha-3": "USA",
        "ISO_3166-2": [
          "US-CA"
        ],
        "_category": "road",
        "_normalized_city": "San Francisco",
        "_type": "road",
        "city": "San Francisco",
        "continent": "North America",
        "country": "United States",
        "country_code": "us",
        "neighbourhood": "Hayes Valley",
        "postcode": "94199",
        "road": "Market Street",
        "road_type": "primary",
        "state": "California",
        "state_code": "CA"
      },
      "confidence": 9,
      "distance_from_q": {
        "meters": 6
      },
      "formatted": "Market Street, San Francisco, CA 94199, United States of America",
      "geometry": {
        "lat": 37.7749481,
        "lng": -122.4194391
      }
    }
  ],
  "status": {
    "code": 200,
    "message": "OK"
  },
  "stay_informed": {
    "blog": "https://blog.opencagedata.com",
    "mastodon": "https://en.osm.town/@opencage"
  },
  "thanks": "For using an OpenCage API",
  "timestamp": {
    "created_http": "Wed, 04 Sep 2024 22:14:48 GMT",
    "created_unix": 1725488088
  },
  "total_results": 1
}
```

---
