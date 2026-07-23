# 🔐 大模型安全相关研究 | 2026年07月24日

> 本类共 **11** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [JailMeter: An Evidence-Based Evaluation Framework for Jailbreak Attacks on Large Language Models](https://arxiv.org/abs/2607.19424)

**<font color=#1a73e8>作者：</font>** Qingjia Huang, Jingyu Zhang, Jianguo Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The assessment of jailbreak attacks against large language models currently suffers from inconsistent evaluation criteria and methods, leading to unreliable estimates of attack success rates. We propose JailMeter, an evidence-based evaluation framework designed to more faithfully measure jailbreak effectiveness. Inspired by the Information Bottleneck theory, JailMeter applies dual-feedback optimization to filter jailbreak noise from model responses while preserving content relevant to the original malicious question. This process produces concise evidence for a rigorous assessment under which an attack is validated only when the response captures the malicious intent and delivers a complete answer, thereby signaling a substantive bypass of model safety alignment. We evaluate JailMeter on JailMeter-Eva, a challenging benchmark containing 330 human-labeled, non-rejected jailbreak instances. JailMeter achieves an accuracy of 97.27%, substantially outperforming existing evaluation methods. To support large-scale evaluation, we further distill JailMeter into a small language model, JailMeter\textsubscript{SLM}, which maintains comparable reliability with significantly reduced computational costs. Code and dataset are available at this https URL.

---


### 2. [ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems](https://arxiv.org/abs/2607.19430)

**<font color=#1a73e8>作者：</font>** Elias Hossain, Md Mehedi Hasan Nipu, Fatema Tuj Johora Faria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions. Existing defenses guard only the input boundary (IBProtector, Llama Guard, perplexity filters, SmoothLLM) or run outside the application as opaque, stochastic provider-side filters. We show this gap carries a consequence rarely measured: on a 2,100-trace evaluation across eight attack families, five defenses, and three model backends, an undefended pipeline that appears fully safe under standard reporting (attack success 0.000 on tool- and memory-poisoning) owes that safety almost entirely to the cloud provider's server-side filter (54 of 60 blocks on Azure GPT-5), and silently shifts to the agent model's own alignment on a backend without such a filter. Outcome-only reporting hides this dependence. We present ChannelGuard, a training-free defense-in-depth framework placing information-bottleneck gates on every inter-agent channel; each scores channel text against an adversarial phrase bank by embedding similarity and deterministically passes, compresses, or blocks it, adding no LLM call, while an attribution method records which layer stopped each attack. ChannelGuard's tool-output gate blocks Tool Poisoning 30 of 30 at the application layer, identically across Azure GPT-5, Anthropic Sonnet 4.5, and Anthropic Haiku 4.5, whereas the undefended pipeline shifts entirely across backends; it also lowers Prompt Injection attack success by half (0.333 to 0.167) and preserves GSM8K accuracy exactly (0.867). White-box adaptive paraphrase evades every embedding gate, where a perturb-and-vote baseline does better. An extended appendix adds baselines, ablations, sweeps, a benign-preservation analysis, and a judge audit (kappa = 0.900), at a total cost of 47.36 USD.

---


### 3. [Integrity of peer-to-peer distributed LLM inference under malicious nodes](https://arxiv.org/abs/2607.19490)

**<font color=#1a73e8>作者：</font>** Mert Cihangiroglu, Antonino Nocera  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Peer-to-peer distributed inference executes a Large Language Model (LLM) on pooled consumer hardware by spreading its layers across many nodes. Every request passes through nodes that are owned and controlled by multiple independent parties. However, in this setting, any party can tamper with the output of its layers to corrupt the end result. Recomputing the forward pass on trusted hardware can catch this, but it introduces additional computational cost. The scientific literature includes several prior integrity-checking approaches, such as known-answer traps for image classifiers and cryptographic commitments. However, these solutions test only the exact correctness and do not account for the ordinary variation that may arise between benign nodes. In this paper, we propose a method that checks the output integrity by measuring the variation in the activations that each node passes to the next. A peer who wants to use the network selects a small set of secret canary inputs whose correct activations are known in advance and mixes them into regular traffic. Because the peers cannot tell a canary from a real query, any tampering node corrupts them as well. The deviation from the known reference then reveals malicious activity: benign nodes exhibit only minor variation from hardware-induced noise, whereas tampered nodes deviate far more. We treat the identification of malicious nodes as a probabilistic test that separates two drift distributions, without relying on a fixed threshold. We study 408 configurations with metrics and success criteria fixed before any experiment ran; the detector reaches AUROC 1.0, correctly ranking the malicious shard above every benign shard on every canary in every configuration.

---


### 4. [Twin Agent: Context Residual Compression for Privilege Separated Agents](https://arxiv.org/abs/2607.19595)

**<font color=#1a73e8>作者：</font>** Zhanhao Hu, Dennis Jacob, Xiao Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are vulnerable to security risks, such as prompt injection attacks from untrusted context that manipulate downstream reasoning and tool use. Existing secure-by-design approaches mitigate this risk by separating untrusted observations from privileged execution and careful control of information flow, but often degrade utility and require extensive task-specific engineering. We thus propose Twin Agent, a general privilege separation design pattern inspired by residual coding in the agent context. Twin Agent consists of two nearly symmetric agents: an Explore Agent that inspects untrusted information and a Safe Agent that executes privileged actions. The Explore Agent is conditioned on the Safe Agent's current context and communicates only compact hints to the Safe Agent about the next action to take. This design reduces the information needed to preserve task utility and thus achieves a better security--utility tradeoff, which we empirically verify by measuring how utility and attack success change as the length of hints varies. We evaluate Twin Agent on long-horizon software engineering tasks with SWE-bench Lite and on heterogeneous multi-tool interaction tasks with AgentDojo and DecodingTrust-Agent. Across both benchmarks, Twin Agent preserves high task utility while preventing prompt injection attacks, outperforming both undefended agents and privilege separation baselines.

---


### 5. [FedLSG: LLM-Enhanced Semantic Calibration for Federated Graph Backdoor Defense](https://arxiv.org/abs/2607.19674)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Yabin Peng, Wei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Graph Neural Networks (FedGNNs) are highly vulnerable to backdoor poisoning, yet existing defenses typically rely on rule-based approaches that lack semantic understanding, making them vulnerable to stealthy triggers and harmful to benign structures. To solve this, we present FedLSG, the first framework that integrates large language models (LLMs) into federated graph backdoor defense. FedLSG introduces a graph and behavior to text grounding scheme that transforms local graph structures and client update behaviors into semantically rich natural language representations. The framework further adopts a lightweight student-teacher architecture. On the server side, a full scale LLM serves as a teacher, providing global contextual guidance and evaluating client updates during aggregation to identify potentially malicious participants. On the client side, a LoRA-based student is maintained to perform semantic reasoning, to suppress the influence of edges associated with backdoor triggers. By enabling semantic interpretation of both graph patterns and client behaviors, the framework adaptively incorporates rule-based signals into message passing and client aggregation for defense. Experiments demonstrate that FedLSG significantly improves resistance to backdoor attacks without compromising graph integrity.

---


### 6. [GhostPrompt: Cross-Image Adversarial Prompt for Vision-Language Models](https://arxiv.org/abs/2607.19683)

**<font color=#1a73e8>作者：</font>** Li Zeng, Zeyu Ye, Meng Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are known to be vulnerable to adversarial attacks, where subtle perturbations to images or texts induce erroneous outputs. However, most text-based attacks are adapted from language-model-centric methods, in which the visual input is fixed during optimization, resulting in adversarial prompts that are tied to specific images and thus limiting their attack effectiveness. To this end, we first introduce a new research perspective: cross-image transferability for adversarial prompts. We then propose GhostPrompt, an adversarial prompt that is optimized once and reused to steer VLM outputs toward attacker-specified responses across diverse images. GhostPrompt employs a joint optimization that distills image-invariant adversarial features into the prompt by "worst-case" generation. Specifically, it alternates between constructing hard visual conditions for the current prompt and updating the prompt to remain effective under these conditions. Extensive experiments on prevalent VLMs verify that \ourmethod achieves an improvement of over 30% in attack success rates compared to state-of-the-art (SoTA) baselines, while reducing computation time by ~70%. Our code is avalable at this https URL.

---


### 7. [An Automated Framework for Extracting Reachable Attack Chains from Cyber Threat Intelligence Reports](https://arxiv.org/abs/2607.19742)

**<font color=#1a73e8>作者：</font>** Wenbo Hou, Ning Hu, Xueping Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber Threat Intelligence (CTI) reports richly describe real-world attack processes, but their unstructured narratives cannot be directly used for automated attack-path reasoning. Existing CTI extraction methods focus on indicators, entities, or TTP labels without modeling the execution conditions and resulting states of each attack step, so the extracted knowledge supports neither state matching nor reachability analysis across multi-stage attack chains. This paper proposes an automated framework that extracts reachable attack chains by modeling each attack step as an attack unit of preconditions, an attack behavior, and postconditions. A multi-stage pipeline assisted by large language models (LLMs) extracts attack behavior skeletons, recovers their preconditions and postconditions, normalizes them into predefined predicates, and repairs broken dependencies; the resulting units are compiled into Datalog-style rules for attack-goal reachability reasoning. On a dataset of 20 CTI reports containing 334 human-validated annotated steps, our framework achieves higher annotated-step coverage than representative CTI extraction systems in recovering attack behaviors. Moreover, by explicitly generating preconditions and postconditions, it produces attack units that are more complete and consistent than those generated by end-to-end LLM baselines. On the extracted chains, Datalog inference reaches the specified attack goal in 19 of 20 reports, while backward search yields 34 attack paths under the generated rules. The source code and experimental artifacts are available in an anonymized repository. .

---


### 8. [DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection](https://arxiv.org/abs/2607.19829)

**<font color=#1a73e8>作者：</font>** Weiwei Qi, Zefeng Wu, Zhilin Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most existing LLM safety evaluation and defense methods follow a static formulation: jailbreak vulnerabilities are evaluated with fixed attack methods, and guardrails are trained on fixed malicious prompt datasets. However, real-world adversaries continuously evolve their capabilities and expand the attack space. To address this challenge, we propose DARWIN, an evolutionary attack-defense framework that formulates jailbreaking as an open-ended evolution process and continuously updates guardrails through an evolving attack-defense loop. DARWIN-Attack is an evolutionary adversary that expands its capabilities through strategy discovery, mutation, selection, and feedback-driven composition. It collects strategies from broad external sources, generates new variants through self-reflection and genetic evolution, and retains effective strategies based on their performance against aligned LLMs. During attack execution, DARWIN-Attack adaptively selects and combines evolved strategies according to feedback from target LLMs and guardrails. Across frontier models and guardrails, it achieves state-of-the-art attack success rates, including nearly 100% on DeepSeek-V4-Pro and YuFeng-XGuard and over 90% on GPT-5.5. On the defense side, we introduce DARWIN-Guard, an online adversarial training paradigm that iteratively learns from emerging adversarial samples generated by DARWIN-Attack. To improve robustness without sacrificing utility, DARWIN-Guard jointly trains on malicious and benign disguised queries, encouraging the model to identify underlying intent rather than superficial attack patterns. DARWIN-Guard achieves an average unsafe recall of 91.6% across 12 safety benchmarks, outperforming strong guardrails such as YuFeng-XGuard and Nemotron Guard, while maintaining a nearly 100% pass rate on standard benign datasets.

---


### 9. [Defense Against LLM Backdoors using Critical Neuron Isolation Pruning](https://arxiv.org/abs/2607.19894)

**<font color=#1a73e8>作者：</font>** Yuxi Li, Zhibo Zhang, Kailong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are vulnerable to backdoor attacks, where hidden triggers induce malicious outputs. Existing defenses generally fall into inference-time detection or training-time mitigation, but face two key limitations. First, they focus on fine-tuning-based backdoors (e.g., PEFT modules) and fail to address insidious model-editing attacks that bypass training pipelines. Second, they target simple classification settings and do not naturally extend to open-ended LLM generation and do not naturally extend to the open-ended generation characteristics of LLMs. Consequently, these methods focus on surface-level behavioral patterns while neglecting the deeper representational causes of malicious activations. This lack of mechanistic understanding forces defenses to depend on empirical heuristics, limiting their robustness, generality, and practical applicability in real-world LLM deployment.
To bridge this gap, we introduce DeCNIP (Defense with Critical Neuron Isolation Pruning), which leverages representational analysis to identify and neutralize backdoors in a unified pipeline. Specifically, DeCNIP identifies trigger-like behaviors by optimizing a cross-entropy loss between harmful prompts with candidate tokens and benign inputs. This representational discovery exposes latent threats by uncovering mechanisms through which triggers hijack model weights. It then isolates Backdoor Critical Neurons (BCNs) and prunes them selectively to remove malicious influence while preserving model utility. Extensive evaluations on six open-source LLMs and two benchmark datasets demonstrate that DeCNIP achieves over 95% relative reduction in Attack Success Rate (ASR), outperforming seven state-of-the-art defenses with only 0.1% neuron intervention. Moreover, it maintains 97% of the model's performance on normal benchmarks, demonstrating its efficacy, robustness, and scalability.

---


### 10. [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/abs/2607.19957)

**<font color=#1a73e8>作者：</font>** Yichi Zhang, Zhiqi Wang, Huan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Key-Value (KV) cache reduces inference latency in large language models (LLMs). Traditional prefix-based reuse has low cache hit rates across inference requests because it requires exact token and position matches. To improve efficiency, recent system optimizations introduce position-independent KV reuse, allowing KV cache to be reused whenever identical text chunks appear, regardless of their position in the sequence.
We show this design introduces a new threat, KV Cache Hijacking. Since KV caches are retrieved by token match but encode the context in which they were originally computed, the KV tied to a benign-looking token chunk may encode an attacker-controlled prefix. When later reused in a victim query, this contaminated KV silently hijacks the model's behavior, even if no attacker-controlled text appears in the input.
We introduce HIJACKKV, the first attack framework that systematically exploits this vulnerability, demonstrating its severity and practicality. HIJACKKV optimizes an attacker-controlled prefix, so that the KV computed for a subsequent common benign text encodes the attacker's goal, while the text remains unchanged for future cache hits. HIJACKKV achieves an average 94% success rate in a single attempt, remains effective under realistic constraints including low hit rates (10%) and frequent recomputation (50%), persists over multi-turn interactions, and transfers across models in black-box settings. We further provide design insights for building secure KV reuse systems.

---


### 11. [Small, Free, and Effective: Orchestrating Open-Weight Small Language Models to Outperform Single LLM for Malware Analysis](https://arxiv.org/abs/2607.20216)

**<font color=#1a73e8>作者：</font>** Adel ElZemity, Shujun Li, Budi Arief  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware analysis demands rapid interpretation of complex detonation reports spanning filesystem, network, and process behaviours. While large language models (LLMs) demonstrate impressive capabilities for technical artifact interpretation, the opacity and escalating API costs of closed-weight frontier models motivate exploration of open-weight alternatives. However, many open-weight models are large, demanding significant compute resources and incurring non-trivial hosting costs that place them beyond reach for resource-constrained deployments. This paper investigates whether orchestrated ensembles of small language models (SLMs) can match or exceed single LLM performance on structured questions about malware detonation reports. We established baselines by testing eleven open-weight SLMs, three cyber security pre-trained models, and six frontier LLMs on Meta's CyberSecEval Malware Analysis benchmark. We then designed and evaluated four orchestration architectures: (i) a multi-agent pipeline that decomposes analysis into structured evidence-collection and reasoning stages, (ii) an adversarial debate framework in which two agents iteratively critique each other's reasoning, (iii) a hierarchical consultation system that pairs a general-purpose SLM with a cyber-specialised expert model, and (iv) a hybrid architecture that combines evidence-grounded pipelines with adversarial debate reasoning. The hybrid system (Qwen3-4B with Foundation-Sec-8B) achieved 35.30% overall accuracy, exceeding the strongest cyber-specialised baseline (22.54%) and the strongest ungrounded frontier baseline (34.77%); when given the same evidence pipeline, grounded Gemini remained the strongest configuration at 38.22%. These findings show that evidence-grounded orchestration can substantially improve the performance of collaborative SLMs for supporting interpretation of malware detonation reports.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
