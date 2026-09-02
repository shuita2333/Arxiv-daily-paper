# 🧠 大模型相关研究 | 2026年09月03日

> 本类共 **295** 篇论文：已确认 **283** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-295](./part-06.md)

---

### 1. [HyperWorld: Hypergraph-Structured State Serialization Improves Learned Textual World Models](https://arxiv.org/abs/2609.00002)

**<font color=#1a73e8>作者：</font>** Yun-Jian Zhang, Chen-Wei Liang, Tian-Yi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models enable language-model agents to predict environment dynamics and plan before acting. In text environments, the model must learn symbolic action effects from serialized state descriptions, but the role of serialization structure remains underexplored. We present HyperWorld, a controlled study of state serialization for learned textual world models. We compare raw observations with three symbolic serializations of the same ground-truth state: independent sentences, pairwise triples, and entity-centered hyperedge units that group multiple related facts around entities and relations. All variants use the same training objective: given a state and an action, predict symbolic effects or judge the action infeasible. Across model scales, data budgets, and in-distribution and out-of-distribution test worlds, hyperedge serialization gives the clearest gains for 0.5B--1.5B models and under distribution shift. Larger models reduce the gap, and pairwise triples can match or slightly exceed hyperedges on in-distribution exact match, but hyperedges achieve the strongest out-of-distribution fact F1 and the best small-to-medium scale trade-off between feasibility detection and effect prediction. In downstream greedy planning, the hyperedge world model also attains the highest success rate among the tested representations. These results show that higher-order state organization is a simple but effective inductive bias for learned symbolic world models, especially when model capacity is limited or test environments differ from training.

---


### 2. [Incremental Risk Assessment of Progressive Elder Financial Scams via Instruction-Tuned Small Language Models](https://arxiv.org/abs/2609.00005)

**<font color=#1a73e8>作者：</font>** Parviz Ghafariasl, Weimin Fu, Xiaolong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial scams targeting older adults increasingly occur through text and voice channels such as email, SMS, and phone calls, unfolding over multiple conversational turns that begin with impersonation or casual contact, escalate through trust building and urgency, and culminate in requests for sensitive information or financial transfers. Because risk signals emerge incrementally across turns, effective detection requires models that continuously update risk estimates under resource-constrained deployment settings. We propose a cumulative turn-based risk assessment framework that incrementally aggregates conversational turns and re-estimates risk at each step, enabling dynamic scam monitoring across progressively evolving conversations. A multi-turn dialogue dataset is constructed to cover investment, charity, and tech support scam scenarios, with each dialogue containing two to eight turns and annotated at every cumulative stage with a qualitative risk level, a continuous risk score, an explanatory rationale, and a safety recommendation. Four small language models (Phi-4, LLaMA-3.2, DeepSeek-R1, and Qwen3) are fine-tuned and evaluated under a unified training framework. Fine-tuned small models capture fraud-related linguistic cues and cross-turn escalation patterns while maintaining compact architectures suitable for mobile and resource-constrained deployment settings. Among the evaluated models, Phi-4 and LLaMA-3.2 achieve stronger turn-aware risk estimation performance relative to their parameter scale. These results suggest that structured cumulative modeling can support incremental scam risk assessment in deployment-oriented settings while highlighting the potential of compact language models for privacy-aware and on-device fraud protection.

---


### 3. [Long-Horizon State Tracking in LLMs: Executing MD5 through a Deep Sequence of Dependent Tool Calls](https://arxiv.org/abs/2609.00012)

**<font color=#1a73e8>作者：</font>** Dheeraj Mohandas Pai, Lu Xian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks remain uncommon in large language model (LLM) evaluation, and for a reason: when each step depends on the last, per-step accuracy that looks excellent in isolation decays catastrophically, as errors cascade and the end-to-end failure probability grows sharply with length. Existing agentic benchmarks report end-to-end success but confound this state-tracking difficulty with instruction interpretation, give no control group that isolates it, and are vulnerable to shortcuts such as a hallucinated final answer, so they cannot say why a long run fails. Whether an LLM can carry exact intermediate state across many tool calls at all is itself not well established. We test this cleanly by having the model compute a cryptographic hash, MD5, step by step: a sequence of $196$ dependent tool calls over $64$ rounds while it carries four $32$-bit words $(a,b,c,d)$ in its own context from one call to the next. Interpretation is trivial and, because we implement MD5 from scratch (RFC~1321), we align every call to the ground-truth trace and check the digest to the bit, so any failure is pure bookkeeping. gpt-oss-120b, a mixture-of-experts model with only $\sim$5.5B active parameters per token, at temperature $0$ with a short fixed prompt, carries the full state across all $196$ calls and returns the correct digest on a majority of completed runs. In the strongest setting we replace every primitive tool with a second LLM, so a driver and a worker compute the whole hash from scratch with no exact-arithmetic oracle in the loop. Two ingredients decide success and neither changes the weights: keeping the model's own reasoning in its context each turn, and voting over a thinking-enabled worker to remove its modular-arithmetic slips. We localize the residual failures by origin, separating state-carrying from arithmetic and from serving.

---


### 4. [Behaviorally Grounded User Profiles from the Wild for Personalized Alignment and Multi-Perspective Reasoning](https://arxiv.org/abs/2609.00014)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Victor Zhong, Ehsan Kamalloo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona-driven techniques increasingly adapt large language models (LLMs) to diverse contexts. However, existing methods predominantly rely on rigid, synthetic personas that flatten individual variation, rely on stereotypes, and miss the nuanced signals driving actual human preferences. We introduce profile behavioral grounding, a framework for extracting open-ended, high-fidelity user profiles directly from authentic, anonymized social media posts. We evaluate these profiles across two paradigms: train-time personalization via supervised finetuning (SFT) and non-parametric test-time multi-perspective reasoning. Across complex recommendation and open-ended query benchmarks, behaviorally grounded profiles consistently improve base models and outperform synthetic profile baselines, driving stronger parametric alignment and enabling richer, multifaceted reasoning. Our findings establish open-ended, behavior-derived profiles as a highly diverse and effective foundation for the next generation of personalized language systems. Our code base is available at this https URL.

---


### 5. [OpenAgentFlow: Enabling System-Wide Safety Boundaries for Heterogeneous AI Agent Fleets](https://arxiv.org/abs/2609.00015)

**<font color=#1a73e8>作者：</font>** Dongsheng Chen, Xiangyu Zhao, Xin Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents powered by large language models are evolving from isolated assistants into heterogeneous systems in which multiple agents, planners, controllers, and execution backends operate over the same user or enterprise environment. In such settings, safety becomes a system-level action-governance problem: deciding whether concrete agent-generated actions should be committed before they modify shared state. Existing safeguards cover prompts, tool calls, GUI actions, and agent-local behavior, but often leave enforcement fragmented, obscure risks that emerge across multi-step action flows, and provide limited support for auditability and policy evolution.
We present OpenAgentFlow, a control-plane/action-plane architecture that enforces safety at the action-commit boundary. It normalizes pending GUI actions, API calls, tool calls, and LLM-generated invocations into a unified AgentEvent stream, routes each event through a shared pre-execution Policy Enforcement Point, and maintains provenance, session state, audit records, and updatable policies in the control plane. This creates a shared governable action stream and allows new rules to take effect without modifying agents, prompts, models, or execution paths.
We instantiate OpenAgentFlow on Android. On a 300-case action-event benchmark, it achieves 94.0% accuracy and a 95.3% attack block rate. On a 30-case dynamic-policy suite, it matches expected behavior in 27 cases after new rules are installed. Across 98 traced cases from a 100-case Android emulator suite, it achieves 90.8% raw accuracy and a 92.9% trace-adjusted pass rate across GUI, API, and LLM-planned cases. These results show that OpenAgentFlow provides a practical shared enforcement boundary for heterogeneous AI agent fleets.

---


### 6. [SCAFFOLD: A Large-Scale Structured Dataset of Computer Science Research Figures with Diagram QA and Chain-of-Thought Reasoning Traces](https://arxiv.org/abs/2609.00018)

