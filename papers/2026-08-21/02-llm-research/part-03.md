# 🧠 大模型相关研究 | 2026年08月21日

> 本类共 **166** 篇论文：已确认 **153** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-166](./part-04.md)

---

### 101. [DocClaw: A Unified Agentic System for Intelligent Document Processing](https://arxiv.org/abs/2608.18685)

**<font color=#1a73e8>作者：</font>** Siqi Xiang, Zhipeng Xu, Yufei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent document processing (IDP) encompasses a broad range of tasks, including optical character recognition (OCR), document question answering (DocQA), and key information extraction (KIE). Despite their distinct objectives, these tasks share a common need to perceive document content, acquire task-relevant information, and progressively refine intermediate results. However, they are typically formulated as separate prediction problems and addressed by task-specific models or processing pipelines. We introduce DocClaw, a unified agentic system that formulates diverse intelligent document processing tasks as a shared process of interaction between an agent and a document. Given a document and a task-specific query, DocClaw follows an appropriate document skill to iteratively identify the information required, invoke relevant tools, and integrate the resulting observations into the desired output. Throughout this process, a structured document state organizes reusable document knowledge and task-specific interaction context, allowing the agent to accumulate, revisit, and progressively refine information as the interaction proceeds. Under this formulation, task-specific requirements are captured by the agent's interpretation of the query objective and the corresponding document skill, while the underlying interaction loop, tool space, and document state are shared across tasks. Extensive experiments across multiple intelligent document processing benchmarks demonstrate that DocClaw effectively handles diverse tasks within a single agentic framework and achieves competitive performance compared with both general-purpose VLMs and task-specific methods.

---


### 102. [Improving LLM-Based SSH Honeypots Through Prompting and Fine-Tuning](https://arxiv.org/abs/2608.18686)

**<font color=#1a73e8>作者：</font>** Muris Sladić, Veronica Valeros, Eman Alibalić 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based SSH honeypots often use closed cloud LLMs because they give strong shell realism, but cloud models create deployment problems. These include no stable versioning, provider-side changes, attacker-driven cost, and model decommissioning. Local open-weight models avoid these problems, but they usually perform worse and make mistakes that reveal the honeypot. These mistakes include malformed outputs, command echoing, inconsistent filesystem state, and AI-style artifacts. This paper studies how to improve and evaluate the shell emulation accuracy of local LLM-based SSH honeypots using prompt design and supervised fine-tuning. We fine-tune and evaluate eight models in total: the original fine-tuned GPT-3.5 model used in shelLM and seven open-weight local models, each compared to its base model. We also test how prompt structure transfers across model families. Using 34 automated unit tests that measure shell emulation accuracy in single-session and fresh-session settings, we find that prompt design has a large effect and that fine-tuning depends on dataset coverage. Fine-tuning on the original 112-conversation dataset does not improve aggregate pass rate, while an expanded dataset built from honeypot logs produces clearly stronger local models. Taken together, the results suggest that prompting and fine-tuning can each improve local LLM honeypots on their own, but their effects do not combine straightforwardly, since strong rule-based prompting and supervised adaptation can also conflict by addressing overlapping shell-behavior constraints.

---


### 103. [Aslema at NADI 2026: Augmentation through Fewshot for SLU](https://arxiv.org/abs/2608.18689)

**<font color=#1a73e8>作者：</font>** Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Aslema, our system for NADI 2026 Shared Task 5, which consists of two subtasks: intent recognition and slot filling. We evaluate four omni LLMs in a zero-shot setting and compare them with fine-tuned models. Our results show that fine-tuning consistently outperforms zero-shot inference. We further explore synthetic data augmentation by using an LLM to generate culturally grounded Tunisian Derja utterances, followed by voice cloning to generate synthetic speech. Incorporating this synthetic data improves performance on both tasks. Our final submitted system, based on Qwen3-Omni-30B and trained with a mixture of original and synthetic data, achieves 86.8% intent accuracy and 34.7 WER on the devtest split. On the official test set it ranks 1st in slot filling (59.5 CoER) and 4th among 8 teams in intent recognition (66.1% accuracy). We release our experimental scripts and will soon share the synthetic dataset to support further research in this area.

---


### 104. [Impact of Iterative Fine-Tuning on Transcription Accuracy in Complex Historical Sanskrit Manuscripts](https://arxiv.org/abs/2608.18696)

**<font color=#1a73e8>作者：</font>** Kartik Chincholikar, Kaushik Gopalan, Mihir Hasabnis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digitizing the text from handwritten historical manuscripts is required to make them easily accessible, preservable, and to enable historical scholars to study them in new ways. Historical manuscripts, however, often exhibit complex heterogeneous layouts and non-standard appearance due to period-specific writing styles, page textures, camera noise, and other nuisance factors, making them difficult to perform OCR on. To tackle this challenge, we introduce a local traditional OCR pipeline, which can be iteratively fine-tuned on the target manuscript at the layout-level and the appearance-level. By adapting to the target manuscript distribution, the proposed Traditional OCR pipeline makes better predictions on subsequent pages, causing iterative reduction in human annotation effort, which is expensive and time-consuming as it requires historical domain expertise. Using this pipeline, we digitize text from three complex historical Sanskrit manuscripts and introduce a dataset with granular layout-level annotations, along with Unicode annotations in the standard PAGE-XML format. We demonstrate quantitative gains due to iterative fine-tuning of the proposed traditional OCR pipeline, and also benchmark the performance of leading Multi-Modal Large Language Models on the introduced Dataset. Code and dataset are available at: this https URL.

---


### 105. [MemFuse: Multi-Source Memory Fusion from Fragmented Observations](https://arxiv.org/abs/2608.18704)

**<font color=#1a73e8>作者：</font>** Chao Li, Yuanfa Li, Wenhao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on single-source textual histories. In realistic settings, however, relevant information is often fragmented across applications and devices, as well as across users and time, requiring agents to integrate dispersed observations into coherent episodic memories while preserving their source provenance. To address these gaps, we introduce **MemFuseBench**, a benchmark for *multi-source memory fusion*. MemFuseBench is built with a Scene-to-Sensor pipeline that synthesizes controllable scenarios into source-tagged observations, evidence-grounded questions, and adversarial distractors. It enables systematic evaluation of temporal reasoning, cross-source evidence fusion, and robustness to noise. We further propose **MemFuse**, a structured memory system that preserves source-level evidence in event-layer atomic memory and organizes related atomic events into cluster-layer fused memory within a causal fusion graph. During retrieval, MemFuse retrieves and organizes related evidence fragments while maintaining traceability to original source events. Experiments on MemFuseBench show that MemFuse achieves the best overall performance among the evaluated memory systems under all three LLM settings and consistently improves performance on questions requiring cross-source evidence fusion.

---


### 106. [Competence, Not Accuracy: A Diagnostic for Reference-Free Judge Gates in Skill Optimization](https://arxiv.org/abs/2608.18719)

**<font color=#1a73e8>作者：</font>** Chenle Chen, Yangbo Wei, Chao Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-space skill optimization adapts a frozen agent by evolving a natural-language skill document, accepting each candidate through a validation gate. Existing gates rely on verifiable rewards, confining these methods to tasks with an automatic verifier. Replacing the verifier with an LLM-judge gate would lift that restriction, but whether such a gate carries usable signal is untested. We ask a prior question: can we tell, before placing a judge in the loop, whether its scores separate correct from incorrect answers at all? We formalize a reference-free judge as a latent solver -- its verdict rests on agreement with whatever it would itself conclude, so its capacity to evaluate is bounded by its capacity to solve. The model yields a closed-form bound on discriminability (ROC-AUC) in the judge's competence $c$ and answer-space size $k$, a necessary condition $c > 1/k$, and the result that the marginal AUC is confounded by item difficulty while a within-question estimator is not. A non-intervening probe records judge scores on genuine optimization runs without altering any decision. We find discriminability at chance where competence sits near the floor and usable above it; that a judge's benchmark accuracy overstates the competence that matters; and, in a closed-loop study, that the screen predicts which kind of gating error occurs. The result is a cheap pre-deployment diagnostic for judge gates.

