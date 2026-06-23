# 🧠 大模型相关研究 | 2026年06月24日

> 本类共 **328** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 201. [Training-Free Semantic Correction for Autoregressive Visual Models](https://arxiv.org/abs/2606.22550)

**<font color=#1a73e8>作者：</font>** Junhao Chen, Chanyu Zhu, Zheqi Lv 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive visual models (AVMs) based on next-scale prediction have emerged as a prominent paradigm for image and video synthesis. However, decomposing the generation process into discrete scales with varying granularities in AVM makes semantic errors difficult to identify and correct, thereby undermining the quality of the final output. Prior efforts to enhance AVM can be categorized into training-based and training-free approaches. Although training-based efforts to enhance AVM generation quality come at substantial computational cost, existing training-free methods neglect intermediate generation states, leaving semantic errors undiagnosed and allowing them to accumulate into the final output. In this paper, we focus on training-free paradigms and propose Gazer, a framework that integrates multimodal large language model feedback into the AVM sampling loop for in-generation semantic correction. Concretely, Gazer operates via two cooperating stages: the Reflective Diagnosis stage diagnoses semantic errors from intermediate states, while the Semantic Correction stage rewinds and rectifies the generation trajectory to realign with the target prompt. Experiments on compositional image and video benchmarks demonstrate that Gazer improves semantic alignment and compositional accuracy across multiple AVMs without additional training.

---


### 202. [Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do](https://arxiv.org/abs/2606.22565)

**<font color=#1a73e8>作者：</font>** Zhuoran Jin, Kejian Zhu, Hongbang Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) has become a standard method for improving reasoning capabilities in large language models (LLMs) by eliciting step-by-step thinking, but its effectiveness in multimodal tasks remains unclear. In this paper, we aim to systematically investigate the key question: What can multimodal Chain-of-Thought reasoning do, and where and why does it fall short? To this end, we evaluate 12 multimodal tasks across perception and reasoning categories using both 14 non-reasoning models and 8 reasoning models. Our analysis reveals several important findings: (1) CoT is not a free lunch and should be used selectively depending on the specific requirements of each task. For perception tasks, CoT can lead to undesirable side effects, such as reduced performance in visual grounding and object counting. In contrast, it proves effective for reasoning tasks involving mathematical, scientific, and multi-image reasoning; (2) Compared to original models, existing open-source multimodal reasoning models often yield only marginal overall improvements, possibly due to an overemphasis on mathematical reasoning at the expense of broader capabilities; (3) Visual reasoning remains a key bottleneck for current multimodal CoT, as models exhibit a Look Light, Think Heavy pattern where verbal reflection rises and falls during reasoning, whereas visual reflection consistently diminishes. These findings suggest that while multimodal CoT handles verbal reflection relatively well, it lacks the ability to maintain deep visual introspection throughout the reasoning process.

---


### 203. [SeFi-Image: A Text-to-Image Foundation Model with Semantic-First Diffusion](https://arxiv.org/abs/2606.22568)

**<font color=#1a73e8>作者：</font>** SeFi-Team  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training image generation foundation models consumes substantial resources. Previous methods have attempted to leverage semantic guidance to accelerate the training process, yet their experiments were only conducted on simple datasets such as ImageNet, at low resolutions, and with small-scale models. In this paper, we propose SeFi-Image, a text-to-image foundation model built upon semantic-first diffusion, a novel latent diffusion modeling paradigm. We instantiate SeFi-Image at three model scales, 1B, 2B, and 5B parameters, enabling systematic study of scaling behavior and flexible deployment under varying compute budgets. Notably, our largest 5B model was trained with merely 125K A800 GPU hours, corresponding to roughly 10-20% of the training compute used by Z-Image. However, it achieves results comparable to or even superior to Qwen-Image and Z-Image. Despite this modest training compute, SeFi-Image achieves strong performance on a wide range of benchmarks, including GenEval, DPG, LongTextBench, OneIG, and CVTG-2K. Moreover, we provide DMD2-distilled few-step turbo variants for each model scale to accommodate diverse hardware constraints and latency requirements. We publicly release our code, weights and hope this work offers the community useful insights into semantic-guided diffusion modeling for T2I generation, while also providing practical and readily deployable model options.

---


### 204. [What are Key Factors for Updates in RL for LLM Reasoning?](https://arxiv.org/abs/2606.22570)

**<font color=#1a73e8>作者：</font>** Peidong Wang, Demi Wang, Xufang Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards (RLVR) has emerged as a promising framework for enhancing the reasoning ability of large language models. However, much of the existing work is guided by heuristic intuition, leading to divergent algorithmic choices, even contradictory ones that nevertheless report empirical gains. To better understand this phenomenon, we conduct a theoretical analysis of RLVR updates. Our study reveals that differences in off-policy degree, determined by the number of gradient steps per rollout, substantially affect the distribution of importance sampling ratios and their clipping behavior, thereby altering which tokens dominate the update. Building on this insight, we characterize gradient expectation as the central quantity governing update dynamics and analyze the roles of token probability, advantage, and importance sampling ratio. Motivated by these findings, we propose Adaptive Clip Policy Optimization (ACPO), which adjusts clipping boundaries across token groups according to the empirical variance of their importance sampling ratios. Experiments on 3B and 7B models across diverse reasoning benchmarks, spanning mathematical problem solving, tabular QA, and logic puzzles, demonstrate that ACPO outperforms strong baselines such as DAPO and CISPO. These results demonstrate that principled, analysis-driven approaches yield more robust and effective RLVR methods. Code is available in: this https URL

---


### 205. [Text2DSL: LLM-Based Code Generation for Domain-Specific Languages](https://arxiv.org/abs/2606.22586)

**<font color=#1a73e8>作者：</font>** Alexander V. Kozachok, Alexander M. Nazimov, Shamil G. Magomedov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Domain-specific languages (DSLs) are widely used for managing operating system security policies, yet manually authoring rules in such languages demands high expertise and is error-prone. This paper formalises the task of automatic DSL code generation from natural language descriptions - Text2DSL - as a distinct problem class, separate from Text-to-SQL and general-purpose code generation. We introduce the PolkitBench dataset comprising 4,204 verified natural-language-to-Polkit-rule pairs, each validated through a three-level AST-based pipeline. Controlled prompt experiments on two MoE models of different scale and provenance - GigaChat-10B-A1.8B (1.8B active parameters) and Nemotron-3-Nano-30B-A3B (3B active) - demonstrate the critical role of structured context (BNF grammar, API specification, permitted identifier vocabulary) for LLM-based DSL code generation. Across both models, supplying context raises syntactic validity to 98.6-99.4%, structural validity by +9.7 to +35.5 pp, and the CodeBLEU score by +60% to +95%. The consistency of the effect across models of different scale and provenance indicates that, for the Text2DSL class of problems, injecting a formal target-language specification into the prompt context is a robust enabling factor for high-quality generation without model fine-tuning.

---


### 206. [MapReason-OSM: Can Vision-Language Models Make Graph-Verifiable Mobility Decisions from Street Maps ?](https://arxiv.org/abs/2606.22597)

**<font color=#1a73e8>作者：</font>** Srinivas Venkatanarayanan, Clement Pakkam Isaac  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used to read maps for logistics, delivery, and accessible navigation, where the output is an actionable decision (a route, a pin, a parking choice) that must respect the road network. Yet most map benchmarks grade free-text or multiple-choice answers that cannot be verified against the underlying graph. We present \textbf{MapReason-OSM}, a benchmark and evaluation harness for graph-verifiable mobility decisions on self-rendered OpenStreetMap panels. We render fixed-style maps for ten U.S. downtowns at two aligned zoom scales, overlay a consistent marker grammar, and pair each panel with a hidden street graph and exact oracles, yielding 6{,}000 instances (12{,}000 panels across the two zooms) over 12 routing, facility-location, and visual-disambiguation tasks. Models return structured decisions that we snap back to the graph and score for validity, legality, optimality, and constraint satisfaction, plus \emph{cross-zoom consistency}. Across seven VLMs, models read maps and route simply but fail at graph-cost reasoning (single-facility pin placement is near chance even for frontier reasoning models), and are frequently scale-inconsistent. We release the benchmark, harness, and deterministic generator.

---


### 207. [Sub-Billion, Super-Frontier: Small Language Models Rival Zero-Shot Frontier LLMs on General and Literary Relation Extraction](https://arxiv.org/abs/2606.22606)

**<font color=#1a73e8>作者：</font>** Despina Christou, Grigorios Tsoumakas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong relation extraction (RE), but their computational demands and reliance on proprietary APIs limit deployment in resource-constrained or privacy-sensitive settings. We investigate how far small language models (SLMs) can close this gap across general-domain and literary text. We evaluate five models from 360M to 3B parameters under three domain-composition regimes and two prompt-conditioned tuning styles (30 configurations), comparing them with zero-shot frontier LLMs and a discriminative RoBERTa baseline. Across nine benchmarks, the best sub-billion model, Qwen2.5-0.5B fine-tuned on pooled general-domain data, achieves a general-domain positive-class micro-F1 of 0.83, versus 0.69 for GPT-5.4 and 0.66 for Claude Sonnet 4.6 evaluated zero-shot. This does not imply that SLMs are intrinsically stronger; rather, targeted task adaptation enables 4-bit models deployable on a single consumer GPU to outperform general-purpose frontier systems under this protocol. An in-domain RoBERTa baseline also exceeds both frontier models, indicating that the gain stems from task adaptation rather than generative decoding. On literary RE, tuned SLMs reach 0.92 on the human-annotated Biographical benchmark versus 0.83 for GPT-5.4, and 0.833 versus 0.578 on the two-benchmark literary average. A targeted domain-adaptive pretraining case study yields no practically meaningful gain over supervised fine-tuning, while the cleanest within-family scale comparison shows only marginal improvement. These results show that, when task-specific data are available, compact task-adapted models can provide accurate, private, and hardware-efficient RE.

---


### 208. [PaperClaw: Harnessing Agents for Autonomous Research and Human-in-the-Loop Refinement](https://arxiv.org/abs/2606.22610)

**<font color=#1a73e8>作者：</font>** Weiwei Ye, Hangchen Liu, Dongyuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have become capable reasoners and tool users that write and run code and search the literature, which makes automating the research process itself a realistic goal. We present PAPERCLAW, a harnessed multi-agent system that carries a project autonomously, from a field of study to a finished paper. PAPERCLAW curates a domain from a field's live literature, datasets, and code; brainstorms it into an idea with a pre-registered main-result contract; and drives a stoppable hypothesis map through an iterative propose, test, reflect loop that grows only from measured verdicts and halts once the evidence supports the idea, at which point it writes a venue-compliant paper. A full-lifecycle memory keeps each stage in a single living record, so a long run can be paused, inspected, and resumed without losing context. At the centre is an in-cycle research assistant with research tools and skills: it can drive the whole pipeline on its own, while the same interface lets a person step in at any stage, turning a first autonomous draft into a stronger paper through human-in-the-loop refinement. Throughout, PAPERCLAW keeps its output grounded and checkable, citing only references validated against open scholarly indexes and reporting results that genuinely ran. An evaluation with an LLM judge finds that PAPERCLAW produces strong papers both fully autonomously and with human-in-the-loop refinement.

---


### 209. [OmniSpace: Efficient Geometry Awareness for Autonomous Vehicles MLLMs](https://arxiv.org/abs/2606.22617)

**<font color=#1a73e8>作者：</font>** Hao Vo, Phu Loc Nguyen, Khoa Vo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable performance on 2D visual tasks, yet enhancing their spatial intelligence for real-world applications such as Autonomous Vehicles (AV) remains an open challenge. Existing geometry-aware MLLMs typically rely on auxiliary 3D models at inference time, introducing pipeline complexity and the risk of cascading failures. In this paper, we present OmniSpace, a simple yet effective plug-and-play paradigm for geometry-aware spatial reasoning from purely 2D observations. Motivated by our finding that current MLLMs are bottlenecked by weak cross-view correspondence and depth estimation, OmniSpace introduces a Camera Pose Injector, a Multi-view Epipolar Attention module, and a 3D Geometric Distillation objective that jointly address these two limitations by transferring geometric knowledge into the model. Extensive experiments show that OmniSpace surpasses existing methods on planning benchmarks (nuScenes, Bench2Drive), risk detection (nuInstruct), language (Omnidrive), and generalization (DriveBench).

---


### 210. [Orthogonal Representation Editing: Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs](https://arxiv.org/abs/2606.22627)

**<font color=#1a73e8>作者：</font>** Wenhao Yu, Zhicong Lu, Bo Lv 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge editing aims to efficiently update factual information in Large Language Models (LLMs) without full retraining. However, existing methods still suffer from performance degradation in batch knowledge editing. We identify that semantic representation entanglement, such as overlapping concepts and shared syntactic patterns, accumulates interference in the representation space and reduces editing precision. To bridge this gap, in this paper, we propose Orthogonal Representation Editing (ORE), which performs edits in the hidden representation space of LLMs by constructing a general semantic subspace and enforcing orthogonal constraints on edit vectors, effectively decoupling semantic entanglement. Furthermore, we introduce a gated non-linear representation head to enable adaptive learning of editing locations and precise control over knowledge injection. Extensive experiments show that ORE outperforms existing methods and achieves superior performance in cross-lingual knowledge editing scenarios. We release our code at this https URL.

---


### 211. [Confident but Conflicted: Internal Uncertainty and Cognitive Dissonance Resolution in LLMs](https://arxiv.org/abs/2606.22633)

**<font color=#1a73e8>作者：</font>** Weihong Qi, Kristina Lerman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently encounter inputs that disagree with their prior outputs, through user pushback, retrieved documents, or web search results. While the way they resolve such conflicts -- a process we frame as cognitive dissonance resolution -- has been characterized behaviorally, its connection to internal model uncertainty is not well understood. To study this systematically, we vary persuasion attempts along two dimensions, source authority and evidence quality, across 12 health-science claims of stratified epistemic status. Dissonance can be resolved through persuasion, backfire, or immunity. We introduce Trust Elasticity (TE), an econometrics-inspired measure of how readily a model is persuaded toward conflicting evidence. Across four LLMs, TE varies substantially, while clearly false claims elicit near-zero TE across all models. On two open-weight models, we further find that this variation is associated with two complementary internal uncertainty indicators, Confidence Miscalibration in Qwen and Internal Uncertainty Change in Llama. These results link cross-model behavioral variation to a measurable internal property and point to interventions targeting internal uncertainty as future work.

---


### 212. [Foundation Models for Epileptogenic Zone Identification in Drug-Resistant Epilepsy](https://arxiv.org/abs/2606.22657)

**<font color=#1a73e8>作者：</font>** Thi Kieu Khanh Ho, Thomas Lai, Petr Klimes 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate identification of the epileptogenic zone (EZ) is essential for seizure freedom after resective surgery in drug-resistant epilepsy, yet seizure freedom rates remain below 50%. We developed EpiiSLM, a dual foundation model system for EZ identification with stereo-electroencephalography (sEEG), by training a signal foundation model on 104,990 minutes of sEEG recordings from the Montreal Neurological Institute & Hospital, while leveraging all recordings regardless of surgical outcome and anchoring EZ biomarker extraction on non-epileptic signals. A language foundation model then integrates sEEG-derived outputs with multimodal clinical information to produce interpretable predictions. Under leave-one-patient-out evaluation, EpiiSLM achieved 0.978 contact-level positive predictive value (PPV), outperforming the seizure onset zone(SOZ)-as-EZ baseline by 15.1% (p < 0.05), and 100% region-level accuracy; on an external dataset, EpiiSLM achieved 0.857 contact-level PPV. EpiiSLM requires only one night of interictal sleep data, suggesting potential to reduce invasive sEEG monitoring duration and improve surgical outcomes.

---


### 213. [AgentLens: Interpretable Safety Steering via Mechanistic Subspaces for Multi-Turn Coding Agent](https://arxiv.org/abs/2606.22673)

**<font color=#1a73e8>作者：</font>** Weidi Luo, Qiming Zhang, Yihao Quan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents based on large language models (LLMs) demonstrate remarkable autonomous capabilities, but they also introduce significant safety and misuse risks during multi-turn interactions with external environments. Existing safety mechanisms mainly rely on external guardrails, which have a limited ability to perform fine-grained behavioral control during execution. Meanwhile, recent mechanistic interpretability methods for LLM safety are mostly confined to single-turn or jailbreak-style QA settings, limiting their ability to capture the evolving risk dynamics of multi-turn agent execution. In this paper, we investigate the safety of multi-turn coding agents from an internal perspective. We propose AgentLens (Mechanistic Subspace Intervention and Steering), a white-box defense framework that performs runtime safety detection and representation-level mitigation for coding agents. Unlike conventional agent guardrails, AgentLens detect harmful execution states from step-level hidden representations and mitigate unsafe behavior by intervening in a 10-dimensional subspace within a single layer. To support this research, we introduce the Mechanistic Agent Safety (MAS) benchmark, comprising comprehensively annotated multi-turn execution trajectories across 194 tasks using LLaMA-3.1-8B, Qwen-2.5-7B, and Gemma-2-9B. Extensive experiments show that AgentLens achieves strong safety detection performance, provides preliminary evidence for lookahead risk anticipation, and substantially reduces harmful actions of the coding agent, establishing a foundation for applying mechanistic interpretability to dynamic LLM agent safety. The code is available at: this https URL

---


### 214. [Skin-Deep: A Geometric Diagnostic for Alignment Fragility in Large Language Model Representations](https://arxiv.org/abs/2606.22676)

**<font color=#1a73e8>作者：</font>** Dongyub Jude Lee, Jungseob Lee, Seungyoon Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alignment tuning is meant to make harmful-request refusal robust, yet this safety behavior can be erased by a small set of benign fine-tuning examples. This is a deployment risk for open-weight models because a checkpoint can pass refusal tests at release time and later lose refusal under low-cost downstream fine-tuning. Prior work has established these refusal failures, but existing studies do not show how to detect this fragility in the aligned model itself before an attack or fine-tuning intervention is run. We introduce Skin-Deep, a geometric diagnostic that detects alignment fragility directly from the aligned model's hidden-state activations before such an intervention is run and compresses the layer-wise safety geometry into a single scalar, the Geometric Fragility Score (GFS). Applied to twenty-one instruction-tuned models spanning six alignment recipes and 3B--32B parameters, Skin-Deep reveals a recurring low-rank safety subspace across model families. Direction ablations show that removing directions in this subspace weakens harmful-request refusal, providing causal evidence that the recovered geometry underlies refusal behavior. Crucially, GFS identifies, before any fine-tuning, the initially safe model that retains the most refusal after small-scale LoRA fine-tuning. These results establish GFS as a practical pre-deployment diagnostic for flagging fragile refusal behavior without running an attack.

---


### 215. [Only Ask What You Don't Know: Grounded Delta Planning for Efficient Multi-step RAG](https://arxiv.org/abs/2606.22681)

**<font color=#1a73e8>作者：</font>** Wei-Chieh Chou, Xuanjun Chen, Jian-Ren Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering remains challenging for Retrieval-Augmented Generation (RAG) because existing approaches either propagate errors across iterative retrieval rounds or over-generate reasoning steps, increasing cost without improving accuracy. We propose Grounded Delta Planning RAG (GDP-RAG), a plan-based framework that targets only the information delta based on three simple design choices: (1) preliminary retrieval to ground planning before execution, (2) a gap-conditioned planning prompt that asks only for missing information, and (3) a skeletal trajectory that pairs each subquery with a Thought capturing evidence from preliminary retrieval and carrying it through to the final answer. GDP-RAG focuses computation on unresolved gaps, yielding concise, reliable reasoning trajectories. Extensive experiments on HotpotQA, 2WikiMultiHopQA, and MuSiQue show that GDP-RAG achieves the highest accuracy (60.63%) among all compared systems while maintaining a cost-of-pass of 0.51, 22% lower than PAR-RAG (0.65) and 68% lower than KnowTrace (1.57), with no method achieving both higher accuracy and lower cost.

---


### 216. [GARIP: A Running-Average Moving Reference for Last-Iterate Self-Play in Two-Player Zero-Sum Games](https://arxiv.org/abs/2606.22688)

**<font color=#1a73e8>作者：</font>** Can Savcı  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Self-play with naive gradient ascent cycles in two-player zero-sum games: the last iterate orbits the equilibrium. Modern methods restore last-iterate convergence by regularizing toward a reference policy -- MMD a fixed one (reaching only the regularized equilibrium), R-NaD a periodic snapshot (the engine of DeepNash). We study GARIP, which anchors to the running average, and isolate what the choice of reference controls. Our central result is a mechanism: collapse tracks the peak lag of the reference, and among causal convex averages of a fixed mean lag the running average (flat profile, peak $=$ mean) uniquely minimizes that peak, while a snapshot's sawtooth has peak $= 2\times$ mean (a one-line theorem). Two consequences follow. Convergence: we prove local last-iterate convergence at constant anchor strength -- the anchor scales the base map's rotation by $1-\beta$, crossing the stability boundary and turning a recurrent base into a contraction (global convergence is conjectured at small $\beta$; we characterize a large-$\beta$ consensus failure). Robustness: GARIP matches R-NaD's peak performance -- on matrix games, the Coin Game, and the board games Connect Four/Othello, both moving references are far more robust than fixed-magnet and magnet-free baselines -- but is the better hyperparameter default; we report it both ways: over the full grid collapse rates are statistically indistinguishable, yet at conventional parameterizations a matched-mean-lag setting collapses in 0/40 vs 10/40 seeds (a snapshot matches it only by knowing to shorten $K$). The boundaries: an anticipatory (negative-weight) reference does better still on the stale side, and the advantage appears only where naive self-play cycles (five deep self-play loops). All experiments are pure JAX and reproducible.

---


### 217. [VISTA Architect: A graph database-oriented health AI system demonstrated in multidisciplinary tumor boards](https://arxiv.org/abs/2606.22692)

**<font color=#1a73e8>作者：</font>** Tuomo Kiiskinen, Jason Fries, Philip Adamson 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce VISTA Architect, a database-oriented AI architecture for integrating large language models (LLMs) with longitudinal electronic health records (EHRs). At ingestion, it transforms complex clinical documentation into a persistent, provenance-linked knowledge graph, eliminating repeated reprocessing of raw records at query time. The architecture has two layers: a source-faithful MEDS Graph preserving granular EHR structure with full provenance, and a clinically abstracted Timeline Object Architecture (TOA) that uses graph-guided LLM extraction to synthesize a concise timeline of deduplicated, temporally coherent clinical events. This addresses key limitations of direct long-context prompting and retrieval-augmented generation (RAG), which often miss temporal relationships and incur high cost and latency from repeated raw-text processing. By precomputing clinical synthesis once, downstream queries access an organized patient state and traverse to source documentation only when detailed verification is needed.
We demonstrate the system in multidisciplinary thoracic oncology tumor boards at Stanford Medicine, where precise reconstruction of patient histories is critical. Across 1,180 patients, VISTA Architect achieved 96.4% accuracy (mean 9.75/10) on 15 tumor board-salient variables (17,700 evaluations; 95% CI 96.1-96.7%), surpassing a matched BM25 RAG baseline and recent benchmarks for LLM-based clinical extraction. An agentic interface reduced preparation for a 30-patient held-out cohort to about 2.2 minutes without sacrificing accuracy. While configured here for thoracic oncology, the modular design adapts to other specialties through customizable event definitions, episode structures, and agentic tools; validation beyond thoracic oncology remains future work.

---


### 218. [Catching Lies Without Sending the Video: Privacy-Preserving Multimodal Deception Detection](https://arxiv.org/abs/2606.22699)

**<font color=#1a73e8>作者：</font>** Nikita Sharma, Pranav Sara, Karan Singla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frontier multimodal models can guess whether a person is lying from a testimony video. To do so, they stream that raw face and voice to a third-party model. We ask whether the heavy media is needed at all. On the Real-life Trial Deception dataset, Whissle on-device speech and vision stack extracts a compact digest: transcript, emotion, age, gender, intent distributions, a deception intent filter, fluency and rhythm, per-frame facial behaviour, and prosody. Under speaker-independent evaluation, we report three findings. A small classifier on this digest reaches AUC 0.741, matching Gemini 2.5 Pro on full video. Handing the digest to a frontier LLM reaches AUC 0.755 with Claude Opus 4.8 at 7.8X fewer input tokens, with no media leaving the device. The reported 75% accuracy is a speaker-leakage artifact. We release code and experiments.

---


### 219. [Safety-Aware Evaluation of LLM-Generated Driver Intervention Messages through Multi-Task Risk Fusion](https://arxiv.org/abs/2606.22706)

**<font color=#1a73e8>作者：</font>** Keito Inoshita  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing driver intervention systems rely on auditory alerts and fixed templates, failing to leverage multi-task recognition outputs. General-purpose metrics such as BLEU and BERTScore cannot capture intervention-specific quality dimensions including risk-urgency alignment, cognitive load, and driver acceptability. In this paper, we propose the Driver Safety-Aware Intervention Score (DSAIS), a domain-specific metric evaluating five dimensions through a hybrid architecture combining lightweight rule-based computation with LLM Judge evaluation, together with an end-to-end framework integrating four-task recognition outputs into an LLM through risk fusion, state history management, and dynamic prompt construction. Experiments on the AIDE dataset with five models and seven conditions demonstrate that DSAIS achieves ICC 0.798-0.840 across three architecturally distinct judges and Cohen's d > 1.5 across all control conditions. Multi-dimensional sub-score analysis quantifies the contextual adaptability gap between rule-based and LLM-based systems, revealing that multi-task integration improves contextual relevance by 9.1% over rule-based baselines. Ablation experiments demonstrate that each framework component contributes to contextual relevance, with sub-score decomposition revealing gains that aggregate scoring masks. Driver emotion recognition is identified as the most critical upstream factor, and compact local LLMs (7B--9B parameters) achieve quality superior to API-based models, providing practical design guidelines for in-vehicle deployment.

---


### 220. [Beyond Penalizing Mistakes: Stabilizing Efficiency Training in Large Reasoning Models via Adaptive Correct-Only Rewards](https://arxiv.org/abs/2606.22716)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Seungyoon Lee, Seongtae Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training large language models to reason efficiently is a critical challenge. While integrating length-penalizing rewards into Group Relative Policy Optimization (GRPO) aims to reduce verbosity, it frequently triggers reward collapse, severely degrading reasoning capabilities. Through a systematic evaluation of various reward configurations, we identify the root mechanism: GRPO's group normalization creates divergent advantages when incorrect answers receive continuous length penalties. Consequently, methods penalizing the length of incorrect answers are structurally prone to collapse under sustained optimization. Furthermore, restricting penalties exclusively to correct answers avoids this primary failure, but leaves the model susceptible to a stochastic collapse driven by response over-compression. To robustly prevent both failure modes, we propose ACOER (Adaptive Correct-Only Efficiency Reward). ACOER eliminates the structural penalty loop by isolating brevity bonuses to correct completions and prevents stochastic compression via dynamic budget normalization and control-loop penalty adjustments. Evaluated across diverse mathematical reasoning benchmarks, ACOER improves overall accuracy compared to the base model while reducing token generation by over 60%, establishing a fundamentally stable approach for efficiency-aware optimization.

---


### 221. [BLUEX v2: Benchmarking LLMs on Open-Ended Questions from Brazilian University Entrance Exams](https://arxiv.org/abs/2606.22723)

**<font color=#1a73e8>作者：</font>** João Guilherme Alves Santos, Giovana Kerche Bonás, Thiago Laitz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) excel in many tasks, their assessment in Portuguese has received less attention, particularly for open-ended, discursive tasks that demand deeper reasoning and generation capabilities. While the original BLUEX benchmark addressed the scarcity of Portuguese evaluation datasets through multiple-choice questions from Brazilian university entrance exams, it did not cover the more challenging second-phase examinations, which require free-form written responses. In this work, we introduce BLUEX v2, a benchmark derived from the second-phase entrance exams of Brazil's two leading universities: UNICAMP (Comvest) and USP (Fuvest), spanning exam years 2022-2025. Our dataset comprises 395 questions unfolding into 919 graded subquestions, with 55.7% of questions containing associated images. Each question is annotated with subject area, official reference answers, LLM-generated rubric criteria, and six cognitive capability tags. We evaluate 21 state-of-the-art LLMs using an LLM-as-a-judge protocol. Results reveal a 4.92-point performance spread across models (4.18-9.10 on a 0-10 scale), with Mathematical Reasoning and Image Understanding emerging as the hardest capability dimensions. The dataset, evaluation code, and model outputs are publicly available at this https URL.

---


### 222. [When Confidence Takes the Wrong Path: Diagnosing Retrieval-State Lock-In in RAG](https://arxiv.org/abs/2606.22728)

**<font color=#1a73e8>作者：</font>** Sahib Julka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The trustworthiness of a retrieval-augmented generation (RAG) system depends on more than the answer it returns, yet many black-box uncertainty methods still read agreement among sampled answers as confidence. That inference fails when repeated samples condition on the same defective retrieval state. The state may be empty, with the model falling back on parametric memory, or populated by a coherent but wrong neighbourhood. In either case, the answers agree because the error is stable. The problem is recognised in deployed RAG, but it has lacked a name, a measurable signature, and a prevalence bound. We supply all three. We name the failure retrieval-state lock-in and diagnose it by separating the three objects a single confidence score conflates: the answer surface, the retrieved evidence, and the retrieval state itself. In an inspectable, ontology-guided knowledge-graph RAG (KG-RAG) system across six question-answering snapshots, we measure the agreement blind spot directly: at five samples per question, 42% of KG-RAG errors and 59% of dense-retrieval errors carry zero answer dispersion, so agreement has nothing to rank, while evidence- and retrieval-state checks still flag most of them. The decomposition supports an auditable decision rule: accepting an answer only when answer, evidence, and retrieval checks all agree that it is low-risk reaches 91.9% pooled precision against a 69.7% accept-all rate. The cost is coverage: it certifies only 7.7% of answers as low-risk. On the clinical calibration domain it reaches 100% precision under an automated judge; this is an in-domain automated-label upper bound, not a clinical safety claim, and still needs human validation. Confidence in RAG is object-specific: when answers agree, the useful question is which part of the pipeline to distrust.

---


### 223. [GroundEval: A Deterministic Replacement for LLM-as-Judge in Stateful Agent Evaluation](https://arxiv.org/abs/2606.22737)

**<font color=#1a73e8>作者：</font>** Jeffrey Flynt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before letting an agent operate over real context, can you prove it used the right evidence? GroundEval turns that question into a deterministic test of what the agent searched, fetched, cited, and was permitted to access. In one case study, two frontier LLM judges scored a plausible agent response above 0.85. But the trace told a different story: the agent had never retrieved the artifact its answer depended on, yielding a GroundEval score of 0.000.
We introduce GroundEval, a judge-free framework for evaluating agents against grounded, time-bounded, and access-controlled evidence. GroundEval uses a domain configuration to generate questions, lets the agent choose how to answer, and then scores both the final answer and the recorded trajectory that produced it. The benchmark targets three failures that LLM-as-judge evaluation struggles to detect: whether an agent checked before claiming absence, reasoned only from evidence available to the actor at the relevant time, and used the correct causal mechanism rather than a plausible one. These correspond to three tracks: Silence, Perspective, and Counterfactual. GroundEval exposes when plausible answers rest on invalid evidence paths, and produces structured per-question diagnostics that pair tool activity with the agent's turn-level narration, making each score inspectable rather than merely reported. What our case studies turned up is that this gap isn't some rare corner case. It's exactly the blind spot that final-answer and judge-based scoring were never built to catch.

---


### 224. [GRADE: Graph Representation of LLM Agent Dependency and Execution](https://arxiv.org/abs/2606.22741)

**<font color=#1a73e8>作者：</font>** Yue Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can one graph represent every kind of LLM agent's run? A trace records what each step did, never what it relied on, the state it read, and the results it reused. GRADE recovers that missing layer: it models any run as one graph over its step nodes with two edge layers, execution edges (what ran in what order) read from the trace for free, and dependency edges (what each step relied on) rarely logged, so each is graded by how it is known, observed, declared, or inferred. One representation, and each layer earns its place. Across six corpora of LLM agents spanning tool use, coding, and the web, the dependency layer can predict failure where run size is weak and, under leave-one-corpus-out transfer, stays above chance on every held-out class while run size fails. Meanwhile, the execution layer localizes the faulting step in a failed multi-agent run. This work also provides a more in-depth analysis of why generic graph neural networks may misread the dependency layer, unlike our feature-based alternative. The same graph representation opens further uses, carrying from failure diagnosis in a single run to efficiency and robustness optimization at scale.

---


### 225. [Language-Specific Sentiment Polarity Biases in Encoder and Large Language Model Classification of Product Reviews](https://arxiv.org/abs/2606.22745)

**<font color=#1a73e8>作者：</font>** Advita Rajiv, Kavitha Kothur, Gautham Reddy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates sentiment polarity biases, specifically, differences in how accurately AI models classify positive versus negative reviews across languages and model architectures. Large language models show a negative bias in French and are more accurate on negative reviews, while encoder models exhibit positive bias in Japanese, missing negative reviews that use indirect criticism. These language-specific polarity biases have implications in both social and business domains deploying multilingual sentiment analysis systems.

---


### 226. [AI Fiction in the Wild](https://arxiv.org/abs/2606.22748)

**<font color=#1a73e8>作者：</font>** Neel Gupta, Maria Antoniak, Melanie Walsh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Some professional authors are beginning to use AI tools to help produce their fiction writing. Are readers using AI to generate fiction, too? This paper examines how large language models are reshaping the production and consumption of fiction by enabling new forms of participation in narrative generation. Drawing on over 500,000 anonymized, English-language ChatGPT-user conversations (arXiv:2405.01470), we find that more than one third of the conversations involve some form of fiction generation -- including original stories, roleplay, fanfiction, and erotica. This AI-generated fiction is notably dominated by power users. We identify common fiction generation patterns and profiles among these users, including what we call "infinite story demanders," who repeatedly request and revise variations of the same or similar narratives over extended periods of time. We show that users especially gravitate toward fanfiction and erotica, and that they are broadly drawn to generic forms, repetition, immediacy, and niche combinations of story elements. Our findings motivate two theoretical provocations. First, we argue that AI technologies may lead to a shift in the conventional relationship between the author and reader, potentially producing what we call a "solipsistic reader-writer," who both generates and consumes fiction within a closed conversational loop, interacting with a machine rather than a human other. Second, we note that LLMs enable interactivity, play, and permutation in ways that are seemingly pleasurable for users, raising questions about where AI will fit into contemporary storytelling and entertainment ecosystems. We situate these developments within broader transformations in literature and media, including self-publishing, fanfiction, and pornography, and suggest that AI-generated fiction shares structural affinities with on-demand, personalized, and repetitive cultural forms.

---


### 227. [Explainable AI for Mental Health Prediction in Drug-Affected Populations with Dragonfly Algorithm and GAN Oversampling](https://arxiv.org/abs/2606.22780)

**<font color=#1a73e8>作者：</font>** Ahnaf Atef Choudhury, Shahriar Siddique Ayon, Md. Ebrahim Hossain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mental illnesses among drug users are an increasing international issue, particularly in regions where early detection cannot be easily undertaken. The current literature tends to ignore the use of AI-based mental health analysis in drug users, and low quality of the class imbalance treatment, low interpretability, and optimal hyperparameter optimization can lower predictive quality and clinical utility. This study present a detailed, explainable machine learning (ML) model of multiclass mental health prediction, using a multidimensional data set of drug-affected persons. We combine hybrid PCA-Information Gain (PCA-IG) feature selection, Generative Adversarial Network (GAN)-based oversampling, and Dragonfly Algorithm (DA)-optimized XGBoost to address some of the limitations of existing methods. The suggested framework is effective to work with high-dimensional categorical data, address the issue of class imbalance, and improve predictive performance due to intelligent hyperparameter tuning. The experimental findings show that the XGBoost model optimized using the DA, in combination with GAN-based oversampling, has an accuracy of 94.17% and a weighted F1-score of 93.80%, which is better than the traditional and baseline models. The behavioral, lifestyle, and health factors, particularly sleep quality, physical health, and emotional regulation, are strongly predictive of mental health, with demographic factors having little impact, as seen through feature analysis. SHAP-based explainable AI provides easy-to-understand, instance-level information, enhancing interpretability and trust in models to be used in clinical settings. The results indicate that this framework has the potential to generate valid mental health forecasting tools, which would facilitate early intervention and enhance the treatment of drug-influenced people.

---


### 228. [The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models](https://arxiv.org/abs/2606.22792)

**<font color=#1a73e8>作者：</font>** Xiang-Jun Ou, Shuang Liang, Xin-Yu Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Large Language Models (LLMs) have enabled sophisticated reasoning and content generation, yet their inherent stochasticity poses significant challenges for ensuring predictive credibility. While traditional uncertainty taxonomy paradigms, such as the dichotomy of aleatoric and epistemic uncertainties, provide conceptual foundations, they often fail to capture the multi-component and multi-stage nature of LLM generation and struggle to evaluate the effectiveness of various Uncertainty Quantification (UQ) methods. In this paper, we propose a granular uncertainty taxonomy that systematically attributes LLM uncertainty into input-level, parameter-level, token-level, and decoding-process sources. Correspondingly, we categorize existing UQ methods into Bayesian, ensemble, consensus-based, and single-pass approaches. Furthermore, we introduce a comprehensive evaluation framework covering diverse generation settings and metrics. We empirically evaluate 21 typical UQ methods across three prominent LLM families, including Qwen3, Llama 3.2, and DeepSeek-V3, on benchmarks such as TriviaQA, GSM8K, and HumanEval. Our experimental results demonstrate that (i) the effectiveness of UQ methods is sensitive to task types and generation settings; (ii) consensus-based methods, typed Deg and EigV, consistently outperform other UQ approaches; and (iii) larger model scales correlate with lower uncertainty estimates, suggesting an empirical scaling law for LLM uncertainty. This work bridges the gap between theoretical origins and practical deployment, providing a versatile diagnostic tool for systematically quantifying uncertainty in LLM applications.

---


### 229. [Measuring Behavior Portability in Large Language Models](https://arxiv.org/abs/2606.22797)

**<font color=#1a73e8>作者：</font>** Tianjia Dong, Nadav Kunievsky, James A. Evans  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as autonomous decision makers, yet the behavioral mapping they exhibit can vary substantially across decision environments that are payoff-equivalent by construction-environments that share identical payoff-relevant structure but differ in surface presentation. This sensitivity renders suite-based evaluation fragile and raises a fundamental question of behavioral portability: how well does a behavioral mapping learned in one decision environment informative on another that preserves the same underlying incentive structure? We introduce a formal framework to measure this property. Our protocol fits an interpretable behavioral model on data pooled from a set of source environments and evaluates its out-of-sample predictive performance in a held-out target environment, benchmarking against an oracle trained directly on target data. Portability is quantified via a loss-agnostic measure that delivers worst-case bounds on the performance of the induced prediction-action mapping in the target environment. In controlled experiments spanning seven canonical economic decision problems, we document substantial and systematic portability losses, suggesting that behavioral characterizations of LLMs obtained in one decision environment cannot be assumed to transfer reliably to structurally equivalent alternatives.

---


### 230. [Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control](https://arxiv.org/abs/2606.22798)

**<font color=#1a73e8>作者：</font>** Kang Chen, Minshen Yu, Junjie Nian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In sparse Mixture-of-Experts language models, does the same token id imply the same router state and the same experts producing it? Holding the emitted token id fixed at repeated anchors, we find it does not: the experts that produce it still separate task context, trajectory history, and reasoning-effort mode. This residual structure supports test-time control: near \emph{boundary} anchors (the final-response transition) and \emph{delimiter} anchors (which open the answer, e.g.\ \texttt{\textbackslash boxed\{} or code fences), routing neighborhoods already align with final-answer basins at a marker-only readout and strongest when the routing is read at the answer opening. We operationalize this as \textbf{RAD} (Routing Agreement Decoding), an answer-string-free multi-rollout selector: it locates a fixed anchor, represents each rollout by its anchor-window MoE routing states, and returns the densest Weighted-Jaccard $K$-NN route-basin center, without parsing, normalizing, executing, or voting over answer strings. Across 10 sparse-MoE configurations (gpt-oss, Qwen3-MoE) and 6 datasets spanning math, GPQA, and code, RAD is on par with Majority where string voting is well-posed, with small positive paired deltas (RAD $73.9$ / RAD+DC $74.2$ vs.\ Majority $73.6$). Like majority voting, RAD is not a verifier: a dense \emph{wrong} basin can still win. Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on.

---


### 231. [Retrieval-Augmented Multimodal Learning for Enzyme-Substrate Interaction Prediction Under Low-Homology Shift](https://arxiv.org/abs/2606.22823)

**<font color=#1a73e8>作者：</font>** Chen Liu, Bingxin Zhou, Xinyuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enzyme substrate interaction (ESI) prediction is a fundamental computational task for biocatalyst discovery and reaction screening in large biochemical spaces. In practical settings, ESI prediction is challenged by sparse positive supervision and low-homology distribution shift, where test enzymes share limited sequence identity with those observed during training. To address these challenges, we propose RAMMESI, a retrieval-augmented multimodal framework for robust ESI prediction. RAMMESI learns explicit pairwise enzyme-substrate representations through directional cross-modal interaction modeling and adaptive fusion. To enhance robustness, RAMMESI retrieves neighboring enzymes at inference time, recombines them with the query substrate, and aggregates the resulting pairwise predictions as contextual evidence. To improve learning under sparse positive supervision, we further adopt an imbalance-aware weighted-BCE objective. Experiments on two ESI benchmarks under sequence-identity-aware splits demonstrate that RAMMESI achieves consistently strong performance, with particular advantages in more challenging low-identity regimes. In addition, the retrieval module improves multiple ESI backbones in a plug-and-play manner, suggesting that retrieval provides a general mechanism for improving robustness under homology shift.

---


### 232. [MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration](https://arxiv.org/abs/2606.22826)

**<font color=#1a73e8>作者：</font>** Devleena Das, Rajeev Patwari, Vikram Kumar Bukka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating LLMs across many model variants -- quantized, fine-tuned, or deployment-specific -- requires running large benchmarks repeatedly, a process that can take tens of hours per model on edge hardware such as NPUs. Existing subset selection methods reduce this cost but depend on large calibration pools or learned prediction layers. We introduce MINCE (Monte Carlo Informed N-sizing for Compact Evaluation), which uses Monte Carlo simulation over per-item logs from a small set of calibration models to find the minimum subset size that bounds accuracy drift and then fixes a randomly sampled subset at that size, with no prediction layer needed. MINCE reduces IFEVAL by 54\%, MMLU by 89\%, and GSM8K by 70\% with maximum drift $\leq$2.62\,pp on BF16 models and mean drift of 0.77--3.59\,pp on held-out NPU models, while delivering median GPU evaluation speedups of 2.7--8.1$\times$ and NPU evaluation speedups of 1.7--2.0$\times$. The method is robust to calibration pool size and achieves lower drift than tinyBenchmarks (12$\times$ lower on MMLU, 3.3$\times$ on GSM8K) while using 57$\times$ fewer calibration models.

---


### 233. [RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving](https://arxiv.org/abs/2606.22840)

**<font color=#1a73e8>作者：</font>** Haifeng Wu, Srinivasan Manoharan, Fangbo Tu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary. A fast, inexpensive draft model generates a candidate response; a capable verify model accepts, enhances, or is bypassed entirely depending on a lightweight complexity router. On a real-world agentic coding workload (Claude Code), RLM-Cascade achieves a draft-use rate of 88.8% across 125 production requests, reducing API cost by 45.8% relative to a direct Opus baseline. Counter-intuitively, the proxy also reduces end-to-end latency: median response time is 2,026 ms versus 3,698 ms for Native Opus -- a 1.83X speedup at p50 -- because the SKIPPED path (DeepSeek only, no Opus call) dominates the workload distribution. Quality matches or exceeds the Opus baseline: 100% pass rate on a 20-task Code/Math/Instruct benchmark versus 95% for Native Opus. We further describe a rule-based complexity router that selects the SKIPPED path for simple agentic turns and a hybrid tool-call strategy that bypasses the speculative pipeline for schema-critical tool-selection turns. RLM-Cascade is deployed in production as an enterprise AI infrastructure component and published as open source with a live metrics dashboard and Prometheus endpoint.

---


### 234. [IndicGuard: A Multilingual Safety Guard Model and Dataset for Indic Languages](https://arxiv.org/abs/2606.22841)

**<font color=#1a73e8>作者：</font>** Parth Bramhecha, Smit Deshmukh, Sairaj Bodhale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) achieve widespread integration across diverse linguistic landscapes, ensuring their safety and alignment with regional normative values remains a critical challenge. Current safety mechanisms are predominantly optimized for English-centric frameworks, often failing to capture the unique socio-cultural sensitivities and localized categories of harm inherent to the Indic region. To address this gap, we introduce IndicGuard, a multilingual safety guard model and dataset for Indic languages. We construct a high-volume, culturally nuanced safety dataset encompassing ten major Indic languages, systematically curated to capture regional harms, sensitive socio-political contexts, and adversarial jailbreaks. Leveraging this corpus, we fine-tune a 4B-parameter instruction-tuned model based on Gemma-3-4B-IT to serve as a multilingual safety guardrail for real-time content moderation and policy compliance checking. Our empirical evaluations demonstrate that IndicGuard significantly enhances LLM robustness against localized vulnerabilities, achieving high moderation consistency across different conversational turns. Crucially, IndicGuard consistently outperforms the existing baseline model, CultureGuard, across evaluated languages. Finally, we demonstrate that our model effectively generalizes to low-resource Indic languages excluded from training, substantiating the structural robustness and cross-lingual transfer capabilities of the framework.

---


### 235. [RaMem: Contextual Reinstatement for Long-term Agentic Memory](https://arxiv.org/abs/2606.22844)

**<font color=#1a73e8>作者：</font>** Wei Yang, Bryce Kan, Shixuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts. Recent memory systems have made past experiences more persistent, compact, and retrievable, but retrieval alone does not ensure that a memory provides valid evidence for the current query. When experiences are compressed into reusable fragments, memories from different situations may appear equally relevant if they involve recurring entities or user states. We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. To address this problem, we propose Contextual Reinstatement for Agentic Memory (RaMem), a framework that turns retrieved memory fragments into contextually verifiable evidence. RaMem operates through four coordinated stages: (i) evidence anchoring grounds each memory in its original episodic conditions, especially event time, mention time, session span, and participants; (ii) recall condition induction derives the evidence conditions implied by the query; (iii) validity-aware retrieval uses these conditions to prioritize context-compatible memories while retaining content-relevant candidates as fallback evidence; and (iv) context-preserved synthesis keeps the selected memories' structured context available to the generator. Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones.

---


### 236. [When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents](https://arxiv.org/abs/2606.22864)

**<font color=#1a73e8>作者：</font>** Yanhang Li, Zhichao Fan, Zexin Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hidden-state probing -- a linear classifier on a frozen vision-language model's internal activations -- has emerged as an attractive evaluation tool for flagging indirect prompt injection (IPI) in multimodal computer-use agents before the agent emits a corrupted action. We argue, on a single-backbone cautionary case study (Qwen2.5-VL-7B on Mind2Web, teacher-forced replay), that a high probing AUC on a clean-vs-attack split is not, on its own, evidence of malicious-content detection. Two post-hoc diagnostics -- a paired-construction scalar baseline on text-side injections, and same-step nuisance-matched visual controls on the overlay surface -- do not license an unqualified malicious-content interpretation of the headline while leaving room for partly-semantic readings. We package the diagnostics as a candidate control set with reporting heuristics for what a high clean-vs-attack AUC does and does not license. Labels are injection-surface-present, not attack success; generalisation beyond this backbone and benchmark is a conjecture.

---


### 237. [VideoLatent: Video-Language Learning via Latent Self-Forcing](https://arxiv.org/abs/2606.22870)

**<font color=#1a73e8>作者：</font>** Zi-Yuan Hu, Zicong Tang, Shijia Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in chain-of-thought (CoT) reasoning have shown promise in enhancing video understanding and reasoning capabilities of multimodal large language models (MLLMs). However, existing CoT-based MLLMs require labor-intensive CoT annotations and incur substantial training and inference overhead. While visual latent reasoning has emerged as a more efficient alternative, existing methods primarily focus on image tasks and heavily rely on additional supervision signals for visual latent generation (e.g., CoT traces, auxiliary images, or fine-grained annotations), limiting their scalability and transferability to video tasks. To bridge this gap, we introduce VideoLatent, a novel MLLM equipped with a latent injection module tailored for video understanding and reasoning. Specifically, VideoLatent learns to perform visual latent reasoning using a new latent self-forcing training paradigm, which comprises latent alignment and latent diversity objectives, and relies solely on standard video-question-answer triplets. Extensive experiments across 14 benchmarks demonstrate that our model consistently outperforms existing standard and latent MLLMs on general video understanding and complex video reasoning. Compared with Video-R1, our VideoLatent achieves superior computational efficiency, reducing training/inference overhead by $\sim$6$\times$/$\sim$68$\times$. Moreover, experiments demonstrate that our method has strong generalizability to different MLLM backbones and different model scales.

---


### 238. [Fursee: Hybrid YOLO-DINOv3 Framework for Fursuit Identity Retrieval and Clustering](https://arxiv.org/abs/2606.22872)

**<font color=#1a73e8>作者：</font>** Jundi Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global furry conventions produce massive fursuit photographs, while manual sorting brings heavy labor costs and calls for automatic identity retrieval and clustering solutions. General multimodal models lack dedicated optimization for complex fursuit scenes, and no public benchmark dataset exists for this task. To fill this gap, we build a specialized fursuit image dataset and present a three-stage hybrid pipeline Fursee for fursuit identity retrieval and clustering. First, YOLO detects and crops high-resolution fursuit head patches to improve localization of small and overlapping targets. Second, ArcFace optimizes DINOv3 embeddings to enlarge angular separation between different identities on the feature hypersphere. Third, DBSCAN performs unsupervised clustering, with silhouette-coefficient-driven search automatically selecting optimal hyperparameters rather than fixed manual radius. Retrieval and clustering experiments verify that our pipeline outperforms mainstream multimodal models including GPT5.5, Claude Opus 4.8 and Qwen3.7-Plus on all evaluation metrics, achieving competitive performance for fursuit head retrieval and grouping.

---


### 239. [SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning](https://arxiv.org/abs/2606.22873)

**<font color=#1a73e8>作者：</font>** SingGuard Team  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed in consumer, medical, financial, and enterprise applications. This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. Most existing guardrails either rely on fixed taxonomies or target only a narrow set of interaction settings, which limits their adaptability when safety rules change at deployment time. We present \textbf{SingGuard}, a policy-adaptive multimodal guardrail model family for safety assessment in multimodal conversations. SingGuard treats the active policy as a runtime input: given natural-language rules, it checks the target content against the active policy rule by rule and predicts both the safety label and the triggered rule. To balance efficiency and interpretability, SingGuard supports fast, hybrid, and slow inference regimes along a fast-to-slow reasoning spectrum, ranging from direct safety judgments to policy-grounded deliberation. We further optimize this behavior with fast--slow decoupled reinforcement learning. We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. Across six benchmark families (35 datasets), SingGuard achieves state-of-the-art average F1 in every family. Dynamic-rule evaluation further shows improved policy-following accuracy from 0.6465 to 0.7415 under runtime policy shifts. Our code is available at this https URL.

---


### 240. [Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning](https://arxiv.org/abs/2606.22878)

**<font color=#1a73e8>作者：</font>** Nuocheng Yang, Yechen He, Sihua Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed at the network edge to provide pervasive generative AI services, decentralized federated learning (DFL) provides a vital mechanism for privacy-preserving, domain-specific fine-tuning through peer-to-peer exchanges of parameter-efficient updates. However, the dynamic nature of practical decentralized edge networks, where devices may dynamically join or leave the collaborative training process, requires the system to continuously adapt to new data while selectively removing prior contributions. This correction process remains a significant bottleneck, as individual device updates become deeply entangled within the global fine-tuned parameters. To address this challenge, we propose a priority-aware learning-unlearning correction framework based on orthogonal LoRA that can enhance the knowledge evaluation through topology adjustment. Specifically, we first design an orthogonal LoRA mechanism that yields post-training contribution coordinates, enabling history-free projection addition and deletion in response to membership changes. We then analyze the correction bottleneck and develop a priority-aware policy that selects among topology refinement, local correction, proximal damping, and synchronization scheduling according to the dominant residual term. A resource allocation algorithm is further developed to allocate limited communication across layer groups, prioritizing the primary bottlenecks within per-round wireless constraints. Experiments demonstrate that the proposed framework achieves robust post-event correction for both device join and leave events and validate that different residual regimes necessitate distinct correction actions.

---


### 241. [Physiology-Aware CNN and Zero-Shot Multimodal LLMs for ECG Image Classification: A Comparative Study](https://arxiv.org/abs/2606.22889)

**<font color=#1a73e8>作者：</font>** Khalil Ahammad, Derek Abbott, Mohsen Dorraki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (LLMs) are increasingly adopted to interpret 12-lead ECG images, though the interpretations often lack validation. However, ECG image understanding significantly differs from general images as it depends on precise waveform morphology, lead relationships and accurate interval measurements. This study investigated whether zero-shot multimodal LLMs can reliably distinguish normal and abnormal ECG images and, in parallel, evaluated CNN-based models for clinically grounded references. Standard 12-lead ECG recordings were rendered as single-page images for a binary normal-abnormal classification task. Three prominent LLMs (GPT-5.2, GPT-4.1, and Gemini-2.5 Pro) were tested using a fixed zero-shot prompt across multiple runs. In parallel, a physiology-aware CNN-based model was developed with the capability to aggregate features from the predefined anatomical lead groups. The model was compared with ResNet18, DenseNet121, VGG16 baselines, and all the models were evaluated on an internal test set and external PTB-XL dataset. Across seeds, CNN-based models demonstrated stable discrimination, with average internal ROC-AUC of 0.92-0.94, and external ROC-AUC of 0.85-0.86. The proposed LeadGroupECG model significantly improved over its backbone internally without compromising external generalization. It remained competitive with other baselines, while consistently highlighting anatomical lead-group contributions. In contrast, zero-shot LLM discrimination remained near-chance (ROC-AUC around 0.5). The PR-AUC improved slightly when ECGs used a grid-based calibration background compared with the grid-free ECGs. Although multimodal LLMs can generate reasonable ECG narratives, their zero-shot diagnostic discrimination remains limited. Therefore, clinically framed, domain-specific architectures remain essential for AI-based ECG interpretation.

---


### 242. [Agent-as-a-Router: Agentic Model Routing for Coding Tasks](https://arxiv.org/abs/2606.22902)

**<font color=#1a73e8>作者：</font>** Pengfei Zhou, Zhiwei Tang, Yixing Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world users typically have access to multiple Large Language Models (LLMs) from different providers, and these LLMs often excel at distinct domains, yet none dominate all. Consequently, routing each task to the most suitable model becomes critical for both performance and cost. Existing routers treat this as a static, one-off classification problem. However, we identify the performance bottleneck for these routers as information deficit: simply augmenting a vanilla LLM router with performance statistics at the task-dimension level yields a 15.3% relative gain, surpassing a heuristic router built on the same dimension-level priors. Motivated by this finding, we propose Agent-as-a-Router, a framework that formalizes routing as a C-A-F loop (Context->Action->Feedback->Context). It closes the information gap by accumulating execution-grounded experience during deployment. We instantiate this framework as ACRouter, composed of an Orchestrator, a Verifier, a Memory module, and introduce CodeRouterBench, an evaluation environment comprising ~10K task instances with verified scores from 8 frontier LLMs, enabling regret-based router comparison on streaming tasks. Experiments show that ACRouter achieves the lowest cumulative regret on in-distribution tasks and generalizes to out-of-distribution agentic-programming tasks, demonstrating that our routing framework actively closes the information gap. Codes and benchmarks are released at this https URL.

---


### 243. [ThermoLLM: Thermodynamics-Aware HVAC Control with Spatial-Semantic Knowledge Graph](https://arxiv.org/abs/2606.22911)

**<font color=#1a73e8>作者：</font>** Kirtan Bhatt, Xiachong Lin, Matthew Amos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-zone HVAC control is a spatial decision problem in which indoor thermal evolution and control decisions depend not only on outdoor conditions and internal heat gains but also on zone layout, physical adjacency, and delayed thermal interactions across the building. Recent LLM-based HVAC controllers have shown that prompt-based control is feasible. However, these methods typically rely on task descriptions, observation values, short textual feedback, or unstructured retrieval, which limits their ability to reason about zone coupling, thermal response, and building dynamics. This paper presents a thermodynamics-aware LLM control framework for a five-zone EnergyPlus building simulation. The controller is grounded in a physics-informed spatial knowledge graph derived from Brick-style building semantics and linked with recent interaction history. At each control step, the model receives the current building state, graph-structured spatial context, and recent environment-controller history, enabling it to make decisions that reflect both building structure and short-term thermal evolution. We evaluate the framework against standard control baselines and several LLM-based alternatives. Results show that the proposed approach achieves the best overall energy-comfort trade-off and the lowest PMV violation while maintaining energy-efficient operation.

---


### 244. [Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving](https://arxiv.org/abs/2606.22913)

**<font color=#1a73e8>作者：</font>** Zisheng Chen, Yuping Qiu, Jianhua Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving by incorporating reasoning for better interpretability and planning quality. However, most existing approaches directly generate the final trajectory without explicitly examining its future consequences, which limits their reliability in complex and dynamic environments. To address this limitation, we propose IRR-Drive (Intend, Reflect, Refine), an adaptive multimodal reflection framework for autonomous driving. Specifically, to tightly couple high-level reasoning with physical constraints, IRR-Drive first generates a preliminary textual intention and anticipates potential interactions by predicting future semantic bird's-eye view (BEV) representations. This dual-modality (Text + BEV) reflection space explicitly models anticipated scene evolution, enabling the model to rigorously self-correct and refine its initial intent before generating the final trajectory. Furthermore, to balance planning performance and computational efficiency, we construct reflection-oriented training data and design an adaptive reflection reward, enabling the model to adaptively select its reasoning mode according to scene complexity. Instead of using reasoning primarily as an auxiliary interpretation, IRR-Drive directly integrates an adaptive reflection mechanism into the planning framework, enabling grounded, decision-aware trajectory correction that is driven by scene complexity. Our method achieves state-of-the-art performance on the NAVSIM benchmark in both PDMS and EPDMS. Extensive experiments demonstrate the effectiveness of our multimodal reflection framework and validate the efficacy of the proposed adaptive reflection strategy.

---


### 245. [Each Judge Its Own Yardstick: Discovering Per-VLM Taxonomies for Physical Video Evaluation](https://arxiv.org/abs/2606.22918)

**<font color=#1a73e8>作者：</font>** Yu Cao, Ziquan Liu, Zhensong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintaining physical consistency in video generators and world models increasingly relies on vision-language models (VLMs) as automated judges that provide reward signals, ranking decisions, and data-filtering criteria. Yet VLMs differ substantially in training data and architecture, encoding physical phenomena through distinct internal representations. A single global evaluation schema therefore gives every VLM the same axes of competence, regardless of what each can actually perceive. We propose JudgeFit, an iterative refinement procedure that discovers a per-VLM evaluation taxonomy. An initial taxonomy is constructed by prompting the target VLM to enumerate physics errors on a small set of videos and clustering the resulting descriptions. The taxonomy is then refined through a diagnostic step: we calibrate the VLM's per-dimension scores to human physical-commonsense ratings, diagnose which dimensions it scores unreliably or redundantly, and prompt an LLM to repair them, iterating until convergence. We further instantiate this procedure as a benchmark and apply it to 16 VLMs spanning eight model families. The refined taxonomy outperforms the global-schema baseline on held-out videos for every VLM tested, with a mean relative improvement of approximately 32%. Beyond aggregate accuracy, the per-VLM profiles expose model-specific blind spots that overall rankings cannot anticipate, with reliability patterns differing markedly across model families.

---


### 246. [MythraGen: Two-Stage Retrieval Augmented Art Generation Framework](https://arxiv.org/abs/2606.22924)

**<font color=#1a73e8>作者：</font>** Quang-Khai Le, Cong-Long Nguyen, Minh-Triet Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation has seen rapid advancements, especially with the development of generative models. However, challenges remain in achieving high-quality, contextually accurate image outputs that faithfully match the provided textual descriptions, especially in artistic generation. In this paper, we present a simple yet efficient retrieval augmented generation framework, namely MythraGen, for text-to-artistic image generation by integrating an art retrieval mechanism with LoRA-based model fine-tuning. Our method extracts features from a large-scale art dataset, optimizing the generation process by combining artist-specific styles and content. Particularly, retrieved images from an external art database that have the highest similarity to the query prompt are used to finetune Stable Diffusion using LoRA for desired art generation. Experimental results and user studies on the WikiArt dataset show that our proposed method can generate artworks that closely match the user's input, significantly outperforming existing solutions.

---


### 247. [FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training](https://arxiv.org/abs/2606.22932)

**<font color=#1a73e8>作者：</font>** Dikshant Kukreja, Kritarth Prasad, Avinash Anand 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. This two-phase schedule sets the memory ceiling of modern training: at the seam between the phases, every layer's gradient is live at once. We argue that this materialized gradient is an artifact of how differentiation is staged, not a quantity that learning requires -- and we eliminate it. FORGE folds the optimizer step into the backward pass and applies it one tile at a time, entirely in registers, so each gradient tile is consumed the instant it is produced and never becomes a tensor. The fusion changes only when the update happens, not what it computes: in full precision the fused step is provably exact -- the identical optimizer update, for every element-wise rule -- and that exactness survives tensor- and sequence-parallel sharding; in the bf16 and 8-bit regimes used in practice it is faithful rather than bit-identical, its deviation bounded and, for the weight store, rendered unbiased by stochastic rounding. Because each gradient tile is born and consumed in the same registers, it is never converted down to bf16 to be stored and read back; FORGE thus preserves the full-precision fidelity that both bf16 and 8-bit optimizers lose to that conversion. Nor is the method tied to one architecture or one optimizer: linear layers are ubiquitous, and FORGE reclaims the gradient memory of any of them under any element-wise rule. Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs.

---


### 248. [When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents](https://arxiv.org/abs/2606.22936)

**<font color=#1a73e8>作者：</font>** Aman Mehta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents can fail quietly: they settle on one reading of the evidence early, then spend the rest of the run defending it. We call this premature commitment. Final-answer scoring misses the failure mode because it sees only the answer, not whether the process has already collapsed to a stable path. We define representational commitment as cross-run hidden-state convergence at a fixed reasoning step, and use it as an early diagnostic of trajectory consistency. On Llama-3.1-70B running ReAct on HotpotQA, step-4 hidden-state similarity predicts downstream behavioral consistency (r = -0.35, partial r = -0.45), with a localized temporal and layer-wise signature. The signal replicates across Qwen-2.5-72B and Phi-3-14B, and on StrategyQA (r = -0.83). It does not track correctness: committed-wrong and committed-correct questions are not separable in activation similarity. That boundary is central to the claim. Commitment tells us whether an agent has settled, not whether it is right. A runtime monitor detects inconsistent trajectories from hidden states at AUROC up to 0.97 (0.85--0.88 under a stricter split), and a prompting intervention cuts behavioral variance by 28% against a token-matched control while leaving accuracy statistically unchanged. We also test whether the signal can route self-consistency compute; on a harder benchmark it helps only modestly and is matched by a simpler output-based baseline. The result is a diagnostic for a hidden process failure, with clear limits rather than a general accuracy lever.

---


### 249. [Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently](https://arxiv.org/abs/2606.22938)

**<font color=#1a73e8>作者：</font>** Stanley Wei, Juno Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have demonstrated that reinforcement fine-tuning of pretrained base models can lead to significant gains in reasoning performance at inference time. In this work, we theoretically analyze why reinforcement fine-tuning induces better reasoning ability than purely supervised fine-tuning (SFT) methods. We model chain-of-thought (CoT) reasoning as a pathfinding problem on graphs and compare the popular method of reinforcement learning with verifiable rewards (RLVR) against traditional SFT. We prove that SFT, when trained on golden shortest paths without negative examples, fails to learn how to efficiently backtrack. In contrast, an RLVR-trained model can learn how to efficiently backtrack from dead ends using only outcome reward. This leads to an exponential separation in inference-time compute between the two methods, and demonstrates that RLVR leads the model to learn the location of difficult decisions in a reasoning chain, ultimately allowing for better allocation of inference-time compute. Finally, we show that the reasoning traces of an RLVR model can be distilled to train a base model to backtrack efficiently as well.

---


### 250. [Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails](https://arxiv.org/abs/2606.22942)

**<font color=#1a73e8>作者：</font>** Xin Liu, Simin Ma, Shujian Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance across many tasks, but their high computational cost limits deployment in resource-constrained environments. Knowledge Distillation (KD) offers a practical solution by transferring knowledge from a teacher model of a larger size to a smaller student model. While prior work has mainly examined task-specific or small-scale settings, the post-training stage for building general instruction-following models has received limited attention. In this paper, we conduct a systematic study of KD in post-training using the large-scale Tulu 3 dataset. We find that KD outperforms supervised fine-tuning (SFT) in low-data regimes, but its advantage diminishes as more training data is added. Distilling from a stronger instruction-tuned teacher restores substantial gains even with abundant data, indicating that KD remains effective when the teacher provides knowledge that the student cannot easily acquire from the training data alone. We further study domain-specific, low-resource scenarios and propose a two-stage KD strategy that leverages synthetic teacher-labeled data followed by refinement on human annotations. This method consistently improves student performance, providing practical guidance for building compact models in data-scarce environments.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