**<font color=#1a73e8>作者：</font>** Ranjit Raut, Aarav Subedi, Sagun Rai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer science papers rely heavily on diagrams: architecture drawings, system flowcharts, and pipeline schematics that often carry more information than the text around them. There is currently no public dataset that pairs this specific kind of figure with captions, context, questions, answers, and step-by-step reasoning, which is exactly what is needed to train a vision-language model to understand them. We present \textbf{SCAFFOLD}\footnote{this https URL}, a large-scale structured dataset of computer science research figures with diagram QA and Chain-of-Thought reasoning traces. This dataset consists of (image, caption, context, question-answer, chain-of-thought) tuples from arXiv computer science papers prepared using layout detection and PDF parsing, with an AI-assisted question-generation step. The resulting large-sized SCAFFOLD-157K dataset spans 3,058 papers with 29,887 figures (157,387 pairs), a medium-sized SCAFFOLD-37K dataset (36,797 pairs), and a small-sized SCAFFOLD-12K dataset (12,000 pairs). We used SCAFFOLD-12K for baseline experiments on Qwen2.5-VL-3B-Instruct.

---


### 7. [trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories](https://arxiv.org/abs/2609.00038)

**<font color=#1a73e8>作者：</font>** Hadi Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Outcome-only evaluation is the production default for LLM agents: show a judge the request and the final reply and ask whether it was handled well. The metric is structurally blind to an agent that reaches the right answer the wrong way. We measure that blind spot where ground truth is known by construction: a deterministic tool-using support-desk environment, a scripted oracle policy that always solves it, and a fault injector that breaks exactly one thing at a known step, stratifying faults by whether the customer-visible outcome survived (silent) or not (loud). Five judges (programmatic rules, outcome-only, step-rubric at two model sizes, and a self-consistency ensemble) are scored on detection, step localisation, fault typing, calibration, and cost over 400 trajectories. The outcome-only judge catches 84% of loud faults but 45% of silent ones while flagging 33% of correct trajectories; a step-rubric judge reaches 77% silent recall with zero false alarms at 3x the cost. No judge reads the final reply: an invented promise appended to an otherwise perfect trajectory evades the rules entirely and the step judge 82% of the time, and self-consistency triples cost while improving nothing. We argue that judge evaluations must stratify recall by outcome survival, and release the environment, the injector, all raw verdicts, and an analysis pipeline that rebuilds every number offline.

---


### 8. [REAL-Q: E2E LLM Quantization via Dynamic Gradient Descent](https://arxiv.org/abs/2609.00049)

**<font color=#1a73e8>作者：</font>** Qian Zhang, Yaoming Li, Zhewen Tan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is essential for deploying large language models (LLMs) under strict resource constraints. State-of-the-art PTQ methods quantize each layer with a single closed-form second-order solver: to remain analytically tractable, they heavily approximate the global loss (dropping cross-channel coupling, pooling output rows into groups), and they then freeze the resulting Hessian across the entire layer, with no way to refresh it as the loss landscape shifts column by column--a phenomenon we call information misalignment. We propose REAL-Q (Real-time E2E-loss Aligned LLM Quantization), a novel PTQ paradigm that breaks this compromise: instead of diluting the objective for the sake of analytic tractability, REAL-Q targets an end-to-end-aligned surrogate of the global loss and refines it via fine-grained, dynamic Block-wise Gradient Descent applied after every column block (128 columns). By coupling this fine-grained correction with a sliding window mechanism for smooth cross-layer transitions, REAL-Q effectively mitigates error propagation across the network. On LLaMA-3.1 (8B and 70B) and Qwen3 (0.6B-32B) at W4A16, REAL-Q reduces end-to-end KL divergence by up to ~49% relative to state-of-the-art globally-guided methods.

---


### 9. [From Detection to Refusal: Safer LLMs via Circuit-Guided Weight Scaling](https://arxiv.org/abs/2609.00051)

**<font color=#1a73e8>作者：</font>** Kuan-Lin Chu, Chung-En Sun, Tsui-Wei Weng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite extensive alignment efforts, Large Language Models (LLMs) remain vulnerable to generating unsafe content under adversarial prompting, yet the internal mechanisms by which safety behaviors are implemented remain poorly understood. We study LLM safety from a mechanistic interpretability perspective and characterize a multi-stage *safety circuit* that organizes refusal behavior, consisting of (i) $\textbf{Harmful Detection Heads}$ that respond to harmful inputs, (ii) $\textbf{Safety Neurons}$ that mediate and stabilize safety signals in the residual stream, and (iii) $\textbf{Refusal Heads}$ that translate these signals into safe response generation. Using targeted attention-head and neuron-level interventions, we provide causal evidence consistent with this circuit organization, showing that suppressing upstream Harmful Detection Heads disrupts downstream refusal behavior and that safety neurons mediate this interaction. We validate that this decomposition recurs across multiple LLM architectures and adversarial attack settings, and use simple, architecture-preserving weight scaling as a mechanistic probe to test its functional relevance. Across six LLMs, circuit-guided scaling improves safety rates under attacks by 26.5%, while incurring only a 1.7% accuracy drop across four standard benchmarks. Overall, our results support a circuit-level interpretation of LLM safety and suggest that mechanistic abstractions can reveal stable and transferable patterns underlying aligned behavior.

---


### 10. [AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes](https://arxiv.org/abs/2609.00052)

**<font color=#1a73e8>作者：</font>** Xun Wang, Bihe Zhao, Michael Backes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to save deployment costs. All existing audits decide backbone identity from the text-output channel, which is structurally fragile for agentic APIs because modern serving stacks (OpenAI, Anthropic, Gemini, Cloudflare Workers AI, LangGraph) discard text and expose only structured actions when the model calls a tool, and provider-injected system prompts can distort text distributions enough that text-channel tests falsely accuse honest providers of substituting the claimed model. We observe that recent agentic post-training internalizes tool-use directly into the weights, opening a new audit channel that the serving stack still exposes and that is largely invariant to deployment context. We introduce Agentic Provenance (AgentProv), the first action-based identity audit for agentic LLM APIs: AgentProv fingerprints a deployed model through its categorical tool-call distribution and decides identity via an MMD permutation test. AgentProv catches every substituted model (100% on 630 evaluated checkpoint pairs), while holding the false-positive rate under system-prompt injection at 7% (vs. 67% for MET and 53% for RUT). On third-party API endpoints, AgentProv's disagreements with MET are consistent with an independent token-count side-channel that detects provider-injected system prompts.

---


### 11. [Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment](https://arxiv.org/abs/2609.00055)

**<font color=#1a73e8>作者：</font>** Mustafa Talha İlerisoy, Hung Manh Pham, Mathias Funk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised respiratory encoders lack semantic grounding in clinical domain needed for zero-shot inference, limiting their utility without task-specific labeled data. We propose a framework that aligns these encoders with medical terminology in a shared latent space turning them into a zero-shot-capable foundation model. To address paired data scarcity, we use a medical LLM to synthesize structured reports from metadata, creating dense semantic anchors for contrastive learning. Our training combines a sigmoid-based contrastive loss with encoder's native SSL objective and similarity-aware negative sampling to sharpen pathological boundaries. Across 9 tasks on 6 datasets, our method achieves a 61.3% mean zero-shot AUC, surpassing CLAP (51.4%) and Qwen2-Audio (54.9%) while reaching the highest linear probing AUC (71.6%) with only 43% of data used by full-scale baselines, showing that structured semantic alignment outperforms large-scale, general-purpose models in clinical diagnostics.

---


### 12. [ValueGraph: Value-Signal Guided Graph Pre-training for Contextualized User Representation](https://arxiv.org/abs/2609.00057)

**<font color=#1a73e8>作者：</font>** Yitong Han, Wei Gao, Yi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Value signals are aggregated user-level moral representations that capture users' inferred value-related tendencies from their online discourse. User behavior on social media is shaped not only by what users say or whom they interact with, but also by the value signal through which they express attitudes. Existing user representation methods largely miss this value-relevant dimension. We propose ValueGraph, a graph pre-training framework that uses automatically inferred moral-value signals as noisy auxiliary signals for contextualized user representation. From post-reply graphs, ValueGraph learns semantic and structural representations and further aligns users through relative value similarity with contrastive and clustering objectives. Rather than treating inferred values as gold psychological labels, ValueGraph uses them as soft constraints for representation learning. Experiments on stance detection and twitter bot detection show consistent gains over strong text-based, graph-based, and text-only LLM baselines, highlighting value-signal guidance as a useful inductive bias for socially informed user modeling.

---


### 13. [CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language](https://arxiv.org/abs/2609.00058)