---


### 107. [Execution-grounded evaluation reveals hidden failures in language-model calculations for environmental science](https://arxiv.org/abs/2608.18726)

**<font color=#1a73e8>作者：</font>** Maohao Ran, Chendong Ma, Yanting Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for quantitative work in the environmental sciences, yet existing evaluations score only final answers, leaving calculation process unobserved. Here we introduce AtmosCoder-Bench, an execution-grounded benchmark that makes the calculation process visible. Built through a transferable semi-automated pipeline (436 problems, 3,910 variants, 7,029 graded quantities), every problem is validated to be unambiguous and human-solvable, with uniquely verifiable answers. We find that (i) multiple-choice formats inflate measured accuracy by at least 12 percentage points; (ii) many failures arise not from missing knowledge but from models failing to apply known formulas and constraints consistently throughout multi-step computation; and (iii) even frontier models remain weak when task-specific conditions invalidate familiar methods, often reverting to canonical solution patterns rather than adapting methods to the relevant physical regime, leaving expert oversight essential.

---


### 108. [CL4D: Contrastive Language-4D Pretraining for Vision-Language Reasoning in Dynamic Scenes](https://arxiv.org/abs/2608.18734)

**<font color=#1a73e8>作者：</font>** Kumal Hewagamage, Isuranga Senavirathne, Sasika Amarasinghe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D understanding and reasoning is a fundamental capability for embodied AI agents operating in dynamic physical environments. However, existing vision encoders are largely limited to static 2D images or 3D point clouds without temporal modeling, or to 2D videos that lack accurate geometric depth reasoning. Consequently, current approaches fail to jointly capture spatial structure and motion evolution in dynamic scenes. We present CL4D, the first foundational 4D vision encoder that directly operates on dynamic point clouds, trained with a contrastive learning objective to align spatio-temporal geometric representations with natural language descriptions. By learning a shared embedding space between text and 4D scene dynamics, CL4D enables zero-shot motion-to-text and text-to-motion retrieval in dynamic environments and serves as a foundational 4D vision encoder for downstream 4D vision-language tasks. Building on this encoder, we introduce 4DVLM, a 4D vision-language model that conditions language generation on dynamic geometric representations. 4DVLM is the first VLM designed to operate directly on 4D point clouds without relying on 2D images, 2D videos, or static 3D point clouds. We train CL4D and subsequently 4DVLM on a newly constructed dataset termed DynAction4D capturing diverse human motions across varying object interactions and scene environments. Extensive experiments across multiple 4D human action benchmarks demonstrate that CL4D achieves state-of-the-art performance, with improvements of approximately ~16.75% over prior methods. Furthermore, 4DVLM outperforms frontier video VLMs such as Gemini and GPT-5 even when these models are provided with RGB video sequences corresponding to the same scenes represented as 4D point clouds for 4DVLM.

---


### 109. [FedLNS: Leverage LayerNorm Signature Modeling to Mitigate Adversarial Manipulation in Federated LLMs](https://arxiv.org/abs/2608.18736)

**<font color=#1a73e8>作者：</font>** Kai Li, Jong-Ik Park, Carlee Joe-Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated training enables language models to learn from distributed private text, but the server cannot directly verify the local supervision or optimization process that produces each client update. A malicious client can therefore train on corrupted targets, introduce incorrect context-token associations, and degrade the global model through repeated aggregation. Such degradation can also increase the risk of unreliable or hallucinatory generation. We propose Federated Learning with Normalization Signatures (FedLNS), a server-side framework for lightweight malicious-update screening. FedLNS represents each client update through changes in trainable normalization-layer parameters and screens suspicious updates against a robust, history-aware cross-client reference. Because the signatures are extracted at the server from the returned local models, FedLNS requires no additional client-to-server parameter or metadata exchange compared to standard federated learning (FL) methods. After screening, the retained full-model updates can be aggregated using standard FL or another compatible aggregation rule. FedLNS requires no raw client data, trusted server dataset, labeled attack examples, or separately trained detector. Experiments on GPT-style, BERT-style, and LLaMA-style models trained from scratch with 200 clients show that, under 40% population-level target manipulation, FedLNS achieves lower test perplexity than the strongest of six baselines for all three architectures under both IID (independently and identically distributed) and non-IID data partitions.

---


### 110. [A Multi-Agent Platform for Automated Enterprise Analytics and Insight Generation](https://arxiv.org/abs/2608.18740)

**<font color=#1a73e8>作者：</font>** Manoj N M, Vijayakrishna S, Manjunath Srinivas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes a multi-agent framework built on CrewAI [1] for conversational business intelligence. Five specialized AI agents operate in a sequential pipeline to process natural language queries, retrieve and analyze data, generate visualizations via the Model Context Protocol (MCP) [2], and deliver actionable insights. The platform features a defense-in-depth security architecture for multi-tenant data isolation and a query parameterization mechanism for transforming conversational insights into reusable dashboard components. Evaluation across 300 end-to-end test cases spanning synthetic and production enterprise datasets demonstrates 95.3% functional accuracy, a mean response latency of 24 seconds, and a response quality score of 4.52/5.0 as assessed by an LLM-as-a-Judge framework, with a 93.0% hallucination-free rate, representing a 22.6 percentage point accuracy improvement and 20.2% quality gain over a single-agent baseline. Cross-model evaluation across four LLM backends and human expert validation confirm architectural generalizability and evaluator reliability. An ablation study confirms that the Data Analysis and Report Aggregation agents are the primary drivers of output quality.

---


### 111. [Metrics That Write Themselves: Evolving an Evaluator from Its Own Blind Spots](https://arxiv.org/abs/2608.18744)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Yanwei Cui, Guanghui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents improve quickly against a reliable automatic metric and stall without one, and the applications that need them most, report generation among them, are the ones nobody knows how to score. Can the metric write itself? Saying what makes an answer good is hard; pointing at something wrong with one is easier, so the metric we evolve is a pool of small Python operators that each flag a candidate for one named defect, or abstain, and vote. Asking a model for operators directly does not work: 183 candidates realise only 96 distinct behaviours, from one narrow region of an enormous space. EvalCEGAR instead borrows counterexample-guided abstraction refinement from program verification. It reads the pool as an abstraction and searches for a collision, two answers the operators score identically, one correct and one not. That pair, not a prompt, is the authoring request, and when a collision defeats every attempt the loop widens what an operator may read rather than resampling. On MBPP+ and HumanEval+, a sandbox whose hidden unit tests give exact ground truth, the loop writes a 55-line operator that closes 15.4% of the gap between flagging nothing and a perfect filter on 428 unseen tasks (+0.0065, p=0.0010) at a quarter of our best hand-written operator's flags. On the benchmark it never saw it matches that operator's effect exactly on a third of the flags. Six of eight runs admit such an operator and all six help out of sample; our 15 hand-written operators applied together as one filter lose accuracy. An LLM judge on the same information ties that delta on a nearly disjoint set of candidates, and charges a model call per candidate forever where the operator charges none.

---


### 112. [Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning](https://arxiv.org/abs/2608.18767)

**<font color=#1a73e8>作者：</font>** Shiyu Miao, Yunlong Mao, Zirui Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gradient matching attacks (GMAs) in LLM split learning (SL) rely on a critical yet underexplored assumption: the gradient exposed at the split interface is a faithful derivative of the client's full-label training objective. This gradient-objective consistency allows a curious server to recover private labels by searching for a sequence whose induced gradient explains the observation. We propose Gradient Mirage, a defense that breaks this consistency without discarding the optimization utility of the backward signal. Our key idea is to induce the adversary to solve a misspecified inverse problem, in which no plausible label sequence in the sequence space can explain the observed gradients. Concretely, Gradient Mirage achieves this by inducing inconsistency across three dimensions: objective, direction, and scale. Selective Autoregressive Supervision derives the exposed gradient from a masked surrogate loss rather than the full-label objective assumed by the attacker; Scale Blinding then applies randomized multiplicative rescaling, obscuring the gradient's natural magnitude; and Directional Privatization further randomizes the gradient direction while preserving its magnitude through the von Mises-Fisher (vMF) mechanism under a directional metric differential privacy guarantee. Crucially, utility is preserved: the Top segment still learns from all target tokens via Dual-Track Backpropagation, the exposed gradient remains informative since each supervised token retains its complete autoregressive context, and Bottom-Gradient Recovery restores the effective gradient for Bottom-segment optimization. Extensive experiments show that Gradient Mirage provides substantially stronger protection than existing defenses under comparable fine-tuning performance, achieving a better privacy-utility trade-off.

