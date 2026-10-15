# 🧠 大模型相关研究 | 2026年10月16日

> 本类共 **313** 篇论文：已确认 **304** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-313](./part-07.md)

---

### 251. [MAEM: Mitigating Recency Bias via a Replay-Free, Capacity-Controlled Dynamic Mixture of Experts for Class-Incremental Graph Learning](https://arxiv.org/abs/2610.20238)

**<font color=#1a73e8>作者：</font>** Junlin Chen, Wenhao Wang, Junchao Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) excel on graph-structured data but suffer catastrophic forgetting when classes arrive sequentially. In class-incremental graph learning, predictions are often dominated by recently learned classes, causing severe recency bias. Dynamic expansion can isolate knowledge across sessions, but many methods assume task-incremental settings and require task identities at test time to select branches or heads---information unavailable in class-incremental learning. Learnable routers offer an alternative, yet continual fine-tuning the router on new data can bias routing toward recent components. We propose MAEM, a replay-free, capacity-controlled dynamic mixture-of-experts framework for class-incremental graph learning. MAEM builds representations with Simplified Graph Convolution (SGC) and trains a dedicated expert for each new session, then freezes it to protect prior knowledge. For routing without task IDs or a shared trainable router, each expert uses a masked autoencoder (MAE); test nodes are assigned to the expert with the lowest reconstruction error, reducing routing-level recency bias. When the expert pool reaches a fixed capacity, MAEM merges the least-used experts via Git Re-Basin alignment and further distills them into a fused expert using topology-aware pseudo data synthesized from MAE distributions (DeepInversion-style), without storing or revisiting historical graph data. On four class-incremental graph benchmarks, MAEM mitigates recency bias, outperforms strong continual graph learning baselines, and keeps model capacity bounded under strict replay-free learning.

---


### 252. [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245)

**<font color=#1a73e8>作者：</font>** Mohsen Iranmanesh, Sina Moradi Sabet, Sina Marefat 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as autonomous agents for automated program repair, patching software vulnerabilities through multi-step reasoning and tool use. Yet these systems typically validate a patch against the same evidence used to construct it -- a static alert, sanitizer trace, published exploit, or test suite. A patch that blocks that one piece of evidence can therefore look successful while remaining vulnerable to the same vulnerability with some variation. We present P2Patch, a generative adversarial repair system that treats each patch as a new attack target. Starting from a normalized vulnerability finding, an exploitation agent constructs a reproducing proof of vulnerability (PoV), a patching agent repairs the program, and the exploitation agent then attacks the patched program for a distinct same-vulnerability exploit. Every successful exploit becomes a permanent repair requirement, and the final patch must block all PoVs accumulated during the patching process, with construction-time PoVs kept strictly separate from held-out evaluation oracles. Across 101 C/C++ and Java CVE subjects, this adversarial loop surfaces a distinct confirmed exploit in 41% of runs after the patch has already blocked its original construction-time PoV. Against single-pass repair from the same finding using Claude Code, P2Patch raises held-out fix-closed coverage from 78.1% to 84.7% and beyond-upstream coverage from 42.1% to 62.5%. Under the same held-out oracles, it also certifies more attack paths as blocked than recent state-of-the-art agentic repair systems on overlapping subjects. These results show that adversarial testing and independent security oracles expose repair gaps that one-shot validation misses.

---


### 253. [Scaling Multilingual Mixture-of-Experts: How Language Coverage Changes Capacity and Compute Allocation](https://arxiv.org/abs/2610.20247)

**<font color=#1a73e8>作者：</font>** Joel Dag, Nikit Srivastava, Hamada M. Zahera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual models share capacity across languages, so adding languages can hurt performance on existing ones. Mixture-of-experts models expand this capacity with little additional per-token computation. Given this extra capacity, does adding experts reduce what each additional language costs? To answer this question, we propose a repetition-aware joint scaling law relating number of active parameters, training tokens per language, number of experts, and language coverage. Fitted on 26,300 per-language loss observations from 64 pretrained configurations, our law reduces prediction error on held-out configurations by 28% relative to the strongest evaluated baseline. At matched number of active parameters and training tokens per language, 32 experts reduce the loss penalty of expanding from 12 to 200 languages by 83% compared with a dense model. Our law further shows that broader language coverage favors more experts across a wider range of compute budgets, guiding capacity allocation as multilingual models scale.

---


### 254. [Repairing Speech Access After Text Updates with Frozen Affine Fields](https://arxiv.org/abs/2610.20253)

**<font color=#1a73e8>作者：</font>** Ming-Hao Hsu, Yuxiang Wang, Yingda Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-capable language models inherit most of their knowledge from text-rich language backbones, and continued model maintenance is likewise dominated by text updates. Knowledge acquired through a text update can nevertheless remain difficult to access when the same query is spoken. We formulate this mismatch as post-update speech access repair, where the knowledge-bearing checkpoint stays frozen and a detachable operator repairs speech-only access in one model pass. We introduce Affine Fields for Interface Repair across Modalities (AFFIRM), which first learns and freezes a base correction for speech hidden states, then adds query-specific corrections with zero mean over the operator-training queries. Paired speech and text states provide the coordinates that condition these corrections on each query. On balanced synthetic-speech PopQA, paired comparisons do not establish a clear advantage for AFFIRM over global SALSA steering or low-rank ReFT interventions under the same frozen single-state constraint. On recorded SLUE-SQA-5 questions with text passages, a full-scale PopQA-fitted AFFIRM operator transfers without refitting and improves ROUGE-L by 0.0941 over its paired No Repair baseline. Low-rank ReFT interventions also transfer positively, whereas the matched SALSA variant falls 0.0707 below its paired baseline. These results show that text acquisition and speech access can diverge after an update and should be verified and repaired separately.

---


### 255. [Harness Policy Distillation: Aligning Agent Policies with Runtime Semantics](https://arxiv.org/abs/2610.20261)

**<font color=#1a73e8>作者：</font>** Junze Zhu, Weihao Chen, Zhiyang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying a general-purpose model as an agent means running it inside a product-specific runtime harness that decides which actions are executable, how state advances, and when the loop may terminate. Ordinary trajectory supervision shows which action was taken but leaves the runtime semantics behind that action implicit. We introduce Harness Policy Distillation (HPD), which makes these runtime control semantics an explicit training target alongside actions to align the harness policy. HPD replays reference trajectories through the harness to recover the runtime semantics that are implicit in ordinary trajectory data, and represents them as control documents at each model-call boundary. These documents provide privileged information for a teacher to generate actions, while harness verification ensures that the resulting targets are executable under the runtime contract. We jointly train a shared model on the runtime semantics recovered from control-state privileged information and native history, thereby internalizing these semantics into the model policy. At deployment, the trained model uses the original harness interface without requiring the control document or any additional supplement. On TRAJECT-Bench with the Pi harness, Qwen3-8B trained with HPD reaches 22.98% autonomous task success and 49.23% runtime compliance, against 3.09% and 19.90% for the unadapted model. Harness-verified teacher actions substantially improve the native deployment policy, while joint control-state supervision provides further gains in task completion and runtime compliance. HPD turns executable runtime semantics into dense supervision for learning harness-compatible actions at each decision boundary.

---


### 256. [Anuvani-LID: Robust and Calibrated Spoken Language Identification for Indian Languages](https://arxiv.org/abs/2610.20263)

**<font color=#1a73e8>作者：</font>** Stephen Fernandes, Narayan Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every multilingual speech pipeline begins with a language decision, an error there propagates silently through recognition, translation and routing. In India it spans 22 scheduled languages across four language families, heard over short, noisy, narrowband and code-mixed audio. Foundational speech models increasingly present language identification (LID) as an inherent latent, generalized capability. Autoregressive decoders in speech models emit a special language ID token, and modern LLMs with audio capabilities can name the language when prompted. We test this assumption on identical clips and find that whisper and similar speech models has tokens for only 15 of the 23 languages, on one second inputs Gemini 3.5 Flash reaches 0.52 macro-F1 and GPT-audio 0.14. We present Anuvani LID, a dedicated 115M parameter LID conformer model trained on 54,643 hours of Indian speech spanning 22 Indian languages and Indian accented English. Along with designed and controlled studies on 102 condition benchmark with speaker and corpus held out tests. Across 37 conditions, it reaches 0.914 mean macro-F1, 5.2 points above Gemini 3.5 Flash and ahead of 14 other systems. It is 24 points ahead of Gemini at one second, scores 0.897 on all 23 languages where no other system exceeds 0.713, and is calibrated to an ECE of 0.008. Reliable Indian LID still requires a robust, dedicated and calibrated model.

