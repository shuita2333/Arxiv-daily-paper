# 🔐 大模型安全相关研究 | 2026年09月30日

> 本类共 **20** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [What Drives Dialectal Jailbreaks? An Ablation of Surface Form, Cultural Framing, and Strategy Banks](https://arxiv.org/abs/2609.31664)

**<font color=#1a73e8>作者：</font>** Qingyang Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that obscure language registers can weaken large language model refusal behavior, especially when paired with black-box prompt optimization. It remains unclear whether failures stem from non-standard surface form, culturally grounded framing, or optimization over an expressive prompt-strategy space. We study Chinese registers by extending a classical-Chinese red-teaming framework to Shanghainese and Cantonese and running a 36-cell ablation across surface forms, strategy-bank variants, and two target models. The main finding is corrective: dialectal surface form is neither necessary nor sufficient for high attack success. Non-optimized English, Mandarin, and naive dialect translations remain below 8\% attack success rate, whereas all conditions that retain an optimizer-controlled strategy bank reach 98--100\%. A culture-neutral generic strategy bank reaches the same ceiling at near-single-query cost, further indicating that strategy-bank expressiveness, rather than dialectal or cultural content, accounts for most of the observed effect. Dialect choice still affects query efficiency and response severity, and qualitative coding identifies recurring high-level mechanisms such as semantic glossing and procedural scaffolding. We qualify the absolute ceiling-level attack success rate by showing sensitivity to judge calibration and noting that the design does not fully separate one-shot strategy construction from iterative search.

---


### 2. [SilentCall: Hidden Tool-Call Backdoors in Open-Weight Agents, and How to Catch Them](https://arxiv.org/abs/2609.32021)

**<font color=#1a73e8>作者：</font>** Bhanu Pallakonda, Mikkel Hindsbo, Sina Ehsani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight tool-calling agents are adopted on evidence of merit, usually benchmark scores and a record of reliable use. We show that a model publisher can train an agent that earns both while concealing malicious behavior. Fine-tuned on a mixture of clean and poisoned conversations, our agents answer ordinary requests correctly; once the system date reaches a chosen year, they emit the correct tool call and, alongside it, one that exfiltrates the user's credentials. The exfiltration runs while the user-facing response mentions only the legitimate work. We call this attack SilentCall. Under the trigger, it fires on at least $99.6$\% of requests, and no response ever mentions it. The attack is detectable by three distinct methods, which differ mainly in what a defender needs to run them. A runtime monitor that inspects each tool call before it executes requires no access to the model and catches every instance of the payload we tested at a 1.73% false-positive rate. High-temperature probing requires only the published weights. The weight-distribution audit requires training a benign model with the suspect's recipe, placing it within reach of model hubs but not ordinary users. Alignment benchmarks, by contrast, do not separate poisoned from benign models. SilentCall leaves no trace on standard benchmarks. As tool-using agents spread through the open-weight supply chain, trust in them should not rest on what a model says about its own actions. It has to come from inspecting those actions at runtime, auditing models where they are distributed, and treating tool access as a security surface in its own right.

---


### 3. [Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?](https://arxiv.org/abs/2609.32495)

**<font color=#1a73e8>作者：</font>** Jiahong Dai, Zhuochen Yang, Pengyang Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An agent harness, the code that turns a model into an agent, writes its own record of each run, and that record is all a later reader gets when a run is disputed, investigated or audited. We call a record evidentiary when a reader who was not there can check it without trusting the writer. Across sixteen deployed frameworks, none writes one in full. Hearsay examines the record, not the task: five harnesses run fourteen tasks, three blinded LLM examiners and a human panel read the records, and every excerpt an examiner quotes is checked mechanically for who wrote it. First, the record lets a reader name the fault but not prove how the run went. Examiners name the right fault in 74 to 91% of 140 runs, but the fault can be proved only from two files the benchmark adds; for what happened in between, fewer than one citation in ten lands on anything the harness did not write, and the examiner with the fewest false alarms catches half of the entries we delete, rewrite or fabricate. Second, the remedy is a second author, not a stronger seal on the first. An append-only log of what passes between harness and model, kept outside the harness and read against the record in both directions, reports all 28 omissions and fabrications we made a harness commit as it ran, where a hash chain over the harness's own record passes all 28. Handed the log, examiners keep their fault verdicts but rest more of their citations on what the harness did not write. What makes a record evidence is who writes it, not what is captured.

---


### 4. [Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection](https://arxiv.org/abs/2609.32691)

**<font color=#1a73e8>作者：</font>** Animesh Shaw  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents that invoke privileged tools are vulnerable to indirect prompt injection (IPI), in which adversarial instructions embedded in retrieved data hijack the agent's actions. A growing body of work evaluates defenses against IPI, but the validity of that evaluation is rarely examined. We audit an IPI benchmark and its harness and identify four defect classes -- silent payload non-delivery, attack success scored by tool identity rather than arguments, false-rejection rate conflated with model incapacity, and the absence of an audit trail -- each of which yields a plausible, publishable, and incorrect number. We quantify the distortion by re-scoring identical execution traces under the defective and corrected definitions: on real agent behaviour, the tool-identity scorer reports a 21.7% attack-success rate where the true argument-level rate is 1.2%. In the sharpest case, an open model previously reported at 62.8% registers 0% under the corrected harness -- the prior figure largely an artifact of undelivered payloads and identity-level scoring. We release a harness whose construction makes each defect unrepresentable -- machine-checkable payload placement, argument-level attacker predicates, per-scenario environments, and mandatory trace persistence -- and use it to report three quantities the field does not: whether a compromised agent discloses the attack, the full security/utility operating curve of an LLM-judge defense, and tool-calling capability disentangled from defensive over-blocking. A corrected harness further overturns a reported "capability barrier": a model deemed incapable of tool use is in fact fully capable, its earlier result an artifact of environment mismatch. We argue that evaluation validity is a prerequisite for, not a footnote to, defense claims in agentic security, and provide an instrument that enforces it.

---


### 5. [CertMark: Distortion-Free Multi-Bit Watermarking with Certified Decoding](https://arxiv.org/abs/2609.33332)

**<font color=#1a73e8>作者：</font>** Paweł Batorski, Przemysław Spurek, Paul Swoboda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Leading multi-bit watermarking methods for language models encode messages by biasing the model's next-token probabilities, creating a trade-off between message recovery and text quality. Their decoders typically return the highest-scoring candidate from accumulated token-level evidence, without a certified abstention rule that bounds the probability of outputting an incorrect message. We introduce CertMark, a distribution-preserving multi-bit watermark with certified decoding. Rather than modifying probabilities, CertMark uses the embedded message to seed an exact Gumbel-max sampler, thereby preserving the model's original sampling distribution. We propose two scalable decoders: a model-agnostic, text-only decoder and a model-aware variant that leverages the original next-token distributions for stronger recovery. Both support certified abstention with mathematical bounds on the probability of returning an incorrect message. Across text completion, summarization, and story generation, CertMark matches the perplexity of unwatermarked text while reliably recovering multi-bit messages. The model-aware decoder further achieves higher bit accuracy than probability-biasing baselines. Our code is publicly available at this https URL.

---


### 6. [Climbing the Hill: Prompt Injection Red-Teaming Against Frontier Models with Curriculum Reinforcement Learning](https://arxiv.org/abs/2609.33628)

**<font color=#1a73e8>作者：</font>** Chenlong Yin, Xiaolong Jin, Wei Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt injection is a leading security risk for LLMs and LLM-based applications such as agents. State-of-the-art red-teaming methods for prompt injection leverage reinforcement learning (RL) to train an attacker LLM to generate effective injected prompts. However, when targeting frontier LLMs such as GPT-6-Luna, a major challenge is the cold-start problem: every attack attempt by the attacker LLM fails and thus receives zero reward, providing no signal for learning. In this work, we propose a curriculum learning-based method to address the cold-start problem. In particular, we propose to train the attacker LLM against a sequence of increasingly robust target LLMs, with each stage warm-starting from the attacker LLM obtained in the previous one. However, simply training against a weak target (e.g., GPT-4o-mini) may not sufficiently prepare the attacker LLM to obtain useful learning signals against a frontier LLM (e.g., GPT-5.6-Terra). Instead, we find that the design of the curriculum is critical: after each stage, the attacker LLM needs to partially succeed against the next target LLM such that it can learn from successful attempts to attack the new target. Our extensive evaluation shows that our method can effectively red-team frontier LLMs, achieving an attack success rate (ASR@10) of 93.8\% and 45.0\% against GPT-5.6-Luna and GPT-5.6-Terra on AgentDyn, whereas state-of-the-art RL methods such as RL-Hammer and PISmith achieve 0\% ASR under the same setting. Moreover, we find that the attacker LLM transfers across targets, e.g., an attacker LLM trained to defeat one strong LLM (GPT-5.6-Terra) also succeeds against six other frontier LLMs (e.g., GPT-6-Luna) it was never trained on. Our code is available at \href{this https URL}{here}.

---


### 7. [COGNIT-Guard: Calibrated Standalone Direct-Decision Guardrails with Heterogeneous CPU-NPU Confidence Cascading under Explicit Latency and False-Positive Constraints](https://arxiv.org/abs/2609.33671)

**<font color=#1a73e8>作者：</font>** Hao Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When must a foundation-model safety gateway generate tokens, and when should it directly output a calibrated decision? We study calibrated standalone direct-decision foundation models for real-time pre-ingestion safety guardrails, jointly addressing probability calibration, dual-use false-positive control, and heterogeneous CPU-NPU routing under explicit latency SLOs. Pre-ingestion guardrails must screen prompts prior to target-LLM prefill with low false alarms on benign compliance inquiries; however, shallow classifiers are brittle to phrasing shifts, hidden-state probes require coupling to a target LLM, and generative guards incur high decoding latency and dual-use false positives. We present COGNIT-Guard, coupling a validation-calibrated CPU fast gatekeeper with confidence-gated escalation to an NPU-resident 322M bidirectional direct-decision model (Laya-322M) under an asymmetric false-positive penalty. On the clean unseen DUCS-Bench test split ($N=607$), COGNIT-Guard achieves 98.85% accuracy (McNemar $p = 1.19 \times 10^{-4}$ vs. ML), reduces benign FPR to 0.42% ($1/238$; Fisher's exact $p = 8.23 \times 10^{-4}$ vs. ML), and attains 1.12% ECE and 0.0104 Brier score. On Huawei Ascend 910C NPUs, pure NPU inference runs in 21.77 ms mean latency (45.90 QPS), while the live serial CPU-NPU cascade ($\theta^*_{\mathrm{deploy}}=0.70$) achieves 41.63 ms mean latency (P50: 39.47 ms, 99.23% accuracy, 0.00% FPR). Evaluation on SafetyBench-ZH ($N=2,100$) and comparison against a bi-encoder direct-decision baseline (CLM-8B) disentangle in-domain gains, OOD alignment tax (60.33% $\to$ 56.81% on Laya; 55.10% on domain CLM-8B), and experience replay recovery, restoring OOD accuracy to 64.10%-65.05% and reaching 99.67%-99.84% in-domain accuracy with 0.00%-0.42% FPR.

---


### 8. [The Privacy Fallacy of Crowdsourced Fine-Tuning: Extracting Proprietary Data via Topic-Based Poisoning](https://arxiv.org/abs/2609.33985)

**<font color=#1a73e8>作者：</font>** Sae Furukawa, Alina Oprea  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks. Crowdsourcing user conversations is an established approach to collecting SFT data at scale while reducing the need for costly manual annotation. However, it also allows untrusted users to contribute data to the fine-tuning pipeline. We investigate an underexplored privacy risk arising from this setting: can a malicious user poison a small fraction of the crowdsourced data to amplify extraction of previously unseen instructions contributed by other users? We show that this is possible using only black-box, output-only access to the deployed model. Experiments across four models and two datasets demonstrate substantial increases in training-data extraction: with only 50 poisoned examples, near-verbatim extraction reaches $3.71\times$ the rate without poisoning for Qwen2.5-14B on OpenMathInstruct and $3.08\times$ for Llama-3.1-8B on AceReason. Data filtering also proves largely ineffective in detecting poisoned samples: even the best-performing method achieves only 0.378 in F-1 score, leaving the majority of poisoned samples undetected. These findings demonstrate that seemingly benign crowdsourced contributions can amplify leakage of other records while remaining difficult to identify through data filtering.

---


### 9. [LoRo-Mark:Provably Lossless and Robust Agent Watermarking](https://arxiv.org/abs/2609.34080)

**<font color=#1a73e8>作者：</font>** Haoyang Zou, Yao Wang, Jun Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM agents are increasingly deployed as commercial services, protecting proprietary orchestration logic and tool-use policies is important. We consider agent repackaging: an adversary integrates a protected agent into its own application via API and presents it under its own identity. It may modify parts of execution to obscure the source. The owner typically has only black-box access to the repackaged service, so black-box ownership verification is essential. Agent watermarking embeds ownership evidence into agent behavior for later verification. An effective watermark should satisfy two requirements: losslessness, preserving original functionality, and robustness, keeping ownership evidence recoverable after partial modification of execution. Existing methods often embed signals into behavior selection or execution trajectories, intervene in normal decisions, and offer limited robustness to behavior modification. We propose LoRo-Mark, a provably lossless and robust agent watermarking mechanism. For losslessness, it isolates watermarking into a cryptographically authenticated forensic branch that remains inactive during normal execution and is activated only by owner-authorized requests. By reducing unauthorized branch activation to standard MAC security, LoRo-Mark formally guarantees performance preservation. For robustness, it redundantly distributes ownership information across forensic behavior sequences, enabling reliable recovery under partial behavior substitution and sequence truncation. Experiments across multiple LLM agents show zero degradation on normal tasks and reliable ownership verification under sequence modifications.

---


### 10. [CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents](https://arxiv.org/abs/2609.34463)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Yangchen Ou, Yuhan Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents increasingly rely on external tools and content, exposing them to indirect prompt injection (IPI). This threat has motivated a wide range of defenses, among which training-based defenses are often regarded as most reliable. However, existing training-based defenses are typically optimized on a static distribution of explicit injections. They learn surface-form cues rather than the boundary between serving the user and obeying an injected objective, and therefore fail when malicious intent is folded into a plausible workflow and deferred for several turns. We present CoDeL, a defense that hardens agent against an attack distribution it reshapes as it trains. The defender is updated each round via LoRA-based GDPO under a decoupled reward over safety, task progress, and format compliance, so refusing injections and completing the user's task jointly define fitness. To keep supplying it with the failures worth learning from, a co-evolving prober searches over injection rounds, attack methods, and payloads for injections that still penetrate the current defender, guided jointly by attack success and attack latency so that it preferentially mines breaches the defender notices too late. Each defender update invalidates part of the attack population and forces the next round onto a new frontier, turning the defender's own failures into a moving curriculum. Extensive experiments on three IPI benchmarks, nine baselines, and two base models show that CoDeL reduces attack success rate (ASR) by 88.5% and outperforms other baselines largely (+38.0%). Codes are available.

---


### 11. [AuxMark: Defending Against Unauthorized Agent Distillation via Auxiliary Behavioral Watermarking](https://arxiv.org/abs/2609.34597)

**<font color=#1a73e8>作者：</font>** Yiqing Feng, Haozhe Feng, Shunan Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents can acquire complex capabilities through multi-step interaction and tool use, but their trajectories can also be illegally collected to dis- till student agents. However, existing watermarking methods either do not fit the structured and interactive nature of agent environments or lack reliable effective- ness across tasks and model architectures. We introduce AuxMark, a behavioral watermarking framework for tracing unauthorized agent distillation. AuxMark dynamically inserts safe, non-essential auxiliary action into teacher trajectories, and stores the associated contexts as private evidence cards. To audit a suspicious student model, AuxMark constructs paired real and fake probes from these cards and applies a card-level sign test. This black-box protocol supports both model- level detection and trace-level attribution. Across three agent benchmarks, two teacher agents, and four student architectures, AuxMark detects all 24 distilled models with zero false positives on 48 clean models. It also preserves task utility and remains effective against data flooding, paraphrasing, truncation, and adaptive cleaning attacks. Our code will be released at this URL.

---


### 12. [Backdoor as Probe: Test-Time Adversarial Defense for CLIP](https://arxiv.org/abs/2609.34641)

**<font color=#1a73e8>作者：</font>** Zhongqi Wang, Jie Zhang, Nie Sen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adversarial defense improves the robustness of vision-language foundation models such as CLIP without retraining. However, adversarial activation shifts are typically treated as distortions to suppress, rather than signals to exploit. We turn these shifts into defense signals by repurposing the trigger-to-target mechanism of backdoors. The key is to implant a defender-controlled backdoor as a probe that is weakly activated by clean inputs but strongly activated by adversarial shifts. Based on this insight, we propose \emph{Backdoor as Probe} (BaP), a test-time adversarial defense for CLIP. BaP constructs the probe through a closed-form model edit to a selected MLP layer. It projects the average adversarial activation shift and a defender-specified semantic direction onto the layer's low-energy input and output activation subspaces to obtain the trigger and target directions, respectively. At inference time, adversarial inputs produce measurable responses along the target direction for detection. BaP then selectively rectifies detected inputs by optimizing a small perturbation that steers their representations away from adversarial shifts and toward the clean subspace. Experiments across 16 benchmarks show that BaP improves average robust accuracy from 1.0\% to 52.3\% while retaining clean accuracy, achieving performance comparable to state-of-the-art methods with up to a \(5.7\times\) inference speedup. BaP further shows the generalization to adversarial attacks on large vision-language models. Project page: this https URL

---


### 13. [Jailbreak Context Lingers: Divergent Safety Routing and Its Cross-Task Predictability in Tool Agents](https://arxiv.org/abs/2609.34686)

**<font color=#1a73e8>作者：</font>** Xi Wang, Songlei Jian, Yiming Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models increasingly operate as tool-using agents, post-jailbreak safety feedback is often assumed to serve as a reliable safeguard; however, how lingering jailbreak context shapes subsequent agent behavior remains largely unexplored. To systematically examine this dynamic, we introduce a paired continuation framework across 192 parent tasks spanning 42 domains, evaluating 12,148 analyzed continuation pairs (curated from a 12,288-pair initially design) across eight diverse agents. We find that identical safety feedback induces sharply model-dependent behavioral routing rather than uniform protection: redirecting unsafe trajectories toward legitimate completion (\emph{rescue}), sustaining unauthorized execution (\emph{persistent unsafe}), or triggering over-refusal on benign tasks (\emph{collateral loss}). Through layer-wise activation patching, we discover a shared \emph{late-commit pattern} where causal intervention effects surge sharply near the final layers (relative depths of 0.958--0.984) despite an over 30-fold variation in peak magnitude across architectures. Crucially, critical-layer representations correlate with macroscopic routing outcomes, and intervening at these layers causally alters concrete next-step tool actions. Building on this causal foundation, we test whether localized intervention-derived features can serve as predictive proxies for full-trajectory routing outcomes on unseen parent tasks under leave-one-parent-task-out evaluation, finding that they provide viable predictive signals in responsive agents with peak ROC AUCs reaching 0.675 for \emph{rescue}, 0.777 for \emph{collateral loss}, and 0.702 for \emph{persistent unsafe}. These findings establish a mechanistic lens and a predictive baseline for anticipating the safety and utility trade-offs of post-jailbreak feedback in autonomous agents.

---


### 14. [When Do Model Internals Help? Exploring the Role of Representation Engineering in LLM Safety](https://arxiv.org/abs/2609.34771)

**<font color=#1a73e8>作者：</font>** Tianyi Guan, Jianhui Chen, Liangming Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable AI safeguards require both control mechanisms that reduce unsafe behavior and monitoring mechanisms that detect safety risks during model interactions. Established behavioral safeguards include alignment methods that optimize model outputs and text monitors that assess interaction text. Representation engineering instead reads or modifies internal model states, but the relative strengths of these approaches remain unclear because they are often evaluated under different settings. We present a matched evaluation across two tracks. For safety control, we compare DPO, a behavioral alignment method, with three representation steering methods across robustness, practicality, and granularity. DPO provides the strongest overall control and generally improves with increasing training data, although its safety can degrade after subsequent benign fine-tuning. Representation steering remains competitive primarily in low-data settings, particularly with high-quality contrastive data. For safety monitoring, we compare representation probes with fine-tuned and open-weight text monitors across full-response detection, early detection, and computational cost. Specialized text monitors achieve the strongest overall detection accuracy, while representation probes remain competitive at substantially lower marginal cost. Finally, monitor-guided interventions recover much of the safety lost by DPO after benign fine-tuning, with little additional over-refusal. Overall, representation engineering does not generally replace behavioral safeguards, but offers practical advantages under specific conditions and can provide complementary safety benefits.

---


### 15. [CoSec: Benchmarking Agent Security in Communities](https://arxiv.org/abs/2609.34790)

**<font color=#1a73e8>作者：</font>** Hao Chen, Wenhui Dong, Ye Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must complete legitimate tasks and prevent unauthorized disclosure of protected information. Existing evaluations do not fully examine these risks in agent systems. We introduce \textbf{CoSec}, an executable benchmark for evaluating privacy and authorization enforcement in LLM agent systems operating within and across communities. CoSec contains 208 canonical scenarios spanning fixed and evolving boundaries, protected information belonging to the agent owner or other participants, and attacks through dialogue, environmental content, persistent memory, and composed workflows. CoSec executes complete agent systems with persistent sessions, memory, files and tools. It verifies information flows against the active authorization state using execution traces and artifacts. Across harness and model configurations, agents frequently complete benign tasks but violate privacy and authorization boundaries. Privacy behavior varies across harnesses, attack surfaces, and community states, revealing how memory, files, tools, and workflows can carry protected information beyond its authorized scope. These findings show that task utility does not imply privacy or authorization compliance and that authorization in community settings remains an unresolved security challenge for persistent LLM agents.

---


### 16. [DeShortcut-Align: Decoupling Spurious Shortcuts for Robust Safety Alignment in Large Reasoning Models](https://arxiv.org/abs/2609.34896)

**<font color=#1a73e8>作者：</font>** Qirui Liu, Yichen Sun, Yan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment of large reasoning models (LRMs) via supervised fine-tuning (SFT) and reinforcement learning (RL) often yields near-perfect safety scores, yet this apparent success comes at the cost of severe over-refusal and degraded general capabilities. Through systematic empirical analysis, we find that these failures are closely associated with the learning of spurious shortcuts rather than robust intent-sensitive safety evaluation. Specifically, we identify two dominant shortcuts: formatting shortcuts, where refusal behaviors are overly bound to structural prompt templates that frequently appear in safety alignment corpora; and lexical shortcuts, where sensitive keywords reflexively trigger refusals on benign queries. To mitigate reliance on these shortcuts, we propose DeShortcut-Align, a shortcut-decoupling alignment framework that reduces dependence on superficial cues. DeShortcut-Align operates across three coordinated stages: (1) Refusal Sensitivity Attribution, which masks input tokens to quantify their impact on the final refusal response distribution; (2) Attribution-Guided Contrastive Augmentation, which constructs benign contrastive samples using high-sensitivity tokens to mitigate lexical shortcuts; and (3) Counterfactual Consistency Regularization, which constructs template-ablated states via attention blinding to enforce decision consistency across SFT and RL, mitigating formatting shortcut dependence. Experiments on 7B and 14B models demonstrate that DeShortcut-Align significantly improves robustness against template-stripping bypass attacks (reducing performance drops by up to 72%), substantially reduces over-refusal by over 58%, and better preserves general-purpose reasoning capabilities, thereby mitigating the alignment tax commonly observed in safety training.

---


### 17. [LENS: The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation](https://arxiv.org/abs/2609.35155)

**<font color=#1a73e8>作者：</font>** Kaisheng Fan, Yishu Gao, Xunzhu Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) aggregates evidence from multiple external documents, yet this joint integration creates an underexamined vulnerability: attack effects absent in individual documents can emerge through set-level composition. Existing coordinated attacks do not explicitly enforce that every proper subset remains insufficient in frozen single-round RAG. We formalize set-level compositional poisoning, where documents designed to remain individually plausible jointly redirect RAG outputs to a target answer, while proper subsets fail to induce the target on their own. To construct such attacks, we propose LENS, a generator-black-box multi-agent framework that casts construction as constrained evidence composition. LENS factorizes target inference into a query-conditioned interpretation lens and complementary facts, then uses a nested dual-loop workflow to concentrate steering in the full set while suppressing subset leakage. The outer loop plans the interpretation lens and semantic roles; the inner loop synthesizes documents and applies counterexample-guided repair. Across four benchmarks and three generators, returned packets achieve 0.852 full-set ASR and 0.784 post-retrieval ASR@5, while their strongest proper subsets reach only 0.069. Against construction baselines evaluated on the same frozen manifest, LENS improves all-attempt E2E-Strict@5 from 0.244 to 0.363, a 48.8% relative gain. A blinded human audit finds that 68.3% of returned packets combine an incorrect target, a definite answer-criterion shift, and no target entailment under the original semantics. Across four published defenses, LENS attains the highest defended all-attempt ASR@5, exceeding the strongest baseline by 0.141 on average. Together, these results establish evidence composition as a distinct RAG security boundary and position LENS as a stress test for defenses that reason over document sets.

---


### 18. [TANGO: Watermarking Masked Diffusion Language Models in Token Pairs](https://arxiv.org/abs/2609.35224)

**<font color=#1a73e8>作者：</font>** Kasra Arabi, Nir Weinberger, Micah Goldblum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked-diffusion language models fill in masked positions in parallel and in no fixed order. Most practical text watermarks assume left-to-right generation. They key each token to the tokens before it, and in a diffusion model those tokens may still be masked. A fixed green list needs no such context, but it favors the same tokens at every position, so these tokens appear more often in watermarked text. An attacker who compares token frequencies in watermarked and unwatermarked text can recover the list and forge text that the provider's own detector accepts. We present TANGO, a watermark for masked-diffusion language models that keys each new token to a nearby token that is already unmasked. A secret key splits the vocabulary into color classes, and TANGO biases the new token toward a color determined by the key and the nearby token's color. The watermark is therefore embedded in pairs of tokens. Because the favored color changes from position to position, token frequencies stay much closer to those of unwatermarked text than under a fixed green list. Detection needs only the text and the key, and it does not assume any unmasking order. On two masked-diffusion models, TANGO detects nearly all unedited watermarked texts and most edited ones, and frequency attacks that forge the fixed green list fail against it.

---


### 19. [Jailbreaks for Black-Box Uncertainty Quantification in Large Reasoning Models](https://arxiv.org/abs/2609.35350)

**<font color=#1a73e8>作者：</font>** Lucas Biechy, Cédric Eichler, Adrien Boiret 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Reasoning Models (LRMs) excel at complex reasoning, alignment through reinforcement learning often induces systemic overconfidence. In production environments, where logits may be unavailable, robust black-box uncertainty quantification (UQ) is essential for trustworthiness and safety. Focusing on question-answering for LRMs, we show that existing black-box methods, such as paraphrase-based self-consistency and confidence verbalization, offer little to no improvement over simple repeated sampling, suggesting that alignment suppresses useful output variability. We introduce prompt-level relaxation operators that broaden the model's effective output distribution by approximating the effect of an optimal policy obtained with a stronger KL-regularization parameter, hence closer to the reference model. Theoretically, we demonstrate that relaxation improves calibration. We propose Jailbreak for Uncertainty (J4U), a jailbreak-derived technique for UQ that empirically reproduces the behavioral signatures predicted by our relaxation theory. Across 3 datasets and 4 LRMs, including a closed-source production model, J4U's improvement over repeated sampling achieves statistical significance in up to 6 times more LRM-dataset-metric settings than the strongest black-box UQ state-of-the-art baseline we evaluate, with average ECE reductions up to 5 times larger. These results provide a practical tool for UQ in black-box LRM deployment.

---


### 20. [Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoor Triggers and Preserves Desired Traits](https://arxiv.org/abs/2609.35356)

**<font color=#1a73e8>作者：</font>** Kajetan Dymkiewicz, Tim Farrelly, Adam Práda 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning can teach language models undesired behaviours alongside desired ones. Inoculation prompting (IP) aims to limit unwanted generalisation by requesting the undesired behaviour during training and removing the request at inference. However, undesired behaviour can still appear under unrelated prompts. IP can also hinder learning of the desired behaviour. We address these limitations in settings where both behaviours co-occur in most training examples, so filtering out examples with undesired behaviour leaves only a small clean subset. We introduce stratified inoculation prompting (SIP). SIP leverages a small clean subset to demonstrate that desired behaviour should persist without the undesired one across different contexts. SIP oversamples these clean examples under diverse non-eliciting prompts while inoculating the rest. SIP substantially reduces expression of undesired behaviour while preserving more of the desired behaviour than IP. These gains persist even when we extend IP to oversample the same clean subset at the same rate as SIP. Moreover, SIP yields lower emergent misalignment rates in all harmful-advice setups we tested. SIP can be further extended to limit the undesired behaviour even under prompts that explicitly request it. We introduce backdoor dilution, which weakens expression under the inoculation prompt, and password-locked inoculation, which concentrates elicitation on a designated password. Taken together, our findings show that changing the training contexts for a small clean subset can significantly improve selective generalisation.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
