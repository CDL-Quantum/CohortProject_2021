# Define our gates

function PastaQ.gate(::GateName"R"; theta::Real, phi::Real)
    [
        cos(theta/2)    (-im * exp(-im * phi) * sin(theta/2))
        (-im * exp(im * phi) * sin(theta/2))     cos(theta/2)
    ]
end

function PastaQ.gate(::GateName"M"; Theta::Real)
    [
        cos(Theta)    0    0    (-im * sin(Theta))
        0    cos(Theta)    (-im * sin(Theta))    0
        0    (-im * sin(Theta))    cos(Theta)    0
        (-im * sin(Theta))    0    0    cos(Theta)
    ]
end

function PastaQ.gate(::GateName"Z";)
    [
        1.00    0
        0     -1.00
    ]
end

function PastaQ.gate(::GateName"X";)
    [
        0    1.00
        1.00     0
    ]
end
#perturbation added to M gate
function PastaQ.gate(::GateName"M_p"; Theta::Real, delta::Real)
    [
        cos(Theta+delta)    0    0    (-im * sin(Theta+delta))
        0    cos(Theta+delta)    (-im * sin(Theta+delta))    0
        0    (-im * sin(Theta+delta))    cos(Theta+delta)    0
        (-im * sin(Theta+delta))    0    0    cos(Theta+delta)
    ]
end
