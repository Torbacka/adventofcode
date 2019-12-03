import java.io.*
import java.util.*


class FastIO : PrintWriter {

    private var bufferedReader: BufferedReader? = null
    private var line: String? = null
    private var token: String? = null
    private var st: StringTokenizer? = null

    /**
     * Constructor for FastIO.
     *
     * @param inputStream the inputStream that should be used
     */
    constructor(inputStream: InputStream) : super(BufferedOutputStream(System.out)) {
        bufferedReader = BufferedReader(InputStreamReader(inputStream))
    }

    /**
     * Constructor for FastIO.
     *
     * @param inputStream  the inputStream that should be used.
     * @param outputStream the outputStream that should be used.
     */
    constructor(inputStream: InputStream, outputStream: OutputStream) : super(BufferedOutputStream(outputStream)) {
        bufferedReader = BufferedReader(InputStreamReader(inputStream))
    }

    /**
     * Get next token and parse it to nextInt.
     *
     * @return return next integer
     */
    val nextInt: Int
        get() = Integer.parseInt(nextToken()!!)

    /**
     * Get next token and parse it to nextDouble.
     *
     * @return return next double
     */
    val nextDouble: Double
        get() = java.lang.Double.parseDouble(nextToken()!!)
    /**
     * Get next token and parse it to nextLong.
     *
     * @return return next long
     */
    val nextLong: Long
        get() = java.lang.Long.parseLong(nextToken()!!)


    /**
     * Get next token and parse it to nextWord.
     *
     * @return return next word
     */
    val nextWord: String?
        get() = nextToken()

    /**
     * Check if inputreader has more tokens.
     *
     * @return return true if the inputreader has more tokens.
     */
    fun hasMoreTokens(): Boolean = peekToken() != null

    @Throws(IOException::class)
    fun getLine(): String? {
        if (line != null) {
            val ans = line
            line = null
            st = null
            token = null
            return ans
        }
        return bufferedReader?.readLine()

    }

    private fun peekToken(): String? {
        if(token == null){
            try {
                while (st == null || !st!!.hasMoreTokens()) {
                    line = bufferedReader!!.readLine()
                    if (line == null) {
                        return null
                    }
                    st = StringTokenizer(line!!)
                }
                token = st!!.nextToken()
            } catch (e: IOException) {
                e.printStackTrace()
            }

        }
        return token
    }

    private fun nextToken(): String? {
        val ans = peekToken()
        token = null
        return ans
    }
}