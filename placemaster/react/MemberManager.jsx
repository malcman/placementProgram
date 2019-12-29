import React from 'react';
import Member from './Member';
import HeadersManager from './HeadersManager';

const classNames = require('classnames');

class MemberManager extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      members: [
        <Member
          name={'Jimmy'}
          email={'jim@umich.edu'}
          campus={'central'}
          gender={'male'}
          year={'senior'}
          groupNumber={1}
          key={1}
        />,
      ],
    };
  }
  render() {
    const className = classNames('Manager', { hidden: !this.props.focused });

    // TODO: change to get this from data
    // column headers for each member
    const memberHeaders = ['Name', 'Email', 'Campus', 'Gender', 'Year'];
    return (
      <section
        className={className}
        id="MemberManager"
        aria-labelledby="MemberTag"
      >
        <HeadersManager headers={memberHeaders} currentSort={'Name'} />
        <ul id="MemberList">
          {this.state.members}
        </ul>
      </section>
    );
  }
}

export default MemberManager;