**<font color=#1a73e8>作者：</font>** Qi Fan, An Zou, Yehan Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing high-performance CUDA kernels demands specialized knowledge in algorithm implementation, correctness validation, and hardware-aware parallel optimization, creating a substantial expertise barrier and making generating CUDA kernels directly from natural language (Text2CUDA) essential. Meanwhile, the general-purpose code generation capability of Large Language Models (LLMs) prompts a series of works exploring LLM-based CUDA kernel generation. They mainly focus on transpilation from high-level frameworks such as PyTorch to CUDA (Torch2CUDA) rather than Text2CUDA, where models must understand the high-level input semantics and handle low-level kernel implementation and validation. Additionally, these methods are vulnerable to reward hacking due to reliance on predefined test inputs. In this paper, we propose CUDA-Harness, a framework for harnessing agentic CUDA kernel generation and optimization from natural language. Specifically, we introduce Intermediate-Structured Generation to connect high-level semantic understanding with low-level kernel generation. To dilute reward hacking in Text2CUDA, we construct Synthesis-Based Verification to provide isolated test data and progressive validation. Furthermore, we propose Feedback-Adaptive Evolution, a kernel evolution strategy that prioritizes correctness while optimizing performance. Finally, through extensive experiments, we demonstrate the effectiveness of CUDA-Harness, with further evaluations illustrating generalization across LLMs, hardware platforms, and to C-to-CUDA transpilation.

---


### 14. [RePro: Proof-Verified Benchmark Rewriting for Reliable Evaluation of LLM Mathematical Problem Solving](https://arxiv.org/abs/2609.00062)

**<font color=#1a73e8>作者：</font>** Xiyuan Zhou, Zhuoqi Li, Xinlei Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data contamination undermines the reliable evaluation of large language models (LLMs) on mathematical problem solving. While rewriting-based evaluation mitigates memorization, existing methods lack guarantees of problem validity and answer correctness. We propose Proof-Verified Benchmark Rewriting (RePro), the first framework to integrate Lean-oriented neural automated theorem provers (ATPs) into benchmark rewriting, which rewrites problems and regenerates answers with correctness ensured by Lean-verified proofs. Experiments on GSM8K and MATH show that RePro's retained rewritten instances achieve 100% well-definedness, feasibility, and answer correctness, while existing methods still produce invalid or incorrect instances. Moreover, several models exhibit accuracy drops on proof-verified rewritten benchmarks, suggesting that their performance is sensitive to surface-level and structural variations and may partly reflect memorization effects. Our source code and data are available at this https URL.

---


### 15. [Medical Causal Hypothesis Verification with Large Language Models](https://arxiv.org/abs/2609.00063)

**<font color=#1a73e8>作者：</font>** Safiyyah Ahmed, Abrar Ansari, Md Aminul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing use of large language models (LLMs) for search and information retrieval underscores the need to evaluate their reliability in high-stakes domains such as healthcare. Although LLMs can effectively answer questions about diseases, symptoms, and treatments, their ability to accurately assess causal relationships and ground their conclusions in verified scientific evidence remains unclear. Here, we present a preliminary, small-scale study that investigates the accuracy of LLMs in evaluating causal medical claims and supporting them with peer-reviewed research. We propose an evaluation framework for causal hypothesis verification that can be used to systematically track the performance of existing and future LLMs. We assess the performance of eight LLMs on 17 medical causal hypotheses to evaluate whether they can reliably verify these hypotheses using scientific evidence from the literature. We systematically annotate the scientific evidence they provide according to six criteria (a total of 1,067 annotation points) and assess them with nine evaluation metrics. Our analysis shows that while LLMs exhibit strong recall, they often perform poorly at providing valid scientific articles and evidence for support and at rejecting unsupported hypotheses. These findings highlight a critical limitation of current LLMs, as they cannot yet be trusted fully to verify causal relationships from the biomedical literature. This work underscores the need for rigorous evaluation before using LLMs for search and retrieval in healthcare settings.

---


### 16. [Attention Sensitivity Is Not Enough: Dissociating Attention-Level and Behavioural In-Context Learning under Fine-Tuning](https://arxiv.org/abs/2609.00064)

**<font color=#1a73e8>作者：</font>** Jinyuan Zhang, Peng He, He Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) lets large language models adapt to new tasks from demonstrations, and fine-tuning can erode this behaviour. Many preservation diagnostics inspect attention: if attention changes when demonstrations change, the model is treated as context-sensitive. This paper asks how far that proxy can be trusted once it is optimised. We formalise \emph{In-Context Sensitivity} (ICS), the average row distance between last-token attention on matched and mismatched demonstration prefixes, and pair it with \emph{ICL-GAP}, the behavioural accuracy gap between the same prefixes. In a controlled four-arm ablation on Llama-2-7B, an ICS-maximising regulariser ($\armKL$) drives ICS to $1.413$, within $0.5\%$ of its geometric ceiling. The behavioural readout tells a different story: ICL-GAP stays near zero and MMLU accuracy moves from $0.371$ to $0.279$, a Goodhart dissociation of the bounded attention proxy. Endpoint statistics locate the mechanism: attention grows sharp and near-disjoint across prefixes yet routes to formatting and demonstration-body tokens rather than labels. A random-label protocol confirms that the behavioural probe family retains dynamic range at the same checkpoints. In a constructive sweep, behaviour gating partially mitigates the effect, while objectives anchored to pretrained computation hold the high-MMLU, moderate-ICS region that divergence maximisers leave. The main lesson is diagnostic: attention-level ICL proxies earn their place as training targets only after validation against behavioural gaps.

---


### 17. [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://arxiv.org/abs/2609.00065)

**<font color=#1a73e8>作者：</font>** Timothy Kassis, Vinayak Agarwal, Yuhuan He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language-model agent asked to analyse an experiment will usually return working code. Whether the analysis is defensible is a different question. A defensible analysis depends on procedural choices: which test the field accepts, which identifier namespace is authoritative, and which caveats must accompany a result. We present Scientific Agent Skills, an open library of 163 such procedures in 16 areas of practice, including genomics, cheminformatics, medical imaging, study design and scientific communication. Each skill is a directory built around a versioned, human-readable instruction file. An agent loads the file only when a task calls for it; the directory often also contains reference material and runnable scripts. We report no task-level evaluation and no host selection rate. Openly licensed and available at this https URL.

---


### 18. [OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization](https://arxiv.org/abs/2609.00066)

**<font color=#1a73e8>作者：</font>** Yishan Yao, Binjun Li, Hanling Yi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> NVFP4 is an efficient microscaling format for low-bit inference, but activation outliers can still degrade quantization accuracy within NVFP4 blocks. Within each quantization block, large activations can dominate the block scale, increasing the quantization error of the remaining values sharing the same scale. Existing post-training quantization (PTQ) methods mitigate outlier errors through strategies such as mixed precision, rotation, or residual compensation, but these approaches are either not specifically tailored to NVFP4 or introduce additional computation. In this work, we revisit NVFP4 from a channel-grouping perspective and define the reducible error incurred by remaining block values under the scale set by the block maximum as Collateral Quantization Error. Based on this insight, we propose OCGQuant, a post-training quantization method centered on Outlier-Companion Grouping (OCG), which adaptively pairs outlier channels with low-magnitude companion channels to improve NVFP4 activation block composition. Experiments on Llama3 and Qwen3 show that OCGQuant achieves the lowest WikiText-2 perplexity and highest average downstream accuracy among evaluated PTQ methods, while maintaining prefill speedup close to RTN and matching its peak decoding memory. Code is available at this https URL.

---


### 19. [Do Multimodal LLMs See Before They Read? Diagnosing Contextual Sycophancy](https://arxiv.org/abs/2609.00067)

**<font color=#1a73e8>作者：</font>** Yi-Cheng Lai, Hen-Hsen Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> External text can override conflicting image evidence in multimodal large language models, a failure we call multimodal contextual sycophancy. We introduce a 998-case diagnostic that independently varies visual evidence, commonsense priors, and external text, and probe when this failure arises by moving the information boundary around a context-blind visual witness. On abnormal images paired with Gemini-generated false text, GPT-5.1 scores 7.9% under joint conditioning, 49.7% when the context-blind witness report is scored directly, 63.7% under a matched two-call witness-arbiter pipeline that exposes the witness to the text, and 84.2% under System-2 Visual Arbitration (S2VA), which withholds the text from the witness. Across six models, S2VA improves over the direct witness report by 19.7 to 44.1 points, with all paired 95% confidence intervals excluding zero. The best information boundary is not uniform: textual context scaffolds some models, and a GPT-4o-regenerated subset changes the relative ordering of joint conditioning, Witness-Only, and S2VA. Contextual sycophancy is therefore sensitive to when text is introduced, as well as to the model and context source.