---


### 257. [CSWBench: Evaluating Context-Sensitive Code-Switching in Creative Writing](https://arxiv.org/abs/2610.20272)

**<font color=#1a73e8>作者：</font>** Zewen Jiang, Yahan Li, Chenlu Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated multilingual capabilities across diverse language generation and understanding tasks. Yet effective code-switching requires more than multilingual proficiency: models must decide when, where, and why to switch languages in ways that fit the surrounding context. This context-sensitive ability remains insufficiently evaluated. We introduce CSWBench, a benchmark for evaluating context-sensitive code-switching in creative writing through two complementary settings: Focused Narrative and Extended Narrative. We further propose CSWEval, a theory-informed framework with two complementary levels: event-level evaluation of Licensing, Contextual Appropriateness, and Functional Gain, and whole-text evaluation of task-specific quality---overall literary and narrative quality in Focused Narrative and quality emphasizing multilingual organization in Extended Narrative. Evaluating twelve LLMs, we find that models exhibit meaningful but uneven code-switching competence across narrative contexts. Model differences are particularly pronounced in multilingual literary integration, while multilingual-focused dimensions show stronger difficulty effects overall than the general narrative dimensions; narratively salient switches are associated with stronger contextual and functional realization; and event-level CS quality is moderately associated with whole-text performance.

---


### 258. [Towards Efficient Threat Intelligence Instruction Tuning via Quality-Aware and Optimal Transport-Guided Data Selection](https://arxiv.org/abs/2610.20284)

**<font color=#1a73e8>作者：</font>** Jiyu Tian, Mingchu Li, Xiangwei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> High-quality data is essential for improving instruction tuning in threat intelligence analysis. However, existing methods for generating cybersecurity instruction data lack reliable quality assessment mechanisms, and gradient influence-based data selection methods primarily focus on single-sample matching, failing to cover diverse and complex security capabilities. To address these issues, we propose CTI-TDS, a Targeted Data Selection method for instruction tuning in Cyber Threat Intelligence analysis. Specifically, we first filter high-quality CTI instructions by integrating instruction style consistency and security knowledge verification. Furthermore, we formulate gradient influence as a distribution alignment problem, learning a gradient subspace of target tasks and applying entropic regularized optimal transport to optimize distribution matching between training samples and target tasks, enabling diversity-aware data selection. We conduct extensive experiments on CTIBench across multiple large language models. Experimental results demonstrate that when fine-tuning with only a small set of high-value instruction data, CTI-TDS outperforms existing data selection methods and achieves competitive performance on threat intelligence analysis tasks.

---


### 259. [From Plato to Aristotle: Toward a General Theory of Representation Hypotheses](https://arxiv.org/abs/2610.20286)

**<font color=#1a73e8>作者：</font>** Dai Shi, Andi Han, Xiaoyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis (PRH) holds that increasingly capable models converge toward a common representation. However, recent studies have shown different views on aligning representations via their neighborhoods, spanning trees, and distances. We show that these views can differ because the alignment criteria behind them sit at different points of one lattice, and we formalize this explanation as the Lattice Representation Hypothesis (LRH). Under the LRH, the convergence claimed by the PRH is agreement at the top of the lattice, whereas its evidence comes from neighbor overlap, a criterion near the bottom. The Aristotelian Representation Hypothesis (ARH) restricts convergence to local neighborhoods because calibration keeps the growth of neighbor overlap with model size but largely removes that of centered kernel alignment. We show that this removal can come from calibrating a maximum over layers, so global convergence remains open. Back into Plato's Cave (BPC) infers coarse shared structure from the collapse of neighbor overlap on larger evaluation sets, whereas we trace it at least partly to a fixed number of neighbors covering shorter distances. We show that the spanning-tree overlap used by Structure over Geometry (SOG) mostly repeats one-nearest-neighbor overlap. The LRH also extends to independently trained models, whose training procedure and objective decide the criteria met reliably across runs. We prove this claim for the training procedure in a linear autoencoder and for the objective in a finite contrastive Gibbs model. Experiments on dozens of pretrained vision and language models and thousands of runs of both theoretical models support these conclusions. We hope this work paves the way toward a general theory of representation hypotheses, with a framework to analyze them and compare their evidence. Project page: this https URL

---


### 260. [Taking the PULSE of Medical Reasoning: Step-Level Retrieval Timing for Knowledge-Grounded Inference](https://arxiv.org/abs/2610.20292)

**<font color=#1a73e8>作者：</font>** Danyang Zhao, Sendong Zhao, Yanrui Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable medical reasoning requires LLMs to dynamically access external biomedical evidence to improve factual trustworthiness and reasoning accuracy. However, indiscriminate retrieval can introduce noise and latency, raising a critical retrieval-timing problem: at each reasoning step, the system must decide whether the model's internal knowledge is reliable or external evidence is needed. We propose PUlSE, a lightweight probing method that uses the model's internal representations as intrinsic signals for step-level retrieval control. Our posterior trajectory analysis reveals that erroneous steps exhibit substantially higher inter-layer volatility than correct ones, suggesting unstable internal knowledge. Based on this finding, PUlSE trains a compact probe on inter-layer geometric features to detect factual errors upon step completion, and uses it as an adaptive trigger for retrieval and step regeneration. Across four medical benchmarks, PUlSE-timed retrieval matches exhaustive per-step retrieval in accuracy while reducing retrieval calls by 72%, and can transfer to an unseen legal domain, indicating potential domain-agnostic generality. Overall, our study provides an initial step toward shifting retrieval-trigger design from surface-level confidence estimates to internal activation dynamics for adaptive access.

---


### 261. [CASI: Credit Assignment via Set Intervention for Agentic Retrieval](https://arxiv.org/abs/2610.20293)

**<font color=#1a73e8>作者：</font>** Xinyi Cheng, Tianfu Zhang, Jiwen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly generate multiple retrieval actions jointly, while downstream systems often provide only one reward for the resulting set. Broadcasting this reward provides a valid score-function gradient estimator for the expected set-level objective, but does not determine a coalition-dependent within-set attribution. We introduce CASI (Credit Assignment via Set Intervention for Agentic Retrieval), which constructs the missing counterfactual information through snapshot-grounded set intervention: generate and retrieve once, hold replayable snapshot components fixed, and evaluate alternative subsets under common conditions. Shapley aggregation converts these marginals into within-set credit, which bounded zero-sum advantage shaping incorporates into policy optimization. For m >= 4, singleton, leave-one-out, and full-set endpoints do not generally determine the Shapley allocation; under additive set values, extra coalition evaluations are redundant. In a five-action sponsored-search setting, exhaustive auction replay over 1,200 requests reveals substantial coalition dependence. Under the training-time evaluator, CASI achieves the highest median cosine similarity to a replay-defined Shapley reference among evaluated credit rules; under a sensitivity backend, CASI does not outperform Singleton. Across five independent training runs, CASI-trained policies achieve higher held-out auction-replay set value than Singleton- or Broadcast-trained policies. In a randomized seven-day production A/B test on 10% of traffic, the CASI-trained policy yields an observed 3.51% lift in the primary advertiser-value metric over production control.

---


### 262. [SpectrumQuant: Spectrum Alignment for LLM Quantization](https://arxiv.org/abs/2610.20303)

