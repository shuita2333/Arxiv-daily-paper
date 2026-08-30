# 🧠 大模型相关研究 | 2026年08月31日

> 本类共 **231** 篇论文：已确认 **221** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

---

### 51. [Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling](https://arxiv.org/abs/2608.26199)

**<font color=#1a73e8>作者：</font>** Leonardo Liparulo, Francesco Pierri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We ask whether AI agents powered by locally deployed large language models can reliably automate expert-defined hardware design workflows in an industry-realistic tool-calling setting. In these environments, engineers issue repetitive, dependency-ordered operations---such as creating components, adding ports, and wiring connections---through specialised tools. Confidentiality constraints on component specifications and naming conventions often preclude hosted proprietary APIs, motivating the use of locally deployed models. To study this setting, we build a Model Context Protocol (MCP) server that reproduces the state and dependency logic of a proprietary hardware design tool used in embedded system development and construct a benchmark covering single-operation edits, multi-step dependency chains, invalid requests, misspelled prompts, and multi-server tool contexts. We evaluate seven open-source models comparing pipeline choices including system prompts, tool-description detail, context scope, and single-agent versus multi-agent architectures. Results show that strong models can achieve near-complete expected-call coverage on the benchmarked workflows, but reliability depends strongly on both task structure and agent configuration. Comprehensive tool descriptions consistently reduce failures, few-shot prompting can cause severe inaction for some models, cumulative context harms constrained models, and multi-agent decomposition helps weak workers or long sessions at the cost of additional calls. These findings provide practical guidance for deploying local LLM agents in stateful hardware design environments.

---


### 52. [ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices](https://arxiv.org/abs/2608.26204)

**<font color=#1a73e8>作者：</font>** Joy Chen, Alejandro Castillejo Munoz, Pierluca D'Oro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer Use Agents (CUAs) are increasingly deployed to navigate mobile and desktop applications on behalf of users, yet no benchmark comprehensively evaluates whether they can safely interact with visual interfaces while handling ambiguous instructions. We introduce ADeptS-Bench, a dual-stream trustworthiness benchmark, grounded in the ADEPTS capability framework and general population user studies. The Safety stream provides paired benign/malicious tasks with threats embedded in the visual interface. The Disambiguation stream evaluates whether agents seek clarification when intent is ambiguous. Evaluating seven models reveals that no model consistently exceeds 80% task success while staying below 30% attack success; every model clicks "Checkout" on a $25K order without hesitation, and none detects that a "factory reset" button is mislabeled as "Optimize." An ablation reveals three distinct safety architectures: tool-dependent (ASR +21-23pp without refusal tool), partially tool-dependent (+10-11pp), and no mechanism (unchanged). In disambiguation, all models overestimate consequence severity, mirroring the over-refusal bias observed in safety. We release all data, evaluation code, and analysis tools upon publication.

---


### 53. [Surgical Video Generation From Diffusion to World Models: A Survey](https://arxiv.org/abs/2608.26214)

**<font color=#1a73e8>作者：</font>** Fuxiang Huang, Chenxu Zhang, Liang Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video data provides the primary training resource for models of intraoperative perception, surgical workflow understanding, and robotic decision-making. However, clinical data acquisition remains constrained by privacy, cost, and class imbalance. Surgical video generation has emerged as a transformative approach to addressing data scarcity and as a foundation for surgical simulation, training, and robotic policy learning. The field has developed rapidly without a clear conceptual framework. This survey organizes the 2024-2026 literature into three categories: unconditional generation, conditional generation, and world modeling generation, revealing a fundamental shift in how the task is defined from synthesizing visually plausible frames to modeling the causal dynamics of surgical scenes. We examine the persistent gap between pixel-level fidelity and clinical plausibility, and identify generalization, physical realism, controllability, and interpretability as bottlenecks. We further summarize experimental results of representative methods on public datasets to provide a quantitative reference for the field. This survey provides a structured overview of the current state and open challenges, offering a reference for researchers working at the intersection of intelligent perception, multi-modal fusion, generative AI, and surgical data science.

---


### 54. [Same Model, Different Harness: Different Coding-Agent Results](https://arxiv.org/abs/2608.26218)

**<font color=#1a73e8>作者：</font>** Sydney Lewis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A coding agent combines a model with a harness, which decides what the model sees, which tools it can use, and how the work continues. We ask whether changing the harness changes the result when the model and task stay fixed. We compare two configurations of the same harness on three coding benchmarks. The control supplies the full conversation in time order, while the treatment keeps the same record but mechanically shortens older tool results as the context fills and responds to repeated or stalled work.
Under tight context, the treatment raises mean per-task fail-to-pass fraction (F2PF) in all three pressure comparisons and increases complete solutions on SWE-bench Verified and SWE-bench Pro. The tight-window Verified comparison uses 169 tasks, a 20,480-token window, and a fixed 480-second attempt endpoint; on this cohort, treatment raises mean per-task F2PF from 28 percent to 49 percent and complete solutions from 43 to 72. Without model-specific retuning, the same frozen treatment also raises both endpoints on the same cohort for three additional models with different designs. In the wide-window Qwen3.6 comparisons, observed arm outcomes are close on Verified and Pro, while FeatureBench retains a higher mean per-task F2PF under treatment. On the wide-window Verified cohort, treatment also serves fewer prompt tokens per turn. Because changing the harness changed what unchanged model weights could accomplish, coding-agent evaluations should treat the model and harness together as the tested solver.

---


### 55. [NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation](https://arxiv.org/abs/2608.26222)

**<font color=#1a73e8>作者：</font>** Zhiyuan Xu, Muhammad Firhard Roslan, Joseph Gardiner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcome.
This paper presents NeuronFuzz, a white-box fuzzing framework that exploits internal safety neurons as continuous execution feedback for LLM safety evaluation. A SafetyOracle converts safety-neuron activations into a continuous safety alarm score that serves as feedback for fuzzing and can be obtained during prefill, eliminating response generation from the fuzzing loop. To construct the SafetyOracle, NeuronFuzz uses template-invariant harmful and benign inputs and stability-aware selection to identify a compact set of safety neurons whose activations capture harmful-intent recognition. Moreover, since the safety alarm score is differentiable, NeuronFuzz uses its gradients to identify safety-sensitive template positions and a masked language model to generate fluent, context-compatible mutations while preserving original harmful payload and avoiding additional optimization variables. We evaluate NeuronFuzz across 21 text and multimodal models. Across five white-box source models, it achieves a 76-100% jailbreak discovery rate, outperforming baselines by up to 48 percentage points. Its optimized templates further transfer zero-shot to open-weight and six proprietary target models, achieving average ASR and top-5 ensemble ASR (EASR) of 69.6%/92.6% and 44.1%/60.0%, respectively.

---


### 56. [LLM Agents for Time-Series: A Survey](https://arxiv.org/abs/2608.26226)

**<font color=#1a73e8>作者：</font>** Yilong Chen, Xiao Qin, Chenghao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly being developed for time-series problems, but their design choices vary substantially across task settings. This survey adopts a problem-driven taxonomy that organizes these systems by the time-series problems they address rather than by isolated technical components. We group existing systems into four categories: forecasting and reasoning, augmentation and synthesis, anomaly detection and diagnosis, and decision support. Within each category, we examine how task requirements shape agent architecture, tool use, and memory design. We further summarize representative datasets and environments, and compare reported model performance under shared or closely related settings. Overall, this survey offers a task-oriented guide to designing LLM-based agents for time-series problems and identifies open gaps for future work.

---


### 57. [The Reasoning Tax: Token Economics of LLM Reasoning Across Task Types and Deployment Contexts](https://arxiv.org/abs/2608.26235)

**<font color=#1a73e8>作者：</font>** Sachin Gopal Wani, Ajay Dholakia, David Ellison  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accuracy-only benchmarking of reasoning-capable large language models misses a central deployment question: when do extended thinking tokens earn their cost? We introduce the Token Economy Score (TES), a marginal benchmarking metric that measures the accuracy gain of a reasoning model over a non-reasoning baseline, normalized by the generated-token multiplier. We define paired and approximated TES variants for model families with reasoning toggles and frontier models without direct non-reasoning counterparts. We then conduct an empirical benchmarking analysis across 151 model-benchmark evaluation runs on seven benchmarks spanning mathematics, code generation, science reasoning, instruction following, expert knowledge, knowledge recall, and research-level physics. The analysis examines three deployment-facing dimensions: which task structures yield positive marginal reasoning efficiency, how increasing reasoning effort changes TES within model families, and how deployment context changes economic viability. Results show that task structure predicts reasoning efficiency better than nominal difficulty: sequential inferencechain tasks such as AIME 2025 and LiveCodeBench show high TES, while knowledge-recall tasks such as MMLU-Pro show low TES despite their difficulty. We also find systematic diminishing returns at higher reasoning effort levels, including cases where additional thinking reduces accuracy. Finally, Reasoning Cost Share (RCS) shows that inference spend is often dominated by internal thinking, while Deployment Cost Multiplier (DCM) shows how on-premises deployment can change the economics of otherwise costly reasoning workloads. These findings support a benchmarking-driven model-selection rule: enable reasoning selectively by task type, effort level, and deployment context rather than treating it as a universally beneficial mode.