---


### 113. [Readable, Faithful, Used: Three Dissociable Properties of Demographic Identity in a Language Model](https://arxiv.org/abs/2608.18768)

**<font color=#1a73e8>作者：</font>** Fathin Difa Robbani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are widely used to simulate survey respondents, yet their answers are homogeneous and unfaithful to real inter-group differences. We ask where demographic group identity lives inside an LLM, how faithfully its geometry mirrors real inter-group opinion structure, and whether it uses what it encodes. Using representational similarity analysis against Pew ground truth over 169 demographic cells, we score 1,089 read-out locations in Mistral-7B and intervene causally across six attribute types. Four results. (1) The standard last-token residual read-out understates the model: attention-head read-outs dominate it in five of six types, with selection-corrected fidelity up to rho=0.63 -- roughly 70% of the measurement-reliability ceiling -- surviving a lexical-similarity control. (2) A single head (L11 H16) is significantly faithful in all six types as a fixed location, while race-based types stay weak and prompt-fragile. Both phenomena replicate -- the analogous head significant in five of six types, weakest on the same race type -- across three checkpoints of a second model family, where ten billion training tokens barely move the map. (3) Causal use does not follow fidelity: the clearest causal pathway sits in one of the least faithful types (p=0.002, cluster-robust, fixed depth), the most faithful type shows no correction-surviving single-layer effect, and replacing the entire identity moves predictions by under 2% of their error. (4) A 128-dimensional probe of the single head lands 21-31% closer to survey truth than the model's own answers -- yet recovers almost none of the per-question group ordering, no better than the answers themselves. Readable, faithfully arranged, and causally used are three dissociable properties of the same model; treating them as one claim is what keeps the "can LLMs simulate populations" debate unresolved.

---


### 114. [Decomposing Wrong-Consensus Agreement in LLM Self-Consistency: A GPT-4.1 Case Study](https://arxiv.org/abs/2608.18795)

**<font color=#1a73e8>作者：</font>** Lizhuo Zhang, Mengmeng Tang, Chenfeng Long 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Majority voting over multiple LLM samples is widely used to raise answer accuracy, yet its gain varies erratically: on hard questions it can even backfire. This paper gives a quantitative account of this failure. A pluralistic agreement index Gamma is defined as the expected fraction of the samples of a wrong run that agree with the consensus, normalized by a reference scale d=(1-p)/(C-1), and is decomposed into a mechanical component (what a vote delivers given only a per-case answer preference) and a preference-unexplained residual. The mechanical null is difficulty-matched and leak-free: each case is resimulated at its own accuracy and option preference, estimated from the case's other runs, so no run predicts its own agreement. On GPT-4.1 the decomposition shows benchmark-associated direction (an observational ordering over n=4 cells per benchmark, not a significance claim). On multiple-choice GPQA-Diamond, the per-case answer preference explains 81-93% of the held-out test-run agreement index: the shared-bias-dominates account over-claims here, because a wrong but attractive option the whole cohort latches onto is captured by the per-case preference channel (whether that preference is induced by shared training bias is not identified). On open-domain AIME, the mechanical preference explains only 59-78% (21-29% if shrunk to pure noise), and a preference-unexplained residual of 1.56-2.80 Gamma units survives, which a run-level preference-heterogeneity reference more than absorbs (1.4-2.1). A self-consistency backfire on hard questions is reproduced (binned voting gap down to -0.09, coupled CI [-0.12,-0.07]), and the highest-agreement bin reaches an accuracy of only 0.42-0.83, a 1.2-3.6x lift over base rate: agreement is graded evidence, not certification. No new voting method is proposed; code and evidence are committed and reproducible.

---


### 115. [Do Large Language Models Hallucinate Electric Fata Morganas?](https://arxiv.org/abs/2608.18816)

**<font color=#1a73e8>作者：</font>** Kristina Šekrst  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI hallucinations - that is, outputs which are made up, cannot be verified, or contradict the source material - are generally regarded as an engineering flaw to be dealt with. This paper contends that they also have philosophical significance when it comes to the question of machine consciousness. We examine the known causes of hallucinations in large language models - such as source-target divergence, discrepancies between training and inference, and overfitting - and we present two empirical investigations. In the first, we apply successive generations of the GPT model to ambiguous factual questions under different temperature settings, finding that higher temperatures result in plausible but incorrect answers while lower temperatures lead to factually accurate ones. The sampling parameters that cause a model to seem creative or spontaneous and thus more likely to pass behavioral tests of intelligence are the same ones that increase its hallucination rate. In the second, we look at an encoder-only model that has been trained on encyclopedic data and which answers questions of the same type factually and without embellishment, indicating that hallucinations are due to exposure to subjective and socially diverse training data rather than to the development of any cognitive ability. Using references to Turing, Searle's Chinese Room, the frame problem, and the cybernetic tradition of Wiener and Ashby, we claim that a model's self-reports of emotion or sentience come within the definition of hallucination, and that any future occurrence of machine consciousness might remain epistemically inaccessible since it would be indistinguishable from a sufficiently advanced hallucination.

---


### 116. [Identifying Implicit Premises for Logical Reconstruction of Argument Graphs](https://arxiv.org/abs/2608.18821)

**<font color=#1a73e8>作者：</font>** Xuyao Feng, Anthony Hunter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The logical reconstruction of argument graphs from natural language text is challenging because of the prevalence of enthymemes (i.e., arguments with implicit premises). There are natural language processing methods for identifying enthymemes in text, and there are symbolic methods based on abduction for identifying missing premises in a logical representation of enthymemes. However, there is a need for methods to generate implicit premises to logically show a known entailment or contradiction relationship between a pair of statements. To address this, we propose a neuro-symbolic pipeline that uses large language models (LLMs) to generate intermediate implicit premises that are translated into logical formulae and used with logical formulae representing explicit premises and explicit claims to show the logical relationships between them (entailment, contradiction, or neutrality). Our approach is evaluated on the Microtext Argumentative Corpus.

---


### 117. [MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models](https://arxiv.org/abs/2608.18827)

**<font color=#1a73e8>作者：</font>** Chenglin Liu, Xun Wang, Ruishuo Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward function design remains a bottleneck in reinforcement learning. While large language models (LLMs) have enabled automated reward generation, existing methods generate and revise reward functions as monolithic programs, making it difficult to reliably preserve and reuse effective components discovered in earlier iterations, leading to unstable performance across iterations. To address this, we propose Module Level Reward Evolution Framework (MLREF). At the core of MLREF is a module pool, a persistent repository of reusable reward components. MLREF treats the module pool as the primary optimization object: the pool evolves across iterations by accumulating successful modules, refining underperforming ones, and reusing proven components; while reward functions are constructed as linear combinations of modules drawn from this pool. To drive this evolution, MLREF integrates three mechanisms: reflection-based refinement, hybrid credit assignment, and a merge strategy with rollback, which together improve the effectiveness and robustness of reward optimization. Experiments on 17 tasks show that MLREF outperforms strong baselines by 25.2% in locomotion and 6.6% in manipulation, with more stable optimization dynamics.

---


### 118. [EVADE: Evidence-Verified Agentic Diagnosis with Escape](https://arxiv.org/abs/2608.18833)