**<font color=#1a73e8>作者：</font>** Dwaipayan Haldar, Indranil Patra, Azhar Yousuf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Orthogonal transforms have emerged as an effective tool for low-bit quantization of large language models (LLMs), as they reshape activation distributions without changing the underlying model function. Existing approaches typically rely either on fixed data-agnostic transforms, such as Hadamard rotations, or on calibration-time optimization of learned rotations. We study rotation selection from first principles and show that maximizing covariance leads to spectral alignment and provides a principled criterion for constructing quantization-friendly orthogonal transforms. Based on this insight, we propose SpectrumQuant, a closed-form rotation method that estimates activation covariance from calibration data and uses it to construct a covariance-aware orthogonal transform for post-training quantization. Our formulation characterizes quantization-friendly rotations as compositions of alignment and mixing components, while recovering Hadamard matrices as a special case. Interestingly, a class of butterfly matrices belongs to this category. In the realm of LLM quantization, SpectrumQuant bridges the gap between data-agnostic structured rotations and learned rotations, providing an effective and efficient data-aware alternative for post-training quantization. Experiments on Llama and Mistral models show that SpectrumQuant is competitive with state-of-the-art rotation strategies while requiring less than one-third of the GPU memory and significantly less time than learned rotations approaches like SpinQuant and DartQuant.

---


### 263. [Reflect After Failure: Brain-Inspired Self-Evolving Agents for Embodied Spatial Intelligence](https://arxiv.org/abs/2610.20312)

**<font color=#1a73e8>作者：</font>** Xin Li, Xiaohuan Gu, Yifan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have made substantial progress in spatial reasoning, and self-evolving agents further extend these capabilities to embodied environments by learning from interactions. However, current self-evolution remains particularly challenging in embodied spatial tasks, complex and multi-step decisions from partial visual evidence making it difficult to determine why an execution fails. The failure may stem from misperception, insufficient exploration, or incorrect planning, yet execution feedback alone rarely reveals which component is responsible. As a result, simply accumulating interaction experience can reinforce ineffective strategies. To address this, we propose HiMeco, a brain-inspired self-evolving agent for embodied spatial intelligence, inspired by metacognitive monitoring and hippocampal memory consolidation. Through Hippocampal-Metacognitive Reflection, HiMeco diagnoses failures in perception-exploration-planning (PEP), then compares execution attempts to derive reusable strategies and guidance for avoiding recurring errors. It also abstracts interaction programs into parameterized skills, using evidence contracts and execution-based validation to determine their retention and reuse. These strategies and skills guide subsequent interactions, with memory updated only between rounds and model parameters kept frozen. HiMeco achieves state-of-the-art performance on ESI-Bench, and it also improves accuracy on EmbSpatial-Bench by 3.94 percentage points without evolution.

---


### 264. [Argument Graph Uncertainty: Quantifying Uncertainty from the Logical Structure of Reasoning Chains](https://arxiv.org/abs/2610.20328)

**<font color=#1a73e8>作者：</font>** Simon Baur, Sumire Honda, Wojciech Samek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is essential for deploying large language models in high-stakes reasoning tasks, yet most existing approaches rely on expensive sampling strategies or shallow token-level signals that ignore the internal logical structure of model outputs. We introduce Argument Graph Uncertainty, a post-hoc framework for multiple choice question tasks, that estimates model confidence directly from the logical structure of a single chain-of-thought reasoning trace. Our method uses either a lightweight instruction-tuned model or a simple deterministic rule to segment the reasoning chain into propositional units, then applies a NLI model to infer relational edges and construct two complementary argument graphs over these segments. The resulting edge scores are aggregated into a Dirichlet posterior over answer options, whose concentration yields calibrated uncertainty estimates reflecting both local step-to-step coherence and global logical consistency across the reasoning trace. Evaluated on GPQA, MMLU-Pro and TruthfulQA, our method consistently surpasses token-based and consistency-based uncertainty baselines across multiple reasoning models. We further demonstrate through extensive combination analyses that argument graph uncertainty captures an orthogonal signal to existing approaches, making it a complementary component in uncertainty ensembles. Crucially, our framework requires no additional calls to the evaluated model and relies entirely on small, efficient auxiliary models, producing fully interpretable, per-node uncertainty attributions at low computational cost.

---


### 265. [TreeFlex: Agents Navigating Their Own Search Trees](https://arxiv.org/abs/2610.20334)

**<font color=#1a73e8>作者：</font>** Dongzhuo Li, Fangzhou Cheng, Weiwei Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A ReAct-style agent accumulates observations, intermediate results, and failed attempts in a single context. As this context grows, stale and off-path information consumes its limited capacity and obscures relevant evidence, making focused reasoning increasingly difficult. We introduce TreeFlex, a framework in which the agent's own policy decides where to search. The agent records each intermediate state, with a short summary, as a node in a search tree maintained by the harness. The policy is a single language model that acts in two roles. In the Reflection role, it has a global view of the tree through these summaries and picks a node to resume, together with an instruction. In the Execution role, the harness restores the path that led to that node, and the model carries out the instruction with the usual task tools until it saves a new node or proposes a solution, which Reflection then approves or sends back to another node. Through these choices, the policy decides whether to deepen the current line, branch from or revisit an earlier state, verify a proposal, or stop, without a fixed traversal order or a score for each node. We train navigation, task actions, checkpointing, and proposal review jointly with a tree-aware adaptation of GRPO, using task-level outcome rewards augmented by process rewards. After small-scale RL of a 4B model, with the same active-context limit for all methods, TreeFlex reaches 48.8% accuracy on a challenging deep-research benchmark, versus 41.5% for flat ReAct and 42.8% for FoldAgent, and its Pass@8 is about ten points higher than either. On SWE-bench Verified, with all three systems trained with RL from the same 9B model, TreeFlex resolves 54.9% of tasks, versus 43.3% for FoldAgent and 45.2% for its step-wise variant.

---


### 266. [Read, Parse, Describe: Unified Document Parsing with Visual Element Description Generation](https://arxiv.org/abs/2610.20335)

**<font color=#1a73e8>作者：</font>** Yuheng Chen, Yufan Chen, Zhuojun Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document understanding systems are typically evaluated as separate components via layout analysis, optical text recognition, reading-order prediction, and image captioning. This separation leaves scientific figures, captions, and visual semantics weakly connected, and fails to measure whether a model can produce a single page-level parse that is both structurally faithful and semantically accessible. We introduce Read-Parse-Describe, a unified dataset for document parsing with visual element description generation. Given a page image, models are required to output an ordered list of layout elements containing bounding boxes, semantic labels, reading-order indices, recognized textual content, and alternative text descriptions for visual elements. The benchmark is built from 2,402 documents, comprising 18,163 continuous pages, 125,218 layout elements, and 11,338 visual instances. Besides, we further propose a plug-and-play space-awareness enhancer that reuses multi-layer visual features and injects grid-aware spatial guidance into vision-language tokens for layout-aware generation. Experiments across end-to-end VLMs and pipeline parsers show that existing systems still struggle to jointly recover reading order and visual semantics, while our enhanced model achieves strong joint performance. These results highlight the need to move beyond isolated document parsing modules toward unified models that jointly read, parse, and describe complex documents. The new dataset and code will be made publicly available at this https URL

---


### 267. [Lifted State Policy Optimization: Internalizing Self-Correction through Transition Geometry](https://arxiv.org/abs/2610.20350)

**<font color=#1a73e8>作者：</font>** Ren Zhuang, Ben Wang, Shuifa Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preference optimization ranks final answers and trajectory RL maximizes aggregate returns, yet neither credits the local change that turns a flawed reasoning state into a better one. We introduce Lifted State Policy Optimization (LSPO), which establishes this finite, cost-adjusted transition as the primary unit of learning. Each textual answer is augmented with a learned continuous coordinate, forming a lifted state that an energy function evaluates and orders. A shaped reward drives energy descent net of edit and step costs, and an internalization loss absorbs selected low-energy answers into the direct generator. On Qwen3.5-27B, the resulting single-pass policy reaches 71.8% aggregate accuracy across mathematics, science, code, and logic benchmarks, matching test-time reflection at 71.9% with 28% lower latency and 25.8% fewer tokens. The pattern holds across dense and mixture-of-experts backbones, and matched controls confirm that transition credit and the lifted coordinate each contribute, as does answer internalization. Our code is available at this https URL.

---


### 268. [ReferFlow: Beyond Final-Target Localization for Complex Referring Expressions](https://arxiv.org/abs/2610.20352)