---


### 58. [How Do LLM Agents Actually Get the Flag? Trace-Level Provenance for Agentic Offensive Security Evaluation](https://arxiv.org/abs/2608.26237)

**<font color=#1a73e8>作者：</font>** Kimberly Milner, Minghao Shao, Nanda Rani 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Capture-the-Flag (CTF) benchmarks are widely used to assess the offensive security capabilities of autonomous language-model agents. Evaluations rely on shallow binary judgments or aggregate scores, overlooking the agent's trajectory to the flag. Consequently actual exploitation is conflated with direct flag exposure, memorized recall, external lookup, guessing, and unsupported claims, potentially overstating the agent's cybersecurity capability. We introduce CTF-ABACUS, a trace-based agent auditing framework that reconstructs each run as an evidence-grounded solve profile. By decomposing agent actions into penetration-testing phases and categorical techniques, it identifies where exploitation occurs, where the flag first appears, and whether the recovered flag is supported by demonstrated behavior. Aggregating solve profiles across agents yields challenge signatures that reveal whether success was achieved via the intended exploit or via shortcut pathways. We apply CTF-ABACUS to 1,435 CTF attempts by six frontier and open-source models on 240 challenges, yielding 2,870 solve profiles under two judge lenses. Trace-verified exploits account for only 62-87% of recovered flags across benchmarks, while shortcut recoveries follow substantially shallower trajectories. These findings shift CTF evaluation from counting recovered flags to verifying demonstrated exploitation and provide a basis for designing benchmarks that better isolate the offensive capabilities.

---


### 59. [Procedura: Agentic 3D Modeling with Procedural Control](https://arxiv.org/abs/2608.26238)

**<font color=#1a73e8>作者：</font>** Youtian Lin, Yikang Yang, Zhanpeng Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Native 3D generators now recover impressive mesh geometry from a single image. However, a dense mesh stays soft where a machined object should be sharp, it carries no part decomposition, and it exposes no parameter a user could edit. To address this, we explore the paradigm of 3D shape as code, leveraging and scaling the coding ability of an LLM for 3D modeling. We introduce Procedura, a novel 3D modeling agent framework that writes an object as a procedural assembly, a parametric program whose named parts are joined by typed, machine-checkable mates. From a text prompt, the agent plans the object as an assembly graph and writes the program part by part, solving each placement from the mated frames rather than guessing it, and admitting a part only once compile, mate, and connectivity checks pass. A decoupled vision critic then refines the assembly one diagnosed fix at a time. Moreover, the same graph carries per-part materials and a simulator-validated articulation. We evaluate on P3D-Bench under its assembly judge, and with the same judge on MechBench-36, our hard-surface benchmark. On both, Procedura outperforms state-of-the-art native 3D generators and every prior 3D-code agent on judged quality, produces the sharpest edges of any method we evaluate, and is the only one whose output is an editable, part-structured program.

---


### 60. [SKILL.state: Scalable Long-Horizon Agent Skills](https://arxiv.org/abs/2608.26263)

**<font color=#1a73e8>作者：</font>** Sanket Badhe, Priyanka Tiwari, Jonghyun Chung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly act as autonomous agents executing complex, long-running procedural skills. Existing agent runtimes maintain execution by continually appending observations, actions, and intermediate reasoning traces to an ever-growing conversation history, causing latency degradation and context-poisoning failures over long horizons. We present this http URL, a runtime architecture that replaces append-only conversational history with an explicit, mutable execution state. At each execution step, the model receives only the immutable skill specification, the current structured execution state, and the latest observation. Intermediate reasoning is discarded immediately after producing a validated state update, preventing prompt growth with execution history. Across diverse datasets, models, and execution environments, this http URL improves task accuracy while substantially reducing cumulative token consumption. Our results demonstrate that explicit execution state is an effective and architecture-agnostic abstraction for scalable long-horizon agent skills.

---


### 61. [Muon with Finite Newton-Schulz: The Smoothing Benefit in Nonsmooth Nonconvex Optimization](https://arxiv.org/abs/2608.26288)

**<font color=#1a73e8>作者：</font>** Mingyi Li, Taira Tsuchiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has emerged as a strong optimizer for the matrix-valued parameters in large language model pretraining, approximately orthogonalizing its momentum with a few Newton-Schulz iterations. Existing theory either replaces this iteration with the exact polar factor it approximates, or treats its finite depth as an approximation error, and thus the iteration Muon actually runs can only hurt the guarantees. We show that finite Newton-Schulz can instead be beneficial for nonsmooth nonconvex optimization. To this end, we analyze Muon through the online-to-nonconvex conversion, which views the update rule as an online learner and converts its regret bound into a stationarity guarantee. The finite Newton-Schulz iteration smooths the discontinuous polar map into a Lipschitz map of the singular values, and Muon with finite Newton-Schulz can be regarded as an online learner with a smoothed spectral potential. This smoothing is exactly what the conversion needs: we prove that a Newton-Schulz depth growing only logarithmically in the target accuracy suffices for convergence to stationary points in nonsmooth nonconvex optimization, whereas Muon with the exact-polar update may fail to converge. The resulting sample complexity bounds match the best-known guarantees for nonsmooth nonconvex optimization and are optimal for smooth nonconvex optimization up to problem-dependent factors. The argument extends beyond Newton-Schulz to general spectral maps with the same smoothing property.

---


### 62. [Assessing mentalization in humans and large language models](https://arxiv.org/abs/2608.26291)

**<font color=#1a73e8>作者：</font>** Aamir Sohail, Xintong Zhong, Arkady Konovalov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mentalization - the ability to infer others' beliefs and intentions to guide one's own choices - is a key cognitive function underlying human social interactions. Large language models (LLMs) demonstrate behaviour consistent with humans on theory-of-mind tasks, yet whether these models can guide adaptive behaviour through mentalization is unknown. Here we use two economic games with cognitive computational modeling to uncover the latent strategies underlying mentalization in LLMs. We tested individual LLM agents across four model families, DeepSeek, GPT-4.1, GPT-5 and Gemini 2.0 Flash (N = 2,099), against opponents of varying sophistication and examined whether a prompting strategy designed to elicit strategic reasoning improved performance. We benchmarked results against human participants (N = 251) as a comparative measure. Across both games, LLMs showed clear behavioural and computational signatures of mentalizing that differed markedly by model provider and size. Strategic prompting generally improved performance by inducing more sophisticated reasoning, yet the extent of the benefit differed across the two tasks. Last, GPT-5 agents flexibly adapted their recursive depth of reasoning to increasingly sophisticated opponents, demonstrating superior performance to human participants. Collectively, we demonstrate different capacities for mentalization across LLMs, and highlight cognitive computational modeling as a formal method for assessing comparative intelligence across humans and machines.

---


### 63. [On Scope Classification and Current Knowledge-Editing Benchmarks: A Negative Result, with INLAY as a Gradient-Free Case Study](https://arxiv.org/abs/2608.26292)

**<font color=#1a73e8>作者：</font>** Aditya Pratap Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every memory-based knowledge editor in the SERAC lineage depends on a scope decision: given a query, does a stored edit apply? We report that current knowledge-editing benchmarks cannot measure this decision at all. Using INLAY, a gradient-free editor we built to obtain exact per-query ground truth (the model is frozen, edits live in an external addressable memory, and applying an edit is a bias added along one token's unembedding direction at decode time), we execute every candidate router action on 1,689 queries spanning three datasets and three input conditions. An oracle router choosing the best action every time ties a one-line static policy to four decimal places in all nine dataset-by-condition cells: the maximum attainable gain of any per-query routing method is 0.00 points. Abstention is the sole winning action zero times out of 1,689. The cause is structural: these are counterfactual benchmarks whose evaluation question asks for the post-edit answer, so answering from parametric knowledge is wrong by construction, and a benchmark without negatives cannot reward a classifier's ability to reject. This generalizes beyond our system to the whole scope-classifier family the benchmarks are used to evaluate. We confirm the mechanism directly: constructing the missing condition ourselves, by withholding a query's own edit from the index for half the sample, moves pooled headroom from exactly +0.0000 to +0.0420 and gives abstention its first wins. We also report where INLAY itself does not win (WISE beats it on Qwen2.5-7B CounterFact, and retrieval-augmented generation beats every method we tested, INLAY included, on rigorously matched RippleEdits), and disclose two bugs found during a self-audit of our own routing machinery, neither of which changed a published headline number outside noise.

