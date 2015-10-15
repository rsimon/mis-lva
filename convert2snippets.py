import json

with open('coins.json') as f:
    data = json.load(f)
    outputForTimeline = open('coins-with-time.json.txt', 'w')
    outputForMap = open('coins-with-coordinates.json.txt', 'w')

    for item in data['items']:
        converted = {
          'title': item['title'],
          'provider': item['dataset_path'][0]['title'],
          'homepage': item['homepage'],
          'image_urls': item['depictions'],
          'geo_bounds': {
              'min_lon': item['geo_bounds']['min_lon'],
              'max_lon': item['geo_bounds']['max_lon'],
              'min_lat': item['geo_bounds']['min_lat'],
              'max_lat': item['geo_bounds']['max_lat']
          }
        }

        if 'temporal_bounds' in item:
            converted['temporal_bounds'] = { 'from': item['temporal_bounds']['start'], 'to': item['temporal_bounds']['end'] }
            outputForTimeline.write(json.dumps(converted))
            outputForTimeline.write('\n')

        outputForMap.write(json.dumps(converted))
        outputForMap.write('\n')

    outputForTimeline.close()
    outputForMap.close()
