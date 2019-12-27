import React from 'react';
import Group from './Group';

const classNames = require('classnames');

class GroupManager extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      groups: [<Group key={1} />],
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
    return (
      <section
        className={className}
        id="GroupManager"
        aria-labelledby="GroupTag"
      >
        <ul id="GroupList">
          {this.state.groups}
        </ul>
      </section>
    );
  }
}

export default GroupManager;
