import json
import subprocess


new_cdata='{"input": {"data": {"SensorMetaInfo": {"CameraDescription": "cisco_cam_type_1", "Ly": "20.98S", "Lx": "10.233N", "FeatureId": "9", "ServerId": "vijaywada_PC_01", "ProductCategoryId": "2", "CameraID": "akashwani_east", "LongDescription": "high range camera"}, "Data": {"CongressionThreshold": "20.0%", "ImageURL": "/home/anuj/git/work/end-to-end-api/hyderabad/deputy-01/vehicle-counter/output/2018-10-17/images/vehicle_counter_08:36:58.jpg", "Vehicles": {"AreaOccupied": "34.0%", "BikeCount": 2, "MiniBusCount": 0, "CarCount": 1, "ReportedTime": "2018-02-26t10:23:51", "HeavyVehicleCount": 0}, "VideoURL": "http://<ip-address>/video-analytics/hyderabad/akashwani_east/vehicle_counter/output/videos/2018_02_26_10_23_11_video.mp4", "CapturedTime": "2018-10-17 08:36:58.041400"}, "Event": {"EventID": 11, "EventDescription": "Threshold Congestion Exceeded"}}}, "configName": "Congestion", "groupName": "TrafficAnalytics", "tenantId": "vijayawada.com"}'
subprocess.call(["curl", "-X", "POST", "https://vijayawadaie.quantela.com/ie-portal/api/v1/source/getInputData", "-H", "Content-Type: application/json", "-H", "tenantId:vijayawada.com", "-H", "x-access-token: 4IHW1663X1XX6IUW13MLPGF3Q62FIOBI", "-d", json.dumps(new_cdata)])