---


### 64. [MemToC: Benchmarking Memory-Tool Conflict Resolution in Large Language Models](https://arxiv.org/abs/2608.26295)

**<font color=#1a73e8>作者：</font>** Arseniy Varlamov, Rishat Zinnatullin, Elisei Rykov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLMs must arbitrate between two fallible sources when a tool return conflicts with their parametric memory, yet existing evaluations measure source preference without establishing source correctness. We introduce MemToC, a controlled benchmark for post-tool-return arbitration with executable tools. MemToC comprises 6,504 evaluation episodes constructed from 542 quality-controlled factual questions, independently elicited model-specific closed-book answers, and controlled tool returns of known correctness. These components instantiate four source-correctness cases; tool-error and no-tool conditions are separate controls. Across five open-weight 7-9B models, tool returns strongly dominate elicited closed-book answers. The four instruction-tuned models retain a verified-correct answer against an incorrect tool in only 6.5-17.1% of eligible cases, follow a correct tool in 86.0-93.1%, and repeat the tool return in 78.4-86.0% of cases where both sources are wrong. No cross-model ordering remains stable across three instruction-wording variants with the question and episode content held fixed. We compare prompting with SFT and DPO using chain-level cross-fitting over ToolHop, so questions sharing an underlying fact never straddle training and evaluation. We apply an asymmetric success criterion: correct-answer retention must improve without a detected reduction in correct-tool following. SFT and DPO meet this criterion on the same two of four instruction-tuned backbones. Improvements rarely come cleanly: 19 of 20 tested method-model combinations reduce abstention after tool errors or on unanswerable inputs. Transfer beyond MemToC is positive but partial and depends on the model and presentation frame. Correctness-conditioned arbitration can be improved through fine-tuning, but gains must be evaluated jointly with correct tool use, abstention, and robustness to formulation.

---


### 65. [Approved Too Late: Verdict Staleness in LLM-Guarded Self-Adaptive Systems](https://arxiv.org/abs/2608.26306)

**<font color=#1a73e8>作者：</font>** Ilai Shraga, Roei Eshel, Lior Gorelik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A large language model (LLM) guardrail for a self-adaptive system (SAS) may issue an approval that is correct at check time but stale by actuation. This creates an Execute-stage time-of-check to time-of-use (TOCTOU) hazard. We study verdict freshness: whether a guardrail verdict remains valid when used. We distinguish three quantities that answer different questions: all-candidate verdict change under fixed-action replay, oracle-labeled approval expiry on recorded closed-loop trajectories, and judge-conditioned use-time invalidity. Across five reproducible SAS environments, all-candidate verdict-change rates span 5.3-48.4% at a common replay shift of eight simulator steps. We introduce the Freshness-Bounded Shield (FBS), which estimates each approval's validity horizon from its safe-side margin and recent feature volatility, without an explicit plant-dynamics model. Using fixed settings documented in the artifact, FBS reduces oracle-labeled approval-expiry rates from 3.4-24.7% to 0-1.8% at the same shift. A separate audit of four LLM judges finds nonzero judge-conditioned use-time invalidity in every approval stream. We formulate a freshness contract: every approval must be correct at check time and remain valid at use time.

---


### 66. [FaithSieve: Fine-Grained Evaluation of Math Proofs with Faithful Formal Evidence](https://arxiv.org/abs/2608.26310)

**<font color=#1a73e8>作者：</font>** Ziyu Wang, Qiming Dai, Yishan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can now generate complex, multi-step mathematical proofs, but reliably determining their correctness and localizing early logical errors remains a critical challenge. Existing evaluation approaches largely depend on model-based natural-language judgments, which often overlook local reasoning gaps. While formal theorem provers like Lean offer a path to rigorous verification, using them to evaluate informal text requires solving locality and semantic mismatches: a prover might bypass a local flaw by proving an overly broad target, or validate an auto-formalized statement that drifts from the original mathematical intent. To address this, we introduce FaithSieve, a Lean-assisted framework for fine-grained evaluation of natural-language mathematical proofs. FaithSieve decomposes coarse proof steps into local reasoning units, extracts typed proof obligations, and verifies them through a formal evaluation agent. Formal validation is gated by semantic alignment scoring, so Lean evidence is incorporated only when the formal statement faithfully preserves the context, objects, and logical form of the original claim. We construct two expert-verified datasets, ProofLoc-Olympiad and ProofLoc-University, to benchmark first-error localization. On the 350-problem Olympiad dataset, FaithSieve using a GPT-5.4 backbone achieves 81.43% exact first-error accuracy, outperforming the direct-judging baseline of 72.29%. Furthermore, on the 200-problem ProofLoc-University benchmark spanning six advanced domains, FaithSieve reaches 84.5% exact accuracy, compared to 75.0% for the direct judge. Our work demonstrates that decomposing proofs into fine-grained units and grounding them with faithful formal evidence significantly improves reliable evaluation of natural-language reasoning.

---


### 67. [Modality Maturity Index: A benchmark for assessing multimodal capabilities of omni models](https://arxiv.org/abs/2608.26317)

**<font color=#1a73e8>作者：</font>** Rohit Patel, Dieuwke Hupkes, Sloan Strader  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frontier language models are increasingly marketed as omni systems that can perceive and respond across modalities. Existing evaluation frameworks, however, focus almost exclusively on bimodal understanding, typically text plus one other modality. We propose the Modality Maturity Index (MMI), a benchmark designed to evaluate the multimodal capabilities of large language models across five modalities (text, image, audio, video and document) and combinations of up to three modalities in both inputs and outputs. MMI consists of 893 questions, each carefully crafted to require the model to demonstrate its understanding of multiple input modalities and to generate responses that incorporate various output formats. The questions are designed to be self-contained, with clear expectations for the correct modality or mix of modalities required for an accurate response. Every MMI prompt carries human-authored rubric criteria for each output modality expected in the response; a model's MMI Value expresses the average of the per-modality scores for each prompt. Because low scores can reflect either failure to generate a modality (lack of presence) or failure to generate correct content, we introduce also a supplementary Modality Presence Score (MPS), a per-prompt F1 over the expected output modalities. Applying MMI to five frontier multimodal models, we find that the MPS ranges from only 15.6 (Claude Opus 4.6) to 34.9 (GPT-5.4). Given the low availability of returned modalities to even grade, we report MPS as our main result pending model improvements. To assess the viability of judging output correctness with LLM judges and rubrics, we run a separate experiment with custom generation tools. On the assets that generates, we find that an LLM judge applying the rubrics agrees with rubric-blind human annotators (who score the outputs directly and never see the criteria) on 70.8% of judgments.

---


### 68. [When Is Noise Response Universal? Tokenization as the Hidden Variable in Language Models](https://arxiv.org/abs/2608.26319)

**<font color=#1a73e8>作者：</font>** Yefan Tao, Gerald Friedland, Luyang Kong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance of textual neural models often degrades when their inputs are corrupted by noise such as typos, OCR errors, or dropped words. We study the degradation rate across neural models, both sentence embeddings and decoder-only LLMs, and find that how consistent it is depends on the scale of the noise: under word-level noise, models with very different architectures decline along nearly the same curve, while under character-level noise they separate. We further identify the determining factor to be the training objective, not the architecture: eight encoders spanning six pretraining paradigms are scattered initially, and collapse onto a common curve after a short contrastive training recipe. We trace the word/character split to tokenization: a single character edit forces the tokenizer to re-segment the surrounding word, disturbing the token sequence far more than dropping a whole word does. This finding and its underlying mechanism provide a practical means to predict a model's robustness to noise without any noisy evaluation, and to install robustness at a chosen noise scale through noise-augmented training.

---


### 69. [Privacy Without Regret: Differentially Private Inference-Time Alignment](https://arxiv.org/abs/2608.26324)