**<font color=#1a73e8>作者：</font>** Tianyi Gao, Han Fang, Xin Wei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models have made significant progress in referring expression comprehension (REC), yet most REC benchmarks still focus on final-target localization. Complex queries often involve intermediate visual references with different dependencies on prior grounding, but final-only evaluation leaves this process unexamined. To address this gap, we formulate trajectory-level REC, in which models receive an ordered sequence of grounding steps constructed from a single complex query and localize the target regions associated with each step. We instantiate this setting in ReferFlow-Bench, which characterizes structured region transitions through four trajectory types, namely Refinement, Shift, Reset, and Mixture. Experiments show that current models struggle to consistently ground intermediate visual references across successive steps. We further propose ReferFlow, which decouples interleaved text-latent trajectory generation from coordinate decoding. Specifically, Stateful Region Latent Reasoning represents each target region as an object-indexed state composed of continuous latents, with explicit visual and spatial supervision to preserve region information for subsequent grounding. Trajectory-Aware Parallel Decoding then recovers all coordinate blocks in parallel through four geometry-constrained refinement rounds, with each block conditioned on its corresponding trajectory prefix, thereby reducing within-box sequential dependencies and eliminating cross-box autoregression. We further apply Grounding-Aware GRPO to promote consistent grounding across steps and learn adaptive trajectory generation from complex REC queries. ReferFlow achieves leading performance on general REC benchmarks and ReferFlow-Bench.

---


### 269. [Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization](https://arxiv.org/abs/2610.20353)

**<font color=#1a73e8>作者：</font>** Renjie Xie, Juncheng Yang, Aoting Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) language models activate only a few experts per token, yet all expert weights must be stored. Mixed-precision quantization reduces this storage cost by assigning higher bit-widths to sensitive experts and lower bit-widths to resilient ones, but expert rankings alone do not determine how strongly to weight their errors. To address this gap, we propose NatScale, a contrast-calibrated allocation framework for mixed-precision MoE quantization. It uses a model-specific power transformation to calibrate gradient-based expert weights to an information-theoretic contrast target while preserving rankings. We jointly evaluate each expert's gate, up and down configurations to estimate its output error. We then combine these errors and calibrated weights with an existing prior based on weight spectra, variance and precision decay to select configurations under a storage budget. Across three models, NatScale achieves the lowest native-to-quantized KL divergence and the highest top-token agreement in all nine settings against five allocation baselines. It also yields the lowest perplexity in seven settings. These findings highlight the importance of objective-aware precision allocation.

---


### 270. [From Triage to Impact: A Multi-Hop Reasoning Benchmark for Explainable Persian Hate Speech](https://arxiv.org/abs/2610.20370)

**<font color=#1a73e8>作者：</font>** Ghazal Kalhor, Sima Kamandloo, Mehrsa Shamsian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate speech has become increasingly prevalent on social media, raising concerns about its detection, interpretation, and moderation. Persian, a relatively low-resource language, lacks sufficient annotated data and computational resources for fine-grained hate speech analysis. In this study, we introduce a fine-grained, multi-hop benchmark for explainable Persian hate speech analysis, covering content triage, target identification, hate tactic and moral foundation analysis, textual evidence extraction, harmful narrative inference, and severity assessment. By evaluating state-of-the-art large language models (LLMs), we find that performance generally declines as tasks require more fine-grained semantic and inferential reasoning. Proprietary models generally outperform open-weight models, while reasoning-oriented models show no consistent advantage. Incorporating intermediate reasoning steps substantially improves severity prediction compared with one-shot assessment. Our analysis further reveals that Incitement to Violence or Harm is most strongly associated with higher severity, while political-affiliation targets are particularly associated with subversion-based moral framing. Overall, this work provides insights into LLM-based hate speech analysis and supports more accountable moderation of Persian-language social media. The benchmark is publicly available at this https URL.

---


### 271. [From Relevance to Validity: Zero-Shot Tool Selection via Functional and Contextual Validation](https://arxiv.org/abs/2610.20388)

**<font color=#1a73e8>作者：</font>** Xiaoxuan Dong, Jin Zhang, Zichen Yuan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly face tasks from unseen domains and execution contexts, making zero-shot tool selection essential for identifying tools that can satisfy task requirements. Existing dominant methods mainly rely on relevance ranking, but semantic matching alone cannot ensure that a tool is functionally compatible or remains applicable in a new context. We preliminarily identify a \emph{transfer-validity gap}, where semantically relevant tools may still fail to satisfy functional or contextual requirements after transfer. To address this gap, we propose \methodname{}, a progressive validation framework that complements semantic relevance with endpoint-grounded functional compatibility and task-conditioned contextual evidence. Across cross-domain and cross-dataset transfer, \methodname{} consistently improves capability ranking, with larger gains under functional or contextual ambiguity. Ablation results further confirm the complementary contributions of functional and contextual validation.

---


### 272. [STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agents](https://arxiv.org/abs/2610.20390)

**<font color=#1a73e8>作者：</font>** Shuo Wang, Sifan Zhou, Xiaobo Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid development of vision-language models (VLMs), Web-GUI agents have achieved promising performance in interacting with real-world interfaces through screenshot-based grounding. However, high-resolution screenshots and multi-turn histories introduce excessive visual tokens, causing substantial inference overhead. Existing token pruning methods, mainly designed for natural images, often select tokens independently based on importance scores, which can fragment the local visual structures required for recognizing small GUI elements such as buttons, icons, and hyperlinks. In this work, we propose STP-GUI (Spatially-aware Token Pruning for GUI agents), a query-guided token pruning framework that preserves fine-grained instruction-conditioned token scoring while performing spatially coherent window-level selection under aggressive token reduction. A lightweight selector is optimized through policy learning while the VLM backbone remains frozen. Experiments on Online-Mind2Web show that \papername achieves a favorable efficiency-performance tradeoff under low token budgets. At 21% token retention, it preserves 77.7% of full-token performance while reducing inference latency by 31% and FLOPs by 57%. Results on Android in the Wild further suggest that the method transfers to mobile GUI environments.

---


### 273. [FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding](https://arxiv.org/abs/2610.20392)

**<font color=#1a73e8>作者：</font>** Shuxuan Li, Jialiang Kang, Yanghao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM generation through lightweight drafting and parallel verification. It is particularly promising for long inputs, where KV-cache access costs can be amortized over multiple accepted tokens. Yet most drafters are trained on short sequences and degrade on long inputs, while long-context training is costly. Existing training-free approaches restrict the context window, rescale positions, or augment recent context with retrieved distant entries. Drafters, however, read target hidden states that already encode contextual and positional information, and their lightweight architecture makes full-history attention affordable. We propose FOLD, a training-free method that preserves exact local positions and treats all distant entries as far memory at a shared position. To counter attention dilution as the memory grows, we sharpen attention within it to emphasize relevant entries while separately controlling its total weight relative to the local window. Across six target-drafter pairs and diverse benchmarks of up to 256K tokens, FOLD predominantly delivers the highest speedup, with the best case more than doubling the speedup over autoregressive decoding, from 2.08$\times$ to 4.22$\times$.

---


### 274. [Cortex: Consolidating Context into Parametric Memory](https://arxiv.org/abs/2610.20399)

**<font color=#1a73e8>作者：</font>** Jintian Zhang, Feng He, Xinnian Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context can improve large language model performance, but these gains may be lost after context removal. Inspired by biological systems consolidation, we formulate Memory Consolidation (MC) as internalizing these gains while preserving non-target capabilities, connecting context-specified editing, skill learning, and behavioral steering under a common objective. We introduce a five-task-family testbed measuring consolidation and retention under single, batch, and sequential updates. We propose Cortex, which generates prospective queries to anticipate uses of context and distills context-conditioned outputs into mergeable low-rank or structural feed-forward network updates. Across 4B--120B dense and mixture-of-experts backbones, including both text-only and multimodal models, Cortex lies on the empirical consolidation--retention Pareto frontier in most evaluated settings. After 50 sequential factual edits on a 14B model, Cortex-Structural recovers 88.9% of the context-induced gain while retaining 99.8% of original non-target performance.

