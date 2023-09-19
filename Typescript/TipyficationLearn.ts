type TypeChannelReturn = {
    name:string
}

const getChannel = (name: string):TypeChannelReturn => {
    return { name }
}

// ------------------------------------------------

// Полная типизация функции ☝🏼

// ------------------------------------------------

function getCar(name: string, price?: number):string {
    return price ? `Название ${name}, Цена ${price}` : `Название ${name}`
}
const car1 = getCar('bmw', 1000)

// ------------------------------------------------

// Перезгрузки ☝🏼

// ------------------------------------------------