---


### 20. [MiNER: Fine-Tuned Biomedical Natural Language Processing for Malaria Disease Entity Recognition in Clinical Texts](https://arxiv.org/abs/2609.00073)

**<font color=#1a73e8>作者：</font>** V. S. Anoop, Devika N  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Malaria remains a significant global health burden, necessitating continuous research efforts to understand its complex molecular mechanisms, epidemiology, and potential therapeutic interventions. Extracting essential biomedical information from the vast and constantly growing malaria literature is a challenging task that demands innovative approaches. Recently, pre-trained language models have revolutionized natural language processing tasks, demonstrating remarkable capabilities in various domains. This paper proposes a fine-tuned pre-trained biomedical language model for biomedical information extraction from scientific literature on malaria disease. The proposed methodology selects and preprocesses a large corpus of scientific articles on malaria, and then annotates them with entities of clinical significance. It then leverages BioBERT, a state-of-the-art pre-trained language model, to encode the textual data into context-aware representations. We fine-tune the model using domain-specific annotations and supervised learning to enhance its ability to extract relevant biomedical named entities. Extensive experiments and comparisons with different encoding and machine learning algorithms show that the proposed approach significantly outperforms them in precision, recall, and accuracy. We also publish our human-labeled dataset for entity and relation extraction to enable other health informatics researchers to train advanced models for malaria information extraction.

---


### 21. [Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops](https://arxiv.org/abs/2609.00077)

**<font color=#1a73e8>作者：</font>** Bowei He, Weixu Zhang, Yili Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-level autonomous research loops (ARLs) have recently emerged as a concrete object of study in automated machine learning research. In such loops, an LLM agent proposes modifications to an experimental training pipeline, executes the modified pipeline, and retains edits that improve a verifiable in-loop metric. Although executable metrics may appear to provide a reliable signal of progress, it remains unclear whether repeated metric-driven code editing leads to genuine improvements that generalize beyond the loop. We provide a systematic diagnosis of this question. Across various experiment settings, we identify a robust failure mode that we call \textbf{algorithmic mode collapse}. In this regime, surface-level edit diversity remains stable, but semantic and mechanism-level diversity collapse: the agent continues to edit different lines of code while repeatedly proposing the same kinds of algorithmic changes. This collapse is accompanied by a widening gap between in-loop metric gains and gains measured on independent held-out evaluations. We then propose Diversity-Aware Proposal Sampling (\textsc{DAPS}), a lightweight mitigation that combines category-coverage reweighting, persistent edit memory, and a validation gate. Under a three-tier protocol separating the in-loop metric, the audit metric read by the gate, and a blind metric no loop component ever accesses, \textsc{DAPS} reduces semantic-cluster decay of edits by $69.1\%$ and improves relative faithfulness by $83.7\%$ blind and $81.6\%$ audited, while preserving in-loop optimization speed. We provide the code in Github \href{this https URL}{repository}.

---


### 22. [KItCAT: Knowledge Injection via Input Corruption for Auto-regressive Training](https://arxiv.org/abs/2609.00082)

**<font color=#1a73e8>作者：</font>** Meghanadh Pulivarthi, Kushagra Bhushan, Vineet Kumar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs acquire vast amounts of knowledge during pre-training, but often lack the specialized knowledge needed to answer questions from niche sources such as manuals or technical documents unseen during pre-training. Continued pre-training (CPT) is widely used to inject such knowledge into model parameters. However, niche documents seldom repeat facts, making it difficult for CPT to robustly acquire such knowledge. Recent works address this by generating multiple paraphrases of the new knowledge, but paraphrasing is computationally expensive and typically requires powerful LLMs. In this work, we introduce KItCAT: Knowledge Injection via Corrupted Auto-regressive Training, a lightweight training strategy that reduces the need for paraphrasing in decoder-only LLMs. KItCAT augments standard next-token prediction by stochastically corrupting the input sequence. During training, a random subset of input tokens is replaced with other vocabulary tokens while the original next-token labels are kept unchanged. This simple intervention generates diverse training inputs from each sample, enabling large-scale data augmentation at negligible cost. We show that KItCAT consistently improves over CPT across multiple datasets and model families. Code is available at this https URL.

---


### 23. [Retrieval, Scoring, and Decoding Shape Performance and Stability in LLM-based Conversational Recommendation](https://arxiv.org/abs/2609.00086)

**<font color=#1a73e8>作者：</font>** Ante Kapetanovic, Tomislav Duricic, Andro Mercep 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as rerankers in conversational recommender systems, yet measured gains depend strongly on the retrieval and inference protocol. On the ReDial conversational movie recommendation benchmark, we compare proprietary, open-weight, and fine-tuned LLM rerankers with collaborative-filtering and sequential baselines in a shared retrieve-then-rerank pipeline. We vary candidate-pool size, first-stage retriever, and decoding temperature. With a shared semantic top-250 candidate pool and strict candidate-aware scoring, the best proprietary reranker reaches NDCG@10 of 0.1497, compared with 0.0939 for the strongest non-LLM baseline. The same reranker reaches 0.2925 in zero-shot generation, showing that unconstrained scoring can yield a much larger apparent advantage than matched-pool evaluation. No evaluated open-weight LLM outperforms the tuned shallow autoencoder baseline under this protocol. For the strongest proprietary and open-weight rerankers, switching from semantic to collaborative-filtering candidates raises NDCG@10 by more than 50%, showing that measured reranker performance is highly sensitive to candidate generation. For the best proprietary reranker, raising temperature from 0 to 1.0 increases top-10 Jaccard distance from 0.0900 to 0.1240 while mean NDCG@10 changes negligibly, whereas weaker LLMs show larger degradation. These ReDial results support treating candidate generation, candidate-pool size, scoring policy, and decoding configuration as required reporting fields rather than implementation details.

---


### 24. [Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding](https://arxiv.org/abs/2609.00097)

**<font color=#1a73e8>作者：</font>** Zhigeng Liu, Zhiyuan Ning, Ruixiao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of long-context Large Language Models (LLMs) is constrained by the memory bandwidth bottleneck and quadratic complexity of the attention mechanism during decoding. To overcome the inherent trade-offs between the memory overhead of metadata-based metrics and the computational inefficiency of adaptive selection strategies, we present Faster Flash Decoding (FFD), a novel hardware-algorithm co-design framework designed to break the memory wall in long-context decoding. FFD integrates the selector and computer into a fully fused kernel, replacing external metadata indices with content-aware scanning via low-bit quantization. Furthermore, we introduce the top-delta strategy, which dynamically filters blocks to achieve distribution-adaptive sparsity without global synchronization. Offering a training-free and plug-and-play solution, FFD also enables the reuse of scanning results for computation, achieving up to 11.6x kernel-level speedup and scaling to 256K context length, with 2.37x end-to-end throughput improvement. Empirical validation on RULER and LongBench confirms that FFD maintains model accuracy while delivering high-ratio sparsity, with code available at this https URL

---


### 25. [Generative artificial intelligence for reliable mechanistic reasoning for corrosion](https://arxiv.org/abs/2609.00099)

**<font color=#1a73e8>作者：</font>** Bharath M N, R K Singh Raman, Alankar Alankar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Corrosion accounts for approximately 4% of global GDP, and reliable prediction is essential for timely mitigation. Machine learning effectively predicts corrosion rates from composition, microstructure, and environmental variables, but cannot explain the underlying mechanisms. A reliable approach in safety-critical materials engineering requires not only accurate retrieval but also mechanistically defensible reasoning, a capability that existing factuality metrics cannot assess. This work presents a domain-adapted retrieval-augmented generation framework for corrosion knowledge synthesis, demonstrated on magnesium alloy corrosion. Three open-weight language models (Llama-3.1-8B, Qwen-2.5-7B, Mistral-7B) are fine-tuned on 3,309 expert-verified question-answer pairs from 840 peer-reviewed papers and integrated with a hybrid dense-lexical retrieval pipeline. Retrieval augmentation produces Token F1 gains of 143-194%, with system faithfulness of 0.964 and context recall of 0.988. Blind external validation on newly published literature and in-house electrochemical data confirms trend-level generalisation. Reason Map, a proposition-graph framework, is further introduced; it independently constructs directed evidence graphs from generated answers and retrieved literature, enabling systematic detection of causal direction inversions and unsupported inferential leaps that flat factuality metrics cannot expose. The modular architecture can be applied across domains, offering a generalizable blueprint for trustworthy AI-assisted knowledge synthesis to circumvent corrosion, which can also be applied to other engineering domains.