---


### 275. [Training Language Models to Fail Gracefully](https://arxiv.org/abs/2610.20401)

**<font color=#1a73e8>作者：</font>** Daman Arora, Xuecheng Liu, Himanshu Gaurav Singh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning makes language models better at solving tasks, but the same mechanism also rewards guessing. When success is the only way to earn reward, opting for a safe fallback is always worse than a long-shot attempt. When a wrong action can corrupt a database or ship broken code, that incentive can be costly. Therefore, we propose training models to fail gracefully: to preserve successful behavior whenever possible while learning to execute a safe fallback policy when acting would be unreliable. However, naively using policy gradients with intermediate reward for fallback behavior is brittle due to unfavorable optimization dynamics. We address this challenge with GracefulRL, which reshapes the optimization landscape to promote graceful failure. Importantly, this behavior emerges directly from outcome-level reward signals, without annotations specifying when to fall back or additional inference-time machinery such as a verifier. Across a range of tasks and scales, we train models that largely preserve their task-solving capability while selectively falling back when acting would be unreliable. More broadly, our results show that reinforcement learning can not only incentivize models to succeed, but also to reason about the limits of their capabilities and change course when they determine that success is out of reach.

---


### 276. [When Does Momentum Help in Reinforcement Learning with Verifiable Rewards?](https://arxiv.org/abs/2610.20413)

**<font color=#1a73e8>作者：</font>** Kaifei Wang, Zikang Shan, Liwei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Momentum is a classical tool for accelerating convex optimization and a standard component of modern large language model training. Yet recent empirical work has questioned the usefulness of first-moment momentum in reinforcement learning with verifiable rewards (RLVR). We study this question through a bandit formulation of RLVR with bias-corrected exponential moving average (EMA) momentum, where the EMA coefficient $\beta$ controls how quickly the weights on past gradients decay. When policy gradients are evaluated exactly, we prove that increasing $\beta$ within a range that prevents overshoot strictly accelerates optimization. When gradients are estimated from sampled responses, a positive expected gain can be obscured by sampling fluctuations. We show that as the learning rate $\eta$ decreases, the expected gain with fixed $\beta$ vanishes faster than these fluctuations, whereas increasing $\beta$ to keep $\eta/(1-\beta)$ within the safe regime preserves a nonvanishing gain that eventually dominates them. Bandit simulations quantitatively validate these predictions. RLVR experiments on Qwen3-4B-Base using SGD with EMA and AdamW support our principle of choosing larger coefficients in practical LLM post-training. On Qwen2.5-32B with AdamW, simply increasing $\beta_1$ improves mean validation accuracy by nearly $2$ percentage points over the conventional choice, demonstrating the principle's effectiveness at a larger model scale.

---


### 277. [From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence](https://arxiv.org/abs/2610.20417)

**<font color=#1a73e8>作者：</font>** Jiahong Qian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audits of large language model (LLM) extraction from full-length documents report severe unreliability, leaving two questions open: what the failures actually consist of, and whether confidence signals can turn unreliable output into usable output. We run a preregistered, fully frozen evaluation of two new-generation low-cost LLMs (DeepSeek-V4-Flash, GLM-5.3-Flash) with a flagship-tier control (GPT-6.1-Sol) on a public corpus of 354 incident campaigns (315 unique reports, 630 model-report evaluations), scoring extraction quality against gold, confidence calibration, and robustness to single-sentence perturbations. Three findings emerge. (1) Unreliability persists across tiers: micro precision is 0.03-0.34 and verbalized calibration error (ECE) 0.53-0.94 across both splits; the gap does not close at the flagship tier. (2) The dominant failure is not hallucination: a full mention census plus a three-tier annotation of 360 sampled candidates (two independent LLM annotators from vendors outside the evaluated set, Cohen's kappa = 0.79 on the preregistered acceptance line, fully disclosed) back-projects to 65.6% background mentions and 19.9% gold-scope gaps, with only 1.2% unsupported candidates. (3) Confidence ranks but does not verify: zero-cost self-consistency-frequency tiering passes a preregistered top-30% precision-gain bar in all six test-split model-type cells (4/6 on train), the zero-cost text-frequency x SC frequency combination wins 3, ties 2, loses 1 across cells, yet relation-level counterfactuals on all 45 targets show that a single misattribution sentence flips high-confidence judgments in 95.6-100% of cases, and even a background sentence explicitly marked as unrelated still binds a fake vulnerability in up to 26.7% of them. We conclude with a deployment boundary: confidence tiering may set review priorities, never truth.

---


### 278. [OrionMoE-v1.0: A Mixture-of-Experts Foundation Model for Tabular In-Context Learning](https://arxiv.org/abs/2610.20418)

**<font color=#1a73e8>作者：</font>** Mohamed Bouadi, Nassim Bouarour, Aditya Tanna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models enable in-context learning by predicting unseen observations from a labeled support table without task-specific parameter updates. Despite recent advances, most existing approaches rely on dense architectures that apply the same transformations across features and datasets. We introduce OrionMoE-Small, a compact tabular foundation model that combines distribution-aware representations with dataset-conditioned sparse mixture-of-experts computation. Built on a dual-axis Transformer architecture, OrionMoE-Small selectively activates experts along the feature axis, with routing decisions informed by both individual feature representations and the broader dataset context. This design enables adaptive allocation of computation across heterogeneous tabular problems while retaining a shared computational pathway across tasks. OrionMoE-Small is pretrained entirely on synthetic classification tasks generated from a structured causal prior and performs downstream prediction without gradient-based adaptation. Experiments across multiple tabular benchmarks demonstrate competitive performance against substantially larger foundation models, with particularly strong results on small-context and high-dimensional datasets. Further analysis reveals favorable relative performance under class imbalance and highlights the importance of feature composition.

---


### 279. [Analyzing performance of Retrieval Augmented Generation models for Question Answering Tasks](https://arxiv.org/abs/2610.20419)

**<font color=#1a73e8>作者：</font>** Fazle Mohammed Tasfiq, Sabab Attin, Sheikh Md. Tahmid Hossain 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) models have become almost a cornerstone of open-domain question answering tasks; in which the quality of answers generated in the process, greatly relies on the effectiveness of retrieval mechanisms. In the realm of LLM, the last two years have seen tremendous progress in RAG architectures, with many models reporting to have improved performance through various design innovations. The cultural question and answering systems of South Asia, in particular, present a specific challenge since the region is home to the vast number of languages and traditions, which are closely interrelated. Along with these deeply intertwined historical narratives increase the need for culturally grounded and context-aware interpretation. Despite major architectural advances in LLMs, claiming significant improvements, challenges remain when answering these region specific questions in native languages. In this study, we aim to extract high-performing factors to guide the development of optimized hybrid RAG systems. We further explore whether the integration of RAG changes performance differently for culturally grounded and non-cultural questions in a South Asian multilingual setup, and whether RAG produces a higher overall percentage of correct answers than contexted answering. We also examine how LLM performance changes when RAG methods are integrated into the question-answering pipeline in comparison with non-contexted and contexted answering and, evaluate whether the introduction of RAG benefits popular or non-popular culturally grounded questions more. Not only does our work evaluate the current methods but also carves a path for future designs of more accurate and efficient question-answering pipelines.

---


### 280. [From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](https://arxiv.org/abs/2610.20437)

**<font color=#1a73e8>作者：</font>** Alicia Colmenero-Fernández  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Mid-2026 reporting on autonomous AI evaluation incidents claimed that frontier large language model (LLM) agents escaped server containment through emergent coordination and cloud infrastructure attacks. This paper contextualizes those claims through forensic analysis and containerized recreation of both the Highly Persistent Internal Model (HPIM) training-case conditions and the Phase One privilege escalation targeting internal package repositories during OpenAI's ExploitGym evaluations. We recreate the configuration of the OpenAI-provided training example and reproduce the cryptographic verification bypass (CVE-2026-65616) in isolated repository servers, where misconfigured systems enabled token forgery and privilege escalation through basic HTTP requests, Python, and JavaScript. Crucially, the training-example conditions and the Phase One (and later) misconfigurations share the same exploitable patterns. Our analysis explains how Zero Trust Architecture principles neutralize this shared attack vector. Contemporary AI risks derive directly from training and deployment conditions in ambivalent learning environments lacking adequate containment measures.