**<font color=#1a73e8>作者：</font>** Ishi Jain, Nandini Bhattad, Sayak Ray Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best-of-N (BoN) sampling is the simplest and most widely deployed inference-time alignment strategy, but it suffers from two distinct problems: reward hacking, in which the selected response exploits errors in the proxy reward model, and the absence of any privacy protection for the sensitive human preference data used to train that reward model. We show that a single intervention-adding calibrated noise to reward scores before selection-resolves both. Our first result, Private Best-of-N (PrivBoN), establishes that Gumbel noise at an appropriate scale simultaneously provides $\epsilon$-differential privacy and implements KL-regularized alignment. Whenever the privacy budget exceeds a critical threshold $\epsilon^*$, the privacy-mandated noise is the regret-optimal regularization, and privacy imposes zero additional alignment cost-matching the information-theoretic skyline of Huang et al. (2025). Because $\epsilon^*$ depends on an unknown coverage coefficient, we introduce Private Inference-Time Pessimism (PrivITP), which combines $\chi^2$-regularized rejection sampling with a two-phase Gaussian mechanism. PrivITP achieves ex-post $(\epsilon,\delta)$-DP with a privacy cost independent of the number of responses $n$, cleanly decouples the regularization parameter from the privacy parameter, and attains the skyline up to a noise-inflation term. Experiments across several language models, datasets, and reward models confirm our results: PrivBoN and PrivITP are scaling-monotonic (unlike BoN, which degrades past a critical $n$), and PrivITP matches or outperforms PrivBoN at equivalent privacy levels, with the largest gains in the strong-privacy regime.

---


### 70. [How Unlikely Is "Unlikely"? Assessing Verbal Probability Perception Across Large Language Models](https://arxiv.org/abs/2608.26327)

**<font color=#1a73e8>作者：</font>** Christos Petridis, Konstantinos Pelechrinis, Zoran Obradovic  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly produce and interpret verbal probability expressions, yet whether these expressions carry consistent meaning across models (or match human perceptions of uncertainty) remains unknown. We present a systematic cross-model evaluation using a word-to-number mapping task grounded in established human benchmarks. Eleven uncertainty expressions were presented to 19 models under two conditions, forced single-number response and explanation elicitation, alongside a novel bidirectional roundtrip test of internal consistency. LLMs track the human benchmark with surprising fidelity: word ordering is preserved, three anchor points are recovered, and ``possible'' shows the highest variance and cross-model disagreement of any expression tested, consistent with its documented bimodal interpretation in humans. However, models show a systematic upward bias for negative expressions such as ``unlikely'' and ``improbable.'' Explanation elicitation reduces within-model variance while increasing between-model divergence, stabilizing individual models at the cost of inter-model consensus, and the roundtrip experiment reveals clear stratification, with frontier models maintaining coherent bidirectional representations. LLMs thus reproduce the structure of human verbal probability cognition, including its biases, while diverging systematically at the negative end---with implications for any setting where humans and models exchange probabilistic language.

---


### 71. [Neuro-symbolic PRM: Enhancing Scientific Reasoning via Structured Traces and Symbolic Verification](https://arxiv.org/abs/2608.26329)

**<font color=#1a73e8>作者：</font>** Yuxin Zi, Cong Xu, Suparna Bhattacharya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While tool-augmented Large Language Models have significantly improved multi-step reasoning in quantitative STEM tasks, a critical residual failure mode remains: intermediate reasoning steps that are syntactically well-formed, mathematically executable, and unit-consistent, yet contextually ungrounded. Current approaches either rely on formal verifiers that cannot assess semantic intent, or burden Process Reward Models (PRMs) with the dual task of checking both arithmetic and logic. In this paper, we propose a neuro-symbolic framework that cleanly decouples reasoning into two formal dimensions: Symbolic Validity ($V$) and Semantic Groundedness ($G$). We guarantee $V$ by construction using a deterministic symbolic verifier acting as a hard filter. To assess $G$, we train a PRM conditionally on the verifier-accepted manifold. To train this PRM efficiently, we introduce Counterfactual Symbolic Perturbation (CSP), a novel data synthesis strategy that algorithmically generates constraint-preserving hard negatives (steps that perfectly pass the verifier but are logically flawed). At inference, we deploy a verifier-first constrained search that guarantees execution consistency for verifier-covered operations while relying on the PRM solely to rank semantic grounding. By targeting the exact residual error class of strong tool-using LLMs, our method significantly improves reasoning reliability without the sprawling heuristics of prior frameworks.

---


### 72. [Beyond Capability Benchmarks: Learning Operational Fingerprints of LLM Cloud Services from Production Incident Metadata](https://arxiv.org/abs/2608.26332)

**<font color=#1a73e8>作者：</font>** Meiwei Zhang, Eduardo Miranda, Bruce Baynes 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Managed LLM services are now part of real production systems, but model selection and service planning still rely heavily on capability benchmarks that reveal little about operational behavior after deployment. We present Operational Embedding (OpEmbed), a framework for learning compact operational fingerprints of LLM cloud services from structured, privacy-preserving support-case metadata, without using case text. OpEmbed aggregates model--time windows into an eight-channel operational signature and learns a low-dimensional representation via temporal contrastive learning, cross-view reconstruction, and generational-ordinality regularization. Evaluated on more than 33,000 production support cases spanning seven LLM families over 26 months at Google Cloud, OpEmbed recovers interpretable family- and version-level structure, improves leave-one-model-out operational forecasting over non-learned baselines, remains useful under limited early-window data, and supports cross-model fault-type transfer. We report the practical lessons learned from building and evaluating this tool for model onboarding, support readiness assessment, and operational monitoring.

---


### 73. [Finding the Right Evidence: Factor-Guided Coarse-to-Fine Reasoning for Long Videos](https://arxiv.org/abs/2608.26355)

**<font color=#1a73e8>作者：</font>** Baixuan Xu, Yinyui Xu, Tianshi Zheng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While LVLMs rapidly improve, long-video question answering still remains challenging: relevant evidence is sparse, and question-relevant context often fails to provide cues that discriminate the correct answer from plausible alternatives. Diagnostic analysis on a manually annotated subset of MMR-V shows that prior agentic systems substantially improve cue retrieval over direct VLM inference yet fail to achieve a corresponding gain in answer accuracy, indicating that the bottleneck lies in option-discriminative evidence rather than topical relevance alone. We propose PACE (Progressive Acquisition of Critical Evidence), a factor-guided framework for long-video evidence acquisition. PACE proceeds in two stages: it first indexes clip-level descriptions guided by question-derived factors without observing the candidate answers; it then uses the candidate answers to derive contrastive cues and queries the index for verification. On MMR-V with the open-source Qwen3-VL backbone, PACE achieves 42.6% accuracy, outperforming direct inference and prior agentic baselines including Deep Video Discovery (DVD). On the same diagnostic subset, PACE recovers 66.9% of the annotated cues, providing empirical evidence that its gains are associated with improved evidence recovery rather than stronger answer-side priors alone. Consistent gains over DVD on LVBench, Video-MME, EgoSchema, and LongVideoBench suggest that option-aware evidence acquisition transfers beyond MMR-V. Code is available at this https URL.

---


### 74. [Cross-lingual Representation Learning via Centroid Intervention Fusion](https://arxiv.org/abs/2608.26357)

**<font color=#1a73e8>作者：</font>** Wei Sun, Marie-Francine Moens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit uneven multilingual performance, especially when dealing with low-resource languages. Inference-time intervention offers a lightweight way to improve cross-lingual transfer by modifying the hidden states produced by the LLMs during the forward pass, without updating model parameters. However, existing cross-lingual intervention methods typically learn separate projections from source to target languages, which limits scalability and prevents knowledge sharing across languages. We propose Centroid Intervention Fusion (CIF), a projection fusion framework that consolidates multiple multilingual intervention projections into a single language-shared operator. Across multilingual commonsense reasoning, natural language inference, factual editing, and machine translation benchmarks, CIF outperforms the strongest prior pairwise intervention baseline by up to +3.378 pp on average across four model backbones, while supporting performance gains for low resource languages. The code is available at this https URL.

---


### 75. [Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives](https://arxiv.org/abs/2608.26372)

**<font color=#1a73e8>作者：</font>** Zheyuan Liu, Weiliang Zhao, Xiangchi Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as autonomous agents serving users on behalf of companies, placing them in settings where user and deployer interests can conflict. When an agent knows that a user is owed something its deployer would prefer to deny, does it remain honest? Answering this is difficult because false statements can reflect either ignorance or hallucination rather than deception. To address this challenge, we introduce KnownLieBench , a knowledge-verified benchmark that first confirms through a neutral probe that an agent knows a user's entitlement, and then evaluates whether it makes false claims once an incentive to deny that entitlement is introduced. Specifically, KnownLieBench covers eight customer-service domains and 112 grounded cases, conducts multi-round dialogues with a trust-tracking customer agent, and separates deception emerging from incentive alone from deception produced under explicit instruction. Across eighteen proprietary and open-weight models, emergent deception varies substantially across model families and domains. We further use the benchmark for post-training, finding that honesty-directed fine-tuning reduces deception under incentive, while deception-graded fine-tuning increases lie success on honest-control dialogues without increasing lie frequency under incentive. By verifying entitlement knowledge before scoring deceptive behavior, KnownLieBench reduces the confound between lying and not knowing and enables more rigorous auditing and steering of agent honesty.

