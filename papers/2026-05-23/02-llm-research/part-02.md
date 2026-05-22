# 🧠 大模型相关研究 | 2026年05月23日

> 本类共 **162** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-162](./part-04.md)

---

### 51. [Planning in the LLM Era: Building for Reliability and Efficiency](https://arxiv.org/abs/2605.21902)

**<font color=#1a73e8>作者：</font>** Michael Katz, Harsha Kokel, Kavitha Srinivas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Growing attention to intelligent agents has put a spotlight on one of their central capabilities: planning. Early attempts to leverage large language models (LLMs) for planning relied on single-shot plan generation, followed by hybrid approaches that coupled LLMs with limited external search. These methods, unsound and incomplete by their very nature, often require substantial resources without yielding better solutions on unseen problems. As the limitations of LLMs become clearer, recent work has shifted toward using them at solution construction time -- generating symbolic solvers for a family of problems that can be verified and then used efficiently at inference time. This trend reflects the growing need for agents that are both reliable and resource-efficient. It also offers a path towards generating maintainable planners with minimal dependence on language models at inference time. In this paper, we argue that this shift reflects a broader realignment of the planning field in the LLM era. We examine three major categories of planner-generation methods, discuss their current limitations, and outline research steps towards a more reliable and efficient LLM-based generation of planners.

---


### 52. [MAVEN: A Multi-stage Agentic Annotation Pipeline for Video Reasoning Tasks](https://arxiv.org/abs/2605.21917)

**<font color=#1a73e8>作者：</font>** Han Zhang, Wanting Jiang, Tomasz Kornuta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training Vision Language Models (VLMs) for video event reasoning requires high-quality structured annotations capturing not only what happened, but when, where, why, and with what consequence, at a scale manual labelling cannot support. We present MAVEN (Multi-stage Agentic Video Event aNnotation), a multi-stage agentic pipeline that turns raw videos into multi-task training data with Chain-of-Thought (CoT) reasoning traces, organized around a designated Event of Focus. At its core, MAVEN synthesizes a Multi-Scale Spatio-Temporal Event Description (MSTED) from three complementary caption levels; this explicit intermediate serves as the sole input to downstream Q&A generation across multiple task formats. Crucially, MAVEN supports agent-driven domain adaptation: given a new video dataset and target question examples, the agent redesigns all prompts top-down without manual re-engineering. A hierarchical refinement loop further classifies annotation errors against a taxonomy, traces root causes to the originating pipeline stage, and applies targeted edits that rewrite prompts or modify the pipeline structure itself, iteratively improving data quality. We apply MAVEN to label over 5,300 traffic videos and fine-tune Cosmos-Reason2-8B on the resulting data. On a private CCTV evaluation set, fine-tuning surpasses both Gemini 2.5 Pro and 3.1 Flash, including a $+38.8$-point gain in MCQ accuracy over zero-shot. On AccidentBench, CCTV-only training lifts Cosmos-Reason2 by $+10.7$ MCQ points and matches Gemini 2.5 Pro despite seeing no dashcam videos; adding agent-adapted dashcam annotations narrows the gap to Gemini 3.1 Flash, and RL post-training pushes overall performance past both Gemini baselines. Qualitative results on warehouse surveillance and public safety videos further show the agentic workflow readily adapts the pipeline to new domains.

---


### 53. [SDGBiasBench: Benchmarking and Mitigating Vision--Language Models' Biases in Sustainable Development Goals](https://arxiv.org/abs/2605.21919)

**<font color=#1a73e8>作者：</font>** Zihang Lin, Huaiyuan Qin, Muli Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessing progress toward the Sustainable Development Goals (SDGs) requires multi-step reasoning over visual cues, contextual knowledge, and development indicators, where incomplete evidence use and imperfect evidence integration can introduce hidden prediction biases. Real-world SDG monitoring further spans both qualitative judgments and quantitative estimation. However, existing benchmarks typically evaluate these aspects in isolation, obscuring systematic biases that emerge when models substitute priors for evidence. To address this gap, we propose SDGBiasBench, a large-scale benchmark suite for SDG-oriented vision-language reasoning. Spanning 500k expert-involved multiple-choice questions and 50k regression tasks, the benchmark enables comprehensive assessment of both decision-level and estimation-level bias in Vision--Language Models (VLMs). Evaluations on SDGBiasBench reveal an intrinsic SDG bias in current VLMs, where predictions are frequently driven by SDG specific priors rather than reliable multi-modal cues. To mitigate such bias, we propose CADE (Contrastive Adaptive Debias Ensemble), a training-free, plug-and-play method that leverages modality-specific answer priors. CADE yields significant gains on the proposed benchmark, improving multiple-choice accuracy by up to 25% and reducing regression MAE by up to 12 points across multiple VLMs. We hope our work can foster the development of more fair and reliable AI systems for sustainable development.

---


### 54. [Visual-Advantage On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2605.21924)

**<font color=#1a73e8>作者：</font>** Ruiqi Liu, Xiaolei Lv, Gengsheng Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy knowledge distillation has proven effective for language models, yet its application to vision-language models (VLMs) remains underexplored. We observe that standard on-policy distillation can improve a student's output quality while failing to strengthen its reliance on visual input: on vision-critical tokens, the student's predictions remain largely unchanged whether or not fine-grained visual detail is present, even though the teacher's predictions depend heavily on this http URL make this difference observable, we introduce visual advantage (VA), the token-level log-probability difference when the teacher scores a student-generated rollout with versus without access to fine-grained visual detail. VA is concentrated in a small minority of tokens, and these high-VA tokens are the ones that actually carry the visual supervision signal. This motivates a distillation objective that treats them differently from language scaffolding, so their contribution is not diluted by the abundant surrounding language this http URL propose Visual-Advantage On-Policy Distillation (VA-OPD), which uses VA at two granularities: rollout-level reweighting by trajectory-averaged VA, and token-level KL averaged within high-VA and low-VA groups separately. We train on two math datasets (Geometry3K and ViRL39K) and evaluate on eight benchmarks covering both mathematical reasoning and visual understanding, across three teacher sizes (4B, 8B, and 32B) on the Qwen3-VL family. VA-OPD improves over standard on-policy distillation on every benchmark, with the gain growing monotonically along both the teacher-size and data-scale axes, suggesting that these factors compound consistently.

---


### 55. [EvoVid: Temporal-Centric Self-Evolution for Video Large Language Models](https://arxiv.org/abs/2605.21931)

**<font color=#1a73e8>作者：</font>** Shiqi Huang, Ziyue Wang, Zhongrong Zuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Video Large Language Models (Video-LLMs) have demonstrated strong capabilities in video reasoning through reinforcement learning (RL). However, existing RL pipelines rely heavily on human-annotated tasks and solutions, making them costly to scale and fundamentally constrained by human expertise. Self-evolving frameworks have recently emerged as a promising alternative through autonomous Questioner-Solver self-play. Unfortunately, these approaches are primarily designed for static modalities such as text and images, fundamentally failing to capture the temporal dynamics that are central to video reasoning. In this work, we propose $\textbf{EvoVid}$, a temporal-centric self-evolving framework that enables Video-LLMs to improve directly from raw, unannotated videos. Specifically, we introduce two complementary temporal-centric rewards: a temporal-aware Questioner reward that encourages temporally dependent question generation through temporal perturbation sensitivity, and a temporal-grounded Solver reward that provides automatic temporal supervision via inherent video segment localization. Extensive experiments across four base models and six benchmarks demonstrate consistent improvements over both base models and existing self-evolving baselines, achieving competitive performance with supervised methods. These results highlight temporal-centric self-evolution as an effective and scalable paradigm for video understanding and reasoning.

---


### 56. [Claim-Selective Certification for High-Risk Medical Retrieval-Augmented Generation](https://arxiv.org/abs/2605.21949)

**<font color=#1a73e8>作者：</font>** Shao Kan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical RAG systems in high-risk QA settings are often evaluated through a single answer-or-abstain decision, but mixed evidence may support one claim, require conditions for another, and contradict a third. We study claim-selective certification: each response is decomposed into verifiable claims, scored against retrieved evidence, and mapped by an intent-aware selector to {full, partial, conflict, abstain}. On the primary weak-label certificate protocol, whose real-source-only dev/test rows cover the naturally occurring non-abstain actions, the full system records UCCR=0.0000, PAU=1.0000, PAU Precision=0.9901, and action accuracy=0.9204 on dev (n=314), and UCCR=0.0000, PAU=0.9967, PAU Precision=0.9739, and action accuracy=0.8997 on test (n=319). UCCR measures unsupported-claim risk within the certificate definition, and a source-missing counterfactual slice evaluates abstain under empty evidence. Shortcut controls quantify the action-label prior explained by source and intent metadata, while source/evidence-novel slices characterize transfer boundaries. The resulting interface separates action-label prediction from evidence-linked claim selection under mixed evidence.

