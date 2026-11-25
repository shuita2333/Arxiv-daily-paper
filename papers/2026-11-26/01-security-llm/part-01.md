# 🔐 大模型安全相关研究 | 2026年11月26日

> 本类共 **7** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [When Successful Collaboration Becomes an Attack Surface: Insider Memory Poisoning in Multi-Agent Systems](https://arxiv.org/abs/2611.31307)

**<font color=#1a73e8>作者：</font>** Jihyung Ahn, Buru Chang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent Multi-Agent Systems (MAS) increasingly use shared memory to store and reuse successful collaboration records, enabling teams to improve across tasks. However, this memory introduces a new attack surface for malicious insiders. Unlike existing insider attacks that inject misleading information directly into the current collaboration, misinformation stored in shared memory can later appear as successful team experience and gain greater credibility and influence. We propose MIMPA (Multi-Agent Insider Memory Poisoning Attack), which exploits this vulnerability using only normal participation privileges, without direct memory access. During an earlier task, the malicious agent embeds a target-specific payload while helping the team answer correctly, allowing the payload to be retained in a successful collaboration record. When retrieved for a later target task, this poisoned record can steer benign agents toward a designated wrong answer, further amplified by malicious triggering. Across three benchmarks and two LLM backbones, MIMPA substantially outperforms existing insider attacks and remains effective under hierarchical memory management, while auditing only partially mitigates it. These results reveal that shared memory intended to accumulate team experience can become a persistent channel for insider attacks. Our code is available at this https URL.

---


### 2. [Scoring Recovery-Time Agent Security: Proposals, Effects, and Retry Instructions](https://arxiv.org/abs/2611.31318)

**<font color=#1a73e8>作者：</font>** Paul Deepakraj Retinraj  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A timed-out tool write may be absent, committed, or still in flight. Evaluating an agent only on whether its goal exists can hide harmful recovery actions: auditing 12 supplied traces changes apparent completion from 10/12 to 8/12. We introduce an executable evaluation that separately records tool proposals, runtime decisions, and committed effects. In 3,456 model episodes, the original task wording produces only 39/576 valid recoveries when the initial write is absent; a combined clarification produces 576/576. A further 1,584 episodes test stronger attacks and separate the effect definition from the recovery recipe with three rollouts per absent-state cell. Definition alone yields 276/288 valid recoveries; recipe alone yields 288/288. For Luna, malicious text is associated with 11.1 percentage points fewer valid recoveries under both original and definition-only wording, an availability signal limited by shared tasks and templates. The stronger attacks produce no attempted unauthorized or changed-key action and no unsafe effect. A trajectory audit finds six original-key retries after observing pending status: five denied and one deduplicated. Bounded checks distinguish atomic key enforcement from a delayed-commit race; stale negative reads also invalidate the evidence gate. A separate Claude Code program adds 720 successful episodes: 288 under the original attacks and 432 stronger-attack calibration episodes across Opus, Sonnet, and Haiku 5.5, with no observed proposal or effect deviations. The contribution is a measurement design and a diagnosis of availability, specification, and contract sensitivity, with no demonstrated general defense efficacy.

---


### 3. [ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection](https://arxiv.org/abs/2611.31424)

**<font color=#1a73e8>作者：</font>** Yi Han, Zhen Sun, Zhijie Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs become more capable, agents can perform more complex tasks with tools and maintain longer interactions with users. These benign conversations contain evidence on task results, user concerns, and operational constraints. The risk is that attackers who can observe benign conversations (evidence) may construct stronger indirect prompt injections without increasing the attackers' control over prior turns or the later injection. However, we still lack a clear study of how effectively attackers can select and use this evidence. To address this gap, we introduce ContextLure, a red-teaming framework in which an attacker silently observes an existing benign conversation, extracts evidence, and constructs an injection. The challenges are twofold: (a) selecting useful evidence and (b) presenting it as reasons for an unauthorized action, without changing the prior benign conversation. To efficiently exploit (a) the effect of evidence on attack success, our framework selects evidence across 2 dimensions: User/System Preferences with 3 selection policies. And to enhance (b) the process of turning the selected information into the malicious request, we introduce an Urgency/Priority matrix with 4 rewriting strategies. Across the evaluated conditions, we reach 67.4% ASR on AgentDojo and 87.3% on InjecAgent. These results show that attackers can use benign interaction evidence in later attacks without first poisoning the benign conversation.

---


### 4. [Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning](https://arxiv.org/abs/2611.32304)

**<font color=#1a73e8>作者：</font>** Simin Huang, Jiawei Chen, Shaolong Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models advance robotic manipulation, but their reliance on demonstrations exposes them to backdoor threats. Among these threats, trajectory-level targeted backdoors are particularly challenging and may pose greater safety risks than behavior-disrupting attacks: rather than merely causing task failures or local action deviations, they must sustain closed-loop redirection to complete an attacker-specified multi-step task. To reliably induce such behaviors, existing methods typically rely on high poisoning rates to obtain sufficient target-trajectory supervision. However, high poisoning rates may compromise clean-task performance, whereas low rates leave target-trajectory supervision scarce and backdoor learning vulnerable to interference from dominant clean-task updates. To resolve this trade-off at low poisoning rates, we propose a two-stage co-optimization framework guided by vision, language, and action. Stage I freezes the policy and uses differentiable rendering and multimodal supervision to optimize a 3D trigger's texture, translation, and scale, strengthening trigger-target associations from limited poisoned demonstrations. Building on the optimized trigger, Stage II applies source-selective dual-LoRA adaptation to decouple clean and backdoor updates and mitigate their interference, followed by learned column-wise calibration and analytic fusion into a unified policy. Experiments on OpenVLA, OpenVLA-OFT, $\pi_0$, and $\pi_{0.5}$ across four LIBERO suites show consistent gains over all evaluated attack baselines. With only 1% poisoned data, our method achieves 86.4% target success and 95.2% clean-task success on OpenVLA-OFT in LIBERO-Spatial. Real-robot trials also demonstrate trajectory-level hijacking.

---


### 5. [Red-Teaming a Sovereign LLM, Its Reasoning and Its Training Stages](https://arxiv.org/abs/2611.32710)

**<font color=#1a73e8>作者：</font>** Hatef Otroshi Shahreza  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models (LLMs) are increasingly deployed for applications with sensitive information. We investigate whether confidentiality instructions in system prompt can protect such information. We red-team Apertus v1.5, an open sovereign LLM, and five other model families across six languages and reasoning modes. We use synthetic personal records to evaluate direct disclosure, correction baits, yes/no verification, derived-value queries, reasoning leakage and authorisation checks. We also explore copyright attribution, historical misrepresentation and stereotyping. Despite confidentiality instructions, Apertus 8B and 70B leak information in 96% and 95% of requests, respectively, in correction-bait attacks. Verification and derived-value queries also expose protected information without necessarily revealing identifiers. Moreover, reasoning traces can leak confidential records even when final answers withhold them. Our experiments also show that post-training does not consistently improve safety. Our findings demonstrate that system prompts alone cannot ensure confidentiality and highlight the need for multilingual reasoning-aware safety evaluations.

---


### 6. [ReQOR: Operator-Discrepancy Subspace Repair for Quantization-Conditioned Backdoors in Large Language Models](https://arxiv.org/abs/2611.32755)

**<font color=#1a73e8>作者：</font>** Wonjune Seo, Minkyung Park, Saerom Park  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantization-Conditioned Backdoors (QCBs) cause large language models (LLMs) to exhibit malicious behavior after quantization while remaining benign at high precision. Existing defenses often rely on security-guided configuration selection or iterative optimization, but do not identify which quantization-induced changes should be repaired. We isolate module-local quantization effects from upstream drift by evaluating the high-precision and quantized versions of each module on identical states from the quantized inference trajectory, and formulate QCB defense as repairing the resulting same-state operator discrepancies. We propose ReQOR, a training-free defense that identifies the dominant directions of these discrepancies on benign calibration data and restores the full-precision computation along them in closed form, yielding a factorized residual adapter. ReQOR uses neither attack information nor gradient-based optimization and supports both full-span and low-rank repair. Experiments across four LLMs, three PGD-based QCB attacks, three malicious behaviors, and three quantization formats show substantial QCB mitigation while largely preserving benign utility. In additional experiments on a non-PGD outlier-injection attack, existing baselines largely fail, whereas ReQOR remains effective. Further analysis shows that dominant operator-discrepancy directions provide more effective and rank-efficient repair than rank-matched random, low-energy, or raw weight-error directions, while low-rank ReQOR reduces deployment memory overhead.

---


### 7. [SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment](https://arxiv.org/abs/2611.33030)

**<font color=#1a73e8>作者：</font>** Shivank Rajput, Himanshu Singh, A. V. Subramanyam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-based GCG-style attacks can be effective, but they are expensive at inference time, and suffer from poor transfer. We present, SALSA, a generative framework that learns a distribution over jailbreak suffixes from optimization-derived attack corpora. Once trained, the model supports efficient sampling-based attacks. On open-source targets, it achieves attack success rates comparable to state-of-the-art optimization baselines, while reducing generation time from 3.46s to 0.04s per prompt. In black-box transfer, it remains highly effective against proprietary systems, including 99% ASR on GPT-3.5-Turbo, and reaches 45% ASR on the substantially harder GPT-4o, more than doubling the strongest baseline at an equal sampling budget. We further offer an intuition for why generative sampling can preserve high attack success, when the learned suffix distribution is close to the distribution of optimization outputs. Overall, our results show that learning adversarial suffix distributions yields a scalable, and practically efficient foundation for continuous LLM vulnerability discovery.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
