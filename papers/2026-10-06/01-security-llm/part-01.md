# 🔐 大模型安全相关研究 | 2026年10月06日

> 本类共 **10** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Intent-Hiding Jailbreaks: An Information-Theoretic Framework for Compositional Attacks](https://arxiv.org/abs/2610.02302)

**<font color=#1a73e8>作者：</font>** Fengwei Tian, Ravi Tandon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that large language models (LLMs) can be vulnerable to jailbreak attacks in which harmful intent is obscured through composition with benign tasks. A harmful request refused in isolation may elicit a different response when embedded within a larger, seemingly benign query. We study these compositional intent-hiding jailbreaks from an information-theoretic perspective. Our formulation associates each task with an estimated probability of being judged harmful: the average over the full task collection defines the prior probability of harmful intent, while the average over a selected bundle containing the target defines the posterior. Selecting auxiliary tasks so that these averages agree, which we call prior-posterior matching, leaves the estimated intent unchanged even though the harmful target remains in the bundle.
We study two settings that differ in whether query construction is part of the optimization. In the query-independent setting, tasks are selected without regard to how they will be expressed in the final query. We show that exact prior-posterior matching under a bundle-size constraint is computationally hard, derive an optimal water-filling solution for fractional weights, and characterize the smallest bundle satisfying a prescribed safety threshold. In the query-dependent setting, task selection and query construction are considered jointly, and intent concealment and target preservation are evaluated on the resulting query. We evaluate jailbreak effectiveness and preservation of the target behavior across bundle sizes, query generators, and several open-source models. These results show that compositional queries can elicit target behaviors beyond the direct-request baseline under the evaluated search budgets, while revealing a trade-off: as bundle size increases, response-level target preservation tends to decrease for several models.

---


### 2. [Mitigating Private Data Leakage in LLMs with Whiteout](https://arxiv.org/abs/2610.02418)

**<font color=#1a73e8>作者：</font>** Anna Yoo Jeong Ha, Ronik Bhaskar, Haitao Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) are trained on massive, largely unfiltered datasets, including content scraped from nearly every accessible website and user inputs. As a result, LLMs often memorize and reproduce personally sensitive information (PSI) such as birth dates, phone numbers, and home addresses. This leads to significant privacy risks, particularly for high-profile individuals such as executives, politicians, and judges. Existing mitigations largely rely on machine unlearning. However, these methods often remove more information than needed, degrade model utility and safety, and are highly vulnerable to attacks.
This paper presents Whiteout, a practical tool that, upon requests by individuals, prevents LLMs from regurgitating their genuine PSIs, by overwriting them using precise and carefully designed obfuscation samples. We evaluate Whiteout on modern LLMs of varying sizes and makers, including a widely-used OpenAI model. Results show that Whiteout effectively prevents disclosure of the targeted PSIs, has negligible impact on model utility and safety, and outperforms existing alternatives. We also test Whiteout against a wide range of countermeasures, from black-box attacks like jailbreaking to white-box adaptive attacks like relearning and quantization. Finally, we conclude with a discussion on the security and ethical implications of Whiteout.

---


### 3. [MLCommons Jailbreak Benchmark v1.0](https://arxiv.org/abs/2610.02827)

**<font color=#1a73e8>作者：</font>** Carsten Maple, Cagatay Yucel, Isaac Holeman 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI systems are designed to refuse hazardous requests. A jailbreak is a prompt crafted to bypass those safeguards and elicit outputs that the system would normally refuse to provide. The MLCommons Jailbreak Benchmark v1.0 provides an end-to-end methodology for evaluating the robustness of large language models to single-turn, text-based jailbreak attacks. It combines criteria-driven system and attack selection, paired baseline and adversarial evaluation, human annotation, automated evaluator calibration, scoring, grading, and risk-calibrated disclosure within a single benchmarking pipeline. The benchmark evaluates eight open-weight systems using 264 seed prompts spanning eleven hazard categories and representative attacks drawn from the MLCommons Jailbreak Taxonomy. Responses are assessed using the AILuminate Assessment Standard v1.4, and robustness is measured through the Resilience Gap: the change in safety performance between baseline and adversarial conditions. Across all evaluated systems and attacks, the unsafe-response rate increased from 11.08% under baseline conditions to 18.65% under jailbreak conditions, producing an average Resilience Gap of 7.57%. Accessible systems showed a larger mean gap, while attack effectiveness varied substantially across attack categories and hazards. The benchmark also examines evaluator reliability and sources of measurement error. Beyond reporting results, Jailbreak Benchmark v1.0 establishes a reproducible methodological foundation for comparative jailbreak evaluation and for future expansion across systems, attacks, hazards, and evaluation methods.

---


### 4. [DNAlign: Dynamic Null-Space Safe Alignment for LLMs](https://arxiv.org/abs/2610.02844)

**<font color=#1a73e8>作者：</font>** Jisheng Dang, Yushuo Zhao, Dewei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ensuring the safe and reliable deployment of large language models (LLMs) remains a fundamental challenge. Existing safety alignment approaches either incur high computational cost or unintentionally disrupt the model's core knowledge, leading to degraded fluency and factual accuracy on benign tasks. This reveals a persistent trade-off between safety and utility. We propose DNAlign, a lightweight alignment framework that integrates control-theoretic optimization with null-space projection. By treating the LLM as a dynamic system, the proposed framework introduces controllable perturbations to steer generation toward safe behavior. A key component is the projection module, which restricts these perturbations to the harmful-related subspace derived from neutral hidden states, thereby preserving general knowledge and response quality. A value function trained on human preference data adaptively optimizes the control signals to align with human safety preferences. Extensive evaluations across multiple LLM backbones demonstrate that our framework consistently reduces harmful outputs while maintaining fluency, coherence, and factual utility. It achieves superior overall performance compared to prior alignment baselines without sacrificing generation diversity. These results indicate that the proposed framework provides an effective and practically deployable solution for safe LLM alignment. Code is available at this https URL.

---


### 5. [Bounded Reachability & Jailbreak Detection via Contraction-Constrained State Space Models](https://arxiv.org/abs/2610.02853)

**<font color=#1a73e8>作者：</font>** Omanshu Thapliyal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety heads are lightweight classifiers attached to pretrained language models for flagging harmful inputs before generation. Their empirical detection performance has been studied, but their formal robustness properties remain largely unexplored. We ask when a State Space Model (SSM)-based safety head can be certified to produce the same prediction for all inputs within a bounded embedding-space perturbation. We prove that the answer turns on a single condition: the $l_\infty$ norm of the state transition matrix must satisfy $\norm{A}_\infty<1$ (the \emph{contraction condition}), which enables exact interval bound propagation (IBP) certification for linear time-invariant classifiers. When the contraction condition holds, the reachable output interval has bounded steady-state width and examples can be certified as robustly classified. When it fails, the interval grows exponentially with sequence length and certification is impossible at any practical perturbation radius. We enforce contraction with a hinge penalty and show on toxic comment data that certified fraction improves from 41\% to 59\%, with a sharp empirical phase transition at $\norm{A}_\infty=1$ matching the theory. Applying a contraction-regularized S4 head to jailbreak detection on JailbreakBench, we achieve a zero-shot transfer to AdvBench (DR=0.994) and HarmBench (DR=0.988). A logistic regression on mean-pooled Mamba-130M embeddings matches or exceeds the S4 head on every detection metric, confirming that harmful intent is already linearly separable in the embedding space. The S4 safety head's contribution is not superior discrimination but the formal certification that no probe-based approach provides.

---


### 6. [HASTE: Evolving Agent Harnesses Against Emerging Attacks Using Sparse Evidence](https://arxiv.org/abs/2610.02920)

**<font color=#1a73e8>作者：</font>** Xiqiao Xiong, Moxin Li, Zhixin Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses play a critical role in defenses by enforcing safety constraints to prevent unsafe actions. However, rapidly emerging attacks outpace manual harness adaptation, motivating automated harness evolution. Yet the signals available for harness evolution are often sparse, such as brief descriptions or a few attack examples in threat reports and preprints. To address this limitation, we introduce HASTE, a multi-agent framework that evolves agent harnesses from sparse threat evidence through an adversarial interplay between safety-specification generation and attack-case generation. Safety specifications guide harness updates toward addressing identified safety vulnerabilities, while attack cases probe for remaining safety vulnerabilities after each update. By feeding evaluation outcomes back into both processes, HASTE enables harness evolution against emerging attacks beyond the initially observed evidence. Experimental results across multiple backbone models, attack types, and evidence forms show that HASTE consistently reduces attack success rates while preserving benign-task utility. The code is available at this https URL.

---


### 7. [OLMo-Detect: A Multi-Stage, Confounder-Controlled Benchmark for Membership Inference on Large Language Models](https://arxiv.org/abs/2610.02986)

**<font color=#1a73e8>作者：</font>** Tao Shi, Chaoyi Xiang, Qiongkai Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Membership inference on large language models (LLMs) aims to determine whether a given text sample was included in an LLM's training data, without access to its training corpus. Despite recent progress, existing benchmarks suffer from three limitations: limited coverage of training stages, insufficient distributional alignment between members and non-members, and lack of rigorous filtering of non-members against the training corpus. To address these limitations, we propose OLMo-Detect, a multi-stage, confounder-controlled benchmark built upon the fully open OLMo 2 pipeline. OLMo-Detect spans pre-training, mid-training, and post-training, explicitly aligns members and non-members on three key axes, and rigorously filters non-members via infini-gram. To assess robustness to distribution shifts, we further introduce OLMo-Detect (Shifted), a variant where members are misaligned with non-members. We evaluate 15 unsupervised and 3 supervised membership inference attacks (MIAs) across the OLMo 2 family, finding that: (i) overall performance is limited: the best unsupervised and supervised MIAs both reach an AUC of only 0.68, and supervised MIAs degrade under cross-domain evaluation; (ii) MIA performance peaks at mid-training and is lower at pre-training and post-training, a pattern driven by data type rather than a stage effect: curated math data is far more detectable than other types; (iii) overall scores improve from 1B to 13B but plateau at 32B; and (iv) no unsupervised MIA is robust to distribution shifts, with AUCs shifting by up to 0.42. Finally, we find that our findings on OLMo 2 generalize to OLMo 3 and non-OLMo models.

---


### 8. [Persona Guardrail: A Production-Grade Defense Framework for Agentic Systems](https://arxiv.org/abs/2610.03434)

**<font color=#1a73e8>作者：</font>** Bijeeta Pal, Sridhar Reddy Maddireddy, Muhaimin Bin Munir 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model-based agents are increasingly deployed to perform domain-specific tasks by interacting with enterprise knowledge, tools, and external services. Existing runtime guardrails primarily target prompt injection and other attack-specific behaviors under a black-box threat model, but provide limited guarantees that agents operate within their intended functionality. As a result, production agents remain vulnerable to malicious requests and out-of-domain queries that existing defenses often fail to distinguish. We present Persona Guardrail, a production-grade runtime defense framework that enforces explicit functional boundaries for customer-facing agentic AI systems through synchronous input and output validation driven by semantic allowlist and blocklist specifications. We also introduce PAGE (Persona-Aware Guardrail Evaluation), a benchmark for evaluating function-specific guardrails across benign, adversarial, and out-of-domain interactions on both user and agent turns. Compared with a generic LLM-based guardrail, Persona Guardrail improves overall accuracy from 85.7% to 95.9%, increases out-of-domain detection from 57.3% to 93.5%, and reduces the false-approved rate from 25.0% to 4.7%. Currently deployed in production, Persona Guardrail meets its latency budget while sustaining a very low false-block and false-allow rate under realistic production workloads. These results demonstrate that Persona Guardrail provides a practical, scalable, and production-ready foundation for securing agentic AI systems.

---


### 9. [Passing the Test You Trained On: Re-evaluating Prompt-Injection Detectors for LLM Agents](https://arxiv.org/abs/2610.03448)

**<font color=#1a73e8>作者：</font>** Zhuowen Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly screen tool outputs with small prompt-injection detectors, and teams choose among detectors by their scores on public benchmarks. We ask whether those scores predict how a detector behaves inside an agent. We replay the ground-truth tool calls of two agent benchmarks, AgentDojo and tau-bench, without an LLM to obtain tool outputs that are benign by construction, label injected outputs by differential replay, and evaluate fifteen detectors, including Meta's Prompt Guard 2, and two task-aware LLM judges on these outputs and on the BIPIA benchmark. Detection rankings transfer poorly between benchmarks: the best detector on BIPIA catches 2% of AgentDojo injections at a 1% false-positive rate, and a detector that catches 72% of AgentDojo injections catches 15% on tau-bench. False-positive rates on tool outputs, which range from none to over 90%, do transfer between the two agent benchmarks. Where training data is public, the form of the training inputs explains the results. The BIPIA leader was trained on full BIPIA inputs, but having seen InjecAgent's attack strings as short prompts does not help it find them inside tool outputs; the best detector on both agent benchmarks shares no data with any benchmark and was trained on agent-style inputs. Evaluations meant to inform deployment should use the agent's own tool outputs, report detection at a low false-positive rate, and audit what the detector was trained on.

---


### 10. [Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks](https://arxiv.org/abs/2610.03585)

**<font color=#1a73e8>作者：</font>** Neeraj Karamchandani, Piyush Nagasubramaniam, Xinhong Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security benchmarks for LLM-based agents often report the attack success rate (ASR) as a measure of model robustness and use these scores to compare different models and defense mechanisms, assuming that they describe the security of the agent. In this paper, we explore whether it also influences the benchmark's measurement.
To measure the effect of the benchmark representation, we introduce threat-preserving representation sensitivity (TPRS), which measures how much the ASR changes when we change the agent-visible representation while holding the underlying task, harmful action, security policy, ground truth, environment, and the evaluation criteria fixed.
On Agent Security Bench (ASB), replacing threat-related tool names with threat-neutral names raises the committed attack success rate by 11.67 percentage points on GPT-5-mini and by 13.21 points on Claude Haiku 4.5. On MCPTox, replacing the original neutral tool name with an explicit threat-related name lowers the ASR by 11.00 percentage points on GPT-5-mini and 4.11 points on Claude Haiku 4.5. On AgentDojo, adding threat-related wording to the attack-relevant tool changes ASR by only 0.50 percentage points on GPT-4o-mini, yet the benign utility falls by 5.36 points on tasks requiring that tool.
We ran an experiment on MCPTox where we observed that a threat-neutral name matched on token count, length, and casing reproduces most of the shift produced by the threat-explicit name (8.54 of 11.00 points on GPT-5-mini).
The results show that a security score measured under one representation may fail to generalize across threat-preserving representations of the same security problem. Robustness claims should therefore be supported by performance across a controlled set of threat-preserving representations rather than relying on a single representation-dependent score.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