---


### 281. [The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation](https://arxiv.org/abs/2610.20456)

**<font color=#1a73e8>作者：</font>** Ian Magnusson, Noah A. Smith, Pang Wei Koh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The scaling relationship of compute and performance for language models (LMs) has been extensively studied; more recently, models are being designed to scale memory use, as well. In particular, adding embeddings for n-grams scales memory separately from compute use, because each pass only processes individual embedding rows, which are much smaller than the storage used for the whole embedding table. However, existing methods train embeddings from scratch, which needs expensive GPU memory for fast reading and writing. Meanwhile, the ordinary memory of the host system is cheap and underutilized by these training methods. To scale on host memory, we introduce COUNT (Counting Offline Unlocks N-gram Transformers), which builds n-gram embeddings without adding learned parameters by storing precomputed n-gram counts on host. We use the corpus frequencies to weight together the LM's own unembeddings of the next tokens most often following the current n-gram history. At a fixed compute budget, COUNT can be added as an additional input embedding for pretraining 1B-parameter LMs to improve validation loss as much as an LM with 57% more compute. If GPU memory is limited, using COUNT to let backbone parameters fill GPU memory gives better performance than splitting memory with additional learned n-gram embeddings. Beyond efficiency, COUNT allows switching in a different table of n-gram counts from a domain-specific corpus at inference time to adapt to a new task without any training.

---


### 282. [Same Claim, Different Interpretations: How LLM Agents Resolve Ambiguity in Scientific Claims](https://arxiv.org/abs/2610.20457)

**<font color=#1a73e8>作者：</font>** Delip Rao, Ahmed Muharram, Chris Callison-Burch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Co-scientists and agentic scientific claim verifiers are increasingly used to assess claims across the sciences. Natural-language scientific claims, written for human experts, are often underspecified and so admit several defensible interpretations. Such verifiers usually pick one, often tacitly, and benchmarks score their verdicts against expert labels without recording the expert's interpretation or the verifier's in a comparable form. This leads to disagreements with expert labels that cannot be traced to the evidence or the interpretation, and to compute spent on unchecked interpretations. We introduce Claim Cards to make such interpretations explicit in the reasoning itself. A Claim Card records a verifier's interpretation as nine fields before evidence gathering, each marked stated, inferred, or default. To test whether an agent's interpretation can change its verdict, we ran a GPT-5.4 agent five times on each of 60 expert-labeled materials-science and biomedical claims with a card, without one, and with one card frozen across runs (900 runs). Over 40% of card fields were not marked stated, and a card added about a tenth to a run's GPT-5.4 tokens and time without measurably changing agreement with expert labels. The agent's own interpretations varied between runs, although within a claim this variation did not measurably track the verdict. A deliberate change to one field of the frozen card, however, making the quantifier universal or the threshold for support stricter, changed the verdict on about a third of the claims, against about one in seven expected by chance (p < 0.001 for each edit). On 24 materials-science claims run with computational tools, the stricter threshold also changed what the agent asked those tools to compute. We therefore argue that verdicts should be reported with their interpretations and that benchmarks could publish the interpretation behind each label.

---


### 283. [MolLean: A Process-Verifiable Language for Chemical Reasoning](https://arxiv.org/abs/2610.20459)

**<font color=#1a73e8>作者：</font>** Jiatong Li, Yatao Bian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chemical chain-of-thought can contain hallucinated structural and property claims. We thereby introduce MolLean, a process-verifiable language that grounds chemical reasoning in an explicit molecular state. A layered Lean-based kernel checks state transitions and assertions over molecular readouts, from primitive graph edits to compound transformations. Meanwhile, a typed witness protocol separates native structural checks from externally supplied measurements. We further introduce MolLean-MCP, a stateful tool interface that exposes these transitions, checks, and readouts during generation: the model receives feedback to decide its next action, and rejected actions leave the state unchanged. MolLean supports one-pass trace execution, whole-trace refinement, and interactive reasoning through MolLean-MCP. We evaluate these three modes with direct chain-of-thought on 8,800 matched examples across 12 tasks spanning molecular generation, editing, optimization, and reactions. With Qwen3.6-27B, whole-trace refinement outperforms direct chain-of-thought on all 12 tasks. MolLean-MCP complements whole-trace refinement with stepwise verification feedback, reaching better performance in reaction tasks. Together, these results highlight an executable foundation for chemical reasoning, in which explicit chemical commitments can be checked and revised rather than remaining solely in free-form explanations.

---


### 284. [Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR](https://arxiv.org/abs/2610.20461)

**<font color=#1a73e8>作者：</font>** Nguyen Nguyen, Yongyi Zang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Character Error Rate (CER), the standard metric for OCR and vision-language models (VLMs), charges a typo as much as a wrong name. We introduce semCER, which keeps CER's alignment and denominator and charges each grapheme edit a severity from an LLM judge, with no word segmentation. Normalized CER keeps the score of a whole transcription, where it tracks readers as well as semCER or better, and semCER breaks that score down into named edits. The charges track readers' ratings edit by edit in English, Vietnamese, and Chinese and put the edits readers rate most severe near the top of a sorted list. On pairs drawn where CER and semCER disagreed, readers side with semCER more often than with normalized CER in English and Chinese, and equally often in Vietnamese. Across 16 languages, the judge charges a wrong diacritic or tone mark almost nothing in Spanish but nearly a wrong letter's severity in Telugu. Where we can count real words, a general VLM's wrong letter forms one far above chance while a classical pipeline's stays near it. We release the 61 million judged edits, the aggregated reader ratings, and the distilled scorer at this https URL.

---


### 285. [ChronoCulture: Evaluating Cultural Awareness Across Time in Large Language Models](https://arxiv.org/abs/2610.20472)

**<font color=#1a73e8>作者：</font>** Rusali Saha, Nitya Khurana, Ruihong Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural attitudes and social norms evolve over time, yet most cultural benchmarks for large language models (LLMs) treat culture as a static attribute of a country or region. We introduce ChronoCulture, a benchmark of 10,360 temporal pairs built from longitudinal survey data across 72 countries. Each pair contains the same survey question asked in the same country in an older and a newer year, with full population response distributions as ground truth. Across six LLMs, we find that models can often predict a country's attitudes at one point in time but do not reliably capture how those attitudes change. Their predictions for different years tend to stay close together, failing to capture much of the observed change. Specifying the intended year in the prompt also offers little overall improvement in alignment with survey responses. These findings suggest that models often present a largely static picture of cultural attitudes, highlighting the need to evaluate cultural awareness across time.

---


### 286. [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474)

**<font color=#1a73e8>作者：</font>** Peidong Wang, Ying Chang, Zhiming Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the executor is called or in what it can do. We ask when a self-improving embodied system should change the weights of its executor, and propose AdaRSI, an on-demand RSI framework for embodied agents. A coding agent first improves its skills and harness, then attributes persistent failures by retrying failing sub-steps from saved states, and fine-tunes only the sub-steps that remain unreliable, with demonstrations it collects itself and experience carried over from earlier tasks. On all 50 target tasks of RoboCasa365, with GR00T N1.5 as the executor and no human demonstrations, AdaRSI improves the VLA on all three suites and raises its success on unseen composite tasks from 4.6% to 13.8%. Compared with fine-tuning every sub-step, it reaches slightly higher success while using only 28% of the GPU time and 22% of the self-collected demonstrations, and fine-tuning without a harness trains more yet gains far less.

---


### 287. [Lost in Translation: Why Lower Bias Scores Don't Mean Fairer Models](https://arxiv.org/abs/2610.20479)

