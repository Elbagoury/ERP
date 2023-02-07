/** @erp-module **/

export const session = erp.__session_info__ || {};
delete erp.__session_info__;