---


### 26. [Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy](https://arxiv.org/abs/2609.00103)

**<font color=#1a73e8>作者：</font>** Shmuel Berman, Jia Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory is widely viewed as an important unsolved problem for LLMs and VLMs, and current benchmarks typically evaluate it by testing accuracy over long text or video. However, accuracy alone misses properties that matter for real long-horizon tasks. We introduce ECCBench, a benchmark and evaluation protocol that measures memory beyond a system's capacity--its raw accuracy at a specific budget--via three axes we call ECC: efficiency--the computation, in FLOPs, needed to answer from memory; compression--whether compressible inputs are remembered more accurately or efficiently; and calibration--whether the system abstains in response to its own uncertainty and the cost of an error. We find that pretrained VLMs compress their memory over text but not video and are poorly calibrated on both. Among a broader set of memory backbones, several non-Transformer architectures achieve better compression-calibration tradeoffs than RoPE Transformers, suggesting they may be useful components for agents operating over long horizons.

---


### 27. [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)

**<font color=#1a73e8>作者：</font>** Xin Zhou, Zongchuang Zhao, Zhibo Yang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving. Qwen-Drive-1.0 retains the architecture of the pretrained vision-language model (VLM) and integrates 3D perception, visual question answering, and motion planning within a unified framework. An external bird's-eye-view (BEV) perception head jointly performs 3D object detection, semantic occupancy prediction, and BEV map segmentation. It serves as a probe of the 3D information accessible from the shared representations and provides an explicit, inspectable interface to 3D scene structure. A Planning Expert conditions on shared VLM representations to generate future ego trajectories. A staged training recipe combines driving supervision with general-purpose vision-language data to acquire driving-specific competence while helping preserve broad visual understanding and instruction-following capabilities. Experiments demonstrate strong 3D perception and driving scene understanding while largely preserving general vision-language capability. Comprehensive evaluations across open-loop, pseudo-closed-loop, and closed-loop settings further show highly competitive motion-planning performance.

---


### 28. [Lingua Franca or Probing Artifact? Rethinking Latent Language in Multilingual LLMs](https://arxiv.org/abs/2609.00155)

**<font color=#1a73e8>作者：</font>** Deniz Bayazit, Badr AlKhamissi, Antoine Bosselut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent language identification is often used to argue that multilingual language models route computation through language-specific states, such as English pivots. However, existing probes infer latent language from different signals, such as the geometry of hidden states or what can be decoded from intermediate representations. Since such claims shape conclusions about how models share and route information across languages, we ask whether these probes measure the same phenomenon or expose distinct aspects of multilingual computation. We study this question across model families, training regimes, domains, tasks, checkpoints, and up to 27 languages. We find that identification probes systematically disagree: the GMM-based representation probe, which draws evidence from hidden state geometry, shows earlier cross-lingual mixing, whereas decoding-based probes, which rely on output-space decodability, retain sharper language-specific and more English-biased signals. These differences track model multilinguality and training progression, but are comparatively stable across domains. Our results suggest a more cautious interpretation of latent language identification, where current probes expose different aspects of multilingual processing, rather than directly revealing a single internal lingua franca.

---


### 29. [Asymmetries in Spontaneous and Instructed Deception](https://arxiv.org/abs/2609.00180)

**<font color=#1a73e8>作者：</font>** Josiah Luikham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models sometimes deceive users without being instructed to. However, much of the study on deception in models involves instructed deception. We investigated the relationship between instructed and spontaneous (uninstructed) deception in Llama-3.1-70B-Instruct. We compared these two deception settings through direction geometry, cross-setting classifiers, and cross-setting steering. We found the two deception settings share a component of direction (cosine of approximately 0.5) and an asymmetry in the transfer between settings regarding detection and causation. Spontaneous trained classifiers performed better on instructed data than vice versa, and instructed derived directions performed better at steering spontaneous prompts than vice versa. Likewise the best token position to derive steering vectors from differed from the best token position to train and apply classifiers.

---


### 30. [Synthetic Worlds for Temporal Evaluation and Knowledge Updating in LLMs](https://arxiv.org/abs/2609.00184)

**<font color=#1a73e8>作者：</font>** Jonathan Zheng, Zirui Shao, Alan Ritter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) rely on static pretraining corpora, causing their knowledge to become outdated over time. Existing approaches for evaluating knowledge edits either suffer from rapid contamination or rely on counterfactual edits that conflict with rigid existing knowledge. In this work, we propose a synthetic, simulation-driven framework for studying knowledge insertion in LLMs. We introduce {\sc ParallelEvents}, a benchmark of fictional yet realistic future worlds that generates coherent event trajectories for controlled evaluation, avoiding contamination while preserving consistency. Building on this dataset, we develop {\sc Synapse}, a training framework that uses model-generated data to update model parameters via mid-training and instruction tuning. This synthetic pipeline enables scalable knowledge integration without costly human-curated data. Empirically, {\sc Synapse} outperforms existing methods by 14.23\%, demonstrating that simulation-based synthetic training leads to robust and coherent knowledge insertions.

---


### 31. [Assessing Suicide Risk in Arabic Crisis Helpline Calls: A Comparison of Arabic and English Large Language Models](https://arxiv.org/abs/2609.00191)

**<font color=#1a73e8>作者：</font>** Linhai Ma, Rita El Hachem, Mahatab El Hajj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Crisis helplines assess suicide risk through structured interviews, a process that is slow and dependent on operator training and workload. Natural language processing could support risk assessment and call prioritization, but almost no work addresses Arabic-language helpline calls or operates within the privacy constraints of real helpline data. We analysed de-identified transcripts from Lebanon's National Lifeline for Emotional Support and Suicide Prevention. Audio never left the helpline: calls were transcribed on site with a speech recognition model for Levantine Arabic, and an Arabic named-entity recognition model removed identifying information locally. Only the de-identified transcripts were shared with the research team. Operators recorded the five suicidal ideation items of the Columbia Suicide Severity Rating Scale, which we combined into two binary outcomes: at-risk and high-risk. We also machine-translated the transcripts into English, giving a paired Arabic/English comparison. On each corpus, we fine-tuned five instruction-tuned large language models alongside six transformer encoder baselines (four Arabic, two English) and evaluated all models on a held-out test set. We included 383 calls: 373 for the at-risk task (52.3% positive) and 297 for the high-risk task (30.0% positive). The best Arabic model reached a macro-F1 of 81.19 and a ROC-AUC of 90.61 on high-risk; the best English model reached 85.00 and 92.59, identifying 88.9% of high-risk calls. In both languages, high-risk calls separated more cleanly than at-risk calls, and translation to English did not reduce the best observed performance. Suicide risk can be classified from de-identified Arabic transcripts without sending audio outside the helpline. The high-risk results support further testing as an operator-facing tool; lower-severity ideation proved the harder case.

---


### 32. [LLM-Driven Autonomous Vehicles Inherit Human Driver Biases in Pedestrian Yielding: Results and Implications From A New Benchmark](https://arxiv.org/abs/2609.00192)

**<font color=#1a73e8>作者：</font>** Irem Yoldas, Martim Brandão, Jie Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public trust in Autonomous Vehicles (AVs) may depend not only on technical success but also on the fairness of their decision making. While a recent trend in AV research involves using general purpose "common sense" models to guide AV decision making, the degree to which these inherit human biases in driving is still understudied. Given that psychology studies have shown human driver biases exist, such as lower pedestrian-yielding rates to Black pedestrians in the US, we argue that analyses of model bias should also be part of AV evaluation. Concretely, in this paper we propose two new bias testing methodologies for Large Language Models (LLMs) and Visual-Language Models (VLMs)-"All Else Being Equal" tests and "Self-Consistency" tests-in order to assess bias in pedestrian-yielding decisions. Our findings show that both LLMs and VLMs make yielding decisions which are influenced by pedestrian gender, ethnicity, religion, disability, age, skin tone and socio-economic status. While the type and degree of bias is different from model to model, we highlight common patterns-and raise questions about the "common sense" model paradigm, particularly the need to either revise the paradigm or address issues of downstream bias.