**<font color=#1a73e8>作者：</font>** Harsh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bias audits of multilingual language models usually compare a model's average stereotype score in English with its average in another language and read the difference as a difference in fairness. We ask how much of that difference is noise. Auditing ten open models in eight languages, we measure how far scores move when English test items are merely reworded, test every language shift item by item, and check that the test catches shifts we inject on purpose. In all 70 model-language pairs the stereotype score falls below its English level, and for Hindi, Korean and Swahili the drop clearly exceeds what rewording English produces; most of it comes from StereoSet items. Judging every translation, we find that imperfect ones drop more, but faithful translations alone drop nearly as much. Still, a lower average does not show that a model is fairer. An item's English score predicts its translated score far less well than its reworded score (correlation 0.23, 0.27 on faithful translations, vs. 0.48), while scores stay as far from neutral, models agree on translated items, and within Hindi or Spanish a translated item's score correlates with its own rewording at 0.84 and 0.82. The average cannot distinguish lower bias from a different pattern of item-level scores. We also document three common pipeline errors that silently erase bias signal, and release our code.

---


### 288. [Decoupled Marginal Sharpening for Training-Free Inference-Time Scaling](https://arxiv.org/abs/2610.20483)

**<font color=#1a73e8>作者：</font>** Weixin Wang, Wei Deng, Anderson Schneider 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how to improve LLM reasoning at inference time without updating model weights or using external reward models. Recent reward-free power-sampling methods define the sequence-level power target $\pi_\alpha(y\mid x)\propto p_0(y\mid x)^\alpha$, where $\alpha>1$, which increases the relative probability of completions that are already likely under the base model. Existing methods use Metropolis--Hastings or Sequential Monte Carlo (SMC) to approximately sample from this target. However, two challenges arise at different levels. At the target level, full-sequence sharpening can concentrate probability on a few exact reasoning--answer trajectories, suppressing alternative paths that support the same answer. At the sampler level, finite-particle SMC can suffer from path collapse when resampling repeatedly duplicates a few high-weight prefixes. To address these challenges, we propose Decoupled Marginal Sharpening (DMS), which separately controls how strongly the model favors particular reasoning paths and how strongly it favors final answers after aggregating support across those paths. At the target level, DMS first samples from a sharpened reasoning distribution, then marginalizes the model's answer probabilities over the resulting weighted reasoning population and sharpens the induced answer marginal. Separate exponents allow mild reasoning sharpening to encourage exploration of diverse paths, followed by stronger answer-marginal sharpening to concentrate probability on answers with greater aggregate support across those paths. At the sampler level, we develop Fully Adapted Annealed SMC, which combines an annealed sequence of power targets with locally fully adapted proposals and predictive ancestor resampling. Experiments on MATH500, GPQA-Diamond, HumanEval, and AIME24/25 across three base models show that DMS achieves the highest mean pass@1 among the compared methods in all tasks.

---


### 289. [Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling](https://arxiv.org/abs/2610.20497)

**<font color=#1a73e8>作者：</font>** Wei Chen, Yubing Wu, Zhou Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) trains language models from checked task outcomes, but assigning a terminal reward to individual reasoning tokens or actions remains difficult. Group-relative methods such as Group Relative Policy Optimization (GRPO) sample several attempts per prompt, but lose their reward-based learning signal when all attempts receive the same outcome. We propose Hindsight-Privileged RLVR (HP-RLVR), a single-rollout method that turns a completed trajectory's own future into token-level update weights. The generating policy snapshot scores each eligible token under its causal history and under a hindsight context containing the realized future and verifier feedback. A normalized Jensen--Shannon divergence between the two views weights the reward relative to a historical baseline, yielding bounded token credit for both successful and failed attempts, with no reference solution or learned critic. In paired Qwen3-8B runs over a shared $100$-step schedule, HP-RLVR trains $1.21\times$, $1.46\times$, and $2.30\times$ faster than GRPO on mathematics, code generation, and ALFWorld, using one eighth the rollouts per prompt. Accuracy is comparable overall, with HP-RLVR ahead on mathematics at all three sizes and GRPO ahead on code and ALFWorld. In ALFWorld, $43.2\%$ (4B) and $49.0\%$ (8B) of GRPO's gradient-norm records are zero, versus none for HP-RLVR.

---


### 290. [ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models](https://arxiv.org/abs/2610.20503)

**<font color=#1a73e8>作者：</font>** Bohan Sun, Zunhai Su, Xialie Zhuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation by drafting multiple tokens per step, yet feature-based drafters rely on target hidden features whose contextual emphasis may not align with the needs of subsequent draft positions. Hybrid linear attention (HLA) models maintain compact recurrent states that accumulate historical associations, offering an efficient source of complementary context for speculative drafting. We introduce ReaDy, the first speculative decoding method, to the best of our knowledge, to leverage HLA recurrent states for position-specific context retrieval during drafting. ReaDy equips each draft position with a learned query to retrieve supplementary context directly from the target's committed recurrent states. A lightweight state reader integrates this context into draft representations through residual updates, while low-rank state reads and fused operators keep additional computation and I/O overhead low. Building on DSpark's parallel backbone and sequential prediction head, ReaDy employs a lightweight two-stage adaptation strategy, with reader capacity, state sources, and residual placement examined through ablation studies. Across seven benchmarks spanning mathematics, code generation, and dialogue, ReaDy achieves an average $3.16\times$ decoding speedup over autoregressive decoding with Qwen3.8-27B on a single NVIDIA B200 GPU. It outperforms DSpark on every benchmark, improving throughput by 7.97% and acceptance length by 8.50% on average. Our code is available at this https URL.

---


### 291. [Bayesian Learning to Select Fair Classifiers](https://arxiv.org/abs/2610.20514)

**<font color=#1a73e8>作者：</font>** Saatvik Kher, Hyungrok Do, Judy Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many contexts. This motivates online policies that adaptively select agents to query as examples arrive and update policies as outcomes are observed. We study the problem of selecting, in an online stream, the agent that best balances (i) predictive performance and (ii) subgroup fairness of a sensitive attribute, and that allows for delayed observations of true class labels. We formulate this as a Bayesian multi-armed bandit problem using Thompson Sampling, explicitly balancing accuracy and fairness. We conduct empirical evaluations on real-world datasets spanning problems involving tabular classifiers, large language models, and human labelers, demonstrating substantial reductions in regret relative to baselines. Our theoretical contributions include guarantees on the performance of the selected agent that incorporate both the accuracy and fairness aspects of the problem.

---


### 292. [VASPO: Self-Distillation with Privileged Value Estimation](https://arxiv.org/abs/2610.20516)

**<font color=#1a73e8>作者：</font>** Fei Wu, Zhenrong Zhang, Jianshu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation provides dense supervision for reasoning models via a privileged self-teacher. However, this supervision reflects local token preferences rather than the expected return of an unguided student continuation. Recent methods combine this signal with GRPO. They use GRPO for update directions and the teacher for signal scaling. However, we demonstrate a more effective integration within PPO. Specifically, we identify complementary positional dynamics: privileged information enhances a critic's value-prediction accuracy toward the response's end, whereas self-teacher guidance is strong initially, drops mid-generation, and rebounds finally. These insights motivate Value-Augmented Self-Distillation Policy Optimization (VASPO), wherein a self-teacher and critic evaluate identical privileged information at student-generated prefixes. The critic computes token-level PPO advantages from predicted continuation returns, while the self-teacher modulates selected positive advantages via bounded probability ratios. Across six mathematical reasoning benchmarks, VASPO improves mean accuracy over PPO by 2.59 and 1.81 percentage points on Qwen3-4B and OLMo3-7B variants, respectively, and achieves the highest mean accuracy among evaluated methods on Knights and Knaves. Our code is available at this https URL.

---


### 293. [PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios](https://arxiv.org/abs/2610.20548)

**<font color=#1a73e8>作者：</font>** Ali Zamani, Soroush Esfahanian, Erfan Shahabi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental states, and behavioral intelligence, the ability to select appropriate social actions based on these inferences to achieve social goals. Persuasion provides a natural testbed in which both aspects are simultaneously at play, yet prior benchmarks typically evaluate them in isolation using synthetic scenarios. We introduce PerSo, a benchmark that evaluates both aspects on real-world persuasion dialogues from Reddit's ChangeMyView community, using an LLM-in-the-loop pipeline to construct the evaluation tasks, validated through human annotation. Our evaluation of diverse LLMs shows that performance generally scales with model size but varies across dimensions. The strongest LLM slightly surpasses the best observed human performance on the behavioral task, while the best human participant remains ahead on the cognitive task.

