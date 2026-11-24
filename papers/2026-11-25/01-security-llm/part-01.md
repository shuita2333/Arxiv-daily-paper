# 🔐 大模型安全相关研究 | 2026年11月25日

> 本类共 **11** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [What Counts as Attack Success? Evaluating Harmfulness in Red Teaming LLMs](https://arxiv.org/abs/2611.28038)

**<font color=#1a73e8>作者：</font>** Ruyuan Wan, Adriana Alvarado Garcia, Md Toufikuzzaman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Judging whether a model response is harmful requires contextual and normative choices, yet red-teaming studies often delegate this judgment to automated evaluators. We examine how harmfulness criteria are specified in red-teaming research and how they carry through to reported results. Reviewing 76 papers, we find that many adopt their criteria from prior datasets, classifiers, or judge prompts rather than defining harmfulness themselves. Applying evaluators from these papers to identical outputs, we find that they can reach different judgments on the same response, which can change conclusions when comparing models. These differences arise partly because evaluators draw the boundary of harm in different places: some count any response that does not refuse, while others count only output that could plausibly cause harm. We argue that red-teaming studies should state their harmfulness criteria and report how they chose and validated their evaluators to support more reliable measurement and interpretation.

---


### 2. [Weight-Space Backdoors in Open-Weight LLMs: Cross-Architecture Attacks and Blind Model Forensics](https://arxiv.org/abs/2611.28543)

**<font color=#1a73e8>作者：</font>** Mohammed Tanveer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight language models are vulnerable to trigger-conditioned behaviors introduced through sparse post-training weight modifications, creating supply-chain risks beyond conventional provenance checks. We present Neural Sentinel, a cross-architecture study of gradient-guided backdoor insertion and model forensics spanning 18 checkpoints across 14 architecture families (124M-31.3B parameters), including state-space and recurrent models.
On Phi-2, modifying approximately 0.0002% of parameters induced an exact short-marker output after 300 steps (332 seconds), with mean next-token KL divergence of $1.5 \times 10^{-5}$ and 100% top-1 agreement over evaluated positions of eight fixed reference prompts. Separate experiments produced structured tool-call-formatted outputs without establishing downstream execution. We identify three procedure-dependent response regimes -- Gradient-Permeable, Scale-Threshold, and Gradient-Fragmented -- and evaluate PPO-based weight-space exploration, which showed no statistically significant advantage over random search.
For defense, Neural Sentinel combines weight-difference analysis, trigger discovery, activation probing, and contextual output inspection. In a 22-artifact development cohort, its reference-optional scanner classified 4/5 backdoored artifacts as BACKDOORED; the remaining positive and all 17 clean artifacts were SUSPICIOUS. These findings establish the feasibility of sparse conditional-output insertion and evidence-producing forensic triage, while identifying limitations in behavioral-drift assessment and clean-model admission.

---


### 3. [Mitigating Backdoors in Masked Diffusion Language Models](https://arxiv.org/abs/2611.28640)

**<font color=#1a73e8>作者：</font>** Chengzhong Wang, Lang Lin, Shengfang Zhai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) have emerged as a promising alternative to autoregressive models because they can predict multiple tokens in parallel rather than generating tokens sequentially. However, recent studies have shown that MDLMs are vulnerable to backdoor attacks: when an input contains an attacker-chosen trigger, a backdoored model generates a targeted output, such as malicious code, while otherwise behaving normally. Despite this threat, backdoor defenses for MDLMs remain largely underexplored. We present UNMASK, the first defense framework for MDLMs that detects trigger-containing inputs, localizes the trigger tokens, and removes the backdoor from the compromised model. UNMASK exploits two fundamental properties of backdoor triggers, specificity and dominance, to assign a suspiciousness score to each input token. By leveraging two distinctive capabilities of MDLMs, parallel token prediction and token reconstruction at arbitrary positions, UNMASK computes these scores both effectively and efficiently. We further provide a theoretical analysis supporting the design of UNMASK. Evaluations across 40 settings spanning two attacks and four models show that UNMASK detects 99.3% of trigger-containing inputs at a 5% false-positive rate, substantially outperforming the strongest adapted baseline, which achieves 54.8%. UNMASK also achieves over 99% trigger-localization accuracy and reduces the average attack success rate from 95% to 1%, while largely preserving the model's utility on clean inputs.

---


### 4. [Beyond Single-Turn Privacy: Training-Data Leakage in Conversational RAG](https://arxiv.org/abs/2611.28748)

**<font color=#1a73e8>作者：</font>** Syed Khaderi, Karima Makhlouf, Sami Zhioua  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is known to reduce training-data leakage in single-turn interactions, but whether this protection persists over multi-turn conversations is unclear. We introduce CRELT (Conversational RAG Extraction Leakage Trajectory), a reusable framework that tracks, turn by turn, the real contact details from the training data that a RAG system discloses. CRELT separates retrieval, conversation history, and attack strategy through a full-factorial design, uses a retrieval corpus verified to contain none of the target PII, and counts an item as leaked only when it is absent from the model input at the turn it is produced. In our main experiment, this criterion excludes 29-53% of raw matches that were already present in the input. Across GPT-J-6B, Pythia-6.9B, and Pythia-12B, targeting real Enron contact details, retrieval reduces disclosure under both full and cleared history, consistent with prior single-turn results. A length-matched control with random passages reproduces 91-99.5% of this reduction under cleared history and 47-78% under full history, so much of it comes from the added context rather than from what is retrieved. With retrieval enabled, however, retaining full conversation history increases disclosure by a factor of 3.6-4.9, while retaining only one previous turn already restores disclosure to approximately the full-history level. With retrieval, clearing the history reduces disclosure by 72-79%, but does not eliminate it. These results show that single-turn privacy audits can substantially underestimate training-data leakage in conversational RAG systems and that conversation-history policy is a critical dimension of privacy evaluation.

---


### 5. [Persistent Jailbreak Backdoor Attack](https://arxiv.org/abs/2611.29217)

**<font color=#1a73e8>作者：</font>** Haichuan Zhang, Xinyu Sun, Shih-Chieh Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety alignment is widely used to align large language models (LLMs) to produce helpful and harmless responses. However, an attacker can plant a jailbreak backdoor in an LLM such that adding a universal trigger word or phrase to a harmful prompt elicits attacker-desired responses. Existing jailbreak backdoor attacks induce distinct behaviors on backdoored inputs and safety samples (harmful prompts paired with refusal responses), making the backdoors susceptible to subsequent safety alignment and advanced defenses. In this paper, we propose a persistent jailbreak backdoor attack that reduces the divergence between clean and trigger-conditioned continuations during LLM decoding, making backdoored samples difficult to distinguish from safety samples. We also introduce a deferred-response mechanism that postpones harmful generations, further disguising the backdoor behavior. We evaluate our attack, PJBack, on eight LLMs from five model families, ranging from 7B to 70B parameters. PJBack achieves an average attack success rate of 93.9% and bypasses all seven evaluated defenses while preserving benign utility. In contrast, five existing backdoor attacks either achieve limited attack success or fail to withstand the evaluated defenses.

---


### 6. [Benchmarking Web Agent Defenses Against Adaptive Visual Prompt Injection](https://arxiv.org/abs/2611.29268)

**<font color=#1a73e8>作者：</font>** Haichuan Zhang, Zhiyuan Zhong, Shih-Chieh Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal web agents automate website interactions but remain vulnerable to visual prompt injection (VPI), where malicious webpage content manipulates their visual processing and induces unintended actions. Although several defenses focus on detecting injected instructions in screenshots, malicious destinations such as phishing URLs embedded in HTML can remain hidden yet accessible through agent interactions. Existing evaluations have also not sufficiently examined adaptive attackers who know the defense mechanisms. To address these limitations, we introduce AdaptiveVPI, the first benchmark for systematically evaluating adaptive VPI threats in web agents. Specifically, we present a dataset of 360 webpage instances spanning 6 distinct hijack strategies across 10 real-world websites, with malicious destinations not visible in screenshots. We design an adaptive attack framework that iteratively refines malicious instructions based on feedback from the defense mechanism being evaluated. We also introduce three metrics to measure the extent of agent hijacking at three different levels. Across 10 defense configurations for computer-use agents and 11 defense configurations for browser-use agents, our adaptive attacks achieve average success rates of 91.87% and 91.99%, respectively. These results reveal a gap between current VPI defenses and realistic threats and highlight the need for defenses designed with adaptive attackers in mind.

---


### 7. [Compared to What? Calibrating Machine-Unlearning Diagnostics with Present, Absent and Suppressed Anchors](https://arxiv.org/abs/2611.29285)

**<font color=#1a73e8>作者：</font>** Arsalan Kaleem  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning methods for language models are judged mainly by behaviour, but a model can stop producing an answer while still encoding it. Internal diagnostics such as linear probes, the logit lens and relearning speed are used to tell removal from suppression, yet none has been checked against cases where the answer is known. We build such cases. A present anchor learned a set of synthetic facts; an absent anchor is a never-taught oracle retrained without them; and suppressed anchors are unlearned with their lower layers frozen, so the facts stay encoded below the frozen block by construction. We compare these anchors with NPO, RMU and gradient difference at a matched operating point on GPT-2 Small and Qwen3-0.6B-Base, scoring every diagnostic per entity with AUROC against the oracle. Behaviour cannot separate the suppressed anchors from the oracle (AUROC 0.51 to 0.58), while probes, the logit lens and relearning gain can (0.65 to 1.00), and the oracle seeds stay near 0.5. Applied to NPO on both models and RMU on Qwen3, the validated diagnostics disagree: probes put the facts at the oracle's level, while the models still relearn them much faster than a never-taught model does. Every unlearned model, anchor or method, also assigns the forgotten answer a far lower log-probability than the oracle does, a black-box signal that flagged all of them. A drift-ratio specificity rule fails on known cases. Code, data and every run are at this https URL.

---


### 8. [Adaptation or Poisoning? Security Risks of Conversational Test-Time Learning in Large Language Models](https://arxiv.org/abs/2611.29532)

**<font color=#1a73e8>作者：</font>** Honghao Feng, Shanhan Qu, Kai Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time learning (TTL) enables large language models to adapt to unlabeled inputs during deployment. The model updates a lightweight adapter by minimizing the next-token prediction loss on the input it receives. When these updates persist across conversation turns, every user query serves both as the request answered in the current turn and as adaptation data for later turns. By choosing the queries used for adaptation, an attacker can influence parameter updates and weaken safety alignment through ordinary interactions with a TTL chat service. To demonstrate this risk, we introduce Progressive Test-Time Adaptation Poisoning (P-TAP), a query-only multi-turn attack that jailbreaks the model by poisoning its session adapter through the service's own updates. A sequence of escalating adversarial queries shapes the adapter turn by turn; the final harmful request is then answered under the accumulated state without itself being used for adaptation. Across four open-weight instruction-tuned models, enabling updates raises attack success rates on average by 13.00 percentage points under greedy decoding and by 22.25 points under best-of-10 sampling, relative to matched sessions receiving the same queries without updates. Answering adversarial queries but adapting on unrelated text or on benign text about the same topic removes most of this increase. Among existing safeguards, screening incoming queries flags every attack stream before the final request, while a perplexity-based detector of unsafe adaptation flags none of the successful attacks.

---


### 9. [MobileGrail: Learning Compact Guardrails for On-Device deployable Mobile GUI Agent Safety](https://arxiv.org/abs/2611.29847)

**<font color=#1a73e8>作者：</font>** Zhiyu Zhang, Yuankai Li, Muhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime guardrails protect mobile GUI agents by assessing each proposed action before execution, but existing guardrails rely on cloud hosted large multimodal models, exposing every screen to a remote server, including private information such as payments, messages, and medical records. We propose MobileGrail, an on-device deployable model that addresses both. It maintains a recurrent task state that retains only the evidence subsequent safety decisions depend on, so that authorization and execution progress persist beyond the short context. To intervene early while keeping the safety boundary precise, it learns two labels, unsafe and block: unsafe marks the action that commits a violation, whereas block may be issued at any step of an intervention window, which spans from the first action that the user's authorization no longer explains to the committing action itself. To support training, we build an environment of 32 applications whose backends verify the effect of every action, supplying verified labels for supervision and rewards for reinforcement learning to calibrate intervention timing. We also build MobileVeto, an offline benchmark of unsafe trajectories largely on held-out applications, each paired with a benign counterpart. On MobileVeto, MobileGrail built on Qwen3.5-2B intercepts 76.2% of violations, up from 64.5% for its prompted backbone, while reducing premature intervention from 58.6% to 5.2%, outperforming the cloud-based OS-Sentinel on both. We further conduct online evaluation on GhostEIBench, where MobileGrail guarding a Qwen3.8-27B agent reduces fully successful attacks from 13 to 3 of 110 tasks while raising task completion from 48 to 58. Quantized to 4 bits, MobileGrail runs on a Snapdragon 8 Elite at a median latency of 4.7 s, comparable to the 5.1s of cloud-hosted Gemini 3.8 Flash.

---


### 10. [Tracing Attacker Diversity Reduction in Adaptive LLM Red Teaming](https://arxiv.org/abs/2611.29960)

**<font color=#1a73e8>作者：</font>** Chris Tava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning can increase the success of automated red teaming but it also narrows the attack vector. This study asks where in the attacker-defender-judge learning loop does the narrowing begin and which mechanisms lead to a narrowing attack. Six mechanisms (defender adaptation, success edge, reward reinforcement, row cap, update size, and measurement) are tested across three experiment arms (co-trained, frozen defender, half learning rate) for twenty-four iterations. A frozen defender narrows attack diversity retention (ADR) earlier 0.496 relative to co-trained 0.891 at iteration twelve. Defender updates delay narrowing but dont prevent it. Successful attacks ("winners") have narrower attack diversity than the full set of generated attacks. Attacks closest to previous winners succeed 10-15 percentage points more often than those closest to previous failures. This winner-neighbor advantage holds after a defender update and for a fixed defender too. Attacks with a common opening have a common-opening advantage of 5-16 percentage points. The training row cap and update size account for little impact on ADR, and attack length accounts for only part of the ADR decrease. Narrowing appears to originate from the success only reward through the group-relative training advantage to the attacker update, with a persistent success edge setting the direction.

---


### 11. [Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection](https://arxiv.org/abs/2611.29977)

**<font color=#1a73e8>作者：</font>** Jiaqi Rong, Yunchen Lu, Lihai Nie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Harnesses secure Computer-Using Agents by enforcing security constraints and defending against prompt injection attacks. However, we find that two core security mechanisms of agent harnesses remain vulnerable. First, consistency checking prevents agents from deviating from legitimate user objectives, while attackers can bypass it by embedding malicious actions that appear logically consistent with legitimate task execution. Second, risk auditing proactively examines high-risk operations. Yet, the auditing process itself would introduce additional exploitable actions that violate security boundaries. To evaluate above defects we found, we propose Conartist, a cascaded adaptive prompt injection framework comprising two progressive stages. First, Conartist employs a goal-pollution strategy to establish deceptive causal dependencies between legitimate user objectives and malicious operations, progressively embedding attack steps into legitimate task workflows. However, these task-coupled attacks remain susceptible to risk auditing. To address this limitation, Conartist further analyzes security-auditing feedback from controlled attack exploration to identify exploitable auditing patterns. Conartist then adaptively refines its deception strategies to either avoid triggering risk auditing or induce additional high-risk operations. Extensive experiments across five backbone models demonstrate the effectiveness of Conartist, achieving attack success rates of 32.12% on 576-instance tool use benchmark and 66.67% in the Reddit GUI benchmark, outperforming the SOTA attack by 14.41 and 29.17, respectively. By analyzing one of the most popular Agent, Openclaw, we furthermore concluded seven realistic exploitable attack patterns, which reveals that security mechanisms designed to prevent malicious actions can themselves be manipulated to facilitate attacks.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
