"""

A module containing various functions that assist in debugging.
"""

from logging import getLogger


class ReadoutError(object):
    def __init__(self):
        pass


class ArgumentConflictError(ReadoutError):
    def __init__(self, message: str = None):
        super().__init__()
        if message is None:
            self.message = 'There has been an unknown conflict of argument values. This is usually caused when one ' \
                           'changes two (or more) mutually exclusive arguments. Please see documentation.'
        else:
            self.message = message


def format_members(dir_res, inc_priv=False):
    from nude_man import APP_NAME as PROG
    """

    A module to get a sorted, formatted list of the requesters members

    Args:
        inc_priv (bool): Should this function include exposed private members in it's returned tuple?
        dir_res (list): The list the caller receives after calling 'dir()'

    Returns:
        Tuple: Returns a list of requesters members. Optionally, does not filter private members

    """

    # Prepare an empty list to transfer the received member names to after manipulating it appropriately
    member_list = []

    # Iterate through the received member list
    #   - If we are not including private members in our return we will refrain from adding members that start with
    #     '__' to the end-result
    for member in dir_res:
        if not inc_priv and member.startswith('__'):
            continue
        else:
            member_list.append(member)

    member_list.sort()

    mem_list_str = ','.join(member_list)

    return member_list, mem_list_str


def conf_sect_readout(config: object, target_section: str, sep_str='|', no_strip=False, pad_size=1, pad_str=' ',
                      no_pad=False, leave_sep_str_alone=False, plain_sep=False):
    """

    Provide this function with a ConfigParser object, and the section you'd like to read-out (and other desired
    parameter arguments) and it will return a string assembled from the key and value returned from each parameter
    defined in that configuration section.

    Example of Returned String:
        theme: DarkAmber | icon_set: sketch | grab_anywhere: False

    Below is a brief description of each of the parameters this function has available to manipulate and what effect
    doing so would have (standard documentation argument section). However, there are a few parameters I'd like to
    make special remarks about:

        sep_str: This argument is not required. If you don't provide a value for this argument it will default to '|'.
            NOTE:
                It's important to understand what happens to the value you provide this argument as the function
            will manipulate it as soon as it starts operation.

                How Does It Change?
                    The 'strip' function is called on the string object to eliminate any preceding or trailing
                    whitespace. This is done to ensure we don't result with a malformed separator after the desired
                    padding is applied by this function.

    Args:
        config (object): A ConfigParser type object that contains the section you'd like to readout

        target_section (str): A string that is equal to the name of the section you'd like to readout

        sep_str (str): A string that is equal to what should sit between the padding in the separator string between
                       resulting entry value pairs

        no_strip (bool): (Defaults to False) Do not strip preceding or trailing whitespace

        pad_size (int): (Defaults to 1) How many times should pad_str (by default: ' ') be repeated on each side of the
                        separator string?

        pad_str (str): (Defaults to ' ') Replace the default pad character (a single whitespace) with whatever string
                    you desire

        no_pad (bool): Do not pad the separation character. This will result in any arguments provided to pad_size,
                       and pad_str will be ignored and no padding will surround the 'key: value' pair

                       NOTE:
                           1. Using this argument and not also using 'no_strip = True' will still result in your input
                              being stripped.

                           2. Using this argument does not ensure that there will be a lack of whitespace after the
                              separator string as the program will insert a single whitespace to ensure readability. You
                              can override this behavior by simple giving a value of True to the 'leave_sep_str_alone"
                              flag instead of using 'no_pad'


        leave_sep_str_alone (bool): Make no modifications to the separator.
                                    NOTE:
                                        Changing this from it's default value will result in the following arguments
                                        being ignored:

                                        * pad_size
                                        * pad_str

                                        This argument conflicts with 'plain_sep' using both arguments will result in
                                        a ConflictingArgumentsError

        plain_sep (bool): If True; the separator between 'key: value' pairs will simply be ', '

                          For Example:
                            'icon_set: sketch, theme: DarkAmber, grab_anywhere: False'

                          NOTE:
                               Changing this from it's default value will result in the following arguments being
                               ignored:

                               * no_strip
                               * sep_str
                               * no_pad
                               * pad_size
                               * pad_str

    Returns:
        str: A string that consists of all the keys and their values that can be found in the target section of the
             provided config object

    """
    log = getLogger(PROG + '.conf_sect_readout')

    if leave_sep_str_alone and plain_sep:
        try:
            raise ArgumentConflictError('Conflicting arguments detected: leave_sep_str_alone and plain_sep. '
                                        'These two can not coexist')
        except ArgumentConflictError as e:
            log.error(e.message)

    if not plain_sep:
        # If we've been denied permission to do any modifications to the provided sep_str we fill the final 'sep'
        # variable with the provided sep_str without touching it
        if leave_sep_str_alone:
            sep = sep_str
        else:

            # If we have permission (which is the default) to strip the incoming sep_str, we do that and assign the
            # result to the 'sep' variable
            if not no_strip:
                sep = sep_str.strip()
            else:

                # If we were told to leave the separator string alone we just make the value of 'sep' whatever is
                # provided by the sep_str argument
                sep = sep_str

            if not no_pad:
                pad1 = str(pad_str * pad_size)
                pad2 = pad1
            else:
                pad1 = ''
                pad2 = pad1

            seperator = str(f'{pad1}{sep}{pad2}')
    else:
        seperator = ', '

    # Using the result of the above instruction as our pad string (so a copy on each side) we assemble a proper
    # separator string
    separator = str(f'{pad1}{sep}{pad2}')

    # Declare a variable that contains an empty list to append to in the next block.
    key_value_pair_list = []

    # Iterate over the target section of the provided config object capturing each key, and it's value which we then
    # concatenate into a string to be added as an entry to the key_value_pair_list and then append it.
    for key, value in config[target_section]:

        # Our string will look like this:
        #   SETTING: PARAM
        #
        #   For Example:
        #       theme: DarkAmber
        f_pair = str(f'{key}: {value}')

        # Append our concatenated string to the key_value_pair_list list
        key_value_pair_list.append(f_pair)

    # Finally, return a string to the caller that is the result of joining the entries in our key_value_pair_list
    # using the provided or default string as our separator.
    #
    # For Example:
    #   icon_set: sketch | theme
    return separator.join(key_value_pair_list)