---


### 33. [ReDeck: Step-Level Render-Grounded Refinement for Document-to-Slide Generation](https://arxiv.org/abs/2609.00194)

**<font color=#1a73e8>作者：</font>** Muzhao Tian, Zezi Zeng, Yifan Yang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Document-to-slide generation is challenging because slides are dense editable artifacts that require both faithful content selection and precise spatial layout. Recent slide agents adopt iterative reflection, but typically follow a monolithic "one version, one feedback" loop: a slide or deck is rewritten, rendered afterward, and critiqued only at the turn boundary. This delayed feedback makes local failures such as overflow, overlap, clipping, and off-canvas placement difficult to attribute and repair. We propose ReDeck, a step-level render-grounded refinement framework that decomposes slide revision into atomic edit actions and returns renderer-derived observations after each step, turning refinement into "one edit, one observation." To balance local repair with global quality, ReDeck uses multi-granular feedback: step-level render feedback for spatial errors, a turn-level adaptive critic for semantic and design guidance, and a submission-level gate for hard layout validation. We further introduce DeckQuiz, a benchmark that decouples content fidelity, spatial correctness, and design quality. Across GPT-5.4, Claude-4.6, and Gemini-3.1, ReDeck consistently outperforms existing slide-generation agents, and ablations confirm that feedback timing and granularity are critical for reliable slide refinement.

---


### 34. [WHALE: A Simple Recipe for Joint Harness-Weight Optimization](https://arxiv.org/abs/2609.00196)

**<font color=#1a73e8>作者：</font>** Haechan Kim, Yoonho Lee, Gisang Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent performance depends jointly on the model parameters and the executable harness code that manages context and control flow. Optimizing either component in isolation can leave the system bottlenecked by its frozen counterpart: weight updates can change which harness is effective, while harness updates can change which model capabilities are exposed. Existing joint-adaptation methods optimize weights and textual prompts but leave the broader harness fixed. We propose Weight-Harness Alternating LEarning (WHALE), a simple recipe that alternates two phases: updating the model under the current harness, then searching for a better harness under the updated model. We instantiate these two phases with online rejection-sampling fine-tuning and Meta-Harness, respectively. When to switch is a key design choice: to separate real improvements from noise without over-optimizing against a changing counterpart, WHALE uses either fixed phase durations or an adaptive patience rule over training signals. Using Qwen3.5-2B/4B agents across three domains (search question answering, mathematical reasoning, and chess puzzles), WHALE outperforms weight-only, harness-only, and Fast-Slow Training by 4.15-24.38 percentage points in best mean@8 accuracy. Either component can be the bottleneck: harness search matches peak weight-only accuracy with far fewer rollouts in SearchQA, but improves math accuracy only after a weight update. Small interleaved updates also outperform stagewise weight-then-harness optimization in accuracy and rollout cost. The code is available at this https URL.

---


### 35. [Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation](https://arxiv.org/abs/2609.00206)

**<font color=#1a73e8>作者：</font>** Ruotong Wang, Zihao Zhu, Siwei Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite their growing use in video moderation, multimodal large language models (MLLMs) exhibit a compositional safety blind spot: videos composed of seemingly benign components can convey harmful meaning when interpreted as a whole. We refer to this phenomenon as Distributed Implicit Harm (DIH), where harm arises from relations among components distributed along a decomposition axis of the video, rather than from any single explicit cue. Among many possible axes, we study two representative cases: temporally distributed harm across visual segments (DIH-T) and cross-modal harm between audio and visual streams (DIH-M). Studying and mitigating DIH at scale requires data that is difficult to collect: such videos lack compositional harm annotations, evade retrieval based on local visual cues, keywords, or single-modality signals, and are consequently absent from existing safety datasets. To bridge this gap, we develop a multi-agent synthesis framework that composes individually benign components into harmful scenarios and generates diverse DIH videos with explicit reasoning annotations, yielding a dataset of over 9,000 videos spanning visual-only and audio-visual settings. Benchmarking over 30 MLLMs spanning frontier proprietary models and leading open-source systems reveals substantial and consistent deficits in detecting both DIH-T and DIH-M. Notably, this failure persists even among the strongest frontier models: they often correctly assess individual components in isolation but fail to recognize the harmful meaning that emerges from their composition. We further evaluate these models on a manually collected set of real-world DIH videos from social media and observe the same failure mode, highlighting DIH as a practical and underexplored challenge for video moderation.

---


### 36. [Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2609.00213)

**<font color=#1a73e8>作者：</font>** Yu Yuan, Yaoyou Fan, Lili Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning fine-tuning of large language models increasingly adopts multiple reward dimensions, including verifiable rules, task-specific evaluators, and learned reward models, to provide richer supervision across diverse capabilities. These dimensions are commonly scalarized with fixed aggregation weights. We identify a failure mode in which aggregation itself induces reward hacking: static projection aliases qualitatively different reward profiles into a single scalar, steering optimization toward whichever dimensions are easiest, densest, or systematically favored by the reward signal. Over training, this traps the policy in suboptimal profiles and prevents convergence to better-balanced ones that would yield higher task performance. To address this, we propose Adaptive Multi-Reward Projection (AMRP), a lightweight online method that reallocates aggregation weights using three signals, relative shortfall, reward volatility, and recent progress, increasing pressure on lagging, unstable, or stagnant dimensions while relieving saturated ones. Across structured reasoning, citation-grounded generation, and open-ended alignment under GRPO, AMRP consistently improves reward-profile balance and downstream performance over fixed and dynamic weighting baselines; it also remains effective with GDPO and PPO, supporting compatibility across RL algorithms. Our code is available at this https URL.

---


### 37. [LLM-as-a-Demographic: Whom Sociodemographic Prompting Helps, and Whom It Hurts](https://arxiv.org/abs/2609.00222)

**<font color=#1a73e8>作者：</font>** Daniela Occhipinti, Andrea Piergentili, Marco Guerini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as judges for subjective tasks, where annotators disagree and the relevant question is not only how accurate a judge is, but whose judgments it reproduces. Sociodemographic prompting conditions the judge on an annotator's demographic profile to align its judgments with the corresponding group's. We test whether this alignment emerges distributionally, comparing the predicted label distributions of 23 open-weight LLMs on three subjective tasks against those of real annotator groups, under three conditions: no demographic information, single-attribute profiles, and intersectional profiles over gender, age, race, and education. Three findings emerge. First, a judge prompted with no demographics is not perspective-neutral: models best reproduce the judgments of White, college-educated annotators. Second, demographic conditioning is asymmetric: it moves the judge toward majority groups and away from minority groups, most strongly on offensiveness, where intersectional profiles amplify the harm. Third, by comparing base and instruct models we identify instruction-tuning as a possible source of the asymmetry. Demographic conditioning should therefore be used with caution to estimate group judgments: conditioning moves predictions away from the reference distributions of the minority groups the method is often invoked to serve.

---


### 38. [QTEA: Ternary LLMs with Sparse Residual Salient Weight and By-Column Optimization](https://arxiv.org/abs/2609.00224)

**<font color=#1a73e8>作者：</font>** Yipin Guo, Arun M George, Jie Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-only post-training quantization (PTQ) can alleviate the computational burden of serving large language models (LLMs) at scale. However, existing PTQ methods often fail to generalize across models and suffer severe accuracy loss below 2 bits. Many leverage unstructured sparsity to mitigate this loss, but at the cost of regularity and GPU-friendly execution. We present QTEA, a sub-2-bit PTQ framework that quantizes weights into ternary values and uses salient weights as residual error compensators. To maintain hardware efficiency, residuals are assigned to selected columns with semi-structured \(1{:}4\) sparsity within the salient columns. We further add column-wise rescale refinement to GPTQ-style column-by-column quantization, alternately updating per-column scales and ternary assignments to reduce reconstruction error. We also identify order-dependent error propagation in GPTQ and introduce error decay to attenuate late-stage error accumulation. On Qwen3-14B, QTEA compresses all weights to an effective 1.7 bits per weight while improving average accuracy over the strongest ternary PTQ baseline by 16.7\%. It also achieves 1.40\(\times\) and 2.61\(\times\) lower perplexity on WikiText and C4 respectively. This trend holds on Llama3-8B, where QTEA obtains a 6.6\% accuracy gain and 1.34\(\times\)/1.95\(\times\) lower perplexity on the same datasets. Finally, we develop a lookup-table based kernel that achieves 7.2\(\times\) faster per-token generation over an FP16 baseline. Code is available at this https URL.

