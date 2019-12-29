import React from 'react';
import Group from './Group';
import HeadersManager from './HeadersManager';

const classNames = require('classnames');

class GroupManager extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      groups: [
        <Group
          key={1}
          number={1}
          day={'Mon'}
          time={'6:00 - 7:00'}
          campus={'North'}
          room={'BBB 1670'}
          level={'Grad'}
        />,
        <Group
          key={2}
          number={2}
          day={'Tues'}
          time={'7:00 - 8:00'}
          campus={'Central'}
          room={'NQ 1500'}
          level={'UG'}
        />,
      ],
    };
    this.fetchGroups = this.fetchGroups.bind(this);
  }

  fetchGroups(fetchURL) {
    fetch(fetchURL, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        const groups = [];
        data.groups.forEach((group) => {
          const newGroup = <Group {...group} />;
          groups.push(newGroup);
        });
        this.setState({
          groups,
        });
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  render() {
    const className = classNames('Manager', { hidden: !this.props.focused });

    // TODO: change to get this from data
    // column headers for each member
    const groupHeaders = ['Number', 'Day', 'Time', 'Campus', 'Room', 'UG/Grad'];
    return (
      <section
        className={className}
        id="GroupManager"
        aria-labelledby="GroupTag"
      >
        <HeadersManager headers={groupHeaders} currentSort={'Number'} />
        <ul id="GroupList">
          {this.state.groups}
        </ul>
      </section>
    );
  }
}

export default GroupManager;
