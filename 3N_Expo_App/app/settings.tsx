import React, { useState, useEffect } from "react";
import { Text, View, StyleSheet, Button } from "react-native";
import { Tabs } from "expo-router";
import { Stack } from 'expo-router/stack';
import { Image } from 'expo-image';
import * as Battery from 'expo-battery';


export default function Settings() {
  const [batteryLevel, setBatteryLevel] = useState<number | null>(null);

  const BatteryStatus = () => {
  
    useEffect(() => {
      const fetchBatteryLevel = async () => {
        const level = await Battery.getBatteryLevelAsync();
        setBatteryLevel(level);
      };
  
      fetchBatteryLevel();
  
      const subscription = Battery.addBatteryLevelListener(({ batteryLevel }) => {
        setBatteryLevel(batteryLevel);
      });
  
      return () => {
        subscription.remove();
      };
    }, []);
  };
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Home Screen</Text>
      <Text style={styles.header}>Battery Status</Text>
        <Text style={styles.batteryLevel}>
          {batteryLevel !== null ? `${(batteryLevel * 100).toFixed(0)}%` : 'Loading...'}
        </Text>
      <Image
        style={styles.image}
        source="assets/images/SmartGlassesDemo.jpeg"
        alt="Smart Glasses Device"
        contentFit="contain"
        transition={1000}
      />
      <Button title="Connect to Glasses" onPress={() => {}} />
      <Button title="Language Settings" onPress={() => {}} />
      <Button title="Select Model" onPress={() => {}} />
      <Button title="Live Feed" onPress={() => {}} />
      <Button title="Custom Commands" onPress={() => {}} />
      <Button title="WiFi Settings" onPress={() => {}} />
      <Button title="Voice Commands" onPress={() => {}} />
      <Button title="Battery Status" onPress={() => {}} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  header: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  batteryLevel: {
    fontSize: 18,
    textAlign: 'center',
    margin: 10,
  },
  image: {
    flex: 1,
    width: '100%',
    backgroundColor: '#0553',
  },
});