---


### 39. [Bridging Lexical Divergence: LLM-Assisted, Cost-Efficient, Zero-shot Scientific Entity Linking](https://arxiv.org/abs/2609.00228)

**<font color=#1a73e8>作者：</font>** Md Rasel Khondokar, Qiao Qiao, Farjana Sultana Samia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific domain entity linking (EL) differs from general domain EL because mentions and entity names often lack lexical overlap. Another challenge is that specialized terminology is used in the scientific domain, which is rarely encountered in models pretrained on general domains. Therefore, models trained on general domains transfer poorly to scientific domains. To address this, in-domain fine-tuning is the natural remedy. However, many scientific domains lack expert-annotated data, motivating the need for a zero-human-annotation approach. Existing zero-shot methods heavily rely on LLMs to generate aliases across entire mention corpora, which incurs substantial computational cost, and those methods provide no mechanism to filter out noise from LLMs. To address these challenges, we propose Sci-ZSEL, a framework that selectively generates entity aliases with an LLM to control computational cost, and applies an ontology-aware filter to remove aliases that semantically drift toward ontology neighbors. Then, filtered aliases are used to construct pseudo-labeled mention-entity pairs for fine-tuning. To enable evaluation of EL under low lexical overlap, we also release a new animal science EL benchmark linked to three livestock trait ontologies, where mentions and entities exhibit substantially lower lexical overlap than in existing benchmarks. Across five benchmarks, Sci-ZSEL outperforms the non-fine-tuned baseline, is most useful on nonoverlapping mentions, and combining it with curated synonyms gives the best performance in most settings.

---


### 40. [Beyond Language Priors: Diagnosing and Fixing Visual-Origin Hallucinations in Multimodal LLM](https://arxiv.org/abs/2609.00231)

**<font color=#1a73e8>作者：</font>** Peiyang Xu, Xiaopei Zhu, Jun Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing research on object hallucination in multimodal large language models (MLLMs) predominantly attributes the problem to language priors such as over-reliance on textual co-occurrence statistics. We challenge this view by presenting quantitative evidence for a complementary, under-explored cause: visual-origin hallucination, where hallucinations arise from incorrect visual feature extraction and misalignment between image and text embeddings. Through cosine similarity analysis and Smooth Grad-CAM entropy measurements, we show that hallucinated samples exhibit systematically lower image-text similarity (average 0.158 vs. -0.122) and inverted attention patterns, where attention is dispersed when the target object is present but wrongly concentrated when it is absent. Guided by this diagnosis, we propose Adversarial Contrastive Fine-Tuning (ACFT). ACFT uses an Adversarial Hallucination Attribute Flipping (AHAF) procedure, involving minimal, targeted adversarial perturbations that flip an image's hallucination attribute, to construct perfectly aligned positive-negative pairs, which are then used for contrastive fine-tuning. AHAF simultaneously serves as a diagnostic probe, revealing that MLLM visual representations lie dangerously close to hallucination decision boundaries. Requiring only 0.9% of the COCO dataset and adding zero inference overhead, ACFT achieves state-of-the-art performance on POPE, MME, and four description-level hallucination benchmarks across LLaVA, MiniGPT-4, and Qwen2.5-VL. Code is available at this https URL

---


### 41. [Beyond Blind Compliance: Benchmarking Task Verification in OCR Reasoning](https://arxiv.org/abs/2609.00232)

**<font color=#1a73e8>作者：</font>** Yue Zhou, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved strong performance on OCR-centric document understanding and text-rich visual reasoning benchmarks. Yet existing evaluations largely assume that every task is valid and answerable. In real-world OCR scenarios, this assumption often fails: questions may rely on illegible text, occluded evidence, nonexistent visual targets, contradictory premises, or missing variables. We study this reliability gap as OCR-grounded Task Verification: before answering, a model should determine whether the Image Premise (IP), Textual Premise (TP), and Question (Q) jointly define an executable task.
We introduce VeriOCRBench, a 1,800-sample human-verified benchmark built from source images drawn from 8 OCR-related datasets and spanning 8 real-world image domains, with controlled, image-grounded diagnostic tasks.
It contains 1,600 trap-injected invalid tasks across 8 trap types and four verification dimensions---Visual, Contextual, Factual, and Logical---plus 200 trap-free controls for measuring over-refusal. Built with a Visual Atomic Fact (VAF)-anchored pipeline and full human auditing, VeriOCRBench enables decoupled evaluation of task verification, root-cause diagnosis, and over-refusal. Evaluating 15 leading MLLMs reveals persistent blind compliance, diagnosis failures, and prompt-induced over-refusal, exposing a critical reliability gap in current OCR reasoning systems.
The code is available at: this https URL.

---


### 42. [Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems](https://arxiv.org/abs/2609.00237)

**<font color=#1a73e8>作者：</font>** Rakibul Hasan Rajib, Mengxing Zheng, Qian Lou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems tackle complex reasoning by orchestrating how multiple agents are configured and how they collaborate. A central challenge is to adapt orchestration to the evolving collaboration state. Routing from the query alone cannot adapt to intermediate progress or errors, which hurts accuracy. Routing from the complete execution history supplies this missing context, but forces later decisions to process every prior step, including redundant or low-utility ones. This creates an execution-history overload that inflates cost. Effective orchestration instead requires a compact state that captures useful progress without accumulating redundant context. We propose Gated-Memory Routing, which conditions each decision on the query and a learned execution memory. A learned Memory Write Gate commits only non-redundant reasoning steps, and a learned Retrieval Gate supplies each agent a compact, relevant subset, so every decision conditions on a clean, informative state. At each step, the system selects the next role and backbone from this memory, while an Adaptive Halting Controller stops execution once the memory contains sufficient evidence for answering. Across five reasoning and code-generation benchmarks, our framework is both effective and efficient: it attains the best average accuracy, exceeding the strongest baseline by 2.44 points, while reducing HumanEval inference cost by 31.9% relative to that baseline. Code is available at this https URL

---


### 43. [CoLT-Drive: Counterfactual Long-Tail Benchmarking and Knowledge-Preserving Adaptation for Driving Affordance Prediction](https://arxiv.org/abs/2609.00242)

**<font color=#1a73e8>作者：</font>** Zhengxu Tang, Guofeng Cui, Ziyu Gong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tail autonomous driving failures are often framed as rare-object recognition errors. We argue that this view is incomplete: the decision-critical question is not only whether a model recognizes an unusual object, but whether it infers how that object changes the ego vehicle's feasible high-level actions. We formalize this problem as decision-level driving affordance prediction, where a model maps a front-view image, ego-motion history, and navigation command to a structured longitudinal--lateral meta-action. To evaluate this capability, we introduce CoLT-Drive, a 3,536-sample counterfactual long-tail benchmark that inserts rare objects into otherwise fixed driving scenes and measures whether models predict acceptable action pairs. To improve deployable small VLMs, we propose KPA, a knowledge-preserving adaptation framework that combines structured perception-to-decision prompting, SLERP-based expert merging, and RegMoE, a regime-aware LoRA mixture-of-experts module. KPA preserves the pretrained model's open-world knowledge while allocating lightweight adaptation capacity to different driving decision regimes. Experiments on an in-domain driving split and CoLT-Drive show that KPA achieves 60.8\% pair accuracy on CoLT-Drive, outperforming the pretrained Qwen3-VL-2B baseline (50.3\%) and LoRA SFT (32.4\%) while maintaining competitive in-domain accuracy. Our benchmark and code are available at this https URL and this https URL.

---


### 44. [Invalidation Contracts for Cross-Episode Agent Memory](https://arxiv.org/abs/2609.00243)