**<font color=#1a73e8>作者：</font>** Mohaimenul Azam Khan Raiaan, Nur Mohammad Fahad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) can achieve high accuracy but remain unreliable: they are systematically overconfident, benefit little from test-time reasoning, and lack the ability to reliably calibrate trust in their own responses. We introduce EVADE (Evidence-Verified Agentic Diagnosis with Escape), an inferential, non-training method that enhances the safety of deploying a single frozen VLM. EVADE responds and, when uncertain, localises the region most diagnostically relevant, re-answers on a zoomed view, and commits only when both the entire image and the zoomed view responses agree; otherwise, it abstains. To directly address verification hallucination in single-model self-checking, our main idea is to verify gate consistency across different image views rather than re-reading the model's own text. Experimental evaluation on VQA-RAD, SLAKE, and PathVQA using Qwen2.5-VL-7B reports that EVADE is the only method that simultaneously improves both calibration and selective risk while maintaining accuracy, reducing expected calibration error (ECE) by up to 45% compared to zero-shot. Chain-of-thought, self-consistency, and self-verification all fail at least one axis. A grounding analysis reports that self-proposed regions perform better at diagnostic structure localisation than centres or random crops. However, a 7B VLM cannot use this localisation to revise answers. Therefore, reliability gains come from the consistency gate and calibrated abstention.

---


### 119. [Verifiable abstention makes AI leak diagnosis accountable in water distribution networks](https://arxiv.org/abs/2608.18836)

**<font color=#1a73e8>作者：</font>** Tianwei Mu, Yue Wang, Mingzhe Yuan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Utilities lose a substantial share of treated water to leakage, yet rarely trust artificial-intelligence localizers to dispatch crews: guessing everywhere cannot justify excavation. The gap is accountability, not accuracy: no method proves when it should not act. Here we recast leak localization as decision-making under verifiable abstention. A physics-grounded executor agent falsifies hypotheses (leak, demand, sensor, valve) against a digital twin; an independent supervisor agent, with a large-language-model (LLM) auditor, checks evidence against a code-verifiable contract, then certifies a dispatch, requests evidence or abstains. Under field-grade noise, a 32% forced baseline becomes 96% decision precision on acted events. On an independently generated benchmark it acts on only 4 of 33 leaks, all correct. A 194-event register of audited real leak locations with twin-simulated pressures and flows yields five excavation dispatches, three correct, and 44% survey recovery at full district precision. Accountable abstention offers a defensible route to autonomous water-infrastructure operation.

---


### 120. [ORBITER: Conflict-Aware Decision-Making for Agentic Last-Mile Delivery](https://arxiv.org/abs/2608.18846)

**<font color=#1a73e8>作者：</font>** Mingzhao Li, Chenxi Liu, Yan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Last-mile delivery aims to handle dynamically arriving orders with couriers while modeling complex spatial and temporal correlations. Recent learning-based methods model spatiotemporal dependencies among orders to predict courier service sequences, but leave next-order decision making unexplained. Describing the current delivery state in language allows LLMs to reason explicitly about the spatial, temporal, and behavioral cues behind an individual decision. As direct predictors, however, LLMs remain sensitive to task presentation and often produce unreliable decisions. To address these challenges, we introduce ORBITER, an agentic Order Arbiter for next-order decision-making in last-mile delivery. ORBITER models courier service through decision points, each containing the courier's spatiotemporal state and visible orders and exposing local trade-offs for modeling and verification. Fixed proposers rank the candidates, and a structured report identifies where their rankings disagree. The LLM uses task-specific tools to gather evidence on the leading alternatives, while an independent critic checks the resulting decision against that evidence. We conduct extensive evaluations on data in four cities, where ORBITER outperforms existing state-of-the-art baselines by up to 9.2% on average showing its effectiveness.

---


### 121. [DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning](https://arxiv.org/abs/2608.18878)

**<font color=#1a73e8>作者：</font>** Zijie Meng, Xiwei Dai, Yixuan Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Oral diseases affect billions of people worldwide, underscoring a pressing need for accurate and reliable dental assessment that integrates heterogeneous evidence from domain knowledge, radiographs, intraoral photographs, and 3D dental data. Most existing dental AI systems remain modality- or task-specific. Although recent vision-language models support flexible dental question answering, directly generated response leaves evidence implicit and untraceable. To address these limitations, we introduce DentAgent, an evidence-centric multi-agent framework, in which the Orchestrator coordinate five specialized agents spanning various modalities. Each specialist utilizes domain tools to convert observations into structured evidence records. The Evidence Blackboard manages these records as a shared evidence state, tracking coverage, gaps, and conflicts before response generation. This standardized evidence representation integrates isolated dental capabilities into a unified agentic workflow. Across four benchmarks, DentAgent demonstrates leading performance, even surpassing the senior specialists by 17.3 percentage points on multi-label diagnosis, which supports its value for broadly applicable and traceable multimodal dental reasoning, and highlights its potential as a technical foundation for population oral health assessment and management.

---


### 122. [Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models](https://arxiv.org/abs/2608.18884)

**<font color=#1a73e8>作者：</font>** Wei Yu, Suxing Liu, Minjie Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning training of reasoning LLMs (e.g., GRPO) is expensive and requires a controllable environment, committing every contribution to a full training pipeline. We present EvoResearcher, a training-free, inference-time protocol that adds cost-bounded self-reflection to a single frozen LLM backbone. The protocol iterates generate -> self-critique -> revise until a maximum depth D is reached or the critique returns the CONFIRMED sentinel, an implicit early stop that lets the backbone self-verify its answer under a strict compute budget. Four self-reflective meta-reward components (correctness, efficiency, reflection depth, tool-call diversity) act as design principles instantiated as prompt-level mechanisms, so their benefits accrue with zero gradient updates. We validate the protocol on Big-Bench Hard (100 questions) and establish cross-domain behavior on GSM8K (500) and MATH (500) on the same frozen backbone, with cross-model replication on Qwen2.5-72B. All experiments use pure-reasoning benchmarks; the tool-call diversity component is validated in prompt-level form, and the environment-level and multi-agent extensions are design blueprints left to future work. On clean BBH the protocol does not raise accuracy beyond the 95% Wilson interval; its value is cost-bounded self-verification, with the CONFIRMED early stop terminating 82-88% of items at equal accuracy (about 2.1 generations per question).

---


### 123. [Assessing Quality of Experience in Natural Language Generation of German Text](https://arxiv.org/abs/2608.18888)

**<font color=#1a73e8>作者：</font>** Dinh Nam Pham, Shushen Manakhimova, Vivien Macketanz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Natural Language Generation (NLG) has made the reliable evaluation of generated text increasingly critical, as these systems, such as large language models (LLMs), are now widely deployed in real-world applications. However, traditional automatic metrics fail to capture the multifaceted nature of perceived quality. In this paper, we introduce TextQ-German, a novel dataset suite for human-centered evaluation of German NLG from a Quality of Experience (QoE) perspective, covering automatic text summarization and machine translation. Through crowdsourcing studies with German speakers, we collect human quality ratings and identify relevant perceptual quality dimensions for each task. We develop automatic QoE prediction models, including transformer-based, linguistic feature-based, and hybrid approaches. Hybrid models outperform pure transformer baselines in almost all experimental settings, while linguistic features alone can approach the performance of fine-tuned language models. The dataset is extended with LLM-generated outputs annotated with overall QoE scores. Final validation on held-out sets indicates generalization to unseen data. Our work contributes a publicly accessible resource for NLG evaluation and baselines for automatic QoE prediction, providing a foundation for developing NLG systems that better align with human quality perception.

---


### 124. [Converting Expert Deliberation into Financial Signals Through A Context-Aware NLP Pipeline](https://arxiv.org/abs/2608.18911)

**<font color=#1a73e8>作者：</font>** Vivek Batra, Kristin Chen, Sanjiv Das 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the CDSP (context-conditional deliberation signal pipeline), converting an investment committee's meeting transcripts into structured predictive features. CDSP segments the meeting transcripts into topical chunks, assigns asset-class context labels using a large language model (LLM), maps financial keywords to a pre-determined taxonomy of labels, and constructs complementary features: sentiment polarity and mention frequency. This feature engineering framework is applied to a dataset spanning 48 monthly committee meetings to predict if global equities will perform better or worse than global bonds in the following month. In experiments with engineered features, raw transcript text, sentence embeddings, and combined representations, the prediction accuracy ranges from 62% to 73%, compared to always choosing stocks, which outperforms bonds 60.4% of the time. The best (73% accurate) model combines sentence embeddings with engineered CDSP features, achieving a 0.73 F1 score (although this is not statistically significant compared to always choosing stocks). Sentiment carries a stronger signal than mention frequency for several taxonomy categories. These findings suggest that experts' deliberations may contain forward-looking information that context-aware NLP can extract.