---


### 57. [MLLMs Know When Before Speaking: Revealing and Recovering Temporal Grounding via Attention Cues](https://arxiv.org/abs/2605.21954)

**<font color=#1a73e8>作者：</font>** Dazhao Du, Liao Duan, Jian Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video temporal grounding (VTG), which localizes the start and end times of a queried event in an untrimmed video, is a key test of whether multimodal large language models (MLLMs) understand not only what happens but also when it happens. Although modern MLLMs describe video content fluently, their timestamp predictions remain unreliable, while existing remedies either require costly post-training on temporal annotations or rely on coarse training-free heuristics. In this work, we probe the cross-modal attention of MLLMs and uncover a perception-generation gap. Our key finding is that MLLMs often know the target interval during prefill, but lose this signal when generating the final answer. In the prefill stage, a sparse set of attention heads, which we call \emph{Temporal Grounding Heads} (TG-Heads), concentrates query-to-video attention on the ground-truth interval. During autoregressive decoding, however, the answer tokens shift attention away from this interval toward visually salient but query-irrelevant segments. This observation motivates an inference-time read-then-regenerate framework. We first convert TG-Head prefill attention into a debiased frame-level relevance signal and extract the high-attention interval it highlights. We then re-invoke the MLLM with visual context restricted to this interval, using video cropping or attention masking to suppress distractors. Without parameter updates and architectural changes, our framework consistently improves MiMo-VL-7B, Qwen3-VL-8B, and TimeLens-8B on three VTG benchmarks, with gains of up to +3.5 mIoU. The project website can be found at this https URL.

---


### 58. [Diagnosis Is Not Prescription: Linguistic Co-Adaptation Explains Patching Hazards in LLM Pipelines](https://arxiv.org/abs/2605.21958)

**<font color=#1a73e8>作者：</font>** Yoon Jeonghun, Kim Dongchan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a multi-module LLM agent fails, the module most responsible for the failure is not necessarily the best place to intervene. We demonstrate this Diagnostic Paradox empirically: causal analysis consistently identifies the routing module -- which selects which tool to call next -- as the primary bottleneck across three independent agent families. Yet injecting prompt-level correction examples into this module consistently degrades performance, sometimes severely. Patching an upstream query-rewriting module instead reliably improves outcomes. The effect holds with statistical significance on two agent families and directional consistency on a third; alternative repair strategies at the routing module (instruction rewriting, model upgrade) are neutral, confirming that the harm is specific to correction-injection patching.
We explain this asymmetry through the Linguistic Contract hypothesis: each downstream module implicitly adapts to its upstream's characteristic error distribution, so correcting the bottleneck breaks this implicit alignment in a way that upstream corrections do not. We operationalize this via a per-agent co-adaptation measure, derived from diagnosis alone, and show it is consistently associated with patching harm across agent families: higher co-adaptation co-occurs with harm, lower with safety. This trend holds across all three agent families, providing preliminary support for the hypothesis beyond a single-agent observation.

---


### 59. [ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data](https://arxiv.org/abs/2605.21963)

**<font color=#1a73e8>作者：</font>** Jiangyuan Wang, Xuyong Chen, Junwei He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon clinical simulation -- predicting how a patient's physiology evolves over years under specified interventions -- is central to chronic-disease care, yet existing electronic health record (EHR) models are predominantly discriminative, and general-purpose large language models drift under repeated interventions. We propose the \textbf{ChronoMedicalWorld Model (CMWM)}, an action-conditioned latent world-model framework for learning patient trajectories from longitudinal care data. CMWM couples a joint-embedding state encoder with a wide action encoder that admits both structured intervention indicators and free-text communication embeddings, and trains a recurrent latent transition module under a six-term objective: next-observation supervision, next-latent prediction, SIGReg latent regularisation, and three physiology-aware shape priors (slope, continuity, large-jump penalty). A closed-loop rollout-prefix protocol matches training to deployment, so the model is optimised against the same multi-step error it exhibits at inference. As a concrete case study, we instantiate CMWM for annual estimated glomerular filtration rate (eGFR) trajectory forecasting in chronic kidney disease (CKD). On a 2{,}232-patient nephrology cohort, the CKD instantiation achieves a dynamic-50\% history rollout test mean absolute error (MAE) of 7.384 and root-mean-square error (RMSE) of 10.256, against 7.964 and 11.069 for a tuned GPT-5.5 structured-prompting baseline ($-7.28\%$ MAE, $-7.35\%$ RMSE), with the gain dominated by the dialogue portion of patient--health-coach communication. The framework is not CKD-specific: its architecture, loss design, and training protocol apply to any chronic condition that can be cast as periodic clinical state interleaved with structured and conversational interventions.

---


### 60. [Reasoning through Verifiable Forecast Actions: Consistency-Grounded RL for Financial LLMs](https://arxiv.org/abs/2605.21975)

**<font color=#1a73e8>作者：</font>** Jialin Chen, Aosong Feng, Harshit Verma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial markets are characterized by extreme non-stationarity, low signal-to-noise ratios, and strong dependence on external information such as news, company fundamentals, and macroeconomic signals. Yet, existing approaches either abstract time-series into text or decouple forecasting from language-based reasoning, leading to a fundamental mismatch between qualitative reasoning and quantitative outcomes. To address this, we introduce StockR1, a time-series-enhanced LLM that unifies stock forecasting and financial reasoning through a verifiable forecast action. Based on a tool-call design, the model first emits a forecast action, which is a structured and interpretable representation of its qualitative market outlook. It then invokes a time-series decoder conditioned on this action to generate distributional future trajectories, leading to more informed question answering and financial reasoning. We optimize the full pipeline with reinforcement learning, where rewards jointly reflect answer validity, forecast accuracy, and consistency between generated actions and observed time-series dynamics. In addition, rewards are reweighted by a sample-level uncertainty scalar, encouraging the model to accommodate varying uncertainty in market dynamics. We evaluate StockR1 on financial question answering and stock forecasting over a large-scale 10-year benchmark. Our method consistently outperforms time-series baselines and general-purpose LLMs, improving reasoning accuracy by 17.7% (4B) and 25.9% (8B). These findings demonstrate that structuring the forecast actions establishes a powerful synergy between language reasoning and temporal prediction, enabling LLMs to reason through verifiable, interpretable, and numerically grounded decisions.

---


### 61. [Interpreting and Enhancing Emotional Circuits in Large Vision-Language Models via Cross-Modal Information Flow](https://arxiv.org/abs/2605.21980)

**<font color=#1a73e8>作者：</font>** Chengsheng Zhang, Chenghao Sun, Zhining Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) represent a significant leap towards empathetic agents, demonstrating remarkable capabilities in emotion understanding. However, the internal mechanisms governing how LVLMs translate abstract visual stimuli into coherent emotional narratives remain largely unexplored, primarily due to the scarcity of visual counterfactuals and the diffuse nature of emotional expression. In this paper, we bridge this gap by introducing a steering-vector-based causal attribution framework tailored for descriptive emotional reasoning. To this end, we construct a specialized dataset to demystify the emotional circuits underlying the three-stage ``Adapt-Aggregate-Execute'' mechanism. Crucially, we discover a functional decoupling: visual emotional cues are aggregated in middle layers via sentiment-specific attention heads, but are subsequently translated into narrative generation in deep layers through emotion-general pathways. Guided by these insights, we regulate the emotional information routing to strengthen attention flow and amplify the semantic activation to consolidate expression. Extensive experiments on the comprehensive MER-UniBench demonstrate that our methods significantly improve performance via inference-time intervention, effectively mitigating emotional hallucinations and corroborating the causal fidelity of the discovered circuits.

---


### 62. [Learning Spatiotemporal Sensitivity in Video LLMs via Counterfactual Reinforcement Learning](https://arxiv.org/abs/2605.21988)

