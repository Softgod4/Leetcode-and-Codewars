type TypeChannelName = {
    another: string
}

type TypeChannelReturn = {
    name: string
} & TypeChannelName;

const getChannel = (name:string, another:string):TypeChannelReturn => {
    return { name, another }
}

type sumB = (a:number, b:number) => number;
const sum: sumB = (a, b) => a + b;

const getLength = (text: string | null): number => {
    return text!.length
}

getLength('gaf')

// ------------------------------------------------

// Полная типизация всего ☝🏼

// ------------------------------------------------

function getCar(name: string, price?: number):string {
    return price ? `Название ${name}, Цена ${price}` : `Название ${name}`
}
const car1 = getCar('bmw', 1000)

// ------------------------------------------------

// Перегрузки ☝🏼

// ------------------------------------------------

class Car {
    name: string;
    price: number;

    constructor(name: string, price: number) {
        this.name = name
        this.price = price
    }
    getInfo(): string{
        return `${this.name} - ${this.price}`
    }
}

class Bus extends Car {
    constructor(name: string, price: number) {
        super(name,price)
    }
}

new Car('BMW', 10000).getInfo()

// ------------------------------------------------

// ООП ☝🏼

// ------------------------------------------------

interface IUserContact {
    email: string
    name: string
    password: string
}

const user: IUserContact = {
    email: 'bigboobs@gmail.com',
    name: 'Max',
    password: '12345'
}

// ------------------------------------------------

// Интерфейсы ☝🏼

// ------------------------------------------------

enum EnumRoles {
    ADMIN, GUEST, USER
}

interface IUser {
    role: EnumRoles
}

const users: IUser = {
    role: EnumRoles.ADMIN
}

const enum EnumColors {
    black,
    pink,
    green,
}

// ------------------------------------------------

// Enum ☝🏼

// ------------------------------------------------

const inputElement = document.querySelector('input')
const value1 = (inputElement as HTMLInputElement).value
const value2 = (<HTMLInputElement>inputElement).value

// ------------------------------------------------

// Утверждения ☝🏼

// ------------------------------------------------

function enitity<T>(args: T): T{
    return args
}
enitity<number>(1)

class Channel<T> {
    private name: T

    constructor(name: T){
        this.name = name
    }

    getName():T {
        return this.name
    }
}


// ------------------------------------------------

// дженерики ☝🏼

// ------------------------------------------------