---


### 125. [SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance](https://arxiv.org/abs/2608.18921)

**<font color=#1a73e8>作者：</font>** Jian Yang, Zhenqi Feng, Zhaoyang Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing LRM-DoS methods rely heavily on model feedback to synthesize attack queries, requiring either repeated queries to the target model or training a dedicated attack model. These expensive operations severely weaken attack leverage. In this paper, we propose \emph{search amplification}, a novel, model-feedback-free LRM-DoS paradigm. It employs the conflict count derived from an Satisfiability Modulo Theories (SMT) solver as a low-cost external signal to guide the synthesis of inference-heavy Constraint Satisfaction Problem (CSP) instances. Our key observation is that LRMs depend on trial-and-backtracking search when solving CSPs, where higher SMT conflict counts on a given CSP instance positively correlate with more extensive LRM backtracking search and substantially longer output trajectories. Building on this finding, we propose \textsc{SMTrap}, a lightweight, CPU-only framework. Guided by SMT conflict counts, \textsc{SMTrap} generates inference-heavy CSP queries without model queries, attack-model training, or GPU computation. Evaluations across seven frontier models demonstrate the state-of-the-art LRM-DoS capability of \textsc{SMTrap}, producing DoS effects multiple times stronger than existing baselines. To mitigate the threat of \textsc{SMTrap}, we demonstrate a tool-based mitigation that significantly cuts token usage.

---


### 126. [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](https://arxiv.org/abs/2608.18931)

**<font color=#1a73e8>作者：</font>** Davide Romano, Kanak Raj, Jerrod Parker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) improves language model outputs by spending additional inference compute - generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine, law, finance, general chat, and creative writing - grounded in a unified framework that decomposes the effectiveness of each method's token budget into exploration and exploitation. The answer depends on which side of that decomposition you examine. Scaling exploration works: the best candidate in the pool improves steadily with compute across all settings. What breaks is exploitation - the step that converts a rich candidate pool into a final output. With state-of-the-art generators, reward models correlate at only $\rho_v \approx 0.12$ with true quality, rendering selection near-random regardless of budget. Tree search amplifies this failure through diversity collapse. Refinement helps on one of five benchmarks; its apparent gains elsewhere are confounded. Only synthesis across candidates (Fusion) consistently improves over single-sample baselines, yet still recovers only ~40% of available quality. The candidate pool is not the bottleneck - choosing from it is.

---


### 127. [Graphical Design of Interpretable Architectures](https://arxiv.org/abs/2608.18936)

**<font color=#1a73e8>作者：</font>** Pietro Barbiero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing, implementing, and comparing interpretable architectures requires a formal language to represent them. The most common representations fall short in one of two ways. Symbolic equations give no global view of an architecture at a glance. Probabilistic graphical models and flowcharts do not describe actual tensor manipulations, thus hiding key insights and limiting reproducibility. To close this gap, we introduce a graphical notation for designing interpretable AI architectures, adapted from Penrose tensor notation. This graphical notation gives a global view of an architecture and maps one to one onto PyTorch einsum code. We first use this notation to describe architectures that are interpretable by construction, including concept bottlenecks, sparse probes, prototype networks, neural additive models, and mixtures of linear models. We then diagram the key architectural components of Steerling-8B, a frontier interpretable language model. The diagram yields global insights into the architecture (e.g., showing that Steerling is a residual model), a geometric interpretation of each individual operation, and a direct translation into 33 lines of PyTorch code.

---


### 128. [MedUAG: Unified Understanding and Generation for Medical Multimodal Models](https://arxiv.org/abs/2608.18937)

**<font color=#1a73e8>作者：</font>** Zijie Meng, Yuncheng Zhang, Hualiang Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent Multimodal Large Language Models (MLLMs) are rapidly evolving into unified understanding and generation (UAG) frameworks. However, extending these unified paradigms to the medical domain is hindered by: the absence of comprehensive training and evaluation benchmarks, and the lack of broadly validated unified medical model. To address these gaps, we present a comprehensive foundation for medical UAG. First, we construct MedUAGCorpus, the largest unified medical understanding and generation dataset to date, comprising over 6 million instances across 14 imaging modalities. Second, we introduce MedUAGBench, a systematic benchmark that expands medical generation evaluation to 12 diverse tasks under standardized protocols. Finally, leveraging these resources, we develop MedUAG, an end-to-end trained unified medical model. Extensive experiments demonstrate that MedUAG achieves strong performance across a wide array of understanding and generation tasks, establishing a competitive baseline and paving the way for next-generation medical multimodal systems.

---


### 129. [Breaking the weakest link to evade vision language models](https://arxiv.org/abs/2608.18938)

**<font color=#1a73e8>作者：</font>** Ilan Zini, Boussad Addad, Katarzyna Kapusta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment. In this work, we investigate the vulnerability of VLMs to adversarial perturbations applied to visual inputs and study two attack settings: untargeted attacks, where the goal is to disrupt the model's interpretation of the original image, and targeted attacks, where the adversary aims to force the model to generate a specific semantic description unrelated to the original image. To efficiently generate adversarial examples, we propose a gradient-based attack method that performs optimization exclusively on the vision encoder of the VLM rather than on the entire multimodal architecture. This design significantly reduces the computational cost and resource requirements of the attack while maintaining strong effectiveness. We evaluate our approach on several open-source VLMs, including Qwen2.5-VL, Granite-Vision, FastVLM, and Phi-3.5-Vision, and show that small, human-imperceptible perturbations can substantially alter the textual interpretation produced by the models. Our findings highlight the vulnerability of modern VLMs to adversarial manipulation and emphasize the need for improved robustness and security mechanisms in multimodal AI systems.

---


### 130. [Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis](https://arxiv.org/abs/2608.18940)

**<font color=#1a73e8>作者：</font>** Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions. We compile CREED-CCV-2+USPTO-XL, an ultra-large-scale dataset of ~45.6 million verified reactions to train the C3LM (Chemistry Constraint-Consistent Language Model). By integrating fine-tuning with ChemCensor-based and novelty-oriented rewards, our model achieves state-of-the-art performance on the OOD URSA-expert-2026 benchmark. Further analysis of reaction uniqueness shows that LLMs and conventional models explore complementary reaction spaces, motivating ensemble-based retrosynthesis systems. Overall, our results establish Top-K, plausibility-aware training as a practical new direction for robust future LLM-based synthesis planning.

---


### 131. [Uncertainty-Aware Art-Historical Dating with Vision-Language Models](https://arxiv.org/abs/2608.18984)

**<font color=#1a73e8>作者：</font>** Stefanie Schneider, Peter Bell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Museum and archival datasets do not mirror historical artistic production, but materialize the contingent histories of collecting, preservation, cataloging, and digitization. This has direct consequences for interpreting pretrained image representations: they may appear to encode historical time while actually encoding the institutional conditions under which objects become visible as data. We describe this phenomenon as temporal entanglement and investigate it by formulating artwork dating as an uncertainty-aware regression task over frozen image embeddings. We evaluate several pretrained vision models on a temporally controlled Wikidata corpus of artworks. Our results show that these models contain usable temporal information, with Vision-Language Models (VLMs) outperforming purely visual self-supervised baselines. However, a qualitative analysis indicates that this temporal knowledge is shaped by various biases.

---


### 132. [DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering](https://arxiv.org/abs/2608.18988)

