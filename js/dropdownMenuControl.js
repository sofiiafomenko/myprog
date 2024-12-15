export default class DropdownMenuControl {
    /**
     * Dropdown menu handler constructor with initialization
     * @param menuItemsElmId - id of an HTML element with the items of the menu
     * @param menuTitleElmId - id of an HTML element with the title of the menu
     * @param showCssClass  - name of a class to be assigned to the HTML element with the items of the menu when displayed
     * @param hamburgerElmId - id of the hamburger menu element
     */
    constructor(menuItemsElmId, menuTitleElmId, showCssClass, hamburgerElmId) {
        this.menuItemsElm = document.getElementById(menuItemsElmId);
        this.menuTitleElm = document.getElementById(menuTitleElmId);
        this.hamburgerElm = document.getElementById(hamburgerElmId);
        this.menuSelector = `#${menuItemsElmId},#${menuTitleElmId},#${hamburgerElmId}`;
        this.showCssClass = showCssClass;

        // Event listeners
        document.addEventListener("click", (event) => this.hideMenu(event));
        this.hamburgerElm.addEventListener("click", (event) => this.toggleMenuWithHamburger(event));
    }

    /**
     * Hides the HTML element with the items of the menu
     */
    hideMenu(event) {
        if (!event.target.matches(this.menuSelector)) {
            const menuClElmCList = this.menuItemsElm.classList;
            if (menuClElmCList.contains(this.showCssClass)) {
                menuClElmCList.remove(this.showCssClass);
                this.hamburgerElm.classList.remove("active"); // Reset hamburger
            }
        }
    }

    /**
     * Toggles the menu using the hamburger icon
     */
    toggleMenuWithHamburger(event) {
        event.stopPropagation(); // Prevent triggering the document click
        this.hamburgerElm.classList.toggle("active");
        this.menuItemsElm.classList.toggle(this.showCssClass);
    }
}
