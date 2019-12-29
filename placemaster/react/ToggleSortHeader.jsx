import React from 'react';

const classNames = require('classnames');

class ToggleSortHeader extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      ascending: true,
    };
    this.sortFunc = this.sortFunc.bind(this);
    this.handleToggle = this.handleToggle.bind(this);
  }

  handleToggle() {
    // switch between ascending and descending sorts
    if (this.props.active) {
      this.setState(prevState => ({
        ascending: !prevState.ascending,
      }));
    }
    this.props.setSortHandler(this.props.headerName);
  }

  sortFunc(a, b) {
    if (this.state.ascending) {
      // perform asceding comparisons of a.props.headerName and b.props.headerName
      return 0;
    }
    // perform descending comparisons
    return 0;
  }

  render() {
    const headerClass = classNames(
      'ToggleSortHeader',
      { active: this.props.active,
        down: this.state.ascending && this.props.active,
        up: !this.state.ascending && this.props.active },
    );
    return (
      <div className={headerClass} onClick={this.handleToggle}>
        <h4>{this.props.headerName}</h4>
      </div>
    );
  }
}

export default ToggleSortHeader;