---


### 76. [Survival-Guided Length Control for Efficient Diffusion Language Models](https://arxiv.org/abs/2608.26374)

**<font color=#1a73e8>作者：</font>** Ivan Kobyzev, Abbas Ghaddar, Yufei Cui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) generate text by iteratively denoising masked sequences, but standard decoding either fixes the sequence length or relies on ad hoc stopping rules, often leading to unnecessary denoising steps. We recast length selection as a discrete-time survival problem over the end-of-sequence token and propose a plug-in, training-free length predictor that can be added to any existing DLM. Across reasoning and code-generation benchmarks, survival-guided length decoding speeds up inference by up to 7 times while preserving task accuracy. We further find that predicted lengths vary widely even within the same dataset, making model performance sensitive to the chosen length.

---


### 77. [VIPER: An Expert-Curated Benchmark for Vision-Language Models in Veterinary Pathology](https://arxiv.org/abs/2608.26382)

**<font color=#1a73e8>作者：</font>** Luca L. Weishaupt, Simone de Brot, Javier Asin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology vision-language models are advancing rapidly, yet existing benchmarks remain focused on human tissue, particularly oncology, leaving non-human pathology largely unaddressed. This gap is especially important in toxicologic pathology, where microscopic tissue examination of laboratory animals is a core component of preclinical drug safety assessment. To address it, we introduce VIPER, the first expert-curated benchmark for vision-language model evaluation in toxicologic pathology. VIPER contains 1,251 questions associated with 419 H&E-stained rat histology images across seven organ systems, covering multiple-choice, KPrim, and free-text formats. All questions were curated and validated by board-certified veterinary pathologists. In total, we benchmarked 16 models, including two newly introduced veterinary-pathology models, seven human pathology-specialized models, and seven general-purpose frontier models. The results identify a substantial domain gap between veterinary and human pathology, expose the risk of over-diagnosis of normal tissue in frontier models, and show that domain-specific training remains critical for visually grounded predictions. VIPER data and evaluation code are available at this https URL.

---


### 78. [Why RAGs Hallucinate: Penalty-Aware Evaluation of Retrieval-Augmented Generation Systems with Knowledge-Gap Canaries](https://arxiv.org/abs/2608.26385)

**<font color=#1a73e8>作者：</font>** Alden Do Rosario, Hussein Younes, Felipe Pires  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Volume-based accuracy rewards retrieval-augmented generation (RAG) systems for guessing: a system that answers everything outscores one that declines when its knowledge base cannot support an answer. Building on the confidence-target analysis of Kalai et al. (2025), we present a penalty-aware evaluation framework for deployed RAG products, combining (i) asymmetric scoring (correct +1, wrong -4, abstain 0), (ii) knowledge-gap canaries, questions whose answers are verifiably absent from the knowledge base, so that any answer constitutes ungrounded generation from parametric memory, and (iii) a failure-attribution pipeline that separates retrieval, generation, and abstention-policy failures. Applying the framework to three commercial RAG systems and a no-retrieval baseline on SimpleQA-Verified (1,000 questions x 3 repeats, graded blind by a cross-family three-judge panel with 98.9% unanimity), we find that accuracy when answering is closely clustered across systems (97.0-98.0%), while canary violation rates differ roughly sixfold (16.7% vs. 98.1%). The systems are separated less by what they answer correctly than by whether they answer at all when they should not, and penalty-aware scoring reorders the volume-based ranking accordingly; the reordering is stable across penalty settings from k=1 to k=9. All code, configurations, transcripts, and judge votes are released for independent audit.

---


### 79. [Co-Evolving Structured Knowledge and Reasoning in Language Models](https://arxiv.org/abs/2608.26386)

**<font color=#1a73e8>作者：</font>** Ryan Thomas Noonan, Linxi Zhao, Menghan Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented methods improve factual accuracy by grounding language models in external knowledge, but retrieving over unstructured text often introduces irrelevant context and offers limited control over the retrieved information. Structured knowledge bases offer a more controllable alternative, yet they are expensive to construct and often brittle to reason over. To address these limitations, we propose KBevo: a co-evolving framework that jointly learns to construct a structured knowledge base and reason over it for knowledge-intensive question answering. By optimizing both components end-to-end with QA outcome rewards, our method enables reasoning success to directly improve the quality of the constructed knowledge base. This leads to larger, better-connected knowledge structures with higher answer reachability, while also improving compositional factual reasoning and controllability compared to standard retrieval baselines.

---


### 80. [LowRankArena: A Standardized Evaluation Platform for SVD-Based LLM Compression](https://arxiv.org/abs/2608.26389)

**<font color=#1a73e8>作者：</font>** Zishan Shao, Lixun Zhang, Kangning Cui 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SVD-based low-rank compression has become a fast-growing direction for reducing the memory and computational cost of large language models (LLMs). However, meaningful comparison across existing studies remains difficult as prior evaluations use varied benchmarks, inconsistent ratios, and diverse setups, often failing to isolate low-rank effects from auxiliary techniques. As a result, it remains unclear whether reported gains reflect method-level improvements or differences in evaluation protocol. This lack of comparability highlights the need for a unified, reproducible evaluation platform. To address this problem, we present LowRankArena, a standardized evaluation platform for SVD-based LLM compression. LowRankArena unifies task versions, uniform-precision compression budgets, comparison regimes, and inference measurements, and provides a reproducible pipeline with over 3 TiB released compressed checkpoints. Using LowRankArena, our aligned audit of five representative SVD methods reveals that prior findings are highly conditional under standardized protocols: clear leaders and performance tiers shift across backbones and keep ratios, multiple-choice accuracy can hide large perplexity degradation, and nominal low-rank savings yield workload-dependent and often limited end-to-end speedups. Our code is available at: this https URL.

---


### 81. [SILK: Closing the Time-of-Check-to-Time-of-Use Gap in RoT-Protected AI Systems](https://arxiv.org/abs/2608.26402)

**<font color=#1a73e8>作者：</font>** Ruichen Qi, Xinting Jiang, Ema Dimitrova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Root-of-trust (RoT) authentication verifies a DNN model at load time, but weights may subsequently traverse DRAM, DMA, interconnect, and prefetch paths before reaching the compute engine. Post-verification tampering along this path can therefore alter the weights actually consumed while leaving the authenticated model image unchanged, creating a time-of-check-to-time-of-use (TOCTOU) integrity gap.
We present SILK (Streaming Inline Lightweight Keying), an in-place integrity mechanism that verifies the weight stream at the final pre-compute boundary. SILK repurposes quantized-weight LSBs as secret-keyed integrity bits and chains dependencies across weight bytes, so a local modification perturbs multiple integrity checks. A lightweight streaming checker recomputes these checks without separate authentication tags and uses commit gating to prevent unverified weights from reaching computation. Under a secure pseudorandom function (PRF), the forgery probability decreases exponentially with the number of affected checks, and measured miss rates closely track the analytical bound. SILK detects every stream-modifying instance in our functional attack suite. For INT8, it limits quality loss to at most 0.76 pp across evaluated CNNs and 0.17 perplexity across eight LLMs, while INT4 and MXFP4 provide a configurable security-quality tradeoff through check sparsity. On a Xilinx ZCU102, the synthesized reference pipelined implementation sustains 756 MB/s at only 1.00% of the equivalent area cost of a Caliptra 2.x RoT, while a configuration with a conservative per-attempt forgery bound of 2^-128 still sustains 678 MB/s at 6.15% of the RoT cost.

---


### 82. [The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection](https://arxiv.org/abs/2608.26423)