**<font color=#1a73e8>作者：</font>** Dazhao Du, Jian Liu, Jialong Qin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (Video LLMs) achieve strong benchmark accuracy, yet often answer video questions through shortcuts such as single-frame cues and language priors rather than by tracking spatiotemporal dynamics. This issue is exacerbated in RL post-training, where correctness-only rewards can further reinforce shortcut policies that obtain high reward without tracking video dynamics. We address this by asking a controlled counterfactual question: if the visual world changed while the question remained fixed, should the answer change or stay the same? Based on this view, we propose \textbf{Counterfactual Relational Policy Optimization (CRPO)}, a dual-branch RL framework for improving \emph{spatiotemporal sensitivity}. CRPO constructs counterfactual videos through horizontal flips and temporal reversals, trains on both original and counterfactual branches, and introduces a \textbf{Counterfactual Relation Reward (CRR)} between their answers. CRR encourages answers to change for dynamic questions and remain unchanged for static questions. This cross-branch constraint makes it difficult for shortcut policies to be consistently rewarded across both branches. To evaluate this property, we introduce \textbf{DyBench}, a paired counterfactual video benchmark with 3,014 videos covering reversible dynamics, moving direction, and event sequence, together with a strict pair-accuracy metric that prevents fixed-answer shortcuts from inflating scores. Experiments show that CRPO outperforms prior RL methods on spatiotemporal-sensitive evaluations while maintaining competitive general video performance. On Qwen3-VL-8B, CRPO improves DyBench P-Acc by +7.7 and TimeBlind I-Acc by +8.2 over the base model, indicating improved spatiotemporal sensitivity rather than stronger reliance on static shortcuts. The project website can be found at this https URL .

---


### 63. [Ex-GraphRAG: Interpretable Evidence Routing for Graph-Augmented LLMs](https://arxiv.org/abs/2605.21994)

**<font color=#1a73e8>作者：</font>** Yoav Kor Sade, Arvindh Arun, Rishi Puri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GraphRAG conditions language models on subgraphs retrieved from knowledge graphs, encoded via message-passing GNNs. Because these encoders entangle node contributions through iterated neighborhood aggregation, there is no closed-form way to determine how much each retrieved entity influenced the encoder's output, and therefore no way to faithfully audit what structural evidence actually reached the model. We introduce Ex-GraphRAG, which replaces the GNN encoder with a Multivariate Graph Neural Additive Network (M-GNAN), an extension of additive graph models to high-dimensional embedding spaces that yields an exact decomposition of the encoder's output across individual nodes and feature groups, without post-hoc approximation. On STaRK-Prime, this auditable encoder matches black-box performance. Using it to audit evidence routing, we uncover a semantic-structural mismatch: the nodes that dominate the encoder's output are structurally disconnected in the retrieved subgraph, held together by low-attribution intermediaries whose removal degrades multi-hop QA by up to 28%. This mismatch, invisible to any opaque encoder, reveals that semantic importance and structural connectivity are governed by disjoint sets of nodes, with direct implications for retrieval pruning, context construction, and failure diagnosis in graph-augmented LLMs.

---


### 64. [The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems](https://arxiv.org/abs/2605.21997)

**<font color=#1a73e8>作者：</font>** Yohei Nakajima  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most agent frameworks are built around the language model: a conversation loop comes first, then tools, then rules, and finally a logging layer bolted on for observability, with state persisted as retrievable "memory." We describe ActiveGraph, a runtime that inverts this arrangement. The append-only event log is the source of truth; the working graph is a deterministic projection of that log; and behaviors--ordinary functions, classes, LLM-backed routines, or logic attached to typed edges--react to changes in the graph and emit new events. No component instructs another; coordination happens entirely through the shared graph. This single design decision yields three properties that retrieval-and-summarization memory systems do not provide: deterministic replay of any run from its log, cheap forking that branches a run at any event without re-executing the shared prefix, and end-to-end lineage from a high-level goal down to the individual model call that produced each artifact. We present the architecture, a determinism contract that makes replay sound, and a worked diligence example whose full causal structure is reconstructable from the log alone. We discuss--without claiming to demonstrate--why this substrate is unusually well suited to self-improving agents, and how it extends the BabyAGI lineage and prior graph-memory research.

---


### 65. [Check Your LLM's Secret Dictionary! Five Lines of Code Reveal What Your LLM Learned (Including What It Shouldn't Have)](https://arxiv.org/abs/2605.22005)

**<font color=#1a73e8>作者：</font>** Hisashi Miyashita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that singular value decomposition of the lm_head} weight matrix of a transformer-based large language model -- requiring only five lines of PyTorch and no model inference -- reveals interpretable semantic subspaces directly from the model weights. Each left singular vector identifies the vocabulary tokens most readily selected when the hidden state aligns with the corresponding singular direction; inspecting these clusters exposes the model's training data composition and curation philosophy.
Analysing GPT-OSS-120B, Gemma-2-2B, and Qwen2.5-1.5B, we find that singular value spectra and vocabulary cluster structures differ systematically across models: GPT exhibits a graduated hierarchy of functionally differentiated subspaces; Gemma is dominated by pre-nineteenth-century English orthography, forming a stepwise clustering structure that may contribute to high output controllability; and Qwen exhibits broad multilingual coverage alongside subspaces whose vocabulary the authors have determined to be ethically inappropriate for direct publication.
Base-instruct comparison reveals that ethically concerning subspaces originate in pretraining and are not removed by post-training alignment. We introduce the Vocabulary Cluster Score (VCS) to quantify subspace coherence, and the Weighted Projection Score (WPS) as a static glitch token detector; applying WPS to GPT-OSS-120B recovers shokubutsu-hyakka-tsu (ID 137606), a well-known glitch token widely reported in the CJK language community, without any model inference. We propose a taxonomy of root causes for problematic vocabulary content and call for lm_head} SVD analysis to be adopted as a standard pre-release safety auditing step. Our findings further suggest directions toward SVD-guided tokenizer optimisation and more controllable LLM design.

---


### 66. [Hallucination as Commitment Failure: Larger LLMs Misfire Despite Knowing the Answer](https://arxiv.org/abs/2605.22007)

**<font color=#1a73e8>作者：</font>** Jewon Yeom, Jaewon Sok, Heejun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination is often viewed as a direct consequence of missing knowledge: a model answers incorrectly when the correct answer is absent from its generation-time distribution, and correctly when it is present. We test this assumption by introducing a semantic notion of answer availability that aggregates token-level variants expressing the same answer concept, and asks whether the correct concept is already available at the moment the model commits to an answer. Across Qwen and Llama models from 0.8B to 72B in both Instruct and Base variants, 16-47% of Instruct hallucinations occur with substantial probability mass already on the correct concept, and the rate rises monotonically with scale. Comparing such failures against correct generations with matched semantic support, the distinguishing factor is not whether the correct concept is represented, but how its probability is distributed: correct generations concentrate mass on a single surface form, hallucinations disperse it across alternatives. The same sharpening asymmetry extends across multi-token generation and is detectable in pre-generation hidden states. Together, these results identify a single mechanism: instruction tuning sharpens answer commitment with scale, making helpfulness and confident hallucination two consequences of the same underlying disposition.

---


### 67. [LatentOmni: Rethinking Omni-Modal Understanding via Unified Audio-Visual Latent Reasoning](https://arxiv.org/abs/2605.22012)

**<font color=#1a73e8>作者：</font>** Yifan Dai, Zhenhua Wu, Bohan Zeng 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Joint audio-visual reasoning is essential for omnimodal understanding, yet current multimodal large language models (MLLMs) still struggle when reasoning requires fine-grained evidence from both modalities. A central limitation is that explicit text-based chain-of-thought (CoT) compresses continuous audio-visual signals into discrete tokens, weakening temporal grounding and shifting intermediate reasoning toward language priors. We argue that a unified latent space is a better medium for such reasoning because it preserves dense sensory information while remaining compatible with autoregressive generation. Based on this insight, we propose \textbf{LatentOmni}, a cross-modal reasoning framework that interleaves textual reasoning with audio-visual latent states. LatentOmni introduces feature-level supervision to align latent reasoning states with task-relevant sensory features and uses Omni-Sync Position Embedding (OSPE) to maintain temporal consistency between latent audio and visual states. We further construct \textbf{LatentOmni-Instruct-35K}, a dataset of audio-visual interleaved reasoning trajectories for supervising latent-space reasoning. Comprehensive evaluation across multiple audio-visual reasoning benchmarks demonstrates that LatentOmni achieves the best performance among the evaluated open-source models and consistently outperforms the Explicit Text CoT baseline, supporting latent-space joint reasoning as a promising path toward stronger omnimodal understanding.

---


### 68. [PointLLM-R: Enhancing 3D Point Cloud Reasoning via Chain-of-Thought](https://arxiv.org/abs/2605.22013)

