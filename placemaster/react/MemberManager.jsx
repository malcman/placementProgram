import React from 'react';
import Member from './Member';

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
    return (
      <section
        className={className}
        id="MemberManager"
        aria-labelledby="MemberTag"
      >
        <ul id="MemberList">
          {this.state.members}
        </ul>
      </section>
    );
  }
}

export default MemberManager;