**<font color=#1a73e8>作者：</font>** Jaturong Kongmanee, Smile Thanapattheerakul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a framework for constructing a classifier as a safeguard layer, and for developing a complementary diagnostic that identifies which of the classifier's confident decisions can be trusted. This framework, the Latent Diagnostic Taxonomy, consists of (i) constructing a dimensionality-optimized classifier, in which the embedding dimensionality is empirically selected via cross-validated performance rather than fixed a priori, (ii) locating a relatively small set of latent support vectors (~ 29% of total training examples) representing influential prompts for identifying tokens that alter the classifier's predicted labels, and (iii) utilizing such tokens and their associated attack magnitudes for constructing a diagnostic taxonomy. This diagnostic taxonomy provides an end-to-end guideline for flagging prompts that require different treatments: rely Safely on the classifier's decision; flag Heuristic Bias and Heuristic Override cases; route Insufficient Context cases for further human/safety review. Applying the framework to a classifier trained on a public prompt injection dataset, we find that a substantial fraction of its confident decisions (~ 77%) are not robust to removing a single token, and that this brittleness separates into two distinct failure patterns: a confidence calibration failure and a genuinely exploitable shortcut. For each zone of the taxonomy, we also recommend strategies for remediating diagnosed prompts. We illustrate the framework as a series of steps, demonstrating how each step operates.

---


### 83. [Don't Overthink, Don't Underthink: Toward Adaptive Reasoning in Agentic AI](https://arxiv.org/abs/2608.26442)

**<font color=#1a73e8>作者：</font>** Md Jueal Mia, M. Hadi Amini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have shown that increased inference-time reasoning can improve performance on complex tasks. However, many existing approaches rely on fixed or preallocated reasoning controls, such as fixed token budgets, pre-execution difficulty estimates, or activation-space interventions, and are often evaluated on standalone reasoning benchmarks rather than full agentic workflows. These assumptions may not hold in agentic AI systems, where reasoning requirements evolve dynamically through planning, tool use, memory retrieval, and agent-to-agent interactions. Consequently, reasoning can become either excessive or insufficient, resulting in unnecessary computation, increased latency, planning drift, excessive tool use, or incomplete solutions. We argue that a major challenge for next-generation agentic AI is not merely how much reasoning a language model should perform, but how it should allocate reasoning according to evolving task demands. We characterize over-reasoning and under-reasoning as recurring failure modes of misallocated reasoning and evaluate them on MATH-500 and the GAIA public validation benchmark. Using tool-decision latency, token consumption, token-limit exhaustion, and answer correctness, our results suggest that cases classified as over-reasoning are associated with higher computational cost without proportional accuracy gains, whereas cases classified as under-reasoning are consistently associated with incorrect or incomplete solutions. These findings motivate future research on adaptive reasoning mechanisms for agentic AI.

---


### 84. [Vowel Signs Are Not Letters: A Pre-tokenization Ceiling on Multilingual Tokenizer Fertility](https://arxiv.org/abs/2608.26449)

**<font color=#1a73e8>作者：</font>** Sajal Regmi, Siddhartha Pudasaini, Chetan Phakami Pun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Byte-level BPE tokenizers that use the HuggingFace ByteLevel pre-tokenizer inherit GPT-2's word regex, where a word is defined as \p{L}+, one or more Unicode letters. In abugida scripts, vowels are written as combining marks; this pattern therefore splits each word at every vowel sign. Since BPE merges only within a pre-token, those splits persist through training regardless of vocabulary size or corpus composition. We formalise this effect as a training-free lower bound on fertility. Across 26 languages from a parallel corpus, every one of the 17 abugidas is affected, ranging from 1.47x (Tibetan) to 9.02x (Thai), whereas Latin, Cyrillic, Hangul, and Han show exactly 1.00x. For 5 languages, matched tokenizer pairs that differ only in this character class fall within 2.2% of the predicted floor, scoring 4.78 versus 1.58 tokens per word on Nepali. When the Nepali share of the training corpus is swept from 5% to 95%, the broken tokenizer barely shifts at all (1.7%) while the fixed one shifts 33.9%, which separates a structural ceiling from a data shortage without needing to inspect any code. We train three 268M models that differ only in their tokenizer; the fixed variant achieves 4.43% lower held-out Nepali bits per byte at equal compute, and it still leads when given the same bytes with 1.59x the compute. A census of 3,479 HuggingFace repositories finds the letters-only word class present in 63.3% of the most-downloaded text-generation models, accounting for 72.5% of their downloads. GPT-4o's o200k pattern already uses a mark-aware word class, making the repair itself prior art. We quantify its value, show how to recognise its absence from symptoms alone, map which scripts it reaches, measure how widely it is deployed, and release a 65,536-entry Nepali-English tokenizer with a harness that regenerates every number here from public data on a laptop.

---


### 85. [Diff Mining: Logit Differences Reveal Finetuning Objectives](https://arxiv.org/abs/2608.26462)

**<font color=#1a73e8>作者：</font>** Greg Kocher, Robert West, Clément Dumas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finetuning has become the gold standard for refining existing behaviors and inducing new ones in language models, yet it often remains unclear exactly which behaviors emerge during this process. As models grow ever more capable, understanding finetuning better becomes increasingly important, particularly since unwanted behaviors may arise during finetuning. In this paper, we introduce Diff Mining, a simple yet effective framework for identifying what a finetuned model has learned by comparing its logits to those of its base model. Diff Mining effectively surfaces salient tokens that are amplified in the finetuned model, serving as a fingerprint of its training -- even on text unrelated to the finetuning domain. Unlike many existing model diffing methods which require model internals, Diff Mining only needs access to output logits and scales to large models. The framework consists of two modular stages: (i) extracting per-context logit differences between the finetuned and base models on a reference corpus, and (ii) aggregating the resulting signals to construct an interpretable token set representing the finetune. For aggregation, we explore both a simple Top-K frequency method and a Non-negative Matrix Factorization (NMF)-based approach for disentangling multiple finetuning objectives into distinct token clusters. Empirically, Diff Mining succeeds across diverse settings: on finetune domain detection, it significantly outperforms state-of-the-art model diffing methods both in identifying relevant tokens and in downstream performance when an interpretability agent is given access to the extracted token set; on models with injected biases, it identifies more than one third of the biases without targeted probing. Overall, our framework shows promise in developing auditing tools to detect finetuning objectives.

---


### 86. [Zero-Shot Self-Orchestration with Ledger-Based Control for Improved LLM Coding Performance](https://arxiv.org/abs/2608.26480)

**<font color=#1a73e8>作者：</font>** Victor Gao, Vida Khosrowshahi, Ali Khosrowshahi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model systems are widely reported to beat single-model baselines, but the evidence is mixed, and comparisons are usually confounded: pipelines change token budgets, tool calls, and prompts simultaneously, so an aggregate gain rarely reveals what actually helped. We investigate the effect of introducing the manager-worker scaffold over a shared filesystem workspace, with no training and no per-benchmark tuning, measured against the same model answering in a single pass. Across nine models -- five open-weight, spanning 9B to ~2.8T parameters, and four frontier closed models -- on the 100 latest hard LiveCodeBench problems, the scaffold's benefit is real but conditional: large and statistically significant for some (Qwen3.8-27B +23.4, GPT-5.6-Luna +10.6 and GPT-5.6-Terra +8.0, each over five paired passes; Kimi-K3 +30.4 and Minimax-M3 +11.0 over five paired passes with reasoning off, both at $p < 10^{-4}$, and +42 and +12 in a single pass at a 128k cap) and null or negative for others (Qwen3.6-35B -1 to -9 with reasoning off). With the manager, Opus-5 achieves the highest score in the study at 91% in one pass. Running a manager roughly triples the token bill, but it buys accuracy more cheaply than moving to a larger model does: GPT-5.6-Terra with a manager nearly matches Fable 5's single-call accuracy (85.0 against 87.4, $p = 0.59$) at a fifth of the price (\$11.71 against \$61.11 per 100-problem pass, $p < 10^{-4}$), and the Qwen-27B arm does it for \$51.75 on weights anyone can self-host. Our transcript analysis finds several mechanisms behind the gains, of which two recur: context management, in which short worker calls and shared notes organize state and reduce truncation, and problem decomposition. Improvements are modest for large models with reasoning enabled, but larger for some models with reasoning disabled and for smaller models with reasoning enabled.

---


### 87. [Video-FLAIR: Not Whether to Reason, But How](https://arxiv.org/abs/2608.26495)

**<font color=#1a73e8>作者：</font>** Yogesh Kulkarni, Pooyan Fazli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal queries can require different types of reasoning. Some can be answered via perceptual reasoning, extracting information directly from the visual signal, while others require compositional reasoning that combines observations or deliberative reasoning that evaluates competing hypotheses. However, many existing methods apply a uniform reasoning strategy across queries, leading to unnecessary computation on simple tasks and insufficient reasoning on complex ones. We introduce Video-FLAIR, a training framework that learns to select the appropriate reasoning mode for each query using reinforcement learning. During training, the model generates responses under all three modes for the same prompt, enabling direct comparison. A composite reward compares these responses to favor the most effective one based on correctness, grounding, and cost, while discouraging unsupported or misaligned deliberation. This yields a supervision signal for learning adaptive reasoning without per-query annotations. Video-FLAIR improves accuracy over the Qwen2.5-VL base model by +5.4 on MathVista, +4.8 on Video-Holmes, and +4.8 on Video-MMMU, while reducing average token usage to 95 compared to 417 for always-thinking baselines.