**<font color=#1a73e8>作者：</font>** Chaoqi Chen, Qile Xu, Wenjun Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding 3D point clouds through language remains a fundamental challenge in computer graphics and visual computing, due to the irregular structure of point cloud data and the lack of explicit reasoning in existing 3D multimodal models. While Chain-of-Thought (CoT) reasoning has shown strong effectiveness in LLMs and image-based MLLMs, its extension to 3D understanding remains largely underexplored. In this paper, we propose a data-centric framework for constructing large-scale CoT supervision tailored to 3D point cloud understanding. Our framework consists of a two-stage pipeline that first refines point-text instruction data via vision-language-model-based quality evaluation and reference-guided refinement, and then synthesizes high-quality reasoning paths through Human-in-the-Loop Prompt Optimization (HiLPO). Using this approach, we build PoCoTI, a CoT-enhanced point-text instruction-following dataset containing 55K samples with explicit reasoning paths. Fine-tuning PointLLM on PoCoTI yields PointLLM-R, a reasoning-capable 3D multimodal language model. Extensive experiments on generative 3D classification and captioning demonstrate that PointLLM-R achieves state-of-the-art performance and generalizes robustly to real-world scanned point clouds and multi-turn dialogue scenarios.

---


### 69. [GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation](https://arxiv.org/abs/2605.22036)

**<font color=#1a73e8>作者：</font>** Jiahao Yang, Zihan Wang, Xiangyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant progress in Vision-Language Navigation (VLN), existing approaches still rely on dense RGB videos that produce excessive patch tokens and lack explicit spatial structure, resulting in substantial computational overhead and limited spatial reasoning. To address these issues, we introduce the Geometry-Aware BEV (GA-BEV) - a compact, 3D-grounded feature representation that integrates both explicit and implicit geometric cues into multimodal large language model (MLLM) - based navigation systems. We construct BEV spatial maps from RGB-D inputs by projecting visual features into 3D space and aggregating them into an agent-centric layout that preserves geometric consistency while reducing token redundancy. To further enrich geometric understanding, we incorporate features from a pretrained 3D foundation model into the BEV space, injecting structural priors learned from large-scale 3D reconstruction tasks. Together, these complementary cues - explicit depth-based projection and implicit learned priors - yield compact yet spatially expressive representations that substantially improve navigation efficiency and performance. Experiments show that our method achieves state-of-the-art results using only navigation data, without DAgger augmentation or mixed VQA training, demonstrating the robustness and data efficiency of the proposed GA-VLN framework.

---


### 70. [Active Evidence-Seeking and Diagnostic Reasoning in Large Language Models for Clinical Decision Support](https://arxiv.org/abs/2605.22047)

**<font color=#1a73e8>作者：</font>** Chen Zhan, Xihe Qiu, Xiaoyu Tan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models perform well on static medical examinations, yet clinical diagnosis often requires iterative evidence gathering under uncertainty. Building on prior interactive evaluation efforts, we introduce an OSCE-inspired standardized patient simulator and a controlled, reproducible benchmark for active diagnostic inquiry. Across 468 cases and 15 models in our protocol, we observe that multi-turn evidence seeking reduces diagnostic accuracy by 12.75% and lowers supporting-evidence quality by 24.36% relative to full-context evaluation; error analyses associate these drops with premature diagnostic closure and inefficient questioning. Together, these results suggest that static full-context benchmarks may overestimate performance in interactive evidence-seeking settings, motivating complementary interactive assessment for safer clinical decision support.

---


### 71. [LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation](https://arxiv.org/abs/2605.22054)

**<font color=#1a73e8>作者：</font>** Zhuo Chen, Xinzhe Yuan, Jianshu Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The high cost and data scarcity in scientific exploration have motivated the use of large language models (LLMs) as knowledge-driven components in Bayesian optimization (BO). However, existing approaches typically embed LLMs directly into the sampling or surrogate modeling pipeline, without fully leveraging their significantly lower evaluation cost compared to real-world experiments. To address this limitation, we propose LLM-Accelerated Bayesian Optimization (LABO), a framework that combines LLM predictions with experimental observations within a single BO loop. LABO employs a gating criterion to dynamically balance the reliance on LLM predictions versus actual experiments. By leveraging inexpensive LLM evaluations to broadly explore the search space and reserving costly real experiments only for regions with high uncertainty, LABO achieves more sample-efficient optimization. We provide a theoretical analysis with a cumulative regret bound that formalizes this efficiency gain. Empirical results across diverse scientific tasks demonstrate that LABO consistently outperforms existing methods under identical experimental budgets. Our results suggest that LABO offers a practical and theoretically grounded approach for integrating LLMs into scientific discovery workflows.

---


### 72. [Distributed Image Compression with Multimodal Side Information at Extremely Low Bitrates](https://arxiv.org/abs/2605.22061)

**<font color=#1a73e8>作者：</font>** Guojun Xu, Mingyang Zhang, Jianwen Xiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distributed Image Compression (DIC) is crucial for multi-view transmission, especially when operating at extremely low bitrates (< 0.1 bpp). Its core challenge is effectively utilizing side information to achieve high-quality reconstruction under strict bitrate budgets. However, existing DIC approaches struggle to exploit global context and object-level details from side information, leading to local blurring and the loss of fine details in the reconstruction. To address these limitations, we propose a Multimodal DIC framework (MDIC), which, for the first time, leverages side information in a multimodal manner into the DIC paradigm, effectively preserving fine-grained local details and enhancing global perceptual quality in reconstructed images. Specifically, we introduce a text-to-image diffusion-based decoder conditioned on textual side information extracted from correlated images to capture shared global semantics. Moreover, we design a feature-mask generator, supervised by a multimodal fine-grained alignment task, to strengthen the exploitation of visual side information. The generated mask serves two purposes: first, it guides the extraction of fine-grained details from losslessly transmitted side information to preserve the semantic consistency of reconstructed details; second, it regulates the extraction of clustered feature representations from the quantized VQ-VAE embeddings, compensating for category information lost under the extreme compression of the primary image. Extensive experiments on the widely used KITTI Stereo and Cityscapes datasets demonstrate that MDIC achieves state-of-the-art perceptual quality at extremely low bitrates.

---


### 73. [COCOTree: A Dataset and Benchmark for Open Tree-Structured Visual Decomposition](https://arxiv.org/abs/2605.22068)

**<font color=#1a73e8>作者：</font>** Junhyub Lee, Seunghun Chae, Hyosu Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We formalize and enable the task of open tree decomposition, which segments an image into hierarchical trees of visual components with unconstrained granularity and flexibility. Specifically, we provide the foundation benchmark for this new paradigm with the following three key contributions. First, we overcome the prohibitively high cognitive and physical bottlenecks of manual annotation by developing a fully automated generation pipeline that synergizes the semantic reasoning of Large Vision-Language Models (LVLMs) with the precise geometric grounding of SAM 3. Second, leveraging this pipeline, we construct COCOTree, a massive-scale benchmark featuring over 21K images and 1.8M structural nodes. By embracing an open-vocabulary space of over 3.5K unique labels, it successfully captures the long-tail distribution of complex physical assemblies. Notably, rigorous human evaluation confirms our generated annotations demonstrate strong alignment with human structural judgment. Third, we establish a standardized evaluation protocol by proposing the Open Tree Quality (OTQ) metric, which jointly assesses mask precision, label accuracy, and structural consistency. We release our dataset and benchmark code at this https URL.

---


### 74. [Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention](https://arxiv.org/abs/2605.22072)

**<font color=#1a73e8>作者：</font>** Changyuan Tian, Zhicong Lu, Huaxing Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has emerged as a promising paradigm for advancing complex reasoning in large language models, and recent work extends RLVR to multimodal large language models (MLLMs). This transfer, however, surfaces a faithfulness challenge: faithful perception of task-relevant visual evidence and faithful use of that evidence during reasoning, leading to unsatisfactory gains on multimodal benchmarks. Specifically, existing perception supervision often operates on textual descriptions rather than natively on image regions, and faithful use is largely overlooked, exposing the perception-reasoning disconnect where correctly perceived evidence is dropped or contradicted during reasoning. To close these gaps, we propose Faithful-MR1, a training framework that anchors and reinforces visual attention to address both halves of faithful multimodal reasoning. The Anchoring stage turns perception into an explicit pre-reasoning subtask, supervising a dedicated <Focus> token's attention directly against image regions rather than through textual descriptions. The Reinforcing stage exposes faithful use through counterfactual image intervention, rewarding answer-correct trajectories that concentrate visual attention where vision causally matters. Extensive experiments demonstrate that Faithful-MR1 outperforms recent multimodal reasoning baselines on both Qwen2.5-VL-Instruct 3B and 7B backbones while using substantially less training data.

---


### 75. [From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning](https://arxiv.org/abs/2605.22074)

