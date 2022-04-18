import React, { Component } from 'react';

import { AppointmentPicker } from 'react-appointment-picker';

export default class App extends Component {
  state = {
    loading: false,
    continuousLoading: false
  };

  addAppointmentCallback = ({
    addedAppointment: { day, number, time, id },
    addCb
  }) => {
    this.setState(
      {
        loading: true
      },
      async () => {
        await new Promise((resolve) => setTimeout(resolve, 2000));
        console.log(
          `Added appointment ${number}, day ${day}, time ${time}, id ${id}`
        );
        addCb(day, number, time, id);
        this.setState({ loading: false });
      }
    );
  };

  removeAppointmentCallback = ({ day, number, time, id }, removeCb) => {
    this.setState(
      {
        loading: true
      },
      async () => {
        await new Promise((resolve) => setTimeout(resolve, 2000));
        console.log(
          `Removed appointment ${number}, day ${day}, time ${time}, id ${id}`
        );
        removeCb(day, number);
        this.setState({ loading: false });
      }
    );
  };

  render() {
    const days = [
      [
        { id: 1, number: 1, isReserved: true },
        { id: 2, number: 2 },
        { id: 3, number: 3 },
        { id: 4, number: 4 },
        { id: 5, number: 5 },
        { id: 6, number: 6 },
        { id: 7, number: 7 },
        { id: 8, number: 8 },
      ],
      [
        { id: 9, number: 1 },
        { id: 10, number: 2 },
        { id: 11, number: 3 },
        { id: 12, number: 4 },
        { id: 13, number: 5 },
        { id: 14, number: 6 },
        { id: 15, number: 7 },
        { id: 16, number: 8 },
      ],
      [
        { id: 17, number: 1 },
        { id: 18, number: 2 },
        { id: 19, number: 3 },
        { id: 20, number: 4 },
        { id: 21, number: 5 },
        { id: 22, number: 6 },
        { id: 23, number: 7 },
        { id: 24, number: 8 }
      ],
      [
        { id: 25, number: 1 },
        { id: 26, number: 2 },
        { id: 27, number: 3 },
        { id: 28, number: 4 },
        { id: 29, number: 5 },
        { id: 30, number: 6 },
        { id: 31, number: 7 },
        { id: 32, number: 8 }
      ],
      [
        { id: 33, number: 1 },
        { id: 34, number: 2 },
        { id: 35, number: 3 },
        { id: 36, number: 4 },
        { id: 37, number: 5 },
        { id: 38, number: 6 },
        { id: 39, number: 7 },
        { id: 40, number: 8 }
      ],
      [
        { id: 41, number: 1 },
        { id: 42, number: 2 },
        { id: 43, number: 3 },
        { id: 44, number: 4 },
        { id: 45, number: 5 },
        { id: 46, number: 6 },
        { id: 47, number: 7 },
        { id: 48, number: 8 }
      ],
      [
        { id: 49, number: 1 },
        { id: 50, number: 2 },
        { id: 51, number: 3 },
        { id: 52, number: 4 },
        { id: 53, number: 5 },
        { id: 54, number: 6 },
        { id: 55, number: 7 },
        { id: 56, number: 8 }
      ]
    ];
    const { loading, continuousLoading } = this.state;
    return (
      <div>
        <h1>Appointment</h1>
        <AppointmentPicker
          addAppointmentCallback={this.addAppointmentCallback}
          removeAppointmentCallback={this.removeAppointmentCallback}
          initialDay={new Date('2021-11-06 09:00:00')}
          days={days}
          maxReservableAppointments={1}
          alpha
          visible
          selectedByDefault
          loading={loading}
          continuousLoading={continuousLoading}
          unitTime='3600000'
        />
      </div>
    );
  }
}