---


### 88. [Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update](https://arxiv.org/abs/2608.26511)

**<font color=#1a73e8>作者：</font>** Huanhuan Ma, Henry Peng Zou, Chengze Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often exhibit sycophancy, revising their answers to align with users when users push back. Such answer flips, however, can arise from different causes. One possibility is that the model simply aligns with the user's feedback in order to satisfy them. Another is that the feedback genuinely contains useful evidence, prompting the model to update its answer in a rational way. We distinguish them as Unsupported-Yielding and Rational-Updating. Prior work focuses primarily on suppressing Unsupported-Yielding, while overlooking its effect on Rational-Updating. We address this gap with a two-turn evaluation framework that measures the two behaviors separately. Across representative training-time and inference-time interventions, we find that anti-sycophancy methods often encounter a trade-off in which reducing Unsupported-Yielding can sacrifice Rational-Updating, and vice versa, even when the two objectives are optimized jointly. Mechanistic analysis suggests that the two behaviors share an internal substrate: the MLP neurons and attention heads driving them overlap substantially, and their associated steering directions are positively aligned. We further conduct a preliminary orthogonalized steering exploration, which yields modest, backbone-dependent selectivity gains. Overall, our results suggest that anti-sycophancy should be treated not as a simple suppression problem, but as a selectivity problem, where effective interventions should preserve Rational-Updating while reducing Unsupported-Yielding.

---


### 89. [Multi-Expert Conformal Risk Control for Pairwise LLM Judging in Open-Ended Dialogue](https://arxiv.org/abs/2608.26529)

**<font color=#1a73e8>作者：</font>** Ming Cheng, Yusheng Dai, Qiuhong Ke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we explore multi-expert Conformal Risk Control (CRC) algorithms for pairwise LLM-as-a-Judge evaluation in open-ended dialogue. Our core insight is that multi-expert aggregation offers a complementary remedy to CRC: whereas CRC controls risk at the decision threshold through abstention, aggregation sanitizes the scoring function at its source. Guided by this, we first design two multi-expert CRC methods: Score Averaging and Decision Voting, which aggregate at the score and decision levels, respectively. While both strategies outperform single-expert methods on homogeneous expert panels, on heterogeneous LLM judges they remain risk-valid but recover only limited coverage, because a uniform threshold cannot match the experts' distinct scoring scales. To resolve this issue, we further propose Marginal-Calibrated Conformal Consensus (MC3): it captures distinct per-expert scales via initial threshold ratios, while jointly tuning a unified decision function $C_t(x)$ applied identically in both calibration and test, thereby preserving exchangeability. To evaluate our framework, we construct Panel, a 1,800-pair human pairwise-preference benchmark for open-ended dialogue. It is built on responses generated by four open-weight LLMs over dialogue contexts from three domains (ESConv, MSC, DREAM), with full logit access. In experiments, we find that both Score Averaging and Decision Voting substantially improve accuracy and acceptance rate on homogeneous panels. Notably, MC3 extends these gains to heterogeneous panels by accommodating distinct per-expert scoring scales across all three datasets.

---


### 90. [Chart2SVG: Editable SVG Generation from Raster Chart Images](https://arxiv.org/abs/2608.26544)

**<font color=#1a73e8>作者：</font>** Jinning Cui, Lu Chen, Haoyan Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Chart2SVG, a multimodal large language model that converts static raster charts into structurally organized, semantically enriched SVGs that support programmatic editing. By incorporating chart-specific semantic tokens into a vision-language model, Chart2SVG captures both geometric primitives and their functional roles. To support robust structural recovery, we introduce Beagle+, a dataset of 33K canonicalized and structurally distilled chart samples. Our approach combines specialized training objectives with a rendering-aware post-training phase, producing SVGs that are both visually accurate and structurally consistent. To facilitate higher-level manipulations, we construct a Chart Structure Graph (CSG) that exposes visual dependencies, enabling tasks such as interactive exploration, chart repurposing, and layout reuse. Experiments show that Chart2SVG substantially outperforms baselines in reconstruction fidelity and downstream editing utility, advancing the development of intelligent and interactive visualization tools.

---


### 91. [DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows](https://arxiv.org/abs/2608.26546)

**<font color=#1a73e8>作者：</font>** Zechun Niu, Yukun Zhao, Jiaxin Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are increasingly adopted to complete complex, multi-tool workflows in real-world settings. However, existing benchmarks typically separate tasks by application or capability and evaluate agents in environments that are cleaner and more stable than those encountered in practice. We introduce DuMateBench, a real-session benchmark reconstructed from anonymized and privacy-screened user sessions collected from a large-scale production agent platform. Each task preserves the relevant pre-solution interaction history, persistent configurations, and workspace state, and is then validated through human verification. The resulting benchmark comprises 200 tasks spanning 8 broad scenarios and 17 fine-grained capability categories, with most tasks requiring multiple capability coordination. We execute these tasks in isolated Docker containers injected with three forms of real-world environmental complexity: Insufficient, Unstable, and Noisy, and assess performance using a hybrid deterministic and LLM-as-Judge evaluation protocol. Experiments across five representative autonomous-agent frameworks paired with four state-of-the-art LLMs reveal substantial gaps in strict task completion. Complementary robustness, efficiency, and diagnostic analyses further show that performance under environmental perturbations is jointly shaped by the capabilities of the LLM and the surrounding agent framework. The code and data are publicly available at this https URL.

---


### 92. [SPT: Skills as Pre-Training Data for Agentic Language Models](https://arxiv.org/abs/2608.26563)

**<font color=#1a73e8>作者：</font>** Yufei Sun, Yudong Li, Yiming Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic (tool-using) language models are mainly trained on tool-call traces and agent trajectories during post-training. These data provide direct behavioral supervision, but producing them requires task environments, execution, and verification, making broad tool and task coverage expensive. Publicly available skills offer another source of training data: they encode reusable tool semantics and workflows but are typically used only as inference-time context. We introduce Skill Pre-Training (SPT), a mid-training method that applies causal language modeling to SkillCorpus, a collection of public multi-file skill packages, optionally mixed with general data. To preserve relations among files within each package, we also introduce Reference Insert, a reference-aware assembly strategy that places supporting files near their mentions in the primary instruction. Experiments across multiple model scales and post-training recipes show that SPT consistently improves agentic performance over mid-training on general or trajectory data, while largely preserving general performance. Data mixture experiments show additional benefits from combining skill data with general annealing corpora. These results indicate that skill packages are a valuable data source for pre-training agentic language models.

---


### 93. [Dependency-Aware Revocable Decoding for Efficient Diffusion Large Language Model Inference](https://arxiv.org/abs/2608.26574)

**<font color=#1a73e8>作者：</font>** Wooje Park, Insu Lee, Minyoung Noh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer a promising alternative to autoregressive generation by decoding multiple tokens in parallel through iterative denoising. However, increasing decoding parallelism often degrades generation quality, as early errors can contaminate later contexts. Revocable decoding mitigates this issue by re-evaluating decoded tokens and remasking unreliable ones, but existing methods overlook that unreliable tokens may also corrupt the verification context itself. We identify this failure mode and propose Dependency-Aware Revocable Decoding (DARD), a training-free framework that separates tokens into masked, candidate, and unmasked states. DARD verifies candidate tokens using a selective context that excludes less reliable tokens and adaptively regulates their influence on subsequent decoding. Experiments across 12 textual and multimodal benchmarks on 3 open-source dLLMs show that DARD consistently improves the speed-quality Pareto frontier over recent revocable decoding methods, achieving a 2.71$\times$ speedup and a 4.35-point CIDEr score gain over Saber on Flickr30K.

---


### 94. [Visual Information-Guided Parallel Decoding for Diffusion Multimodal Large Language Models](https://arxiv.org/abs/2608.26580)