**<font color=#1a73e8>作者：</font>** Xujia Wang, Yizhe Zhang, Bin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieve-then-generate pipelines are commonly used to produce deep-research answers for open-ended questions, but retrieval alone is insufficient: LLMs must organize noisy and fragmented evidence into comprehensive, well-cited answers. We refer to this process as evidence synthesis. However, direct generation often underuses evidence, misaligns citations, and collapses diverse information into shallow summaries, exposing an evidence synthesis gap between retrieval and generation. Thus, we propose DeepWeaver, a novel framework that weaves noisy retrieved evidence into comprehensive answers by maintaining Thought Block Chains (TBCs), a structured representation that groups claims, salient information, keywords, and supporting evidence. DeepWeaver uses subordinate TBCs to inspect residual evidence, commit TBC revisions, and discover new claims before final generation. We evaluate DeepWeaver on open-ended QA over both knowledge bases and the web, and introduce LoQA, a high-density benchmark for evidence synthesis. Across multiple LLMs, DeepWeaver improves content sufficiency, citation grounding, and detail preservation on LoQA, while achieving deeper insights and higher citation quality on DeepResearch Bench. These results show that evidence weaving is an effective mechanism for bridging retrieval and generation in open-ended QA. Our code is available at this https URL.

---


### 133. [ForeSightGuide: An Anticipatory Framework toward Accurate and Low-Redundancy Guidance for the Visually Impaired](https://arxiv.org/abs/2608.18993)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang, Xu Li, Shikang Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electronic travel aids are pivotal for the independent mobility of the visually impaired. While Vision-Language Models (VLMs) offer rich environmental understanding, they often suffer from excessive false positives in dynamic scenarios, leading to cognitive overload. To address this, we present ForeSightGuide, an anticipatory assistive guidance framework that couples semantic scene understanding with predictive hazard assessment. Unlike reactive systems, ForeSightGuide leverages the reasoning capabilities of VLMs to anticipate obstacle motion, effectively filtering out non-threatening objects to provide concise, actionable guidance. To validate our approach, we introduce a novel dataset captured in complex, dynamic real-world traffic scenes, designed to benchmark predictive capabilities. Extensive experiments on both public benchmarks and our proposed dataset demonstrate that ForeSightGuide achieves state-of-the-art performance. Notably, it significantly mitigates information overload by reducing redundant alerts to 0.299 per guidance output while maintaining a low missed-hazard rate of 0.112, proving its efficacy for safe walking assistance.

---


### 134. [TractorBeam: Personalized AI Sensemaking Support via Collaborative Machine Annotation](https://arxiv.org/abs/2608.18994)

**<font color=#1a73e8>作者：</font>** Sireesh Gururaja, Jordan Taylor, Emma Strubell  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Language model-based systems which allow asking questions of documents have become popular tools for sensemaking. Despite their implied capability, these systems still suffer from issues of factuality and provenance, while encouraging confirmatory, rather than exploratory, research. We present TractorBeam, a browser extension-based mixed-initiative system that uses collaborative annotation as an interface metaphor for sensemaking, re-framing language model (LM) outputs as suggested highlights in a process that we call \textit{collaborative machine annotation}. This metaphor allows us to present LM results in-context on PDF documents, directly addressing concerns of provenance and factuality, while allowing users to iteratively construct mental schemas and queries for language models directly in the context of a document. In a preliminary user study, all of our participants felt that TractorBeam enabled them evaluate and iteratively improve the model's reflection of their intended highlighting, and several found suggestions that made them reconsider their original schema. TractorBeam suggests that systems that facilitate exploratory research on individual documents may lead to verifiable sensemaking for users and complement tools that work across broader corpora.

---


### 135. [Mise-en-Scène: Implicit Layout Emergence in Diffusion Transformers for Human-AI Design Co-Creation](https://arxiv.org/abs/2608.19000)

**<font color=#1a73e8>作者：</font>** Zipeng Xu, Ryan Murdock, Umberto Michieli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating graphic design synthesis from user-provided elements requires both a coherent overall composition and the exact preservation of each asset. Existing methods predict a layout as explicit bounding-box coordinates with a language model and then paste the assets into it, which separates spatial planning from visual synthesis and tends to produce rigid, mis-scaled compositions. We instead ask whether the layout can emerge implicitly inside a pretrained image-editing diffusion transformer. We present Mise-en-Scène, a two-stage framework. In the first stage, a diffusion transformer adapted with a small, knockout-selected LoRA drafts a complete design in which the arrangement of the elements emerges jointly with the rendered canvas. In the second stage, a deterministic match-and-place step moves the original high-resolution assets to the drafted positions, which guarantees exact asset fidelity and yields an editable, layered design that a designer can keep refining rather than a flat image. Notably, a minimal adaptation of the pretrained transformer already suffices, without the specialized conditioning machinery commonly introduced for multi-element generation. On the large-scale PrismLayersPlus benchmark, the designs produced by Mise-en-Scène are the closest to the ground truth in perceived quality among all compared methods, by a wide margin over both an LLM layout planner and a specialized layout transformer, while our match-and-place stage bridges the remaining fidelity gap to the ground-truth composites.

---


### 136. [A Theory of Post-hoc Debate Judgement](https://arxiv.org/abs/2608.19002)

**<font color=#1a73e8>作者：</font>** Xiang Yin, Adam Dejl, Antonio Rago 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Debates have recently emerged as a useful methodology for agentic AI to improve performance as well as to aid explainability and user engagement. For example, LLM-empowered agents may debate internally (with themselves) and/or externally (with other agents). In many settings where debates are used, debates' outcomes and resulting outputs are determined post-hoc by external judges, often LLMs. In this paper we develop and test a novel theory of debate judgement applicable to all settings where agents engage in debates by providing pros and cons for their opinions therein. Specifically, we identify a number of formal properties that debate judgement may be required to satisfy in general, as concerns reproducibility, robustness, groundedness and explainability. Then, we explore their satisfaction formally and/or experimentally, for claim verification settings, for two specific alternative debate judgement methods: variants of the LLMs as a judge idea and formal semantics drawn from computational argumentation. We show that the two methods give similar accuracy performances but the former may lack formal guarantees that the latter brings. Overall, our study indicates argumentation semantics as an ideal candidate for principled judges in debate-driven AI.

---


### 137. [Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning](https://arxiv.org/abs/2608.19009)

**<font color=#1a73e8>作者：</font>** Yajie Yin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly paired with verifiers (step checkers, self-consistency filters, tool-based fact checkers, formal proof assistants) that claim to detect the model's errors. Yet the verification literature uses the word "level" to mean at least five different things: verification granularity, concept abstraction, risk tier, system-stack layer, and the epistemic source of the ground truth. We propose Verification Autonomy Levels (VAL), a meta-standard classifying verification schemes along a single axis: where does the verification spec come from, and what does the verdict guarantee? VAL ranges from L0 (LLM self-declaration, no deterministic anchor) through L2 (objective ground truth, correctness only) to L3/L4 (decidable systems with single-property or domain-level completeness), with L5 impossible in the unrestricted case. Central to VAL is the completeness blind spot: substitution- and sampling-based verifiers can confirm that proposed candidates hold, but cannot prove that no candidate was missed. We further identify a dichotomy the literature has not stated: completeness is reachable only for formally specifiable properties, while empirical open-world verification (fact-checking, diagnosis) caps at anchored correctness (L2). We document this across four domains (symbolic mathematics, behavior monitoring, medical diagnosis, and code generation) and in the strongest existing formal-verification baseline, whose authors note the verifier "focuses on the correctness of each step." We show the levels of granularity, concept hierarchy, risk, and system stack are orthogonal to VAL, resolving a systematic conflation across 17 surveyed papers. Code and full assessment are released as supplementary material.

---


### 138. [From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation](https://arxiv.org/abs/2608.19011)

