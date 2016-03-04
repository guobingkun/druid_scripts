[{
  "dataSchema": {
    "dataSource": "wikipedia_index_test_chelsea",
    "metricsSpec": [
      {
        "type": "count",
        "name": "count"
      },
      {
        "type": "doubleSum",
        "name": "added",
        "fieldName": "added"
      },
      {
        "type": "doubleSum",
        "name": "deleted",
        "fieldName": "deleted"
      },
      {
        "type": "doubleSum",
        "name": "delta",
        "fieldName": "delta"
      }
    ],
    "granularitySpec": {
      "segmentGranularity": "DAY",
      "queryGranularity": "second"
    },
    "parser": {
      "type": "map",
      "parseSpec": {
        "columns": [
          "timestamp",
          "page",
          "language",
          "user",
          "unpatrolled",
          "newPage",
          "robot",
          "anonymous",
          "namespace",
          "continent",
          "country",
          "region",
          "city",
          "added",
          "deleted",
          "delta"
        ],
        "timestampSpec": {
          "column": "timestamp",
          "format": "iso"
        },
        "dimensionsSpec": {
          "dimensions": [
            "page",
            "language",
            "user",
            "unpatrolled",
            "newPage",
            "robot",
            "anonymous",
            "namespace",
            "continent",
            "country",
            "region",
            "city"
          ]
        }
      }
    }
  },
  "ioConfig": {
    "type": "realtime",
    "firehose": {
      "type": "receiver",
      "serviceName": "chelsea",
      "bufferSize": 200000
    },
    "plumber": {
      "type": "realtime"
    }
  },
  "tuningConfig": {
    "type": "realtime",
    "maxRowsInMemory": 500000,
    "intermediatePersistPeriod": "PT10m",
    "windowPeriod": "PT10m",
    "basePersistDirectory": "\/tmp\/realtime\/basePersist",
    "rejectionPolicy": {
      "type": "serverTime"
    }
  }
},
{
  "dataSchema": {
    "dataSource": "wikipedia_index_test_bingkun",
    "metricsSpec": [
      {
        "type": "count",
        "name": "count"
      },
      {
        "type": "doubleSum",
        "name": "added",
        "fieldName": "added"
      },
      {
        "type": "doubleSum",
        "name": "deleted",
        "fieldName": "deleted"
      },
      {
        "type": "doubleSum",
        "name": "delta",
        "fieldName": "delta"
      }
    ],
    "granularitySpec": {
      "segmentGranularity": "DAY",
      "queryGranularity": "second"
    },
    "parser": {
      "type": "map",
      "parseSpec": {
        "columns": [
          "timestamp",
          "page",
          "language",
          "user",
          "unpatrolled",
          "newPage",
          "robot",
          "anonymous",
          "namespace",
          "continent",
          "country",
          "region",
          "city",
          "added",
          "deleted",
          "delta"
        ],
        "timestampSpec": {
          "column": "timestamp",
          "format": "iso"
        },
        "dimensionsSpec": {
          "dimensions": [
            "page",
            "language",
            "user",
            "unpatrolled",
            "newPage",
            "robot",
            "anonymous",
            "namespace",
            "continent",
            "country",
            "region",
            "city"
          ]
        }
      }
    }
  },
  "ioConfig": {
    "type": "realtime",
    "firehose": {
      "type": "receiver",
      "serviceName": "bingkun",
      "bufferSize": 333333
    },
    "plumber": {
      "type": "realtime"
    }
  },
  "tuningConfig": {
    "type": "realtime",
    "maxRowsInMemory": 500000,
    "intermediatePersistPeriod": "PT1m",
    "windowPeriod": "PT1m",
    "basePersistDirectory": "\/tmp\/realtime\/basePersist",
    "rejectionPolicy": {
      "type": "serverTime"
    }
  }
}
]