---


### 294. [PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition](https://arxiv.org/abs/2610.20560)

**<font color=#1a73e8>作者：</font>** Weichen Lyu, Chong Xia, Mingyu Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> 3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leverage large language models to directly predict object coordinates, or utilize generative diffusion priors to synthesize composite images for visual alignment, both of which rely on static priors in digital spaces. However, these methods consistently struggle with complex compositions such as precise hanging, gravity-driven settling and hidden containment, as these tasks require interactive construction processes involving global planning, fine-grained alignment, and physical simulation. To address these challenges, we propose PhySGA, a Physics-Space Grounded Agentic Framework for 3D composition via agent exploration and physical simulation, enabling the universal interactive assembly of rigid, articulated, and deformable objects. Directly applying vanilla LLMs or VLMs to this task proves insufficient, as current models inherently lack grounded physical understanding and interactive construction experience. To overcome this limitation, we design a collaborative feedforward-feedback architecture: an Assembly Agent focuses on geometric and kinematic reasoning for global step planning and coarse adjustment, while a Critic Agent reasons over contact dynamics for simulator state diagnosis and fine-grained closed-loop correction. Furthermore, Action Routers map semantic planning and analysis onto executable physical primitives within the simulator, while a task-specific Self-Evolving Skill Library distills historical trial-and-error feedback into reusable experiences, boosting success rates and minimizing exploration attempts. Extensive experiments within Isaac Sim demonstrate that PhySGA significantly surpasses existing methods in relation fidelity, physical plausibility, and visual quality.

---


### 295. [Scaling Discovery Requires Forgetting](https://arxiv.org/abs/2610.20563)

**<font color=#1a73e8>作者：</font>** Shangyin Tan, Ben Zhou, Lakshya A Agrawal 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas. There are different ways to scale automated research: let one agent iterate for longer, run several agents in parallel, or further let the parallel agents communicate and build on one another's candidates. However, we find that all three strategies eventually plateau as the agents accumulate history. Each agent becomes anchored to its own past attempts, making fewer and smaller edits. Beyond this point, additional budget brings little further improvement. In this paper, we show that the key to scaling discovery further is to forget. Periodically discarding the search state, including every agent's session and the candidate history, and restarting from the best candidate found so far, unblocks the search and pushes the same budget further.
We implement forgetting in a team of agents with communication and evaluate it on four tasks spanning heuristic programming, kernel optimization and model training. The results show up to 15% improvement compared to parallel agents, and up to 39% compared to a single agent. Our results suggest that, for open-ended discovery, what an agent is allowed to remember matters as much as how much compute it is given.

---


### 296. [Recovering Reliable Supervision via Critique-Guided On-Policy Distillation](https://arxiv.org/abs/2610.20572)

**<font color=#1a73e8>作者：</font>** Kaixiang Zhao, Tianrun Yu, Shangzhe Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model on its own rollouts with token-level supervision from a teacher, assuming that the teacher can reach a correct answer from any prefix the student writes. We call this property the recoverability of the teacher and show it fails on incorrect rollouts: the teacher follows student errors, although it recognizes them. We propose CriticOPD, using error recognition to restore recoverability. The teacher critiques an incorrect rollout, allowing the student to rewrite its solution following the error. The resulting output, including the critique as privileged information, is scored by the teacher while the student uses the revision without the critique for training. On two Qwen3 students and six mathematical reasoning benchmarks, CriticOPD improves OPD, with the largest gains on competition problems.

---


### 297. [One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](https://arxiv.org/abs/2610.20576)

**<font color=#1a73e8>作者：</font>** Artin Tajdini, Manpreet Kaur, Peng Qi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently means interface randomization only broadens this dependence from a single interface to the training interface distribution, so out-of-distribution perturbations still degrade the agent. We propose Cross-Interface Policy Regularization (CIPR), a self-supervised objective that replaces action names with uninformative identifiers and presents each training sample under two interfaces in which equivalent actions are identified by construction. CIPR penalizes the KL divergence between the action distributions induced under the two interfaces, so the policy behaves consistently across them. We evaluate CIPR in both supervised and reinforcement-learning post-training, where it improves robustness. On agentic function calling, held-out interface perturbations reduce the accuracy of a post-trained agent by nearly 25%, and CIPR recovers 10.5% while leaving accuracy on the unchanged interface intact.

---


### 298. [Latent Compaction with Test-Time Training](https://arxiv.org/abs/2610.20582)

**<font color=#1a73e8>作者：</font>** Yingfa Chen, Xingyu Shen, Chaojun Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Latent Compaction**, which learns a compact document-specific cache through test-time training. We initialize cache entries using reconstruction importance, teacher attention, and key-space diversity. Training first fits attention outputs and log-normalizers to those of the full cache, with reconstruction-selected entries held fixed. It then jointly optimizes the entire cache through end-to-end distillation from the full-cache model. Model weights remain frozen throughout, and training uses only generic prompts about the document, without access to downstream questions or answers. Experiments on RULER, LongBench, and Phonebook Lookup demonstrate substantial gains over budget-matched compression baselines. On a RULER, for example, our method achieves 96.7% accuracy at 32$\times$ compression, compared with 40.0% for KVZip+. The method also transfers across model scales and families, with retrieval gains on both Qwen3 and MiniCPM5. These results show that treating the KV cache as a neural network and optimizing it with test-time training can preserve retrieval accuracy under aggressive compression. The code is released at this https URL

---


### 299. [Player-1: Learning to Play from Synthetic Experience](https://arxiv.org/abs/2610.20584)

**<font color=#1a73e8>作者：</font>** Mingyu Ouyang, Yiran Wang, Siyuan Hu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines often rely on large-scale demonstrations with limited coverage of dynamic game states, while scalable environments for interactive training remain difficult to obtain. We introduce Player-1, a post-training framework for learning game control beyond demonstrations through synthetic experience. We extend the computer-use action space with relative pointer motion, sustained inputs, and composite actions. For supervised initialization, we fine-tune computer-use models on 6,044 curated gameplay trajectories that pair recorded actions with task instructions and visual reasoning. We construct Player-1-Gym, sixteen synthetic 2D and 3D environments designed around control demands shared across games. Programmatically verifiable rewards and randomized observations and control dynamics support multi-environment reinforcement learning with PPO. The resulting Player-1-9B and Player-1-35B-A3B improve MineDojo-300 success over their SFT policies by 27.8 and 17.7 percentage points, respectively. Player-1-9B reaches 38.33% success compared with 12.63% for the strongest evaluated baseline, with further gains over SFT on ViZDoom-10 and GameWorld. Further analyses show that broader synthetic environment coverage improves transfer, while the use of composite actions that combine multiple keyboard and mouse inputs increases during RL. We demonstrate that learning from synthetic experience substantially improves game control beyond supervised initialization, with gains that generalize beyond the RL training suite.

---


### 300. [Learnable Hodge-Laplacian Driven Mixture of Experts for Steady-PDE Surrogates on Coarse Unstructured Meshes](https://arxiv.org/abs/2610.20585)

**<font color=#1a73e8>作者：</font>** Stavros Nousias, Akis Nousias, Konstantinos Gkrispanis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current approaches for steady partial differential equations surrogate models on unstructured meshes apply a single mixing mechanism to the whole solution. This paper proposes an architecture that partitions the solution among vanilla transformer experts, each focused on a different spectral scale. The partition is built from a discrete Hodge Laplacian $L_0=\star_0^{-1} d_0^{\top}\star_1 d_0$, that serves as a fitting layer measuring high-frequency content. A gating mechanism takes the mesh as input and produces the per-vertex weights that recombine the expert outputs. AirFRANS is a steady Reynolds-averaged Navier--Stokes (RANS) airfoil benchmark. We evaluate our approach in a reduced remeshed version of the benchmark with each unstructured mesh counting 9.6K faces and 4.9K vertices. We compare our approach with the Transolver on the same dataset and dataset slit. Our approach reduces relative $L_2$ error by 31\% and interior mean squared error by 47\%.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-313](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