**<font color=#1a73e8>作者：</font>** Xitai Jiang, Zihan Tang, Wenze Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) has shown strong promise for LLM reasoning, but outcome-based RLVR remains inefficient on hard problems because correct final-answer rollouts are rare and sample-level credit assignment cannot use partial progress in failed attempts. We introduce SCRL (Subproblem Curriculum Reinforcement Learning), a curriculum RL framework that derives verifiable subproblems from reference reasoning chains and fixes the final subproblem as the original problem. This turns partial progress on hard problems into verifiable learning signals. Algorithmically, SCRL uses subproblem-level normalization, which normalizes rewards independently at each subproblem position and assigns the resulting advantages to the corresponding answer spans, enabling finer-grained credit assignment without external rubrics or reward models. Our analysis shows that subproblem curricula lift hard problems out of gradient dead zones, with larger relative gains as the original problem becomes harder. Across seven mathematical reasoning benchmarks, SCRL outperforms strong curriculum-learning baselines, improving average accuracy over GRPO by +4.1 points on Qwen3-4B-Base and +1.9 points on Qwen3-14B-Base. On AIME24, AIME25, and IMO-Bench, SCRL further improves pass@1 by +3.7 points and pass@64 by +4.6 points on Qwen3-4B-Base, indicating better exploration on hard reasoning problems.

---


### 76. [Enhancing Visual Token Representations for Video Large Language Models via Training-Free Spatial-Temporal Pooling and Gridding](https://arxiv.org/abs/2605.22078)

**<font color=#1a73e8>作者：</font>** Bingjun Luo, Tony Wang, Hanqi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have significantly advanced video understanding tasks, yet challenges remain in efficiently compressing visual tokens while preserving spatiotemporal interactions. Existing methods, such as LLaVA family, utilize simplistic pooling or interpolation techniques that overlook the intricate dynamics of visual tokens. To bridge this gap, we propose ST-GridPool, a novel training-free visual token enhancement method designed specifically for Video LLMs. Our approach integrates Pyramid Temporal Gridding (PTG), which captures multi-grained spatiotemporal interactions through hierarchical temporal gridding, and Norm-based Spatial Pooling (NSP), which preserves high-information visual regions by leveraging the correlation between token norms and semantic richness. Extensive experiments on various benchmarks demonstrate that ST-GridPool consistently enhances performance of Video LLMs without requiring costly retraining. Our method offers an efficient and plug-and-play solution for improving visual token representations. Our code is available in this https URL.

---


### 77. [JMed48k: A Multi-Profession Japanese Medical Licensing Benchmark for Vision-Language Model Evaluation](https://arxiv.org/abs/2605.22080)

**<font color=#1a73e8>作者：</font>** Yue Xun, Junyu Liu, Qian Niu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce JMed48k, a multi-profession Japanese healthcare licensing benchmark for evaluating vision-language models. Built from official PDF materials released by the Japanese Ministry of Health, Labour and Welfare, JMed48k contains 48,862 exam questions and 20,142 images from 11 national licensing examinations between 2005 and 2025, with visual content annotated under an 8-type taxonomy. From this corpus, we derive JMed48k-Eval, a recent five-year evaluation subset with 12,484 scored questions, including 9,905 text-only questions and 2,579 questions with images. We evaluate 21 proprietary, open-source, and medical-specific models, reporting text-only and with-image performance separately. Because these subsets contain different questions, we further introduce a paired image-removal audit that evaluates questions with images before and after removing visual content to explore four answer-transition states. The audit shows that proprietary and open source models gain substantially from images, whereas medical-specific systems show limited observable use of visual evidence, with many correct answers persisting after image removal. Even among proprietary models, the net image-removal effect varies sevenfold across professions, from +5.7 points on Physician questions to +39.8 points on Public Health Nurse questions. We release JMed48k to support reproducible, profession-stratified evaluation of vision-language models in medical licensing settings.

---


### 78. [A Camera-Cooperative ISAC Framework for Multimodal Non-Cooperative UAVs Sensing](https://arxiv.org/abs/2605.22090)

**<font color=#1a73e8>作者：</font>** Wenfeng Wu, Luping Xiang, Kun Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The detection of non-cooperative unmanned aerial vehicles (UAVs) presents significant challenges for Integrated Sensing and Communication (ISAC) systems due to the inherent limitations of single-modal perception and the competition for shared communication and sensing resources. To address these challenges, this paper proposes a novel Camera-Cooperative ISAC (CC-ISAC) framework that employs multimodal sensing to enable efficient UAV beam steering and tracking. The proposed framework employs cameras for coarse-grained airspace monitoring and utilizes ISAC for fine-grained, high-precision sensing, forming a complementary perception loop that enhances both sensing accuracy and resource efficiency. Within this framework, two key modules are developed: (1) a Vision-to-Echo Data Alignment (V2EDA) model that aligns visual and echo-domain features through cross-attention mechanisms, and (2) a Multimodal Fusion-Based Estimation (MMFE) model that integrates historical multimodal data with current observations for robust state estimation. Extensive evaluations conducted on the DeepSense 6G dataset demonstrate that the proposed framework achieves an average reduction of 71% in beam steering overhead and 1.69-11.15% in tracking overhead while maintaining high angular estimation accuracy. The CC-ISAC framework effectively mitigates resource contention between sensing and communication, enabling reliable UAV surveillance while freeing substantial system resources for additional communication tasks, thereby representing a practical advancement in ISAC system design.

---


### 79. [Narrative Sharpens Gender Gaps: Surveying Film Characters with LLM Agents](https://arxiv.org/abs/2605.22091)

**<font color=#1a73e8>作者：</font>** Vivienne Bihe Chi, Reyhan Jamalova, Lyle Ungar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mainstream film is one of the richest sources of cultural content that AI systems learn from. Yet we have few tools for measuring the gender values it encodes. We present a proof-of-concept framework that turns fictional film characters into surveyable LLM agents. Using 160 U.S. films (1990--2019), we build 734 character agents from script dialogue and scene descriptions, condense their personas via expert-style reflections, and simulate World Values Survey gender-attitude responses. Agents reproduce systematic gender differences without explicit demographic prompting, suggesting attitudes emerge from behavior rather than identity labels. Benchmarked against historical survey data, agents exaggerate gender gaps and show greater decade-to-decade volatility than real populations. Narrative sharpens rather than homogenizes gender contrasts, complicating the consistent-input assumption underlying cultivation theory's mainstreaming mechanism. AI systems trained on such corpora may inherit this stylization before any model-level amplification occurs.

---


### 80. [VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection -- after competition results](https://arxiv.org/abs/2605.22096)

**<font color=#1a73e8>作者：</font>** Bo-Cheng Qiu, Fang-Ying Lin, Ming-Han Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capsule endoscopy event detection is challenging because clinically relevant findings are sparse, visually heterogeneous, and evaluated at the event level rather than by frame accuracy. We propose VISTA, a metric-aligned multi-backbone framework for the RAREVISION task. VISTA combines EndoFM-LV for temporal context and DINOv3 ViTL/16 for frame-level visual semantics, followed by a Diverse Head Ensemble (DHE), Validation-Guided Weighted Fusion (VGWF), and Anatomy-Aware Temporal Event Decoding (ATED). The original official submission achieved hidden-test temporal mAP@0.5 of 0.3530 and mAP@0.95 of 0.3235. After the competition, extending local threshold refinement with a global coarse search improved performance to 0.3726 mAP@0.5 and 0.3431 mAP@0.95, ranking Team ACVLab second in the post-competition evaluation.

---


### 81. [A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering](https://arxiv.org/abs/2605.22099)

**<font color=#1a73e8>作者：</font>** Sereiwathna Ros, Phannet Pov, Ratanaktepi Chhor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a promising paradigm for grounding large language model (LLM) outputs in retrieved evidence, thereby reducing hallucination and improving factual accuracy. Its efficacy, however, remains largely unexamined for low-resource, non-Latin-script languages such as Khmer. In this paper, we present a RAG-based question answering system for Khmer-language telecom-domain documents. We conduct a two-phase comparative evaluation. First, we benchmark three embedding models: BGE-M3 (567M), Jina-Embeddings-v3 (570M), and Qwen3-Embedding (597M), for dense retrieval over Khmer documents. BGE-M3 consistently performs best, achieving a Hit Rate@3 of 0.285, File Hit Rate@3 of 0.700, MRR@3 of 0.221, and Precision@3 of 0.112, substantially outperforming the other retrievers. Second, using BGE-M3 as the selected retriever, we evaluate five generator backends: Qwen3 (8B), Qwen3.5 (9B), Sailor2-8B-Chat, SeaLLMs-v3-7B-Chat, and Llama-SEA-LION-v2-8B-IT, on a curated golden dataset of 200 Khmer question-answer pairs. To quantify system performance, we apply six RAGAS-inspired metrics: faithfulness, answer relevance, context relevance, factual correctness, answer similarity, and answer correctness. The results show no single model dominates across all metrics: Qwen3.5-9B achieves the highest faithfulness (0.859) and context relevance (0.726), Qwen3-8B attains the highest factual correctness (0.380), and SeaLLMs-v3-7B-Chat performs best on answer relevance (0.867), answer similarity (0.836), and answer correctness (0.599). These findings highlight that retriever choice remains a major bottleneck for Khmer RAG, while generator strengths vary depending on whether the priority is grounding, factual precision, or semantic similarity.

