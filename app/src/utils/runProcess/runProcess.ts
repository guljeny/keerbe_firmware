import child_process from 'child_process'

type TCommand = 'scan' | 'upload_layout' | 'get_layout' | 'reset_memory' | 'update' | 'flash'

export default function (cmd: TCommand, args: string[] = [], cb?: (v: string) => void) {
  const process = child_process.execFile(`../bin/${cmd}`, args)
  cb && process.stdout?.on('data', cb)
  return process
}
