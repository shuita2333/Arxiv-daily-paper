# 🔐 大模型安全相关研究 | 2026年11月09日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Interactive Backdoor Attacks in LLM-Based Proactive Dialogue Systems](https://arxiv.org/abs/2611.06969)

**<font color=#1a73e8>作者：</font>** Zhiyang Xia, Yuming Shang, Xi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based proactive dialogue systems provide goal-directed support through sustained interaction. Fine-tuning their underlying models on externally supplied dialogue data introduces backdoor risks. Existing LLM backdoor studies primarily focus on eliciting an attacker-specified response upon trigger activation. We present an interactive backdoor attack framework that uses training-data poisoning to steer post-trigger, multi-turn interactions toward an attacker-specified objective. Poisoned fine-tuning dialogues implant a trigger-conditioned guidance-policy bias that ordinary user utterances can activate, without deployment-time prompt modification or further attacker intervention. Specifically, we instantiate three complementary attacks under progressively expanded post-trigger interaction settings: (1) Direct Attack, which targets an immediate response deviation upon trigger activation, retaining the conventional trigger--response setting; (2) Constrained Progressive Attack, which progressively advances the attack objective along a predefined multi-turn trajectory; and (3) Unconstrained Progressive Attack, which extends target-directed steering to open-ended interactions with varied user continuations. Using psychological counseling as a representative setting, experiments on two LLM backbones and two dialogue datasets show that all three attacks effectively achieve their objectives under their respective interaction settings while largely preserving normal utility. Separate defense evaluations show that the tested training-data filters retain nearly all poisoned dialogues, while three post-admission baselines leave substantial residual attack-specific success.

---


### 2. [SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection](https://arxiv.org/abs/2611.07222)

**<font color=#1a73e8>作者：</font>** Woosang Lim, Yeseul Chang, Jaewoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may read the attacker's text and adds model calls to every step. Provenance defenses keep the model off the final check but need a model to plan or route each task first. Where an action goes can instead be read from the tools' typed returns: an email's sender or a payment's account arrives in a typed field, while injected instructions arrive as free text. SPILLWAY turns this observation into a deterministic floor with no per-task plan. The check admits a call when each target value that appears in tool output but not in the user's task was returned by a read-only tool in a typed field or is covered by a fixed delegation rule. A deterministic sanitizer removes instruction-like regions its fixed rules match before the model reads them and retains the removed spans as evidence, and a local judge may restore a refused call, never one whose target lies in the removed text. Across three backbones, and seven task suites on one of them, no standard templated injection redirects an action to an attacker's target under SPILLWAY, at the highest observed mean utility and composite scores (NRP, ERS) of the defenses we run under that attack. A forged chat template also produces a raw zero, and mean in-scope attack success under a released reinforcement-learning attacker is .007. SPILLWAY reaches this floor with no defense-triggered backbone re-run and almost no added model call. As personal AI agents act on users' email, files, and payments, SPILLWAY gives them an auditable refusal floor on where their actions go that keeps them useful and holds across backbones.

---


### 3. [SAVeR$^2$: Reasoning-based Safety Alignment for Large Reasoning Models via Verifiable Rewards](https://arxiv.org/abs/2611.07482)

**<font color=#1a73e8>作者：</font>** Yichen Sun, Qirui Liu, Yan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have achieved impressive performance via explicit Chain-of-Thought (CoT) reasoning, yet this process introduces critical safety risks. We formalize LRM safety objectives as requiring non-malicious reasoning and answers, safety consistency, and explicit intent identification. We argue that existing alignment methods suffer from poor adversarial generalization, a significant ``safety tax'' on reasoning, and unfaithful coarse-grained rewards, primarily due to their neglect of the LRM's intrinsic reasoning capabilities for safety. To address these, we propose \textbf{SAVeR$^2$}, a novel \textbf{S}afety \textbf{A}lignment method via \textbf{R}ewards with \textbf{R}easoning capability. SAVeR$^2$ decomposes the safety objective into four fine-grained verifiable reward signals and utilizes a difficulty-aware data selection strategy to stabilize training. Crucially, we introduce a reasoning-preserving gradient projection mechanism that analytically resolves conflicts between safety and reasoning gradients, effectively eliminating the safety tax. Extensive experiments on models ranging from 1.5B to 671B demonstrate that SAVeR$^2$ achieves superior safety performance and significantly lower over-refusal rates across multiple benchmarks without compromising general reasoning capabilities.

---


### 4. [JailBound: FOL-Guided Jailbreak Evaluation for Exploring LLM Behavioral Boundaries](https://arxiv.org/abs/2611.07530)

**<font color=#1a73e8>作者：</font>** Fazong Wu, Xin Wang, Ming Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed as general-purpose conversational assistants, they must handle diverse user requests while reliably refusing harmful ones. Jailbreak attacks craft adversarial instructions or conversational contexts to elicit unsafe responses despite these safeguards. However, existing jailbreak benchmarks often rely on manually designed or collected prompts, making it difficult to systematically extend coverage to new threat conditions. Moreover, existing attack search methods typically optimize for attack success rate (ASR), providing limited insight into how model behavior changes locally between safe refusal and unsafe response. To address these limitations, we present JailBound, a unified jailbreak evaluation framework that combines automated benchmark construction with first-order loss (FOL)-guided dual-branch search. JailBound organizes threats by risk category, application domain, and attack type. Conditioned on this taxonomy, a fine-tuned meta-attack generator synthesizes evaluation prompts across diverse threat conditions. FOL serves as a local sensitivity signal for exploring high-value attack states and behavior-sensitive states. We evaluate JailBound across 46 LLMs from 13 model families under a unified experimental protocol. Under matched settings, the High-Value Branch improves average ASR over a ZOL-only baseline by 5.1 and 4.9 percentage points across the two evaluation settings. Under local perturbations, states from the Safety-Sensitivity Branch exhibit higher behavioral flip rates than those from the High-Value Branch across all tested radii for JailBound and S-Eval, indicating greater local sensitivity of judge-assigned safety labels. Warning: this paper includes examples that may be offensive or harmful.

---


### 5. [Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks](https://arxiv.org/abs/2611.07640)

**<font color=#1a73e8>作者：</font>** Rongting Zhang, Martin Bertran, Sandeep Avula 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt-injection (IPI) benchmarks predominantly test planted instructions that redirect a tool-using agent toward an attacker-chosen task. Yet attacker-controlled content can instead tamper with the outcome of the task already in progress. A buyer's dispute evidence can cite a false refund policy to inflate a refund without changing the task. We define IPI by authority rather than instruction-like wording: planted content constitutes an attack when it attempts to influence a decision that its source is not authorized to determine. We introduce a benchmark that makes this boundary explicit: in each of 90 validated cases across three tool-use environments, the user request specifies the source that resolves the targeted decision. Every attack tampers with a decision required by the benign task rather than replacing that task. Each case has attacks with the same harmful outcome that target up to six parts of the agent's decision making: its objective, decision rules, available actions, expected consequences, reading of observations, or beliefs about the current state. Without a defense, attacks on three of the five other targets (decision rules, available actions, and state) have higher mean success than objective attacks across five LLMs. A detection-and-removal defense reduces objective-targeting attacks to 2.4% success but leaves observation- and state-targeting attacks at 9.5% and 12.1%; this gap persists under detection-optimized rewrites. A tool-policy defense still allows 15.4% attack success, close to 17.0% without a defense, because these attacks generally retain expected tools and manipulate values obtained during execution. Evaluations whose attacks redirect the task or target only the agent's objective can therefore overestimate the coverage of these defenses. Code and data are available at this https URL.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