**<font color=#1a73e8>作者：</font>** Sepehr Ghaffarzadegan, Boubakr Nour, Makan Pourzandi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mechanisms for dynamically converting cyber threat intelligence (CTI) into actionable detection capabilities are necessary due to the rapid evolution of Advanced Persistent Threats (APTs). Sigma rules are an essential part of contemporary threat detection workflows because they offer a platform-independent framework for expressing detection logic that can be converted into particular queries across SIEM systems. Conventional techniques for manually crafting Sigma rules are prone to mistakes, and necessitate extensive knowledge, which restricts their scalability. Although there are open-source and industry-maintained Sigma rule repositories, they often fail to keep pace with emerging threats and require frequent customization to fit diverse operational environments. This emphasizes the necessity of dynamic rule generation that is adapted to evolving attack techniques as well as particular use cases. In this work, we design AUTOSIGMA, an automated solution for transforming unstructured CTI reports into relevant Sigma rules. Rather than relying solely on language models, AUTOSIGMA leverages a structured knowledge base to enrich partial inputs, matches the enriched content against a repository of existing Sigma rules, and then employs an LLM-as-a-Judge mechanism to iteratively validate the rules. By combining knowledge-driven enrichment, template-based rule grounding, and a multi-stage solution, AUTOSIGMA enables accurate, context-aware, and relevant rule generation. Evaluations across multiple real-world APT reports and multiple security blogs demonstrate that AUTOSIGMA outperforms alternative solutions and LLM models in rule validity, rule relevancy, MITRE ATT&CK technique coverage, and robustness to input quality.
AUTOSIGMA's Demo: this https URL

---


### 139. [Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models](https://arxiv.org/abs/2608.19025)

**<font color=#1a73e8>作者：</font>** Valentin Romanov, Monique Bax, Steven Niederer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) to extract highly contextualized information. We demonstrate four escalating workflows, 1) given an expert curated prompt and research articles, most frontier LLMs perform well at data extraction, however can struggle with interpreting scientific context and nuance, 2) given simple instructions, LLMs can author their own prompts which were almost as eNective as expert-written prompts, 3) autonomous discovery of research literature was diNicult, agents either missed or hallucinated references, and 4) LLMs can create new datasets from published guidelines that closely match human-expert judges, but still require a human-in-the-loop. Together, these findings define an auditable division of labour in which experts specify the evidence standard, models cross-check repeated extractions and researchers resolve disputed cases, providing a practical route to scaling scientific data curation without relinquishing expert oversight.

---


### 140. [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](https://arxiv.org/abs/2608.19066)

**<font color=#1a73e8>作者：</font>** Yechan Park, HyunJin Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displacement of the camera mount can reduce the success rate on the LIBERO benchmark from about 90% to about 10% in the worst case. Prior approaches, such as large-scale fine-tuning or generative data augmentation, are computationally expensive and risk catastrophic forgetting. To address this, viewpoint shifts are reformulated as a localized novel-view synthesis problem. Under a Locality assumption, that camera perturbations remain within a small bounded region relative to the workspace, viewpoint normalization reduces to a scene- and policy-independent disocclusion task. Our work implements this idea with a 4M-parameter 3D-Gaussian canonicalizer prepended to a frozen VLA policy. Without modifying policy weights, GS-VLA improves performance across three orthogonal axes: (1) Policy architectures, (2) Unseen task suites, and (3) Perturbation scales. These results show that a lightweight visual module can recover a large fraction of the performance lost under viewpoint shift, without policy retraining.

---


### 141. [What is Missing from AI Post-Training AI: An Empirical Analysis](https://arxiv.org/abs/2608.19072)

**<font color=#1a73e8>作者：</font>** Joy Jia Yin Lim, Xin Huang, Hao Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-AI. We argue that this picture conflates two distinct capabilities: execution-level capability, iterating within a selected training strategy; and strategy-level capability, revising the high-level judgment as experimental evidence accumulates. Analyzing a large corpus of publicly released post-training trajectories, we find that across different tasks, the agent's training strategy is locked in at the very beginning, and the entire remaining budget is spent on local adjustments within the selected strategy. We then examine three natural explanations--missing experience, missing guidance, and insufficient reasoning--with escalating interventions. Extensive experiments show that (1) an experience-driven scaffold improves execution across the board (+12.6 points on GSM8K and +40.8 on HumanEval) but leaves the strategy static; (2) human guidance effectively redirects the initial strategy, yet the agent falls back into local adjustment loops once training starts; and (3) additional inference compute pays off on easier tasks but yields almost no gain on the hardest one. In conclusion, what agents lack is neither experience, guidance, nor reasoning compute, but a mechanism for spontaneously reevaluating their strategy during execution.

---


### 142. [ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2608.19075)

**<font color=#1a73e8>作者：</font>** Jihae Jeong, Junha Choi, Hwanjo Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) often hallucinate, generating content that the input image does not support. Preventing such content during decoding calls for a candidate-specific measure of how strongly the image supports the token under consideration. The model's visual-token states offer a natural source of this evidence because projecting each state through the output head reveals which vocabulary items that position favors. These position-wise readouts cannot be pooled directly because their probability magnitudes are not comparable across visual positions. Vocabulary ranks provide a scale-invariant basis for pooling, but tokens still differ systematically in their typical rank-based evidence. We propose ReWEIGH, a training-free decoding intervention that aggregates these ranks across visual positions and compares each candidate with a token-specific reference estimated from unlabeled images. At inference, ReWEIGH caches the image evidence during prefill and applies a bounded penalty only to candidates that fall below their reference. On four 7B backbones, ReWEIGH reduces hallucinated object mentions by up to 21.3% while largely preserving or improving descriptive and general performance. With evidence cached, the average added latency is 1.33% per token, and the reductions extend across six architecture families to 32B parameters.

---


### 143. [When Readability and Source Retention Diverge: An Evaluability Gap in AI Translation](https://arxiv.org/abs/2608.19083)

**<font color=#1a73e8>作者：</font>** Chenchen Mao, Hanjing Shi, Haiyan Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Readable AI output can leave an evaluability gap: even when the source is shown, an overall-quality judgment may not reflect what an output preserves. We investigated how source-text condition and output rendering relate to perceived translation quality, and how output and system appraisals relate to trust and stated disclosure willingness in a plain-text interface. A focal 2 * 2 comparison (N=306) using TransLingo examined simple generated narratives and complex literary-philosophical prose alongside LLM-generated readability-oriented outputs and researcher-revised fidelity-oriented outputs. A descriptive stimulus audit indicated greater source retention in fidelity-oriented outputs in both source-text conditions. Factorial analyses showed a significant rendering-by-source-text-condition interaction in perceived quality. Participants rated fidelity-oriented outputs higher than readability-oriented outputs for the simple narratives, whereas no reliable rendering difference emerged for the complex prose. A corresponding source-condition-dependent pattern was observed for perceived intelligence, agency-oriented anthropomorphic attribution, and task-performance trust. A separate theory-ordered appraisal-structure SEM characterized concurrent associations among perceived quality, perceived intelligence, agency-oriented anthropomorphic attribution, task-performance trust, and stated disclosure willingness across six domains, with task-performance trust as the proximal correlate of stated willingness. The observed rating pattern distinguishes source access from source evaluability: for the complex stimuli, displaying the source did not ensure that one overall-quality rating reflected differences in retained content. It also separates support for evaluating translation output from data-handling support for decisions about what personal text to entrust to a system.

---


### 144. [Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.19098)

**<font color=#1a73e8>作者：</font>** Huan-ang Gao, Haohan Chi, Yong Yan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) experts into a single generalist student via dense, token-level reward supervision. Despite its practical success, the optimization dynamics governing multi-teacher capability integration remain poorly understood, and open, rigorously reproducible recipes are conspicuously lacking. In this work, we establish a controlled M-OPD benchmark on SmolLM3-3B-Base with oracle routing, isolating capability integration from routing ambiguity. Our investigation reveals a pronounced capability integration gap: standard M-OPD captures only 35.6% of the available headroom relative to a domain-routed oracle ensemble, with concise tasks such as instruction following suffering severe degradation and premature stagnation. Crucially, we show that this failure stems not from gradient conflict, but from a severe misallocation of the token-level optimization budget. This pathology is driven by three orthogonal factors: structural sequence-length disparities across domains, dynamic convergence drift due to non-uniform learning rates, and multi-step reward staleness from asynchronous policy updates. To resolve these imbalances, we introduce Open-MOPD, a principled framework incorporating token-share balancing, gap-aware dynamic budget allocation, and student reward refresh. Together, these mechanisms systematically restore cross-domain balance, elevating headroom recovery from 35.6% to 83.4% in a single deployable student. We fully open-source our end-to-end post-training recipe, training trajectories, and evaluation suites on an academically accessible hardware budget.

