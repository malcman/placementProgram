import React from 'react';

const classNames = require('classnames');

function Member(props) {
  const memberClass = classNames('member');
  return (
    <li className={memberClass}>
      <p>{props.name}</p>
      <p>{props.email}</p>
      <p>{props.campus}</p>
      <p>{props.gender}</p>
      <p>{props.year}</p>
      <p>{props.groupNumber}</p>
    </li>
  );
}

export default Member;