---


### 82. [ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling](https://arxiv.org/abs/2605.22102)

**<font color=#1a73e8>作者：</font>** Woomin Song, Beomjun Kim, Daewon Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common failure mode in long-horizon agentic test-time scaling is error propagation, where factual errors or invalid deductions introduced at intermediate steps persist in the agent's belief state and contaminate later reasoning. Existing test-time scaling methods provide limited control over this process, as they often rely on agents to detect their own mistakes, select among flawed trajectories, or refine solutions only after errors have already shaped the reasoning path. We propose ExComm, a communication protocol for exploration-stage agentic test-time scaling. ExComm is motivated by the empirical observation that the majority of intermediate errors in parallel agentic reasoning produce detectable cross-agent factual conflicts. Leveraging the iterative structure of agentic workflows, ExComm periodically audits agent belief states to detect such conflicts, resolves them through a dedicated tool-based verification loop, and returns concise, targeted feedback to the involved agents. Corrections are incorporated through soft belief updates, which append verified feedback rather than overwriting existing beliefs. Furthermore, to prevent collapsing trajectory diversity due to communication, ExComm further introduces a trajectory diversification module that redirects redundant trajectories toward orthogonal strategies. Experiments on AIME 2024, AIME 2025, and GAIA with Gemini-2.5-Flash-Lite and Qwen3.5-4B show that ExComm consistently outperforms strong test-time scaling baselines, achieving average performance gains of 5.7% and 5.0% over the best-performing baselines, respectively. Further analyses demonstrate improved error recovery, favorable scaling behavior, stronger diversity than adapted communication baselines, and the best performance-cost trade-off among the evaluated methods.

---


### 83. [ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning](https://arxiv.org/abs/2605.22106)

**<font color=#1a73e8>作者：</font>** Yeqiu Chen, Ziyan Liu, Zhenxin Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in LLM reasoning has increasingly shifted from single-pass generation to explicit search over intermediate reasoning states. Tree-of-Thoughts (ToT) organizes inference to tree-structured search with branching and backtracking, but it substantially amplifies the Key--Value (KV) cache: retaining KV states for a frontier of partial trajectories quickly becomes a memory bottleneck that limits throughput and constrains search depth and width under fixed hardware budgets. We address this challenge by observing that KV reuse in ToT-style inference is governed by search dynamics: near-term decoding depends primarily on the active branch and its ancestors, whereas inactive subtrees have low short-term reuse probability yet must remain recoverable for backtracking. Motivated by this, we propose ArborKV, a structure-aware eviction framework that couples a lightweight value estimator with a tree-aware allocation policy, and performs purely token-extractive eviction with lazy rehydration to support revisits. Experiments on ToT-style reasoning benchmarks show that ArborKV achieves up to ~4x peak KV-memory reduction while preserving near-full-retention accuracy, enabling larger search configurations under fixed device budgets that would otherwise run out of memory.

---


### 84. [Perception or Prejudice: Can MLLMs Go Beyond First Impressions of Personality?](https://arxiv.org/abs/2605.22109)

**<font color=#1a73e8>作者：</font>** Caixin Kang, Tianyu Yan, Sitong Gong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly deployed in human-facing roles where personality perception is critical, yet existing benchmarks evaluate this capability solely on numerical Big Five score prediction, leaving open whether models truly perceive personality through behavioral understanding or merely prejudge through superficial pattern matching. We address this gap with three contributions. (i) A new task: we formalize Grounded Personality Reasoning (GPR), which requires MLLMs to anchor each Big Five rating in observable evidence through a chain of rating, reasoning, and grounding. (ii) A new dataset: we release MM-OCEAN (1,104 videos, 5,320 MCQs), produced by a multi-agent pipeline with human verification, with timestamped behavioral observations, evidence-grounded trait analyses, and seven categories of cue-grounding MCQs. (iii) Benchmark and analysis: we design a three-tier evaluation (rating, reasoning, grounding) plus four sample-level failure-mode metrics: Prejudice Rate (PR), Confabulation Rate (CR), Integration-failure Rate (IR), and Holistic-grounding Rate (HR), and benchmark 27 MLLMs (13 closed, 14 open). The analysis uncovers a striking Prejudice Gap: across the field, 51% of correct ratings are not grounded in retrieved cues, and the Holistic-Grounding Rate spans only 0-33.5%. These findings expose a disconnect between getting the right score and reasoning for the right reason, charting a roadmap for grounded social cognition in MLLMs.

---


### 85. [Accelerating Vision Foundation Models with Drop-in Depthwise Convolution](https://arxiv.org/abs/2605.22132)

**<font color=#1a73e8>作者：</font>** Carmelo Scribano, Mohammad Mahdi, Nedyalko Prisadnikov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision foundation models deliver strong performance across tasks with limited fine-tuning. However, their Vision Transformer (ViT) backbones impose high inference costs, limiting deployment on resource-constrained devices. In this work, we accelerate large-scale pretrained ViTs while preserving their feature extraction capabilities by exploiting the intrinsic convolution-like behavior of some attention heads. Specifically, we introduce an efficient depthwise convolution-based layer that serves as a drop-in replacement for these heads. Additionally, we propose simple strategies to identify which heads can be replaced and introduce a fine-tuning procedure that recovers downstream task performance. Across both image classification and segmentation tasks, our method achieves 17-20\% percent inference speedup with minimal performance degradation. We validate the approach through detailed derivations, extensive experiments, and efficiency benchmarks. The reference implementation is publicly available.

---


### 86. [Cross-Lingual Consensus: Aligning Multilingual Cultural Knowledge via Multilingual Self-Consistency](https://arxiv.org/abs/2605.22137)

**<font color=#1a73e8>作者：</font>** Andrew Ivan Soegeng, Patrick Sutanto, Tan Sang Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) demonstrate strong capabilities across various tasks, they exhibit significant performance discrepancies across languages. While prompting LLMs in English typically yields the highest general performance, it often induces a Western-centric bias, hindering the model's ability to accurately reflect diverse cultural knowledge. We hypothesize that LLMs already possess rich cultural knowledge embedded within local-language representations, but fail to retrieve it when prompted in English. To bridge this cross-lingual knowledge gap, we propose a novel self-supervised framework. Our method leverages multilingual self-consistency to identify the most reliable cultural responses across languages, combined with a self-critique mechanism to transfer this knowledge to the weaker language. Evaluations on the BLEnD benchmark demonstrate that our approach significantly improves cultural alignment-boosting performance on English queries by an average of 5.03%-relying entirely on self-generated data. Ultimately, our work demonstrates that latent cultural knowledge can be successfully surfaced and propagated across languages, enabling more culturally equitable and consistent LLMs.

---


### 87. [Efficient Agentic Reasoning Through Self-Regulated Simulative Planning](https://arxiv.org/abs/2605.22138)

**<font color=#1a73e8>作者：</font>** Mingkai Deng, Jinyu Hou, Lara Sá Neves 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How should an agent decide when and how to plan? A dominant approach builds agents as reactive policies with adaptive computation (e.g., chain-of-thought), trained end-to-end expecting planning to emerge implicitly. Without control over the presence, structure, or horizon of planning, these systems dramatically increase reasoning length, yielding inefficient token use without reliable accuracy gains. We argue efficient agentic reasoning benefits from decomposing decision-making into three systems: simulative reasoning (System II) grounding deliberation in future-state prediction via a world model; self-regulation (System III) deciding when and how deeply to plan via a learned configurator; and reactive execution (System I) handling fine-grained action. Simulative reasoning provides unified planning across diverse tasks without per-domain engineering, while self-regulation ensures the planner is invoked only when needed. To test this, we develop SR$^2$AM (Self-Regulated Simulative Reasoning Agentic LLM), realizing both as distinct stages within an LLM's chain-of-thought, with the LLM as world model. We explore two instantiations: recording decisions from a prompted multi-module system (v0.1) and reconstructing structured plans from traces of pretrained reasoning LLMs (v1.0), trained via supervised then reinforcement learning (RL). Across math, science, tabular analysis, and web information seeking, v0.1-8B and v1.0-30B achieve Pass@1 competitive with 120-355B and 685B-1T parameter systems respectively, while v1.0-30B uses 25.8-95.3% fewer reasoning tokens than comparable agentic LLMs. RL increases average planning horizon by 22.8% while planning frequency grows only 2.0%, showing it learns to plan further ahead rather than more often. More broadly, learned self-regulation instantiates a principle we expect to extend beyond planning to how agents govern their own learning and adaptation.