**<font color=#1a73e8>作者：</font>** Michael Wu, Arquimedes Canedo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents that cache recovery suggestions from API errors can skip re-derivation in later episodes, spending fewer tokens and fewer model calls on constraints they have already learned. Server-side data drift turns those cached fixes into silent failures, and the usual remedy, re-deriving on every episode, gives the savings back. We introduce invalidation contracts, a protocol layer that attaches version stamps and cacheability hints to every recovery suggestion so the client can evict stale entries without trial and error, and keep the rest. The contract decomposes realized savings into two independent factors: validity, the fraction of cached suggestions that remain correct after a drift event, and compliance, the fraction the planner applies on the first attempt. Validity depends only on the protocol and is vendor-independent. Compliance depends on the planner model: identical wire bytes yield 100% first-try compliance on Claude Haiku 4.5 and 11% or below on Claude Sonnet 5, which exhibits input-schema conservatism, refusing fixes that add fields the original request did not contain. We evaluate across seven models, three serving paths, two domains, and approximately 9,400 episodes. Row-level invalidation raises compliance by 0 to 66.7 percentage points across the seven models, 55.6 to 66.7 on three, and recovers 29-33% of baseline token cost on four of seven models, while table-level invalidation destroys co-located entries and drops post-drift first-try rates to 0% on five of seven. Eviction precision is 1.00 at row granularity on every model under the row-level oracle of Section 4.1. The contract adds 15% to response payload. Version-stamp validity is deterministic by construction and produced identical results across every model and serving path, with zero contract failures in the entire evaluation.

---


### 45. [Authority Bias in Conversational Search Engines for Academic Paper Recommendation](https://arxiv.org/abs/2609.00248)

**<font color=#1a73e8>作者：</font>** Uthman Jinadu, Parsa Ghazvinian, Anjila Budathoki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used as conversational search engines for academic literature, yet whether they judge papers on content or on authority signals has not been tested causally. We investigate authority bias: systematic preference for papers based on author prestige, venue, and citations rather than content. Holding title and abstract constant, we vary authority metadata across three counterfactual conditions (original, flipped, boosted) over eight LLMs (five open-weight and three frontier closed-weight) in an in-context, single-turn, top-1 recommendation setting. Our experiments show that authority bias is substantial and directional, varies markedly across models, and is only partially addressable through prompt-level debiasing. We further document a say-do gap: debiasing instructions suppress authority mentions far faster than authority-driven flips, so surface auditing systematically underestimates behavioral bias.

---


### 46. [Hypotheses-Guided Self Distillation for Continual Personalization](https://arxiv.org/abs/2609.00251)

**<font color=#1a73e8>作者：</font>** EunJeong Hwang, Kushan Mitra, Dan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As people increasingly interact with LLM assistants in daily life, continually adapting to individual preferences has become essential for effective long-term interactions. However, user preferences are rarely stated in full, and instead emerge through heterogeneous, latent, and noisy signals, with existing methods relying on raw interaction histories or costly reward-based optimization to manage personalization. We introduce HypReflect, a reliable, scalable framework for continual personalization that infers explicit, uncertainty-aware preference hypotheses from diverse user signals, reflectively refines them as new evidence accumulates, and incorporates the resulting user model through hypotheses-guided self-distillation. Experiments across three personalization settings: online personalization, multi-session interactions, and implicit behavioral signals, show that HypReflect outperforms a range of baselines, including raw-history and incremental-update methods. We further demonstrate strong generalization to unseen users and cross-domain settings, along with stability across context budgets, reusable hypotheses, and more focused personalization. These results suggest a step towards reliable and scalable continual personalization through explicit, revisable user preference hypotheses.

---


### 47. [NSIDDx: A Design Framework for Neuro-Symbolic, Practitioner-First Differential Diagnosis in Low-Resource Settings](https://arxiv.org/abs/2609.00256)

**<font color=#1a73e8>作者：</font>** Aarav Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based diagnostic systems achieve high semantic accuracy on benchmarks, but open-ended evaluation on clinically uncommon presentations reveals a systematic gap between headline accuracy and verifiable clinical reliability. We evaluate an LLM+rare-disease-RAG pipeline across two cohorts and show that the paradigm produces confident outputs that are frequently unverifiable and systematically resistant to clinician interrogation. We present NSIDDx (Neuro-Symbolic Integrated Differential Diagnosis System), a design framework arguing that DDx systems in low-resource settings must treat the clinician as an active reasoning agent. We instantiate this through a neuro-symbolic pipeline with ternary symptom encoding, contradiction detection, audit strings, and practitioner override - running offline on consumer hardware. We distill five design principles for clinician-in-the-loop clinical NLP and invite the prospective studies needed to validate the claim at scale.

---


### 48. [The Answer Is Not the Argument](https://arxiv.org/abs/2609.00264)

**<font color=#1a73e8>作者：</font>** Will Yeadon, Sergio Juárez, Paul Mackay 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought monitoring is proposed for AI oversight, yet evaluations often provide monitors with a trusted reference answer. We ask whether answer access improves reasoning verification or mainly exposes incorrect conclusions. We collected 237 step-numbered solutions to 79 Humanity's Last Exam physics questions from three frontier models, with no inserted errors, and independently labelled final-answer correctness and the first false step. The reference standard combined physicist annotations, an independent LLM debate, and source-masked adjudication. This yielded 24 critical traces in which the answer was correct but the trace contained a genuine error. 8 LLM monitors evaluated traces blind, with an unverified or certified answer, or after a blind commitment. Certification raised mean balanced accuracy from 0.637 to 0.796, while exact first-error localization rose from 0.261 to 0.379. Certification changed recall (the fraction of error traces flagged as erroneous) from 0.653 to 0.951 on wrong-answer traces but from 0.521 to 0.438 on critical traces; the contrast had the same direction for all 8 monitors (question-bootstrap 95% CI [+0.256, +0.506]). After blind commitment, monitors shown the answer newly flagged 93.8% of previously passed wrong-answer traces as erroneous, but only 18.0% of critical traces. Answer access therefore improves conclusion-consistency checking rather than independent verification of the supporting argument. For AI safety, these traces provide a benign analogue of reward hacking: an acceptable output does not establish that the process producing it was sound. Although the errors studied here were ordinary and mostly non-load-bearing rather than adversarial, trusted-answer evaluations may similarly overstate monitoring capability when acceptable outputs conceal unsound reasoning.

---


### 49. [Autoresearch for Marketplace Catalogs: From Legacy Forms to AI-Native Matching](https://arxiv.org/abs/2609.00274)

**<font color=#1a73e8>作者：</font>** Kartik Ravisankar, Hojat Abdolanezhad, Daniel Capo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two-sided service marketplaces are moving from deterministic request-form intake to AI-native probabilistic matching, enabled by large language models (LLMs) that infer intent, preferences, and latent constraints from natural language. Relying on inferred intent rather than fixed-form fields forces these platforms to regenerate the provider-side preference taxonomy underwriting matching, search, and pricing: attributes interpretable to service providers while remaining a useful signal for marketplace decisions. We present an autoresearch loop that generates this taxonomy, one occupation at a time, and has been deployed in production at a major U.S. consumer services marketplace since April 2026, spanning 132 occupations. Instead of one global hierarchy, the loop treats each occupation as an independent generation problem and runs iterative propose-evaluate-keep refinement cycles. Each candidate tag set is scored by a recalibrated six-rubric LLM-as-judge framework, and a 7-critic panel of distinct personas contributes weighted penalties to an adjusted score, with no hard vetoes. A separate parity-mapping stage maps legacy request-form Q&A pairs back to the generated taxonomy, yielding both a coverage signal and an interface for human quality assurance; it does so by first inferring the provider attribute each legacy question was meant to measure, rather than translating questions to tags literally.

---


### 50. [The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems](https://arxiv.org/abs/2609.00275)

**<font color=#1a73e8>作者：</font>** Bardia Mohammadi, Laurent Bindschaedler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fleets of LLM agents now externalize effects that cannot be fully undone: they move money, deploy code, delete data, and disclose information. Current controls check one effect at a time, so a fleet of individually authorized agents can overdraw its principal's risk under a shared trigger while every local gate stays correct. We propose the irreversibility budget, a cumulative account of residual value-at-risk that a trusted runtime maintains for each principal across agents, workflows, and tenants. Treating irreversibility as a first-class resource, the runtime charges each effect its residual loss below the agent and denies the marginal effect once the aggregate would overdraw the budget. Getting the price right is hard, because effects are heterogeneous, adversarially declared, and correlated. We perform a controlled study in which per-effect gates admit fleet-level overdraws of up to 48 times the tenant's risk limit while the budget holds every correctly charged run within that limit. Conservative, dependency-aware pricing remains the central open problem for a deployable design.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-295](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
