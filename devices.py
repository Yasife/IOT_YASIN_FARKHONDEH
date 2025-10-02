class Device:
    import paho.mqtt.client as mqtt
    import RPi.GPIO as GPIO  
  
    def __init__(self,location,group,device_type,device_name,pin):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name
        self.status='off'
        self.mqtt_broker='fuhgoihtpoih'
        self.port = 37362  
        self.mqtt_client=pin
        self.connect_mqtt()
        self.setup_gpio()
      
  def turn_on(self):
        print('Done!!!')
        self.status='on'
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')
 
    def turn_off(self):
        print('Done!!!')
        self.status='off'
        mqtt.publish(self.mqtt_client,self.device_name,'TURN OFF')
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
    def connect_mqtt(self):
        mqtt.connect(self.mqtt_broker,self.port)
        
        
    def setup_gpio(self):
        
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
          
        elif self.device_type=='camera':
          GPIO.setup(38,GPIO.OUT)
          
class Sensor:
    
    def __init__(self,location,group,sensor_name,sensor_type,pin):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        self.pin=pin
      
    def read_data(self):
        humidity,temeprature=Adafruiy_DHT.read_retry(Adafruiy_DHT.DHT22,self.pin)
        
        return temeprature

l1 = Device('office', 'living_room', 'lamps', 'l1')
cam1 = Device('home', 'room1', 'cameras', 'cam1')
s1= Sensor('home', 'kitchen', 'termo', 's1')