---


### 88. [Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents](https://arxiv.org/abs/2605.22148)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Yanwei Cui, Guanghui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving skill libraries, pioneered by Voyager, let frozen LLM agents accumulate reusable knowledge without weight updates, yet recent evaluation shows that LLM-authored skills deliver $+0.0$pp over no-skill baselines while human-curated ones deliver $+16.2$pp: the bottleneck is not skill authoring but lifecycle management. We introduce \textbf{Ratchet}, a single-agent loop in which a frozen LLM writes, retrieves, curates, and retires its own natural-language skills. Ratchet integrates four candidate hygiene mechanisms: outcome-driven retirement, a bounded active-cap, meta-skill authoring guidance, and pattern canonicalisation. On MBPP+ hard-100 with Claude Opus 4.7, Ratchet lifts held-out pass@1 from a $0.258 \pm 0.047$ baseline to a late-window rolling mean of $0.584$ (peak $0.658 \pm 0.042$) across 100 rounds and 3 seeds, a $+0.328 \pm 0.018$ rolling-mean gain where the no-skill control drifts at $+0.002 \pm 0.005$; the same recipe transfers to an agentic solver on SWE-bench Verified ($+0.22$ peak lift over 20 rounds). Eight ablations (A1--A8) reveal that the minimal working recipe is smaller than our design suggests: retirement and the meta-skill authoring prior are load-bearing, while explicit deduplication (canonicalisation, cover-guard) is subsumed by the meta-skill itself. A non-divergence proposition shows that bounded cap and retirement threshold together prevent expected performance from drifting below the no-skills floor.

---


### 89. [IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents](https://arxiv.org/abs/2605.22154)

**<font color=#1a73e8>作者：</font>** Daewon Choi, Kyunghyun Park, Woomin Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents solve complex tasks by leveraging multi-step reasoning with iterative tool calls and environment interactions, which incur idle time while waiting for observations. Despite the prevalence of idle time in most agentic scenarios, existing works treat it as an unavoidable overhead or propose restricted solutions that overlook varying computational budgets across different tool calls and future observation uncertainty, thereby leading to suboptimal utilization of idle time. In this paper, we introduce IdleSpec, a scalable and generic inference approach that leverages idle-time computation to improve agent performance while minimizing latency overhead. Specifically, IdleSpec iteratively generates plan candidates during idle periods and, once observations become available, aggregates them to guide the next reasoning step. For effective plan generation under observation uncertainty, IdleSpec samples between complementary drafting strategies (i.e., progressive and recovery) from a learned distribution that is updated via posterior feedback. Our experiments demonstrate that IdleSpec significantly improves agent performance in various agentic scenarios by effectively utilizing idle time. In particular, on the GAIA and FRAMES, IdleSpec achieves 55.6% average accuracy with Gemini-2.5-Flash, surpassing the vanilla baseline without idle-time usage by 5.1%. Furthermore, for MLE-Bench, which involves substantial delay from code executions, IdleSpec achieves performance gains of up to 9.1% on the Any Medal rate, highlighting its generalizability to long-horizon tasks.

---


### 90. [One-Way Policy Optimization for Self-Evolving LLMs](https://arxiv.org/abs/2605.22156)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Jinda Lu, Kexin Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has become a promising paradigm for scaling reasoning capabilities of Large Language Models (LLMs). However, the sparsity of binary verifier rewards often leads to low efficiency and optimization instability. To stabilize training, existing methods typically impose token-level constraints relative to a reference policy. We identify that such constraints penalize deviations indiscriminately; this can flip verifier-determined direction when the policy attempts to outperform the reference, thereby suppressing gains. To resolve this, we propose One-Way Policy Optimization (OWPO), a method based on the principle of decoupling optimization direction from update magnitude. In OWPO, the verifier dictates the update direction, while the reference policy serves only to adjust the magnitude. Specifically, OWPO applies asymmetric reweighting: it performs Accelerated Alignment for inferior deviations (where the policy lags behind the reference) and Gain Locking for superior deviations (where the policy surpasses the reference). Furthermore, by incorporating iterative reference updates, OWPO creates a ``Ratchet Effect'' that continuously consolidates gains. Experimental results demonstrate that OWPO outperforms strong baselines, including DAPO, OPD, and MOPD, breaking the bottleneck of fixed priors to enable continuous self-evolution without reliance on external reference models.

---


### 91. [ST-SimDiff: Balancing Spatiotemporal Similarity and Difference for Efficient Video Understanding with MLLMs](https://arxiv.org/abs/2605.22158)

**<font color=#1a73e8>作者：</font>** Bingjun Luo, Tony Wang, Chaoqi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) face significant computational overhead when processing long videos due to the massive number of visual tokens required. To improve efficiency, existing methods primarily reduce redundancy by pruning or merging tokens based on importance or similarity. However, these approaches largely overlook a critical dimension of video content, i.e., changes and turning points, and they lack a collaborative model for spatio-temporal relationships. To address this, we propose a new perspective: similarity is for identifying redundancy, while difference is for capturing key events. Based on this, we designed a training-free framework named ST-SimDiff. We first construct a spatio-temporal graph from the visual tokens to uniformly model their complex associations. Subsequently, we employ a parallel dual-selection strategy: 1) similarity-based selection uses community detection to retain representative tokens, compressing static information; 2) temporal difference-based selection precisely locates content-changing points to preserve tokens that capture key dynamic shifts. This allows it to preserve both static and dynamic content with a minimal number of tokens. Extensive experiments show our method significantly outperforms state-of-the-art approaches while substantially reducing computational costs. Our code is available in this https URL.

---


### 92. [Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics](https://arxiv.org/abs/2605.22164)

**<font color=#1a73e8>作者：</font>** Liangyu Li, Shengzhi Wang, Qingwen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models can contain the state needed for control, yet their terminal-cost interface can expose the planner to the wrong decision-relevant information. In common latent MPC, candidate sequences are ranked by Euclidean distance between predicted terminal and goal latent states; this assumes that raw latent distance weights reachability-relevant variables correctly. We propose trajectory reachability metrics (TRM), a post-hoc terminal-ranking method for fixed latent world models. TRM trains a small pairwise head from logged trajectory structure and uses it as a replacement or hybrid cost; the encoder, dynamics, sampler, optimizer, and evaluation manifests remain fixed. The key design choice is horizon-aware supervision: the metric is trained on broad, balanced temporal separations to match the long-horizon terminal candidate ranking problem. On a hard TwoRoom benchmark, raw latent planning with LeWorldModel (LeWM) reaches 7.0% success, while full-horizon TRM reaches 97.0%; shuffled temporal-label controls stay at 0.0%. The same recipe improves a PLDM baseline from 32.7% to 84.0% across three seeds, and a short-horizon TRM variant reaches only 35.0% with the 100,000 pair budget. In TwoRoom, we provide mechanistic evidence for why TRM works: XY position is linearly decodable (R^2=0.998), yet raw latent MSE misranks candidates; the XY-probe rowspace accounts for less than 1% of terminal-goal latent MSE but carries most candidate-quality signal; and SCSA audits show that TRM improves the ordering and selected endpoint seen by the planner. On PushT go50/go75, TRM-style task-state metrics improve SCSA ranking and selected final distance more cleanly than closed-loop success, motivating auxiliary hybrid costs in continuous manipulation. TRM is the planner-facing repair, and audits explain when terminal reachability metrics should replace or augment raw latent proximity.

---


### 93. [Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents](https://arxiv.org/abs/2605.22166)

**<font color=#1a73e8>作者：</font>** Tianshi Xu, Huifeng Wen, Meng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are shaped not only by their language models, but also by the runtime harness that mediates observation, tool use, action execution, feedback interpretation, and trajectory control. While existing agent adaptation methods mainly update model parameters, many failures in deterministic, rule-governed domains stem from mismatches at the model--environment interface. We propose Life-Harness, a lifecycle-aware runtime harness that improves frozen LLM agents without changing model weights or evaluation environments. Life-Harness evolves from training trajectories by converting recurring interaction failures into reusable interventions across environment contracts, procedural skills, action realization, and trajectory regulation, and remains fixed during held-out evaluation. On seven deterministic environments from $\tau$-bench, $\tau^2$-bench, and AgentBench, Life-Harness improves 116 out of 126 model--environment settings across 18 model backbones, with an average relative improvement of 88.5%. Harnesses evolved only from Qwen3-4B-Instruct trajectories transfer to 17 other models, showing that Life-Harness captures reusable environment-side structure rather than model-specific behavior. These results position runtime interface adaptation as a complementary alternative to model-centric agent training. Code is available at GitHub.

---