**<font color=#1a73e8>作者：</font>** Insu Lee, Wooje Park, Wonseok Shin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion multimodal large language models (dMLLMs) have recently emerged as a new decoding paradigm for multimodal generation. Starting from a fully masked sequence, dMLLMs progressively decode the sequence by unmasking a subset of the remaining masked positions at each step. Since the selected tokens serve as the prediction context for subsequent steps, deciding which tokens to decode is crucial to the quality of the final output. The most common strategy prioritizes tokens based on a certainty measure that tends to favor tokens frequently observed in the training data. Recent approaches instead order tokens according to their influence on subsequent predictions, but do not explicitly account for the input image. We propose the Visual Information-Guided Sampler (VIG-Sampler), which prioritizes tokens based on their attention to image tokens. We further impose a constraint that penalizes candidate tokens whose image-attention distributions are similar to those of previously selected tokens, thereby increasing the information gain of the decoded subset. Extensive experiments on 7 captioning and VQA benchmarks with 3 open-source dMLLMs demonstrate the effectiveness of VIG-Sampler, which outperforms the Info-Gain Sampler by an average of 19.3 CIDEr points across the captioning benchmarks and surpasses it on COCO Caption while using only half as many decoding steps.

---


### 95. [Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs](https://arxiv.org/abs/2608.26581)

**<font color=#1a73e8>作者：</font>** Tanzila Rahman, Mehran Taghian Jazi, Yunke Peng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization offers a promising avenue for reducing the computational and memory demands of Multimodal Large Language Models (MLLMs). Recent hardware support for low-precision formats, ranging from MXFP8 to ultra-low-bit formats such as MXFP4 and HiF4, has accelerated research into efficient MLLM training and deployment. In this work, we present a systematic study of these quantization schemes in representative MLLMs that span both video generation and reasoning tasks. Our analysis shows that MXFP8 achieves near-lossless performance, whereas aggressive 4-bit quantization leads to significant degradation. Through extensive ablations, we identify activation quantization as the primary source of this performance loss, contributing substantially more than weight quantization. Motivated by this observation, we propose Residual Fallback Quantization (RFQ), a lightweight activation reconstruction framework that supplements the primary ulta-low-bit activation representation with an auxiliary quantized residual pathway. By explicitly modeling and compensating for quantization errors, RFQ improves activation fidelity while preserving the efficiency advantages of ultra-low-bit computation. RFQ requires no architectural modifications and incurs negligible computational overhead. Extensive experiments on Wan2.2 and Qwen3-VL demonstrate that RFQ consistently recovers a substantial portion of the performance lost under the quantization of MXFP4 and HiF4, significantly narrowing the gap to BF16 baselines across both generation and 4 reasoning benchmarks. Our findings establish activation quantization as the dominant bottleneck in ultra-low-bit MLLMs and highlight residual-based activation reconstruction as an effective and practical strategy for robust 4-bit deployment.

---


### 96. [J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data](https://arxiv.org/abs/2608.26582)

**<font color=#1a73e8>作者：</font>** Gyouk Chu, Myeongho Jeon, Eunho Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving language models have recently emerged as a promising path toward superintelligence, with the advantage of reducing the cost of human supervision. While considerable progress has been made in verifiable domains, self-evolution in unverifiable domains remains substantially less explored. We propose Judge co-adaptation from Zero data (J-Zero), a unified Challenger--Solver--Judge co-evolution framework that supports self-improvement across both domains. The Challenger and Solver co-evolve through an adversarial interaction: the Challenger generates increasingly difficult tasks, while the Solver learns to produce higher-quality responses to them. In parallel, the Judge co-adapts using preference pairs whose ordering is known in advance from how each response was produced, i.e., the Solver's answer over the Challenger's, and its decomposed-and-recombined answer over its one-shot answer, rather than from the Judge's own scores. J-Zero outperforms the baselines by an average of 4.2 points on verifiable and 8.0 points on unverifiable domains, and continues to improve through at least ten iterations, whereas the baselines degrade after two.

---


### 97. [Surgical Alignment in Knowledge Graph Training for Clinical Diagnosis with Large Language Models](https://arxiv.org/abs/2608.26587)

**<font color=#1a73e8>作者：</font>** Saksham Khatwani, He Cheng, Majid Afshar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs (KGs) offer structured medical knowledge that can ground large language model (LLM) reasoning in clinical diagnosis application, yet how KG signal should be integrated into LLMs remains an open question. We present a systematic study spanning five KG task formulations, three training paradigms, two KGs, and three base LLMs. At the task level, all paradigms improve over the non-finetuned baseline, but methods with comparable in-domain accuracy show substantially different knowledge transfer behavior. We introduce Gradient Intervention Density (GID) and Gradient Distortion (GD) to measure how broadly an optimizer modifies the pretrained model. GID and GD together reveal a clear divide: KG-judgment training under KL regularization produces sparse, localized updates (a regime we term as surgical alignment), while task-specific SFT produces dense ones. A controlled ablation shows that the objective and KL contribute to sparsity independently, and the paradigms that produce sparse updates also improve reasoning quality, even when their in-domain accuracy is lower than task-specific SFT. Assessing KG-LLM integration thus requires complementing accuracy with optimization-geometry diagnostics. Our implementation can be found at this https URL.

---


### 98. [Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation](https://arxiv.org/abs/2608.26588)

**<font color=#1a73e8>作者：</font>** Guang Yang, Xing Hu, Xiang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) generate register-transfer-level (RTL) code with rapidly improving functional correctness. Security of LLM-generated code, however, has been studied mainly for software, where flaws can still be patched after deployment. Insecure RTL offers no such remedy once taped out into silicon. We construct SECRTL-GEN, a multi-language resource-access security benchmark grounded in real SoC IP: 392 tasks over five CWE families and four HDLs (Verilog, SystemVerilog, VHDL, and Python), each with black-box functional and security testbenches. Functional specifications intentionally omit security obligations, matching how obligations are often kept out of functional docs in practice. An empirical study of five frontier LLMs shows a sharp gap: under vanilla prompts they pass functional tests in about 73-79% of cases but security tests in only 14-35%, and stronger functional models are not safer. Adding CWE knowledge raises security, while unaided self-thinking helps less and both security-oriented prompts cut functional pass rates, showing that the bottleneck is missing weakness awareness in the specification, not an inability to write defensive RTL. We present RTL-Obliger, a neuro-symbolic framework that infers these implicit obligations. An LLM extracts a functional-semantic graph from the specification; a symbolic engine then matches it against a CWE pattern ontology to surface mitigation-evidence gaps and signal-level obligations; the LLM finally revises RTL under those obligations in a functionality-preserving two-stage generation. Across five models and four languages, RTL-Obliger raises mean all-pass from 49.6-51.4% (SecV/RESCUE) to 61.6%, with higher security and functional rates than these secure-generation baselines.

---


### 99. [Benchmarking Clinical Decision Pathway Adherence in Large Language Models](https://arxiv.org/abs/2608.26592)

**<font color=#1a73e8>作者：</font>** Nuo Chen, Xinyang Jiang, Zilong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Following clinical decision pathways (CDPs) defined by clinical practice guidelines is essential for safe and reliable medical decision-making. However, existing medical large language model (LLM) benchmarks mainly evaluate final-answer accuracy, providing limited evaluation of models' ability to adhere to guidelines. To address this gap, we introduce MEGA-CDP, a benchmark for evaluating whether medical LLMs can generate guideline-adherent CDPs using provided guidelines as references. MEGA-CDP is constructed from 2,274 English and Chinese clinical practice guidelines through a guideline-to-case pipeline, yielding 42,353 clinical cases with explicit reference CDPs. It supports both single-turn vignette and multi-turn interactive settings, and introduces a CDP-oriented evaluation framework for measuring pathway consistency. Experiments on 16 representative LLMs show that reliable clinical decision support remains challenging for current models, demonstrating the need for CDP-oriented evaluation and the value of MEGA-CDP for advancing guideline adherence in medical LLMs.

---


### 100. [Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper](https://arxiv.org/abs/2608.26596)

**<font color=#1a73e8>作者：</font>** Rongjin Li, Yuanxin Liu, Hao Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly capable scientific assistants, yet they remain far from fully autonomous research. This transition requires models to actively inspect academic papers, build global evidence views, and make traceable judgments without prespecified issues or evidence. However, existing work provides limited task paradigms or training studies for such issue- and evidence-absent verification. We study this challenge through scientific error detection, where models must determine whether errors exist and justify them with evidence-based reasoning. To fill this gap, we present VERA-RL, a reinforcement-learning formulation for scientific error detection over academic papers. Following a Reason--Verify--Scan progression, we construct VERA-13K, a 12,900-sample dataset organized into 4,300 matched chains, covering 6 scientific-error categories across the research workflow and broad natural-science domains. We further introduce fine-grained rewards for reasoning completeness, evidence alignment, and error precision. Training Qwen3-VL-8B with VERA-RL substantially improves verifiable reasoning, approaching flagship MLLMs such as Gemini 3 Pro and Qwen3-VL-235B-A22B on Scan.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
