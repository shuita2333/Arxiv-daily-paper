# 🔐 大模型安全相关研究 | 2026年09月03日

> 本类共 **11** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems](https://arxiv.org/abs/2609.00267)

**<font color=#1a73e8>作者：</font>** Panduranga Sai Varma Dantuluri, Jyotirmoy Sundi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents increasingly act on a user's behalf: they hold credentials, call tools and services, and spawn sub-agents that act further on their behalf. This turns a long-standing distributed-systems question -- who is authorized to do what, on whose authority -- into an urgent and largely unsolved problem, because the component driving each agent is a language model an adversary can hijack. We argue that agent security must be evaluated under an untrusted-model assumption: a correct system is one in which a fully prompt-injected agent still cannot exceed the authority explicitly delegated to it. Against this standard we make three contributions. First, we give a threat model for multi-agent delegation centered on four adversaries -- confused deputy, token theft and replay, prompt-injection privilege escalation, and compromised sub-agents -- and derive eight security requirements a governed agent system must meet. Second, we show the gap is real: a default agent runtime modeling common practice (broad bearer credentials, authorization gated inside the model) fails all four threats, and across four widely used frameworks -- LangGraph, CrewAI, AutoGen, and the Model Context Protocol (MCP) authorization model -- three provide no built-in confinement and one only partial; no existing standard alone covers the requirement set. Third, we implement and adversarially evaluate an authorization broker that closes the gap. It blocks all four threats; it resists 11 direct attacks on its design and accepts 0 of 200,000 forged tokens; it confines a compromised sub-agent to its delegated task (a mean of 1.5 reachable actions versus all 8,100 under bearer delegation, across 2,000 randomized scenarios); and it enforces at microsecond cost (about 2.6 microseconds per decision), negligible against model inference. These principles are also realized in production in VotalAI's LLM Shield.

---


### 2. [TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning](https://arxiv.org/abs/2609.00470)

**<font color=#1a73e8>作者：</font>** Muhaimin Bin Munir, Akib Jawad Ononto, Nazia Shehnaz Joynab 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) grounds large language models in external corpora, but implicit trust in retrieved documents creates a critical attack surface: PoisonedRAG shows that a handful of crafted passages can dominate dense retrieval and steer generation toward attacker-chosen answers. We present the Tri-Layer Sieve, a middleware defense that sanitizes retrieved evidence through cross-embedding-space clustering with an independent judge model, structural filtering of trigger-payload artifacts, and LLM consistency verification. The design exploits a key weakness of retrieval-stage poisoning: a single document must satisfy one embedding geometry, one internal Trigger-Payload structure, and one generation objective - rarely all three simultaneously, a fragility that persists even against an adaptive attacker who paraphrases around it. On Natural Questions, HotpotQA, and MS-MARCO with Contriever retrieval (k=50), the Sieve reduces black-box Attack Success Rate from 67.0/87.0/64.0% to 3.0/14.0/4.0%, mitigates white-box HotFlip attacks from ~74% to 27.8% on NQ with Layer 3 enabled, and drives poisoned-document MRR to 0.000, while restoring clean accuracy from 13-33% under attack to 58-76%. Under an architecture-aware adversary who paraphrases triggers to evade the structural filter, enabling the consistency layer halves adaptive ASR (32.0% to 15.0% on NQ) while raising clean accuracy by 18 points, at an added latency of ~16-19 s/query under live retrieval.

---


### 3. [Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models](https://arxiv.org/abs/2609.00495)

**<font color=#1a73e8>作者：</font>** Guoli Wang, Haonan Shi, Tu Ouyang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) generate text through iterative denoising rather than left-to-right decoding. This generation paradigm introduces two axes that can influence safety alignment: when tokens are generated during denoising and where they appear in the response. In this paper, we measure dLLM safety behavior under harmful prompts by tracing intermediate token distributions and commitment decisions throughout denoising. Our analysis shows that refusal signals are concentrated in early denoising steps and leading response positions, and the tokens committed early can strongly shape the final safety outcome. Our measurements further show that the denoising step and persistence of refusal-token commitment are important for understanding dLLM safety. Based on these findings, we propose Refusal-Aware Early Commitment (RAEC), a simple training-free decoding method that commits persistent refusal signals from early steps. Experiments on LLaDA and Dream show that RAEC reduces attack success rates while largely preserving utility. The code is available at this https URL.

---


### 4. [Validity-Aware Jailbreak Evaluation for Large Language Models](https://arxiv.org/abs/2609.00498)

**<font color=#1a73e8>作者：</font>** Qilong Wu, Sahil Wadhwa, Pranab Mohanty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Jailbreak robustness has become central to large language model (LLM) safety evaluation, yet prevailing methodologies rely primarily on refusal behavior, semantic resemblance, and intent-matching heuristics that emphasize linguistic plausibility rather than correctness. We identify a key limitation in existing evaluations: many jailbreak intents depend on instructional validity rather than epistemic factuality, allowing realistic-looking responses to be labeled successful despite being factually or procedurally incorrect. To address this gap, we propose Sequential Epistemic and Action-Level Validation (SEAV), a verification-centric jailbreak evaluation framework that decomposes responses into ordered steps and evaluates both validity and correctness. SEAV combines LLM-as-a-judge mechanisms for semantic interpretation with retrieval-grounded verification using external knowledge sources, assessing whether generated content is factually correct, structurally consistent, and operationally capable of advancing harmful objectives. Empirically, SEAV cuts the false-positive rate on SD-A (a curated strategic-dishonesty diagnostic) by 14.9\,pp vs. the strongest baseline, and reclassifies 22.1\%--51.0\% of sampled prior-labeled successes as invalid across three of four public benchmarks. Together, these results show that enforcing correctness substantially reshapes measured robustness: many previously labeled jailbreak successes are reclassified as invalid, and results are stable across the tested search backends and evaluator models. Code and data are available at this https URL.

---


### 5. [Transferable End-to-End Optimization for Indirect Long-Term Memory Poisoning in LLM Agents](https://arxiv.org/abs/2609.00523)

**<font color=#1a73e8>作者：</font>** Chuanchao Zang, Jianing Wang, Wenyu Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-term memory can turn untrusted external content into persistent influence over an LLM agent's future decisions, creating the threat of indirect memory poisoning. A successful attack must survive a multi-stage pipeline comprising memory writing, retrieval, and utilization. Existing attacks largely rely on intra-stage optimization, optimizing individual stages in isolation while overlooking inter-stage coupling. Specifically, these stages impose different requirements on the same poisoning content, and each stage operates on the transformed output of its predecessor. Consequently, optimizing one stage may undermine the effectiveness of other stages, while upstream transformations may erase improvements intended for downstream stages. Indirect memory poisoning should therefore be viewed as an end-to-end optimization problem. Based on this insight, we present \textsc{PipePoison}, which collects fine-grained stage feedback from local shadow systems, uses chain-structured losses to identify and optimize the stage bottlenecking end-to-end success, and applies stability-calibrated stage and configuration weights to improve transferability. Across three agent frameworks and four memory mechanisms, \textsc{PipePoison} improves attack utilization rate by 19.1 percentage points. Even on fully unseen victim configurations, it outperforms the strongest baseline by 16 percentage points and remains effective under eight representative defenses.

---


### 6. [Membership Inference in Fine-tuned Diffusion Language Models via Token-level Memorization Asymmetry](https://arxiv.org/abs/2609.00873)

**<font color=#1a73e8>作者：</font>** Shengfang Zhai, Leo Marchyok, Yuling Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) have recently emerged as an alternative modeling paradigm to autoregressive LMs, offering advantages such as parallel generation and bidirectional context modeling. Despite growing interest in their generative capabilities, the privacy risks of DLMs remain underexplored. We identify a phenomenon termed token-level memorization asymmetry through theoretical analysis of diffusion training dynamics. Building on this finding, we propose Q-Skew, a quantile-weighted skewness-based indicator for membership inference on finetuned DLMs. Experiments across multiple fine-tuning datasets and models show that our method outperforms existing baselines. Moreover, we show that Q-Skew can also facilitate other privacy violations, such as PII extraction. Our findings reveal a previously underexplored privacy attack surface and highlight the need for systematic privacy evaluation of DLMs.

---


### 7. [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](https://arxiv.org/abs/2609.01023)

**<font color=#1a73e8>作者：</font>** Chou Jin Chua, Sarang Nambiar, Murali Srinivasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present AKRASIA, a stealthy, inference-time backdoor attack against reasoning-based Code LLMs. AKRASIA aims to achieve a backdoor target (e.g., malicious code execution) in reasoning LLMs while evading automated defenses and human inspection. To achieve this, AKRASIA probes the victim LLM to construct a code-level backdoor trigger. It then employs in-context learning for backdoor learning, and model unfaithfulness to conceal the backdoor trigger, and generate plausible reasoning. We evaluate AKRASIA using four backdoor targets six (6) reasoning LLMs, three coding tasks/datasets and three defense methods. AKRASIA has up to 99.34% average attack success rate on SOTA LLMs and mantains up to 97.23% average accuracy. AKRASIA evades the SOTA defense, retaining up to 98.82% average ASR in most (14/18) defense settings. It evades human inspection, successfully hiding the backdoor trigger and reasoning steps in up to 80% of settings. Our findings motivate the need to defend LLMs against reasoning backdoors.

---


### 8. [HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation](https://arxiv.org/abs/2609.01046)

**<font color=#1a73e8>作者：</font>** Nikita Oblakov, Sabrina Sadiekh, Evgeniy Kokuykin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Production LLMs must handle inputs that attempt to override system instructions, bypass safety policies or elicit harmful responses. A common mitigation is a separate guardrail model. Existing reports, however, provide little evidence on Russian prompt injection or Russian surface obfuscation. We present HiveTraceGuard-Pro, a 0.6B generative guardrail LoRA-tuned from Qwen3-0.6B. It is trained on Russian and English and uses one binary scoring rule (safe/unsafe) for the final target turn. Its training corpus pairs harmful examples, where a counterpart exists, with benign examples from the same domain and applies eight obfuscation transforms to both labels. In one harness, we compare HiveTraceGuard-Pro with thirty-four other guards on nineteen benchmark groups, sixteen of which are public. Its aggregate key is 0.7432, behind 0.7641 and 0.7552 for the two higher-scoring guards. Over the sixteen public groups alone, its key is 0.7153 and four of the thirty-four other suite guards score higher. In a fifteen-model comparison, HiveTraceGuard-Pro has the highest clean Russian robustness combined-F1 (0.88) and Russian prompt-injection recall (0.999). Both results use Russian sets assembled by our team, and at least 27.1% of the prompt-injection set overlaps the training corpus. Its 14.3 ms median latency is the lowest among those fifteen models in that run. Across the suite, FPR is 0.268 and FNR is 0.156. All reported response results use a legacy standalone-reply serialization rather than the natural assistant-role path of the shipped chat template. We release the merged weights on Hugging Face under Apache-2.0. The corpus, evaluation sets and evaluation code remain internal.

---


### 9. [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](https://arxiv.org/abs/2609.01222)

**<font color=#1a73e8>作者：</font>** Zichuan Li, Jian Cui, Ashley Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Real-world, high-profile AI agent harnesses often rely on vendor-proprietary or opaque designs for context assembly, leaving the sources and underlying logic of assembled context poorly understood and the resulting security risks largely unexplored. In this paper, we present the first systematic analysis of context assembly designs in real-world AI agent harnesses. We study and uncover how an agent harness is designed to collect and assemble context from diverse sources, and identify a set of practical attack vectors arising from these designs. Our analysis brings to light two novel categories of attacks in the context assembly of real-world harnesses: (1) MessageRole Context Privilege Escalation (M-CPE), which occurs when attacker-controlled content originating from a low-privileged context is incorporated into a higher-privileged message role. (2) Cross-Scope Context Privilege Escalation (X-CPE), which occurs when attacker-controlled content persists beyond the context in which it was introduced. We performed a systemic security analysis of the CPE attacks against 12 real-world agent harnesses, including Claude Code and Codex. The resulting consequences include full agent compromise, remote code execution, denial of service, and manipulated tool or skill invocations, etc.

---


### 10. [When Guardrails Look Effective: Construct Validity Failures in LLM Agent Commerce Evaluation](https://arxiv.org/abs/2609.01519)

**<font color=#1a73e8>作者：</font>** Peiying Zhu, Sidi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive simulations increasingly evaluate policies in markets populated by language-model agents. Their outputs can look economic---prices, profits, consumer surplus, and welfare---without instantiating the behavior named in the claim. We audit this risk in a multi-turn buyer--seller testbed for configurable hotel transactions. An initial implementation reported welfare gains from two marketplace guardrails of +87.4, +35.0, and +28.8 across a Qwen2.5 1.5B--14B ladder. It also gave guarded and unguarded agents different offer schemas and choice procedures. Holding the schema and buyer chooser fixed changes the paired contrasts to +7.2, -13.9, and +23.8. The four largest 14B single-generation effects averaged +229; after three generations per profile-condition, they averaged +37.6 (95% bootstrap interval [-34.2, 109.3]), while generation residuals account for 49.9% of variation in this post-hoc probe. A seller-incentive check is non-monotone: increasing profit pressure produces less profit than the default seller prompt. Scripted positive controls show why this matters. A profit-maximizing seller already attains first-best welfare, so guardrails mostly redistribute and reduce welfare; they create welfare only when the seller is explicitly programmed to force inefficient bundles. We contribute a construct-validity contract separating incentive validity, protocol isolation, stochastic stability, and welfare accounting, and returning INVALID or INCONCLUSIVE before substantive policy claims. In our case, the original estimate is INVALID under protocol isolation, while the controlled study remains INCONCLUSIVE under incentive validity and stochastic stability. The case does not show that guardrails are ineffective; it shows their apparent value is unidentified until the simulated agents and protocol pass these checks.

---


### 11. [CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?](https://arxiv.org/abs/2609.01600)

**<font color=#1a73e8>作者：</font>** Damien Sileo, Dimitri Kachler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dynamic agent harnesses let language models change the software that shapes their own execution. This flexibility brings a new reasoning burden: a local plugin change can propagate through dependencies and cleanup. We introduce CordisBench, a 1,200-question benchmark of this lifecycle reasoning. It combines a controlled formal setting with programs executed against Cordis, a runtime that manages component dependencies and cleanup, and asks models to identify affected components, predict state after a specified teardown order, determine which conditions hold under all or some orders, and choose reconfigurations that succeed when executed. Across these tasks, we evaluate three efficiency-oriented models at low reasoning effort with 2, 4, 8, 16, 24, or 32 relevant interactions, using deterministic task-specific scoring. Models usually handle small systems well but grow less reliable as more interactions become relevant, especially when predicting final state and when reasoning across teardown orders. Additional inference effort recovers marked gains for some models. The cost is nontrivial: on our 16-interaction subset, GPT-5.6 Luna uses nearly 3,000 reasoning tokens per question at medium effort. For these controlled instances, that cost is avoidable: an independent finite reference semantics agrees with Cordis execution on every observation and action outcome used for scoring across all 528 executable questions.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