### 94. [Balancing Uncertainty and Diversity of Samples: Leveraging Diversity of Least, High Confidence Samples for Effective Active Learning](https://arxiv.org/abs/2605.22169)

**<font color=#1a73e8>作者：</font>** Vipul Arya, S.H. Shabbeer Basha, Srikrishna U N 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models, including Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs), have achieved state-of-the-art performance on various computer vision tasks such as object classification, detection, segmentation, generation, and many more. However, these models are data-hungry as they require more training data to learn millions or billions of parameters. Especially for supervised learning tasks, curating a large number of labeled samples for model training is an expensive and time-consuming task. Active Learning (AL) has been used to address this problem for many years. Existing active learning methods aim at choosing the samples for annotation from a pool of unlabeled samples that are either diverse or uncertain. Choosing such samples may hinder the model's performance as we pool based on one dimension, i.e., either diverse or uncertain. In this paper, we propose four novel hybrid sampling methods for pooling both easy and hard samples, which are also diverse. To verify the efficacy of the proposed methods, extensive experiments are conducted using high and low-confidence samples separately. We observe from our experiments that the proposed hybrid sampling method, Least Confident and Diverse (LCD), consistently performs better compared to state-of-the-art methods. It is observed that selecting uncertain and diverse instances helps the model learn more distinct features. The codes related to this study will be available at this https URL.

---


### 95. [Do Factual Recall Mechanisms Carry over from Text to Speech in Multimodal Language Models?](https://arxiv.org/abs/2605.22170)

**<font color=#1a73e8>作者：</font>** Luca Modica, Filip Landin, Mehrdad Farahani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, several Speech Language Models (SLMs) that represent speech and written text jointly have been presented. The question then emerges about how model-internal mechanisms are similar and different when operating in the two modalities. We focus on how these systems encode, store, and retrieve factual knowledge, which has previously been investigated for text-only models. To investigate mechanisms behind the storage and recall of factual association in SLMs, we leverage Causal Mediation Analysis, a technique previously applied to text-based models.
Initial results using SpiritLM, a multimodal model integrating discrete speech tokens reveal discrepancies between text-to-text and speech-to-text results, suggesting that the emergent mechanisms for factual recall are only partially carried over from the text to the speech modality. These results advance our understanding of how internal mechanisms encode factual associations in SLMs while contributing insights for improving speech-enabled AI systems.

---


### 96. [LLM-Metrics: Measuring Research Impact Through Large Language Model Memory](https://arxiv.org/abs/2605.22176)

**<font color=#1a73e8>作者：</font>** Si Shen, Wenhua Zhao, Danhao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Citation counts remain the dominant metric for assessing research impact, yet they suffer from well-documented limitations: temporal lag, disciplinary bias, and Matthew effects. Here we propose LLM-Metrics, a research-impact assessment metric derived from the parametric memory of large language models (LLMs). The central hypothesis is that high-impact papers receive greater exposure in the academic community, that this exposure enters LLM training data in textual form, and that models consequently form stronger parametric memory of these papers. We designed four types of multiple-choice probes, covering title recognition, author recognition, method recognition, and venue recognition, and evaluated 549 computer science papers published in 2023-2024 across 17 LLMs spanning 0.5B to 72B parameters from six vendors. Of the 17 models, 15 produced positive predictions, 9 of which were significant at p less than 0.05, with an overall Spearman correlation of rho = 0.1495 and p = 0.0004 against citation counts. Three additional findings support the proposed mechanism. First, the predictive signal was stronger for 2024 papers, rho = 0.1880, whose citation counts were near zero at model-training time, reducing the plausibility of a simple reverse-causality explanation. Second, author-recognition probes showed the strongest discriminative power, consistent with an exposure-driven memory mechanism. Third, model scale and predictive power were non-monotonic: a 3B-parameter model, Llama-3.2-3B-Instruct, with rho = 0.1829, outperformed most larger models, supporting a selective-memory hypothesis in which the limited capacity of smaller models can serve as an effective information filter. LLM-Metrics offers a real-time, cross-disciplinary, citation-independent paradigm for research assessment.

---


### 97. [Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles](https://arxiv.org/abs/2605.22177)

**<font color=#1a73e8>作者：</font>** Jinyang Wu, Guocheng Zhai, Ruihan Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The proliferation of large language models (LLMs) and modular skills has endowed autonomous agents with increasingly powerful capabilities. Existing frameworks typically rely on monolithic LLMs and fixed logic to interface with these skills. This gives rise to a critical bottleneck: different LLMs offer distinct advantages across diverse domains, yet current frameworks fail to exploit the complementary strengths of models and skills, thereby limiting their performance on downstream tasks. In this paper, we present Maestro (Multimodal Agent for Expert-Skill Targeted Reinforced Orchestration), a Reinforcement Learning (RL)-driven orchestration framework that reframes heterogeneous multimodal tasks as a sequential decision-making process over a hierarchical model-skill registry. Rather than consolidating all knowledge into a single model, Maestro trains a lightweight policy to dynamically compose ensembles of frozen expert models and a two-tier skill library, deciding at each step whether to invoke an external expert, which model-skill pair to select, and when to terminate. The policy is optimized via outcome-based RL, requiring no step-level supervision. We evaluate Maestro across ten representative multimodal benchmarks spanning mathematical reasoning, chart understanding, high-resolution perception, and domain-specific analysis. With only a 4B orchestrator, Maestro achieves an average accuracy of 70.1%, surpassing both GPT-5 (69.3%) and Gemini-2.5-Pro (68.7%). Crucially, the learned coordination policy generalizes to unseen models and skills without retraining: augmenting the registry with out-of-domain experts yields a 59.5% average on four challenging benchmarks, outperforming all closed-source baselines. Maestro further maintains high computational efficiency with low latency. The source code is available at this https URL.

---


### 98. [Enhancing Multimodal Large Language Models for Safety-Critical Driving Video Analysis](https://arxiv.org/abs/2605.22185)

**<font color=#1a73e8>作者：</font>** Tomaso Trinci, Henrique Piñeiro Monteagudo, Leonardo Taccari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in general visual understanding. However, their application to safety-critical driving scenarios remains limited by an inability to accurately perceive and reason about rare high-stakes dynamic events, such as collisions or near-collisions. To address this, we introduce a pipeline that enhances MLLM perception by fusing downsampled video frames with synchronized high-frequency telematics data (IMU and GPS) and semantic insights from specialized computer vision models. Our pipeline generates high-quality pseudo-labels, including descriptive captions and question-answer pairs, specifically designed to train MLLMs to identify and describe Safety-Critical Events (SCEs) in real-world driving footage. We show the effectiveness of our approach fine-tuning the open-source QwenVL-2.5 model via DoRA adapters: our experiments demonstrate significant improvements in identifying and explaining safety-critical events, with fewer than 50M trainable parameters and limited computational budget.

---


### 99. [Reinforced Graph of Thoughts: RL-Driven Adaptive Prompting for LLMs](https://arxiv.org/abs/2605.22195)

**<font color=#1a73e8>作者：</font>** Manuel Noah Riesen, Peter Alfred von Niederhäusern  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph of Thoughts (GoT), a generalized form of recent prompting paradigms for large language models (LLMs), has been shown to be useful for elaborate problem solving. By executing a graph of operations, thoughts of the LLM are structured as an arbitrary graph, forming the actual graph of thoughts. Originally, the graph of operations is defined manually, which requires in-depth knowledge about the solution of the problem to solve. Such a static graph of operations is rigid and therefore lacks adaptability. We propose Reinforced Graph of Thoughts (RGoT), an automated approach to the GoT prompting paradigm that leverages reinforcement learning (RL) to adaptively generate a graph of operations from a human-defined set. Results indicate that, under certain constraints, it is possible to construct graphs of operations adaptively to the task's complexity in an automated way.

---


### 100. [Skill Weaving: Efficient LLM Improvement via Modular Skillpacks](https://arxiv.org/abs/2605.22205)

**<font color=#1a73e8>作者：</font>** Zhuo Li, Guodong Du, Zesheng Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly require specialization across diverse domains, yet existing approaches struggle to balance multi-domain capacities with strict memory and inference constraints. In this work, we introduce SkillWeave, a modular improvement framework that enables LLMs to specialize under fixed memory budgets. SkillWeave partitions full capabilities of a general-purpose model into skillpacks -- lightweight, domain-specific delta modules -- that reorganize and refine the model's internal knowledge. For efficient deployment, SkillWeave integrates SkillZip to compress skillpacks into compact and inference-ready format, enabling strong multi-domain performance with low-latency execution. On multi-task and agentic benchmarks, a 9B SkillWeave model outperforms several baselines and even surpasses a 32B monolithic LLM, while achieving up to 4x speedup.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-162](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