---


### 145. [Intercepting the Kangaroo: Experimental Astrolinguistics with Constructed Lexicons, Active Probing, and Large Language Models as Informants and Hypothesis Proposers](https://arxiv.org/abs/2608.19124)

**<font color=#1a73e8>作者：</font>** Francesco Cordella, Mauro Cappelli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Astrolinguistics -- communication with minds that categorize reality differently from ours -- has been purely speculative since Freudenthal's Lincos (1960). We make it experimental. Two language models with deliberately incompatible constructed lexicons (one encoding shape, color, and motion; the other fusing color with motion, encoding parity, and lacking shape) serve as informants with complete ground truth, while a fully scripted orchestrator translates between the two category systems. The central failure mode is the kangaroo effect: the silent attachment of a word to the wrong referent -- Quine's indeterminacy of translation, operationalized. Across 400+ simulated and live runs, a protocol combining cross-situational elimination, pre-registered predictive probes, active scene selection, a stricter recovery round, and quarantine produced no undetected mistranslations under the tested conditions and exceeded a passive baseline's coverage (d = 0.62). Injected kangaroo traps defeated naive ostension and pure statistical learning in 100% of runs, while the full protocol intercepted every decoy and, where discriminating evidence is ontologically unavailable, declared Quinean equivalence classes instead of guessing. Under informant noise it degrades gracefully: zero kangaroos persist up to 2% per-word noise; at 10% the protocol predominantly abstains rather than errs. Finally, words outside the scripted hypothesis space (a history-dependent relational term and an XOR contextual homonym) are recovered by a generate-and-test loop in which an LLM proposes rules and the script verifies them: coverage scales with proposer capability (0% -> 18% -> 72% -> 100%) while undetected mistranslations stayed at zero throughout. In the tested conditions, correctness is a property of the protocol; coverage is a property of the instruments.

---


### 146. [Tuning the Stochastic Machine: A Systems Engineer's Operating Model for Human-AI Engineering](https://arxiv.org/abs/2608.19125)

**<font color=#1a73e8>作者：</font>** George Andrikopoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an expert corrects an LLM assistant's error, the correction usually dies with the session, and the error class returns. I argue this is an operations problem, not a tooling problem: mechanisms for persisting corrections exist and are shipping, but the discipline for governing them -- versioning with provenance, recurrence monitoring, counter-metrics, retirement of stale rules -- does not. Writing as a systems engineer of thirty years, I map the LLM stack onto the machines my profession already operates (frozen silicon, firmware, loadable modules, persistent configuration, volatile memory), identify where the mapping fails (stochastic generation, configuration that binds only probabilistically, no general-purpose retirement (verification) stage by default), and derive from the failures a seven-principle operating discipline with an error loop at its core. Three cases from my own practice illustrate the mechanism, among them a control that silently became the exact harm it was built to prevent. I close with the measurement framework this view implies and the lab study required to test it.

---


### 147. [Comment-level Topic Drift Analysis in the Reddit Corpus](https://arxiv.org/abs/2608.19133)

**<font color=#1a73e8>作者：</font>** Steven Morse, Daniel Runfola, Trenton W. Ford  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a novel application of embedding-based dynamic topic modeling techniques to detect and quantify topic drift at the comment level in a massive corpus. By leveraging pretrained language models to generate contextualized semantic embeddings for short text, we analyzed 12.7 billion Reddit comments spanning 2006 to 2022. Using unsupervised methods on these embeddings, we identify dynamically evolving topic clusters over time. Our primary contribution is a methodology for analysis of semantic drift and discourse evolution in the embedding space itself. We also demonstrate modifications to existing methods that enable this analysis at scale, and we propose and demonstrate a null model comparison test to filter spurious dynamics. Key findings suggest that politically and socially contentious topics exhibit significant directional drift in embedding space, with inter-topic distances changing systematically over time beyond what the null model can explain, whereas domains such as music and sports remain comparatively stable.

---


### 148. [Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems](https://arxiv.org/abs/2608.19140)

**<font color=#1a73e8>作者：</font>** George Andrikopoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models are compared, marketed, and benchmarked on capability -- what their best or average output can achieve. I argue this measures the wrong axis. The models have saturated accuracy: their mean output lands on the target. What now separates one system from another in practice is precision: how tightly concentrated their outputs are around that target across repeated, identical requests. Borrowing the marksman's distinction, capability is where the average shot lands; reliability is the size of the group. I make three claims. First, precision, not capability, is the frontier differentiator between systems, and benchmark culture systematically fails to measure it, reporting central tendency rather than spread. Second, precision is measurable, cheaply and without circularity, by running a fixed suite of deterministically scored tasks many times at fixed temperature and computing the per-task consistency of outcomes -- no model-in-the-loop grader required. Third, the measurement is not merely descriptive but decision-guiding: it separates consistent failures (a tight group off-centre, correctable by the operating discipline of Paper 1 -- a sight adjustment) from scattered failures (a wide group, correctable only by changing the model or its sampling -- a rifle problem). I define a grouping metric, specify a harness, and show how tracking a human-AI pair's grouping over time yields the compounding signal that Paper 1's field study requires. A first real run, since replicated, illustrates both the method and its most important limit: one measured gap was closed completely by a single rule (0/5 -> 5/5), while a suite of tasks authored from the rules themselves found no value, because a frontier model already embodies explicit good practice -- establishing that a discipline's worth is found by measurement on real work, not constructed from its own rulebook.

---


### 149. [Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication](https://arxiv.org/abs/2608.19161)

**<font color=#1a73e8>作者：</font>** Ramneet Kaur, Pradyumna Chari, Ramesh Raskar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent Alignments (VLA), an activation-aware framework for monitoring and steering these private communication channels. For every monitored decision, VLA links the private latent-state record and channel status to the resulting public action using a shared event identifier, enabling matched causal analysis. Our first contribution is a neutral-only three-layer monitor combining representation anomaly detection, counterfactual action-distribution influence, and sparse-autoencoder interpretation support. Our second contribution is a steerability framework spanning black-box behavioral instructions and white-box matched-neutral counterfactuals. Our third contribution is an evaluation on a controlled multi-agent auction benchmark covering homogeneous and heterogeneous model pairs, many-agent scalability, and intervention effectiveness. The sequential monitor achieves mean area under the receiver operating characteristic curve (AUROC) of 0.993 for homogeneous agents and 0.854 for heterogeneous pairs when text- and latent-collusion rows are pooled as positives. In Qwen3-0.6B auctions with 25-100 bidders, monitoring requires only a small normalized load relative to all possible directed pairs, while full white-box steering achieves 100% bid-distribution recovery and reduces collusive low-bid behavior by 47.3 percentage points. Because full white-box steering replays the matched neutral counterfactual, its exact recovery is a sanity check by construction. Overall, the controlled study shows that the evaluated private channel attacks can be monitored without training the primary monitor on attack examples and mitigated when matched counterfactual access is available.

---


### 150. [ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos](https://arxiv.org/abs/2608.19165)

**<font color=#1a73e8>作者：</font>** Thales Bertaglia, Catalina Goanta, Gerasimos Spanakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ChildSafeAds is a shared task on commercial content in YouTube videos likely to reach children and teenagers. It contains 3,360 videos from 939 channels. Each instance begins with a segment submitted to SponsorBlock, an open-source crowdsourced browser extension whose users mark sponsor segments so that others can skip them. We pair the segment with its available transcript, video and channel information, and a sales or service page linked from the video description. Systems determine what kind of offer is being promoted (ST1), assign product categories (ST2), and identify legal risk flags (ST3). The evidence is divided into four cumulative access levels, from the transcript to the linked page, so results can be compared against the cost of collecting the data. 45.5\% of videos in our data failed to properly use the in-platform ad disclosure method (the ``Includes paid promotion'' label). GPT-5.4 produced the labels after the expert organiser team reviewed samples and iterated on the taxonomy, prompts and model choices. GPT-5.6-luna independently labelled the development set. This report describes the task, data and evaluation. An updated version will add participating systems and shared-task results.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-166](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
