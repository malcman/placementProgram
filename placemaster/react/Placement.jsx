import React from 'react';
import GroupManager from './GroupManager';
import MemberManager from './MemberManager';

const classNames = require('classnames');

class Placement extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      groups: [],
      members: [],
      groupFocus: true,
    };
    this.fetchPlacement = this.fetchPlacement.bind(this);
    this.toggleFocusEl = this.toggleFocusEl.bind(this);
  }

  toggleFocusEl(groupFocus) {
    // set groupFocus as indicated by target with the attached handler
    this.setState({
      groupFocus,
    });
  }

  fetchPlacement(fetchURL) {
    fetch(fetchURL, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        const groups = [];
        const members = [];
        data.members.forEach((member) => {
          console.log(member);
        });
        this.setState({
          groups,
          members,
        });
      })
      .catch();
  }

  render() {
    const groupsClass = classNames({ hidden: !this.state.groupsFocus });
    const membersClass = classNames({ hidden: this.state.groupsFocus });
    return (
      <section className="Placement">
        <ul
          id="placementTabs"
          role="tablist">
          {/* group tab */}
          <li
            id="GroupTag"
            role="tab"
            aria-selected={this.state.groupFocus}
            aria-controls="GroupManager"
            onClick={e => this.toggleFocusEl(true, e)}
          >
            <h3>Groups</h3>
          </li>

          {/* member tab */}
          <li
            id="MemberTag"
            role="tab"
            aria-selected={!this.state.groupFocus}
            aria-controls="MemberManager"
            onClick={e => this.toggleFocusEl(false, e)}
          >
            <h3>Members</h3>
          </li>
        </ul>
        <GroupManager
          role="tabpanel"
          focused={this.state.groupFocus}
        />
        <MemberManager
          role="tabpanel"
          focused={!this.state.groupFocus}
        />
      </section>
    );
  }
}

export default Placement;
