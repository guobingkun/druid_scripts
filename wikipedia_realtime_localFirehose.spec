[
  {
    "dataSchema": {
      "dataSource": "wikipedia_index_test",
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
        "segmentGranularity": "HOUR",
        "queryGranularity": "second"
      },
      "parser": {
        "type": "string",
        "parseSpec": {
          "format": "json",
          "timestampSpec": {
            "column": "time",
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
        "type": "local",
        "filter": "wikiticker-2015-09-12-sampled_0.json",
        "baseDir": "/Users/guobingkun/Documents/tmp/wikipedia_play"
      },
      "plumber": {
        "type": "realtime"
      }
    },
    "tuningConfig": {
      "type": "realtime",
      "maxRowsInMemory": 500000,
      "intermediatePersistPeriod": "PT30m",
      "windowPeriod": "PT1m",
      "basePersistDirectory": "/tmp/realtime/basePersist_0",
      "rejectionPolicy": {
        "type": "none"
      },
      "shardSpec": {
        "type": "linear",
        "partitionNum": 0
      }
    }
  },
  {
    "dataSchema": {
      "dataSource": "wikipedia_index_test",
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
        "segmentGranularity": "HOUR",
        "queryGranularity": "second"
      },
      "parser": {
        "type": "string",
        "parseSpec": {
          "format": "json",
          "timestampSpec": {
            "column": "time",
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
        "type": "local",
        "filter": "wikiticker-2015-09-12-sampled_1.json",
        "baseDir": "/Users/guobingkun/Documents/tmp/wikipedia_play"
      },
      "plumber": {
        "type": "realtime"
      }
    },
    "tuningConfig": {
      "type": "realtime",
      "maxRowsInMemory": 500000,
      "intermediatePersistPeriod": "PT30m",
      "windowPeriod": "PT1m",
      "basePersistDirectory": "/tmp/realtime/basePersist_1",
      "rejectionPolicy": {
        "type": "none"
      },
      "shardSpec": {
        "type": "linear",
        "partitionNum": 1
      }
    }
  }
]