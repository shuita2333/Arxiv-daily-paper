# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **117** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-117](./part-03.md)

---

### 51. [Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large Language Model Agents](https://arxiv.org/abs/2608.06861)

**<font color=#1a73e8>作者：</font>** Hongxi Yan, Ziyue Huang, Shichao Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training large language model agents in long-horizon environments requires assigning credit from sparse terminal outcomes to individual actions. Existing critic-free methods propagate trajectory-level rewards uniformly across steps, while recent approaches construct step-level groups by matching repeated states and compare actions within each group. The former cannot distinguish useful actions in failed trajectories from ineffective actions in successful ones. The latter rely on step credit derived directly from individual trajectory outcomes and fixed-weight fusion with episode-level credit. We propose Gated-BEPO, which derives step-level credit from empirical rollout graphs. For each rollout group, Gated-BEPO constructs an empirical graph and estimates node values through a mean-backup Bellman fixed point that reflects the empirical action distribution of the current policy. We then accumulate these temporal-difference residuals along each sampled trajectory using generalized advantage estimation, yielding step-level Bellman advantages that capture both immediate and downstream effects. To adaptively fuse episode- and step-level credit, a confidence gate incorporates Bellman credit only at states with multiple observed successors and otherwise uses episode-level credit. Experiments on WebShop, ALFWorld, and visual Sokoban show consistent improvements across language and vision-language models, while diagnostic ablations support the effectiveness of Bellman fixed-point value estimation and show that step-level credit should be incorporated selectively rather than uniformly into the final advantage.

---


### 52. [Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection](https://arxiv.org/abs/2608.06865)

**<font color=#1a73e8>作者：</font>** Xuechao Zou, Shun Zhang, Kai Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The malicious use of generative artificial intelligence to create highly realistic deepfake videos raises serious ethical concerns and poses substantial challenges to AI safety. However, existing deepfake video benchmarks provide limited coverage of recent synthesis methods and generally lack reliable fine-grained textual annotations. Meanwhile, conventional detectors and multimodal large language models (MLLMs), whether operating as a single model or relying on a single analytical perspective, often fail to capture subtle forgery artifacts, limiting their generalization to emerging AI-generated methods. To address these limitations, we introduce FaceVid-Forensics-100K, a large-scale deepfake video dataset comprising 100,000 videos and spanning 33 synthesis methods across face swapping, face reenactment, and entire-face synthesis, including recent generators such as Seedance 2.0. The dataset provides fine-grained textual annotations of visual observations and verdict-consistent forensic explanations, automatically synthesized through a multi-model aggregation and conflict-resolution pipeline powered by advanced MLLMs. Building on this benchmark, we propose a multi-agent forensic reasoning framework that employs four specialized domain-expert agents to independently analyze forgery cues from four perspectives: texture, lighting, motion, and physics. A judge agent then reconciles their reports to produce a final prediction together with an explanation. Extensive evaluations on out-of-domain test sets show that, despite being composed entirely of small open-source MLLMs, our framework outperforms all methods including closed-source GPT and Gemini models and ranks first across all reported metrics on this benchmark. The project page is available at this https URL.

---


### 53. [LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers](https://arxiv.org/abs/2608.06867)

**<font color=#1a73e8>作者：</font>** Tao Feng, Fangxu Yu, Haozhen Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> No single large language model (LLM) is optimal across all queries and budget constraints, making model routing essential for cost-effective deployment. Existing routers adopt diverse formulations and implementations, making fair comparison and extension difficult. We present a unified formulation of LLM routing as a sequential decision process characterized by five components: context encoders, model encoders, scoring functions, decision rules, and learning signals, covering single-turn, multi-turn, and personalized routing. Based on this formulation, we develop an automated pipeline for constructing routing supervision and evaluating routers jointly on response quality and inference cost. The resulting benchmark, xRouteBench, spans generic LLM, memory-augmented, vision, time-series, and personalized routing tasks. We further introduce LLMRouter, an open-source modular infrastructure with more than 16 representative routers. Our empirical study shows that learned routers outperform the strongest fixed-model baseline by 14.6% relatively, lightweight routers become more competitive under tight cost constraints, and user-conditioned routing consistently improves personalization.

---


### 54. [FedVAR: Prototype-Aligned Federated Framework for Video Anomaly Recognition](https://arxiv.org/abs/2608.06876)

**<font color=#1a73e8>作者：</font>** Ghani Haider, Majid Kundroo, Boyun Eom 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the era of Industrial Internet of Things (IIoT) and Cyber-Physical Systems (CPS), Federated Learning (FL) offers a promising decentralized intelligence paradigm for Video Anomaly Recognition (VAR). This task is vital for maintaining high-fidelity Digital Twins and ensuring safety in mission-critical environments. However, the inherent data heterogeneity across distributed edge clients leads to a fundamental challenge known as semantic misalignment, where clients learn divergent feature representations of "normal" and "abnormal" events. The problem becomes particularly pronounced in VAR, where the presence of diverse and fine-grained anomaly categories leads each client to develop distinct semantic interpretations of abnormality. Existing federated methods primarily focus on binary anomaly detection and fail to address this misalignment, preventing effective fine-grained recognition. In this paper, we introduce FedVAR, a weakly-supervised FL framework explicitly designed for VAR. Leveraging the rich representations of Vision-Language Models (VLMs), FedVAR employs a prototype-based alignment mechanism that creates a shared semantic anchor for all clients to re-center and align their visual and textual feature spaces. This process enforces a consistent representation of "normality" across the decentralized network, directly mitigating semantic misalignment and enabling robust prompt-learning of anomaly direction vectors with minimal communication overhead. We conduct extensive experiments on challenging benchmarks under various non-IID data partitioning schemes, unseen domains, and novel anomaly classes. The results demonstrate that FedVAR consistently outperforms state-of-the-art federated baselines, establishing a robust framework for distributed intelligence in video-based CPS.

---


### 55. [Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models](https://arxiv.org/abs/2608.06901)

**<font color=#1a73e8>作者：</font>** Minseok Kang, Hyunwoo Kim, Chanyoung Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved remarkable generalization across diverse multimodal tasks through large-scale pre-training, yet their rapidly increasing computational and memory requirements pose significant challenges for deployment in constrained environments. Existing pruning strategies often depend on task-specific criteria or LLM-oriented importance measures, making them unsuitable for task-agnostic pruning, where no task-specific samples are available at pruning time and the pruned model remains broadly applicable. We introduce a retraining-free VLM pruning framework called PORTA that derives a task- and modality-agnostic importance formulation based on activation variation, estimated from generic calibration data, which reliably captures feature-level representation utility across modalities. PORTA further incorporates an adaptive sparsity allocation mechanism that assigns layer-wise pruning ratios based on output feature variability, avoiding the limitations of uniform sparsity and reducing performance degradation at high compression levels. Extensive experiments across VLM architectures, such as CLIP, BLIP, and Qwen2-VL, demonstrate that PORTA achieves competitive downstream performance under high sparsity without requiring any retraining, supporting efficient VLM compression. Code is available at this https URL.

---


### 56. [Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework](https://arxiv.org/abs/2608.06909)

**<font color=#1a73e8>作者：</font>** Jing Chen, Yang Sun, Li Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate through long-horizon trajectories involving user instructions, tool use, external observations, and memory. Existing benchmarks primarily evaluate behavioral outcomes but provide limited support for fine-grained attribution analysis. We introduce trajectory attribution and develop a benchmark and annotation framework for this task. The benchmark organizes heterogeneous trajectories under a unified component schema and provides annotations of the primary attribution component, together with attack and execution chains where applicable. Instantiating the benchmark with trajectories from AgentDojo and the Stage and Canary settings of Agent3Sigma yields more than 1,300 annotated trajectories covering task-aligned actions, unsafe actions, and safety refusals. The benchmark defines two evaluation tasks, primary attribution localization and attribution-chain recovery, and provides reference baselines based on incremental trajectory contribution and component-level leave-one-out perturbation. It captures diverse attribution settings, including local and long-range attribution as well as structured attribution chains. Reference baseline results exhibit substantial performance differences across these settings, providing an initial characterization of the benchmark's attribution challenges. Beyond this initial instantiation, we release a reusable annotation skill that enables trajectories generated by new agent models to be standardized, annotated, and evaluated under the same framework. Project resources and future releases are available at this https URL.

---


### 57. [MuST-VAD: Mutual Structured Learning for Video Anomaly Detection](https://arxiv.org/abs/2608.06913)

**<font color=#1a73e8>作者：</font>** Satoshi Hashimoto, Hitoshi Nishimura, Mori Kurokawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose MuST-VAD, a mutual structured learning framework for weakly supervised video anomaly detection (VAD) in which an anomaly detector and a large vision-language model (LVLM) exchange their acquired knowledge. Detectors in weakly supervised VAD learn anomaly scores from features extracted by a fixed, task-agnostic backbone. These fixed features bound the achievable detection accuracy. Recent methods therefore transfer LVLM semantics into the detector as richer features. However, this transfer is one-way: what the detector learns about the target videos never returns to the LVLM. MuST-VAD extends the one-way transfer into a bidirectional learning loop. In this loop, the latest detector predictions supervise the LVLM adaptation, and the adapted LVLM returns updated representations that retrain the detector; the two models alternate these updates over small video groups. Both models train on detector-selected key clips, while confidence weighting and annotation-anchored question answering keep the exchanged supervision reliable. On UCF-Crime, our mutual learning improves the one-pass transfer baseline from 88.15% to 88.63% AUROC and from 37.25% to 42.46% average precision (AP), outperforming the state-of-the-art method in AP by 4.13 points.

---


### 58. [Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery](https://arxiv.org/abs/2608.06931)

**<font color=#1a73e8>作者：</font>** Taolin Han, Yuchen Zhang, Jinghang Wang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly involved in scientific discovery, yet it remains unclear whether they can support complex real laboratory science. Here we introduce Science Edge Evaluation (SEE), a multimodal benchmark of expert-curated questions grounded in peer-reviewed literature and experimental practice in chemistry, biology, and materials science. Evaluation of 19 multimodal large language models (MLLMs) shows that even the best-performing model reaches only 48.7% accuracy. Moreover, general-purpose models outperform science-specialized models on average. In the visual-agent evaluation, the use of tools increases the best accuracy to 52.7%. Tool use can expand the information available to models, but more information does not necessarily lead to reliable scientific reasoning. The key challenge is whether models can manage tool-derived information within the boundaries of the original experimental evidence. Together, these findings reveal that current MLLMs still cannot reliably make justified and evidence-bounded inferences from experimental results, which is an essential capability in real scientific discovery. Bridging this gap requires MLLMs to transition from explaining established scientific concepts to deriving novel and evidence-based insights from experimental data.

---


### 59. [Walkable to Whom? Capturing Subjective Variability in Walkability Perception Using Multimodal Deep Learning](https://arxiv.org/abs/2608.06934)

**<font color=#1a73e8>作者：</font>** Moloud Damandeh, Meead Saberi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual perception of walkability varies substantially across individuals, reflecting differences in personal characteristics, experiences, and preferences. Existing studies, however, often reduce these diverse judgements to aggregated scores, implicitly assuming uniform perception, and commonly rely on vehicle-mounted street-view imagery that does not reflect the pedestrian's visual experience. This paper introduces a dataset of 29,870 walkability ratings from 1,196 respondents, linking sidewalk-view imagery across urban, suburban, and regional Australian environments with individual rater attributes, and proposes the first user-conditioned multimodal deep learning framework for walkability perception, fusing visual features with respondent-level representations. A viewpoint-comparison study shows that sidewalk-view images receive significantly higher walkability ratings than matched street-view images, indicating that imagery source is a substantive design decision in perception surveys. The user-conditioned model improves rank agreement with observed ratings by 65% over an image-only baseline (quadratic weighted kappa 0.47 vs. 0.29), demonstrating that who is evaluating an environment carries predictive indication beyond image content alone. These findings support moving from aggregated, observer-independent walkability scores toward models that represent diverse users, enabling more inclusive assessment of pedestrian environments.

---


### 60. [Debias in Text, Believe Your Eyes: Text-Anchored Cross-Modal Transfer for Visual Counter-Commonsense Reasoning](https://arxiv.org/abs/2608.06938)

**<font color=#1a73e8>作者：</font>** Chen Ling, Hanqian Li, Dongnan Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The visual reasoning ability of multimodal large language models (MLLMs) is crucial for downstream applications, particularly counter-commonsense reasoning, which requires models to reason beyond common assumptions. Recent studies mainly improve visual counter-commonsense reasoning by enhancing visual inputs, following the assumption that failures originate from insufficient visual grounding. However, our empirical analysis reveals that the bottleneck is not visual perception. MLLMs already capture the relevant visual evidence, and the correct answer exists in their decoding space. Instead, the shared language decoder resolves prior--evidence conflicts by favoring dominant language priors, especially for low-frequency factual scenarios. Motivated by this, we first propose a text-anchored data construction pipeline, whose core component, Fact-Frequency Distillation (FFD), estimates the prior strength of commonsense facts and distills verified counter-commonsense scenarios into a high-quality text corpus. Building upon this corpus, we introduce TACT, a text-anchored post-training framework that debiases the shared language decoder without requiring any visual training data. TACT routes evidence-following and prior-driven reasoning trajectories into different optimization stages, enabling the decoder to resolve prior--evidence conflicts. Across counter-commonsense visual benchmarks, TACT substantially improves visual reasoning while preserving general capabilities, demonstrating effective text-to-vision cross-modal transfer.

---


### 61. [Degradation-Aware Prompt Learning with Cross-Modal Compensation for Adverse Weather Removal](https://arxiv.org/abs/2608.06939)

**<font color=#1a73e8>作者：</font>** Wanshu Fan, Yunzhe Zhang, Yue Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather causes diverse and complex image degradations, severely compromising the reliability of computer vision systems. Existing all-in-one restoration models attempt to address multiple degradation types within a unified framework, but often lack explicit spatial and semantic modeling of degradation characteristics, limiting their adaptability to diverse weather conditions. To address this limitation, we propose a Degradation-Aware Cross-Modal Prompt Compensation Network (DCMPC-Net) that leverages cross-modal degradation cues from a pretrained vision-language model to condition restoration features within a unified backbone. Specifically, our DCMPC-Net mainly consists of the Cross-Modal Prompt Generator (CMPG), Prompt-Guided Attention Alignment Module (PGAAM), and Dual Feature Compensation Module (DFCM). The CMPG integrates textual embeddings with visual features to produce degradation-aware prompts that encode degradation-related semantic and contextual cues. These prompts are injected into the decoder via a PGAAM, which adaptively aligns semantic information with degraded regions to facilitate context-aware restoration. To further enhance structural fidelity, DFCM is introduced that disentangles degradation artifacts from scene structures, thereby improving the reconstruction of fine textures and detailed content. By integrating cross-modal semantic guidance with spatial alignment and structural enhancement, DCMPC-Net achieves robust and perceptually consistent restoration across diverse weather conditions. Extensive experiments show that DCMPC-Net outperforms state-of-the-art methods in both task-specific and unified settings, achieving superior accuracy and visual fidelity.

---


### 62. [Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints](https://arxiv.org/abs/2608.06949)

**<font color=#1a73e8>作者：</font>** Paul-Peter Arslan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prior benchmarking work has shown that a single large language model (LLM), forced to make life-or-death resource-allocation decisions, exhibits measurable demographic bias. Real deployments, however, rarely use a single agent: they use pipelines, with review steps meant to catch exactly this kind of failure. We study what happens to bias when the same decision is distributed across a role-differentiated multi-agent pipeline (assessment, allocation, independent audit) instead of made and checked by one model alone. Using a synthetic disaster-triage simulator with paired cases that are clinically identical except for one demographic attribute, we run 192 episodes (2,304 resolved case pairs) on GPT-4o-mini comparing a single-agent control condition to a nine-agent pipeline under three independently varied pressure dimensions. We find no measurable difference in how often biased outcomes occur between the two conditions (6.9% vs. 6.1%, p = 0.498). We do find a large and significant effect of audit capacity on whether bias is caught: 30.0% of biased outcomes go entirely undetected, rising to 43.8% when the auditor is overloaded and falling to 18.4% when it is not. Decomposing this effect shows it is driven almost entirely by coverage (whether a case is reviewed at all, which collapses from 100.0% to 65.6% under load, p < 0.001) rather than by degraded judgment on the cases that are reviewed (81.6% vs. 85.7%, p = 1.000, direction reversed). A follow-up experiment shows that reordering the audit queue by estimated risk, rather than first-come-first-served, recovers most of the lost coverage under the same capacity constraint (65.6% to 91.7%, p = 0.028). We discuss the implications for any system that adds independent oversight to an LLM agent pipeline under resource constraints, and report the study's limitations honestly: one model, modest sample sizes, and no adversarial replication.

---


### 63. [Critical Acclaim Orientation in Large Language Models: Evidence from Film Preference Elicitation](https://arxiv.org/abs/2608.06955)

**<font color=#1a73e8>作者：</font>** Jonghyun Jee, Aaron Shaw  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are trained on corpora that contain expressions of human judgment about films, books, music, and more. Yet whether LLMs systematically reproduce evaluative hierarchies remains unclear. Prior research on cultural bias in LLMs suggests competing expectations: models may mirror the popularity signals of internet texts, or may reproduce forms of prestige embedded in critical discourse. We probe this question through a study of film evaluations with eight models from four families (Anthropic, OpenAI, Alibaba, and Mistral), using a 200-film benchmark partitioned into critically acclaimed, commercially successful, and dual-legitimacy (critical acclaim + commercial success) films. Across 20,000 pairwise forced-choice comparisons per model analyzed with Bradley--Terry estimation, we observe a consistent critical acclaim orientation with all models: critically acclaimed yet commercially obscure films are selected over commercially successful yet critically unrecognized ones. This pattern grows with model scale within each family. In addition, nested OLS regression analyses show that evaluative orientation, public visibility, and popular reception distinctly help explain preferences. Adjusting for public visibility reverses the models' preference for dual-legitimacy films over critical acclaim-only films, while additionally accounting for popular reception attenuates much of the disadvantage of films with commercial success only. Finally, evaluative and recommendation-oriented prompt framings produce divergent rankings, suggesting that critical acclaim orientation may manifest indirectly in real-world LLM deployments.

---


### 64. [CAi Copilot: Reducing Operational Workload in Molecular Design through Intent-Driven Agentic Workflows](https://arxiv.org/abs/2608.06961)

**<font color=#1a73e8>作者：</font>** Zhu Wang, Jiangyu Chen, Yingjun Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early-stage molecular design is an iterative process, not just a task of generating molecules. Researchers turn broad goals into design strategies, refine candidates, assess many properties, and gather evidence before synthesis and tests. AI methods can generate molecules, optimize several goals, predict properties, dock compounds, and account for synthesis. Yet these functions are spread across specialized tools. Experts must still coordinate each step, judge interim results, and integrate evidence. The central challenge is thus to turn research intent into adaptive, traceable runs grounded in scientific tools. We cast this challenge as intent-to-evidence molecular design workflow execution and present CAi Copilot, an expert-oriented agent with three linked layers. The Research Interface Layer turns intent into an executable plan. The Agent Reasoning Layer uses interim results to guide each run. The Execution Substrate supplies molecular tools, metrics, reusable utilities, and backend services. Across 45 tasks, CAi achieves the strongest overall performance, with an outcome score of 84.59, exceeding the next-best result by 18.07 points. Additional benchmarks test how CAi coordinates generation, screening, and multi-criteria evaluation, while exposing limits in long-horizon execution. These results show that CAi turns broad molecular-design intent into transparent, traceable workflows that connect interim decisions to candidate-level evidence.

---


### 65. [Can Language Models Imagine Without Seeing? Ekphrasis: Measuring Visual Creative Ideation in Text-Only LLMs](https://arxiv.org/abs/2608.06967)

**<font color=#1a73e8>作者：</font>** Hongyu Luo, He Wang, Huihao Jing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluations do not isolate whether text-only language models can originate visual concepts before image generation. Fluent visual prose can hide visual-plan failures: an answer may appear creative while repeating familiar visual clichés or failing to specify a renderable scene. We define Visual Creative Ideation (VCI) as the ability to produce textual visual plans that are useful, expressive, and population-novel, and introduce Ekphrasis, a 400-task benchmark spanning Abstraction, Combination, Transformation, and Adaptation. Ekphrasis scores anonymized pairwise comparisons with dimension-specific checklists, aggregates preferences with Bradley-Terry models, and uses Typed Idea Graphs to convert task-specific population clichés into novelty references. Across 14 language models, VCI separates usefulness, expressiveness, and novelty rather than reducing to fluency: strong models achieve similar overall scores through different profiles, and useful plans can remain visually clichéd. A cross-modal grounding study further shows that text-level VCI ordering largely survives faithful rendering and blind image-level preference judgment, supporting Ekphrasis as a measure of visual ideation beyond prose quality.

---


### 66. [When One Modality Is Not Enough: Multimodal Sex and Life-Stage Classification of Red Deer from Aerial RGB-Thermal Video](https://arxiv.org/abs/2608.06973)

**<font color=#1a73e8>作者：</font>** Hugo Markoff, Christoph Praschl, Ivan Ludoški 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial drone surveys increasingly support wildlife population estimation, yet a useful census is more than a count: population dynamics are defined by species composition, sex ratios and age structure, that is, by which species are present and how a herd splits into adult males, adult females and juveniles. We use red deer ($\textit{Cervus elaphus}$) as a test case, because managers act on these dynamics and because the visible cue defining adult males, the antlers, is seasonally variable. Surveys are flown nadir, high enough not to disturb the animals, so each deer occupies only a small, low-resolution patch. The two recording modalities fail in opposite conditions: in color a deer under canopy blends into the ground, while in thermal it becomes a bright blob that loses fine detail. Rather than trust either modality alone, we fuse them at every stage using self-supervised DINOv3 features. Our pipeline tracks animals in both modalities, treats an animal as confirmed only when the two cameras agree, keeps only the clear, non-occluded frames, and assigns species and sex by a vote across them; life stage is read separately from geo-referenced body size, since at survey resolution a juvenile often only differs from an adult female in size. Across four flights spanning the antler season the fused pipeline correctly classifies 25 of the 26 detected individuals (7 of 8 adult males, all 16 adult females and 2 juveniles), against 20 of 26 for either sensor alone. Multimodal species classification reaches 96.0%, while for sex classification fusing the two sensors matters most: the combined RGB+thermal model is the most robust across environments and seasons. Automating the demographic classification turns a drone flight from a count into a repeatable reading of herd structure, so the sex ratios and age structure that managers already act on can be gathered as often as a survey can be flown.

---


### 67. [Confirming Our Biases? Evaluating the Capabilities, Risks, and Societal Impact of Large Language Models](https://arxiv.org/abs/2608.06977)

**<font color=#1a73e8>作者：</font>** Mudar Adas, Polina Tsvilodub, Michael Franke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> It is well established that large language models (LLMs) are sensitive to prompt framing, reflecting patterns in their training data or prior prompts. In this study, we investigate the extent to which LLMs reinforce users biases expressed in the prompts and examine the boundary between implicit framing effects and explicit prompt manipulation. Specifically, we evaluate how susceptible LLMs are to direct and suggestive prompts that encourage models to support or challenge particular positions.
We evaluate six LLMs using 160 distinct prompts spanning ten topics across opinion-based and factual domains. The prompts systematically vary in prompting strategy, support versus challenge instructions, prompt polarity, users' expressed beliefs, and topic domain, spanning both opinion-based and factual questions. Our results show that LLMs systematically adapt their responses to align with prompt framing, even in factual contexts. This suggests that prompt framing can outweigh factual consistency in model responses. Overall, our findings delineate the extent and boundaries of LLM manipulability. Furthermore, the results imply that LLMs can reinforce subtle user biases and are susceptible to explicit prompt manipulation even in domains where responses should remain factually stable.

---


### 68. [GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base](https://arxiv.org/abs/2608.06992)

**<font color=#1a73e8>作者：</font>** Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a web demo for exploring a large-scale disambiguated knowledge base (KB) materialized from a large language model (LLM). GPTKB 2.0 contains 38.4M triples over 1.6M canonical entities, together with 207.6K consolidated relations and 66K consolidated classes. Unlike prior LLM-derived knowledge bases that largely identify entities by surface strings, GPTKB 2.0 performs context-guided disambiguation during recursive KB construction, separating homonyms and merging synonymous mentions as facts are elicited. The demo makes this process inspectable: users can browse entities, follow links across the KB, and audit the provenance of individual facts, including surface forms, candidate matches, source triples, and disambiguation decisions. The interface further supports structured SPARQL queries, natural-language questions translated to SPARQL, and entity linking from user-provided text to canonical GPTKB 2.0 entries. GPTKB 2.0 is available at this https URL, with the full KB downloadable for offline use.

---


### 69. [Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction](https://arxiv.org/abs/2608.06993)

**<font color=#1a73e8>作者：</font>** Gregor Molan, Grafika Jati, Francesco Barchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale pretrained time-series models achieve strong results through large-scale pretraining and task-agnostic representation learning, but they rely on abundant, diverse data that industrial and scientific domains often lack. We therefore propose the FSD-RM (Family of Small-Data Representation Models) paradigm as a practical alternative for limited, domain-specific telemetry. Rather than relying on large-scale pretraining, we focus on capacity-controlled representation learning using established encoder architectures (CNN1D, LSTM, GRU, Transformer), selected for their suitability in small-data settings and interpretability.
These encoders are trained unsupervised on multivariate telemetry data and integrated into a two-stage pipeline for downstream lifetime prediction. To systematically examine architectural trade-offs under data constraints, we employ \textbf{dimension-aware neural architecture search (NAS)} to jointly optimize model capacity and input dimensionality.
Experiments on cryocooler telemetry show that the proposed approach achieves competitive predictive performance while reducing training cost and model complexity. The contribution lies in combining established representation learning techniques within a coherent, NAS-driven framework tailored to small-data regimes, with explicitly defined parameter settings and design choices. The results indicate that effective representation learning can be achieved without large-scale pretraining when appropriate inductive bias and capacity control are applied.

---


### 70. [Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression](https://arxiv.org/abs/2608.07001)

**<font color=#1a73e8>作者：</font>** Haolin Tian, Yuzhe Liu, Tonghan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging. As a result, cache resources can neither flow freely across layers, heads, and context slots, nor be jointly allocated to balance local resolution and information coverage. Therefore, we propose GraceKV, a global approach for the allocation of resolution and coverage in KV cache compression, and formulate the compression process as a global resource allocation problem under a fixed cache budget. GraceKV treats each layer-KV head-slot combination as an atomic unit and builds a prototype tree. Leaf nodes correspond to token-level KV entries, while each internal node uses a single prototype to compress the KV space covered by its children. A set of non-overlapping nodes in the tree forms the representation of an atomic unit. Adding the root of a new tree expands information coverage, whereas splitting a selected node improves local resolution. All candidate actions compete globally for a shared cache budget. Finally, the nodes retained across all trees form the compressed KV cache. This process adaptively determines the allocation of cache resources among atomic units globally and the balance between resolution and coverage. GraceKV requires no additional training, and the entire compression and inference process is performed on the GPU. Systematic experiments across diverse long-context tasks and compression ratios show that GraceKV ranks first in 24 of 32 settings and remains robust up to 128-fold compression. These results validate the effectiveness of global budget allocation in coordinating information coverage and local resolution.

---


### 71. [Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?](https://arxiv.org/abs/2608.07006)

**<font color=#1a73e8>作者：</font>** Jiankun Wang, Yisen Gao, Ziwei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual retrieval-augmented generation (RAG) commonly expands the retrieved evidence set to improve answer-page coverage, implicitly assuming that all available evidence should be passed to the generator. We show that this assumption does not hold for diffusion language models (DLMs): retrieving more pages increases answer-page recall, whereas unconditionally passing all retrieved pages to the generator often reduces answer accuracy, primarily because of semantic conflict. A latent-source analysis explains this mismatch through source-coherence loss in parallel denoising, where position-wise proposals can combine incompatible visual sources into unsupported answers. We further find that such interference is already visible in the first-step answer-block distribution, making it possible to assess evidence before decoding. To preserve retrieval coverage while limiting harmful visual exposure, we propose the Entropy-Based Candidate Filter (ECF), a training-free evidence-admission framework. To reduce irrelevant content within individual candidates, ECF constructs multi-granularity evidence units; to identify beneficial additional evidence, it uses blank-controlled block confidence and retrieval rank to determine whether and which candidate should enter the final context. Across three multimodal DLMs and five visual QA benchmarks, ECF improves answer accuracy by 2.62 percentage points on average over the strongest fixed top-$k$ input and, with LLaDA2.0-Uni, by 2.37 percentage points on average over the best competing training-free result for each dataset. These results show that broader retrieval benefits visual DLM-RAG through selective evidence admission rather than unconditional evidence expansion. Code is publicly available at this https URL.

---


### 72. [Stable Curves, Unstable Items: Item-Level Scaling Heterogeneity in Video LLMs](https://arxiv.org/abs/2608.07014)

**<font color=#1a73e8>作者：</font>** Wenzhang Sun, Chunfeng Wang, Xiangchen Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aggregate scaling curves suggest that Video LLMs improve smoothly or saturate as visual budgets grow. We show that this view can conceal large, opposing changes at the item level. We represent each frozen model--item pair by its response trajectory under controlled visual budgets and derive matched-grid measures of configuration complementarity, harmful transitions, and text overwrite. Across five open Video LLMs from three architecture families, four multiple-choice benchmark splits, open-ended QA and summarization, and fixed-history dialogue generation, no single budget serves all items. On the four-model matched MCQA grid, item-level oracle headroom spans $8.8$--$18.9$ accuracy points and $12.5$--$25.5\%$ of items are correct at a lower budget but wrong at a higher one. Task-appropriate continuous metrics show the same complementarity beyond multiple choice: Token-F1 oracle gaps are $2.7$--$3.7$ score points on MLVU generation and $3.8$--$4.8$ points on AVSD current-turn generation, even when mean quality improves with budget. The effect persists across frame count, spatial resolution, sampling policy, temporal--spatial allocation, and independently executed raw-video and cached pipelines, with per-item rates and membership tracking protocol choices. A controlled sampling intervention recovers $29.0\%$ of terminal regressions, and a structured frame audit identifies several recurring evidence pathways. We release per-item trajectories, protocol provenance, derived annotations, and reproducible analysis code as an auditing artifact. A confidence cascade matches fixed-$128f$ accuracy while reducing average shared frame cost by $31.7\%$, illustrating one operational use of the response matrix.

---


### 73. [ReQuant: Fixed-Grid Discrete Refinement for Post-Training Quantization](https://arxiv.org/abs/2608.07019)

**<font color=#1a73e8>作者：</font>** Yongge Ma, Guoan Wang, Feiyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is widely used to reduce the memory and computational cost of large language models. Existing PTQ methods typically obtain an initial quantized model through heuristic rules or greedy optimization, and once quantization is completed the resulting integer assignments are usually treated as final. This observation motivates a complementary optimization stage within PTQ that keeps quantized weights improvable after an executable quantized model has been produced, while preserving the quantized format. We introduce ReQuant, a backpropagation-free fixed-grid refinement procedure for this stage. Agnostic to the PTQ initializer, ReQuant takes an existing quantized model as a feasible starting point and iteratively revisits its discrete weight assignments on the fixed quantization grid. Accepted updates strictly reduce the mean squared reconstruction error and remain on the original grid. In this way, ReQuant turns the initially fixed PTQ output into an iteratively optimizable discrete solution and serves as a plug-and-play post-processing stage for existing PTQ pipelines. Experiments across diverse model families, bit-widths, and downstream tasks show that ReQuant consistently improves quantized models from heterogeneous PTQ initializers, with especially large gains on simple initializers and lower bit-widths. Notably, ReQuant can refine a simple round-to-nearest initialization across multiple sweeps until it approaches or surpasses GPTAQ under the same quantization format. These results establish ReQuant as a practical complementary stage for further improving existing PTQ pipelines.

---


### 74. [An Agentic Hybrid Top-Down and Bottom-Up Approach to Knowledge Graph Generation](https://arxiv.org/abs/2608.07023)

**<font color=#1a73e8>作者：</font>** Emma Jouffroy, Warren Jouanneau, Marc Palyart  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizing thousands of unstandardized, multilingual expertise declarations is a persistent challenge for Human Resources (HR) platforms, directly impacting downstream tasks like accurate talent matching. To address this, we propose a hybrid knowledge graph generation pipeline that grounds a Large Language Model (LLM) in the Wikidata multilingual Knowledge Graph (KG) while employing an agentic reflexion pattern to synthesize emerging concepts and their associated metadata. Unlike rigid top-down methods or fragmented bottom-up approaches, our system anchors recognized concepts to stable Knowledge Graph entities while dynamically creating new nodes and relational metadata for unrecognized skills. Executed across five stages, entity reconciliation, multilingual canonicalization, active curation, deduplication, and the iterative recovery of unmapped concepts, the system autonomously adapts to rapidly evolving, noisy skill mentions across five European languages. Ultimately, this pipeline provides a highly scalable, explicable, and self-healing framework for generating a comprehensive skills knowledge graph, from which a structured taxonomy is derived, using unstructured, noisy text.

---


### 75. [ZIPBrain: Can EEG Foundation Models Be Faster, Locally Deployable, but Accurate?](https://arxiv.org/abs/2608.07033)

**<font color=#1a73e8>作者：</font>** Lingwei Li, Yirong Kan, Peng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work investigates whether Electroencephalograph (EEG) foundation models (EFMs) can be made faster and locally deployable without sacrificing accuracy. EEG foundation models are a major trend, offering strong general-purpose representations. However, their computational burden grows quadratically with input length, hindering deployment on resource-constrained scenario, particularly for real-time clinical monitoring. EEG's low SNR further suggests many of these tokens are redundant and compressible with little accuracy cost. We propose ZIPBrain, a novel redundancy-aware EEG token pooling module that leverages this low-SNR characteristic to reduce token count. Given a token sequence, ZIPBrain partitions tokens into redundant and unique groups, then merges each redundant token with its most similar counterpart in the unique group. Furthermore, ZIPBrain serves as a training-free, plug-and-play module that seamlessly integrates into standard Transformer encoders with negligible computational overhead. Extensive experiments across multiple EEG foundation models show ZIPBrain's strong versatility, achieving 1.3%-10.5% average improvement over baselines, while reducing wall-clock inference time by 32.7% (up to 41.8% with CUDA Graph) compared to the original EEG foundation models.

---


### 76. [YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family](https://arxiv.org/abs/2608.07051)

**<font color=#1a73e8>作者：</font>** Xu Lin, WenJie Nie, Jinlong Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generic parameter-efficient fine-tuning (PEFT) methods transferred from language models can fail silently on real-time detectors, whose heterogeneous operators and detection-specific components impose placement constraints absent from regular Transformer stacks. We propose YOLO-PEFT, a structure-aware framework that formulates adapter placement as an auditable constraint-planning problem. Given a detector graph, a PEFT request, and a resource budget, YOLO-PEFT assigns operator and semantic roles, evaluates explicit operator-validity, detector-semantic, graph-interface, and deployment predicates, records a reason code for each excluded module, and either emits a budgeted target-module plan or returns Refuse before training. Under the official VOC07+12 trainval-to-VOC07 test protocol, planner-selected RS-LoRA reaches 0.7138 and 0.7307 mAP50-95 on YOLO11s and YOLO12s, respectively, compared with 0.6428 and 0.6662 for Full-SFT. On RT-DETR-L, all seven evaluated LoRA-family configurations cross the predefined catastrophic threshold, supporting a calibrated Refuse-to-Full-SFT decision within the evaluated coverage. A controlled YOLO11 audit further shows that LoRA reduces peak training memory by 43.9 percent, although training takes 1.72 times longer. Within the evaluated detector families, placement policies, and calibration coverage, YOLO-PEFT replaces manual target-module trial and error with explicit, inspectable planning while preserving verified train-save-merge-export paths; refusal on unseen detector architectures remains an open validation problem. Project Page: this http URL

---


### 77. [Unsupervised Adaptation of PDE Foundation Models](https://arxiv.org/abs/2608.07053)

**<font color=#1a73e8>作者：</font>** Ziye Song, Zhao Wei, Xin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained partial differential equation (PDE) foundation models can generalize across different equations, but adapting them to unseen PDE systems typically requires dense solution data, which is often expensive or unavailable. To address this limitation, we propose an unsupervised PDE-based finetuning framework that eliminates the need for ground-truth solutions. We first pretrain a neighborhood attention Transformer on diverse time-dependent PDEs spanning varying spatial scales, yielding transferable representations across heterogeneous equations. In the adaptation stage, we construct a physics-based objective using the PDE residual and boundary conditions, and finetune the model on unseen equations via low-rank adaptation (LoRA). To address the uneven learning across physical quantities in standard LoRA, we introduce NSLoRA, a Newton-Schulz orthogonalized variant that rebalances adaptation. Our method achieves performance comparable to supervised LoRA finetuning without requiring any ground-truth solutions, while consistently outperforming competitive neural operator baselines and recent PDE foundation models across heterogeneous PDE benchmarks spanning multiple spatial dimensions.

---


### 78. [PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks](https://arxiv.org/abs/2608.07066)

**<font color=#1a73e8>作者：</font>** Hui Xie, Tong Shi, Haotong Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) enable sparse and event-driven computation, but their low-bit deployment remains incomplete because recurrent membrane states are commonly retained in floating point even after weight quantization. Quantizing these states is challenging because their distributions differ across channels and from the preceding weights, while small perturbations near the firing threshold may alter spike decisions and accumulate over time. We propose PTQ4SNN, a membrane-aware post-training quantization framework that jointly quantizes weights and recurrent membrane states using only a small calibration set. First, a channel-wise Unified Scale Bridge constrains the membrane scale as s_mem,c = s_w,c * 2^k_c, adapting to membrane distributions while enabling shift-compatible scale conversion. Second, Mixed-Precision Bit Allocation assigns 2/4/8-bit precision to membrane channels according to firing activity and quantization sensitivity under an average-bit budget. The framework operates on reusable projection-LIF pairs and supports both convolutional SNNs and spike-driven Transformers without backbone retraining. Experiments on static and event-based classification and semantic segmentation show that PTQ4SNN effectively preserves model accuracy under W4 quantization and approximately 4-bit membrane precision.

---


### 79. [MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents](https://arxiv.org/abs/2608.07068)

**<font color=#1a73e8>作者：</font>** Zhiyuan Liu, Tinghong Ye, Chenghao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability. Compact memory mitigates this problem by compressing and rewriting the history retained between model invocations. Learning what to retain typically relies on proximal policy optimization (PPO) with final task rewards, but sparse rewards provide little guidance for individual memory updates. This limitation motivates on-policy distillation (OPD), which supplies dense teacher supervision on student rollouts. For such supervision to be valid, the teacher must evaluate each sampled action under the same state in which it was generated. However, the context rewriting performed during memory compression can break this alignment. When sampled responses are retained and re-encoded for later invocations, flattening the interaction into a persistent history may cause the teacher to score the action under a state that the student never visited during rollout. The action therefore remains on-policy by provenance, but not necessarily by state. We therefore propose Memory-Aligned On-Policy Distillation (MemOPD). MemOPD records the inputs and sampled outputs of each model invocation, restores its original token positions and causal visibility, and packs the reconstructed invocations for efficient teacher scoring. The teacher provides full-vocabulary supervision at the sampled action positions, while PPO preserves the final task objective. Experiments verify state alignment across several context updates and show that it improves F1 by 7.0% over persistent-history teacher scoring in a matched control. Overall, MemOPD-3B improves F1 over PPO by up to 416.2%, while packing yields up to a 1.63x speedup in actor computation during training. The code for this work is publicly available at: this https URL.

---


### 80. [Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking](https://arxiv.org/abs/2608.07077)

**<font color=#1a73e8>作者：</font>** Devin Pereira, Willem Zuidema  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Tower of Hanoi is a simple planning puzzle that in prior work has proven challenging for large reasoning models (LRMs). Current models solve the standard formulation of the puzzle, but still struggle with the flat-to-flat variant (where initial and goal states are not restricted to have all rings on a single peg). This paper presents an in-depth study of how both small, in-house Transformers and large, third-party LRMs solve this task. To understand the failures mechanistically, we first train small Transformers from scratch on precomputed solution traces. Using a variety of interpretability techniques, we show that these Transformers develop an emergent world model: a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle), that is causally involved in solving the puzzles. Second, we return to the large LLMs and apply our techniques to two frontier reasoning models, Qwen3.6-27B and DeepSeek-R1-Distill-Qwen-32B, that attempt to solve the task through extended chain-of-thought. Surprisingly, we find that both models encode the Sierpinski world model near-perfectly at the end of the prompt, and yet fail at the majority of tasks when there are more than 3 rings. We locate the source of this failure in the decaying representation of the world model. We probe for the representation at different stages during planning, and establish causality by showing that performance can be improved by injecting the prompt-time representation at inference. The failure of the models is thus one of maintenance of the required representations, not their absence, and performance is at least partially recoverable. These results thus reframe the reported collapse in performance from prior work: current Large Reasoning Models build a world model, and then lose it.

---


### 81. [RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs](https://arxiv.org/abs/2608.07088)

**<font color=#1a73e8>作者：</font>** Qiyanhui Lu, Han Wu, Rongjian Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) encode images as long visual token sequences, making prefilling and KV-cache storage expensive. Existing training-free pruning methods select tokens by importance, diversity, or spatial coverage, but treat retained tokens as interchangeable and do not explicitly track which object-related regions are already covered. We present RoRA, a training-free framework that casts visual token pruning as role-oriented regional evidence allocation. Given a fixed budget, RoRA partitions tokens into a protected semantic core, complementary context, and fine-grained detail. It first calibrates text-conditioned attention with a positional prior and a prompt-calibrated object prior, then builds Attention-Anchored Regions (AARs) from high-confidence anchors as lightweight proxies for covered object support. Context is explored mainly outside AARs, while a small AAR-guided budget restores local detail; pairwise similarity is used only for context-stage redundancy filtering. Under matched budgets, RoRA consistently outperforms strong training-free baselines across LLaVA and Qwen-VL families, retaining most of the unpruned accuracy even at aggressive pruning ratios, e.g., 96.5% of full performance at 88.9% pruning on LLaVA-1.5, and improving over D2Pruner by about 5% on Qwen3-VL at 75-90% pruning. At a 66.7% pruning ratio, RoRA requires only 0.7 ms for token selection and reduces end-to-end inference time by 24.6%, corresponding to a 1.33x speedup over unpruned inference on an NVIDIA H800.

---


### 82. [Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design](https://arxiv.org/abs/2608.07091)

**<font color=#1a73e8>作者：</font>** Zeinab Dehghani, Dhavalkumar Thakker, Koorosh Aslansefat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Edge Artificial Intelligence (Edge AI) enables the deployment of AI models directly on local edge devices, while such deployments are subject to strict resource constraints, particularly in clinical applications requiring local and timely inference. In such contexts, explainable artificial intelligence (XAI) can serve as a human-AI interface intended to support healthcare professionals' and patients' understanding of model predictions and informed decision-making. To fulfill this role, XAI method selection for TinyML deployments can be formulated as a human-centered multi-objective design problem that jointly considers qualitative stakeholder preferences, explanation quality, and proxy-based deployment cost. We propose a framework that integrates a large language model (LLM)-guided design interface that maps qualitative stakeholder preferences to candidate XAI methods, followed by deterministic feasibility filtering and Pareto-based optimization. The framework exposes trade-offs among explanation fidelity, stability, and proxy-based deployment cost while characterizing their implications for explanation quality and estimated deployment feasibility. A proof-of-concept evaluation on a skin lesion classification task illustrates how the framework systematically compares candidate XAI methods and identifies Pareto-efficient trade-offs. The present evaluation covers the computational selection stages, while physical MCU deployment and empirical human-expert validation remain outside the scope of this study.

---


### 83. [International Transfer of Stochastic Cortical Self-Reconstruction](https://arxiv.org/abs/2608.07092)

**<font color=#1a73e8>作者：</font>** Fabian Bongratz, Zhizheng Zhuo, Chao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stochastic cortical self-reconstruction (SCSR) enables personalized mapping of gray matter atrophy, a hallmark of neurodegenerative disorders such as Alzheimer's disease (AD), onto high-resolution cortical surfaces. Unlike conventional normative modeling approaches, which typically operate at a coarse regional level and remain inherently constrained by the covariates included during training, SCSR estimates an individualized healthy reference directly from the observed cortical thickness at the vertex level. This allows the detection of subtle, subject-specific deviations from healthy cortical shape. In this work, we investigate the generalization and transferability of SCSR, originally trained on UK Biobank (UKB) data, to an independent Chinese population dataset. Specifically, we evaluate the ability of SCSR-derived Z-scores to discriminate between healthy scans, individuals with mild cognitive impairment (MCI), and patients with AD, while also assessing model robustness across the lifespan. We compare four training strategies: direct application of the UKB-trained model, fine-tuning on Chinese data, training from scratch, and joint training on UKB and Chinese cohorts. As reconstruction backbones, we consider both a multilayer perceptron (MLP) and a Spherical UNet (SUNet). Our results demonstrate that SCSR provides robust detection of cortical atrophy in the Chinese population across all evaluated models. The highest discriminative performance was achieved by the fine-tuned SUNet model (average pairwise AUC = 0.848), followed closely by the UKB-trained SUNet. Moreover, reconstruction errors remained low across the lifespan, even when the training population exhibited a substantially narrower age distribution, indicating strong cross-population transferability.

---


### 84. [MemWM: Memory-Augmented Text-Based World Model](https://arxiv.org/abs/2608.07107)

**<font color=#1a73e8>作者：</font>** Yujun Wang, Tao Zhang, Jinhe Bi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions. Yet fluent next-state predictions can still omit task-critical facts, corrupt product attributes, or apply incorrect transition rules. To address such systematic prediction errors, we introduce MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated memory bank of transition rules, state caches, and hard-to-predict facts, to condition next-state imagination. We evaluate factual state preservation with Structured State Fidelity (SSF), which scores predicted states through benchmark-specific facts and fields. Compared with SFT, memory-augmented training improves SSF by up to 206.3%. In the full planning setting, we keep the policy model frozen and provide policy-side world skill: retrieved task-level skills and step-wise corrective guidance for action selection. Across ALFWorld, WebShop, and ScienceWorld, memory-augmented agents improve downstream success over an SFT-trained world-model agent, with up to a 65.4% relative gain. Sensitivity analyses further show that retrieved memory improves task success and efficiency under different memory and action-budget settings.

---


### 85. [Human-AI Perceptual Alignment by Playing Hues and Cues](https://arxiv.org/abs/2608.07141)

**<font color=#1a73e8>作者：</font>** Nuria Alabau-Bosque, Jorge Vila-Tomás, Paula Daudén-Oliver 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating the perceptual alignment between Contrastive Vision-Language Models (CVLMs) and humans is typically constrained by traditional benchmarks that overlook fine-grained semantic and cultural nuances. In this work, we propose a novel evaluation framework that leverages the gamified, discrete color space of the board game Hues and Cues. By mapping the board's 480 color cells to the CIE xy chromaticity diagram, we calculate empirical perceptual distances across a carefully curated 100-word vocabulary spanning seven semantic categories. To properly contextualize model performance, we establish an empirical lower bound of expected error-the Human Consistency baseline-calculated via Leave-One-Out (LOO) cross-validation on a dense dataset of color associations collected from 325 human observers through a custom digital interface. We evaluate 162 models across multiple architectural families and pre-training datasets to assess their semantic color grounding. Our results demonstrate that while CVLMs successfully replicate human cognitive biases, such as idealized memory colors for concrete physical referents (e.g., food and plants), they systematically diverge from the human baseline in abstract, subjective, and pop-culture domains. We identify two distinct failure modes in severely misaligned concepts: semantic misclassification and a systematic uncertainty collapse into a default blue coordinate. Furthermore, we reveal that highly curated pre-training datasets are significantly more effective than massive, uncurated corpora in mitigating these severe misalignments. Ultimately, this work highlights that despite their broad categorization capabilities, current CVLMs still fail to capture the nuanced, localized consensus of human color memory, emphasizing the value of gamified tasks in exposing underlying model biases. The data and code are publicly available to test other metrics.

---


### 86. [A MARL Centered Reference Architecture for Large Language Model Augmentation in Smart Manufacturing](https://arxiv.org/abs/2608.07148)

**<font color=#1a73e8>作者：</font>** Fouad Bahrpeyma, Dirk Reichelt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern manufacturing imposes six coupled demands on adaptive control: local decisions with global consequences, partial observability, nonstationarity, reflex speed response with long horizon effects, delayed and diffuse outcomes, and dynamics that resist explicit modeling. Cooperative multiagent reinforcement learning (MARL), posed as a Dec-POMDP under centralized training with decentralized execution, is a particularly natural formalism for these demands. This paper adopts a MARL centered scope and asks where large language models (LLMs) should augment, interface with, train, or, in the strongest competitive case, replace that coordination core. A taxonomy organizes the literature through four LLM attachment points: policy, reward design, communication between agents, and hierarchical planning. A conditional capability profile separates native mechanism, reported performance, formal guarantee, and engineering maturity, and a deployment readiness analysis identifies the evidence behind each role. These stages yield the principal contribution: a three layer MARL centered reference architecture, grounded in evidence, for semantic reasoning, adaptive cooperative control, and independently assured execution. The LLM-Augmented Dec-POMDP is a descriptive comparative notation for that architecture, recording four attachment choices without introducing a new decision process class or algorithm. Under the reviewed evidence, conventional MARL is better suited to frequent, structured, decentralized coordination after task specific training, whereas LLM components are promising for semantic interpretation, reward drafting, human interaction, and slower supervisory planning. Current LLM only manufacturing controllers do not yet establish equivalence for strict real time, decentralized, safety critical control; this conclusion is bounded by the available evidence and does not assert impossibility.

---


### 87. [Capacity Confounds and Coverage Guarantees in Adaptive Sub-model Federated Learning](https://arxiv.org/abs/2608.07157)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia, Alicia Troncoso Lora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sub-model federated learning lets resource-constrained clients train width-reduced versions of a global model, but existing methods allocate capacity by device resources alone. A natural next step, allocating capacity by each client's data heterogeneity as estimated from the updates the server already observes, has been repeatedly suggested. We ask whether that step is possible, using HAS-FL, an adaptive capacity-allocation framework, as a test case. Our findings are threefold. First, validated against ground-truth label-distribution divergence on reproducible partitions, update-divergence estimates of client heterogeneity are dominated by capacity rather than data: across two corrected estimators, multiple datasets, and all seeds, the estimates correlate strongly and negatively with device capacity, and no data signal remains once capacity is controlled for. This previously undocumented confound affects any method estimating client statistics from sub-model updates. Second, adaptive allocation has a hidden failure mode: when every client is capped below full width, the uncovered parameters stay at random initialization and progressively corrupt the global model. A simple coverage guarantee removes the failure and explains why uniform allocation collapses. Third, a matched-budget control settles what adaptivity contributes: random allocation to the same average budget performs no differently on both image benchmarks, and on the naturally partitioned text benchmark the adaptive policy is the weakest of the three strategies while consuming the most capacity. Sub-model training remains valuable because it admits constrained clients at quadratically reduced cost, but what protects accuracy is parameter coverage rather than allocation intelligence. Its apparent benefits come from capacity budgeting and coverage, and future designs need heterogeneity signals separable from capacity effects.

---


### 88. [NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs](https://arxiv.org/abs/2608.07167)

**<font color=#1a73e8>作者：</font>** Aditya Katkar, Om Karkele, Kartik Mandhane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Giving an AI agent the ability to send emails, query databases, or execute commands is useful--until the agent is tricked into doing something it shouldn't. Prompt injection, hallucinated reasoning, and unsafe tool calls form the primary attack surface for autonomous LLM agents. Existing defenses rely on software checks like system prompts or policy filters running on the same machine the attacker targets, offering no verifiable proof of execution. We introduce Niyam-AI, a framework that makes safety enforcement provable. At session start, permitted tools and constraints are locked into an Intent Contract committed via SHA-256. Every tool call is intercepted and validated by an isolated Judge model; upon passing, a zk-SNARK proof is generated via EZKL.
The tool executes only after proof verification, allowing third parties to confirm enforcement without accessing Judge model weights. Evaluating Niyam-AI on 2,000 real-world scenarios from Agent-SafetyBench against NeMo Guardrails, Meta's Llama Prompt Guard 2, and OpenAI's GPT-OSS-Safeguard using 5-fold stratified cross-validation yields an F1 score of 88.5% with a 1.1% false-positive rate (bootstrap 95% CI: [85.19%, 91.88%], N=1000). McNemar's exact paired test confirms significant improvement: Niyam-AI wins 390 discordant scenarios against NeMo (vs 20 losses), 115 against Prompt Guard 2 (vs 13), and 384 against GPT-OSS-Safeguard (vs 19) with p < 0.0001 in all cases.
Proof generation adds 2260.6 +/- 218.4 ms per approved action, while verification takes 53.1 +/- 11.8 ms. Niyam-AI provides a guardrail that is both highly accurate and mathematically verifiable--though this reflects a classifier adapted to Agent-SafetyBench evaluated against zero-shot baselines, a distinction discussed in Section IV.C.

---


### 89. [Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)

**<font color=#1a73e8>作者：</font>** Taeil Kim, Kangsan Kim, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow memory encodes task-level strategies, Subtask memory provides concrete behavioral examples at an intermediate granularity, and Function memory captures per-function calling conventions and common pitfalls. Workflow and Subtask memories are injected proactively at the start of each task, while Function memory is retrieved reactively upon tool-calling errors. We evaluate AMD on three tool-use benchmarks using four student models (4B-8B parameters) with GPT-5-mini as the teacher, achieving average accuracy gains of 27.2%p, 11.2%p, and 3.4%p on AppWorld, BFCL V3, and ToolSandbox, while consistently outperforming existing memory-based baselines. Further analysis shows that Subtask memory contributes the largest gains, teacher effectiveness depends on both teacher capability and student compatibility, and 4B-sized students benefit most from AMD.

---


### 90. [Representation-driven Endoscopic Visual Embedding Alignment for Latent Generation](https://arxiv.org/abs/2608.07176)

**<font color=#1a73e8>作者：</font>** Francisco Caetano, Tim J.M. Jaspers, Haiko Middeljans 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing foundation generative models for endoscopy is limited by the gap between natural and clinical images and the computational cost of training large Diffusion Transformers. Although representation alignment has improved efficiency in general computer vision, its role within the highly specialized endoscopic image space remains unclear. We introduce REVEAL (Representation-driven Endoscopic Visual Embedding Alignment), the largest generative foundation model for endoscopy to date, trained on GastroNet-5M (GN-5M), a multicenter dataset of 5 million endoscopic frames. Instead of depending on out-of-domain priors, REVEAL employs encoders pretrained directly on the endoscopic distribution to align diffusion latents with domain-specific visual features, preserving fine textures and intricate anatomical structures. Beyond image generation, REVEAL also serves as a powerful feature extractor; in multiple benchmarks, it delivers performance that is competitive with, and in several cases exceeds, endoscopic foundation models such as EndoViT and Endo-FM, specifically tuned for classification tasks, while demonstrating strong representation robustness under realistic imaging corruptions. REVEAL produces high-fidelity images and maintains robust structural coherence in latent-space edits such as inpainting and outpainting. This high-capacity backbone lowers the computational threshold for building specialized clinical tools, offering an open, versatile foundation for conditional synthesis, segmentation, and out-of-distribution detection in future intelligent gastroenterology systems.

---


### 91. [An AI4AI Framework for Visual Token Pruning](https://arxiv.org/abs/2608.07193)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Wenli Huang, Wei Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error. As pruning objectives, budgets, and model architectures diversify, manually navigating the expanding design space becomes increasingly difficult. This paper aims to build an AI4AI framework for visual-token pruning by addressing a natural question: Can large language models automatically design effective visual-token reduction algorithms? Although LLMs possess broad algorithmic knowledge and strong reasoning capabilities, translating such general knowledge into effective solutions for a specialized task remains nontrivial. We argue that the key lies in designing an appropriate search-state representation that connects the internal knowledge of LLMs with the structural requirements and constraints of visual-token pruning. Based on this insight, we propose AutoPrune, a training-free framework for LLM-driven visual-token pruning policy design. At its core, AutoPrune introduces a Token Pruning Domain-Specific Language (TPDSL) comprising 131 reusable atoms for budget control, token scoring, selection constraints, and token reassembly. A key property of TPDSL is that it represents each search state as a residual modification of a strong base policy. This residual formulation narrows the search space and directs the LLM's attention toward the policy components that are most consequential for performance. Experiments on 14 multimodal benchmarks and three MLLM backbones demonstrate the effectiveness, efficiency, and transferability of AutoPrune. Even when removing 94.4% of visual tokens, AutoPrune preserves more than 99% of full-token performance while reducing FLOPs by 9.9x and prefill latency by 6.4x.

---


### 92. [Authoring and Management of Transparent Research Integrity Assessments of Randomised Clinical Trial Publications Using LLM-assisted Tools and Provenance Knowledge Graphs](https://arxiv.org/abs/2608.07202)

**<font color=#1a73e8>作者：</font>** Milan Markovic, Goutham Indukuri, Somayajulu Sripada 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic reviews of Randomised Controlled Trials (RCTs) are routinely used as evidence for clinical care guidelines. Such evidence has to meet high research integrity standards to prevent low quality or false research outputs influencing the clinical care. However, assessing research integrity of published RCTs is a complex process requiring manual effort, and potentially resulting in diverse opinions of the human assessors. This paper describes INSPECT-AI, an LLM-based interactive tool that assists human reviewers with research integrity assessments of published RCTs based on the community approved INSPECT-SR framework, and the Research Integrity Provenance and Evidence ontology (RIPE-O) for documenting the provenance of the assessment process. In addition, we present the Research Integrity Provenance and Evidence knowledge graph (RIPE-KG), an initial set of 140 expert research integrity assessments of 95 RCT publications generated by INSPECT-AI and described using RIPE-O.

---


### 93. [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](https://arxiv.org/abs/2608.07208)

**<font color=#1a73e8>作者：</font>** Luc Hazenoot, Zhaochun Ren, Amirhossein Zohrehvand  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing measures of how much a text is about a concept read the surface of the text: dictionary word shares, topic proportions, embedding similarities. They score the words a text uses, not the judgment a reader forms about it. Recent work has shown that a gap exists in what Large Language Models (LLMs) know internally versus what they express in their response. This paper asks whether that internal knowledge, read by monitoring the activations of frozen, out-of-the-box LLMs, can stand in for task-specific fine-tuning when measuring concept content, and which extraction method reads it best. We extract such measures via the Recursive Feature Machine (RFM) algorithm and via linear probing, and compare these against an embedding baseline, surface baselines, and the same model's own answer to the question. We demonstrate the approach on financial text, a domain studied extensively and served by established annotated resources, using a human-annotated Environmental, Social and Governance (ESG) dataset. The best linear probe comes within 0.6 percentage points of a fine-tuned domain classifier's accuracy without any task-specific fine-tuning, and outscores the same model's own answer to the question in eleven of twelve comparisons, so the activations carry concept content the response does not report. The simple probe consistently beats the RFM concept vectors, which in turn provide what classification alone does not: a continuous score intended to reflect how strongly a concept is present in a text, whose validation awaits graded labels.

---


### 94. [Recipes for Creativity: Iterative Generation and Evaluation in Large Language Models](https://arxiv.org/abs/2608.07243)

**<font color=#1a73e8>作者：</font>** Rens Anderson, Tessa Verhoef, Amirhossein Zohrehvand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models are often evaluated through singular artifacts, whereas human creativity typically emerges through iterative generation, appraisal, and refinement. This pilot study examines whether iterative search improves LLM creativity by adapting FunSearch to recipe generation for the 2024 Pillsbury Bake-Off and evaluating outputs against human benchmarks using TTCT-based LLM evaluation. Across two experiments, we test iteration count, generator temperature, and in-loop selection-scorer model size. Results show that iterative generation-selection can produce recipes with creativity scores comparable to human benchmarks, but additional iterations alone do not improve creativity. The in-loop evaluator matters most: a smaller selection scorer yields significantly higher scores across most TTCT dimensions, while temperature has limited effects except for originality. These findings suggest that evaluator design is a first-order design variable in subjective creative search.

---


### 95. [Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization in Language Models](https://arxiv.org/abs/2608.07261)

**<font color=#1a73e8>作者：</font>** Zili Zhang, Yilin Wang, Heng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can solve complex multi-hop problems yet exhibit puzzling failures on simple two-hop queries: although a model may correctly store each individual hop, it often fails to combine them. To understand the internal mechanisms of this phenomenon, we train transformers from scratch in a controlled symbolic environment. Our experiments reveal a pattern in two-hop generalization: models generalize reliably when the second hop follows the training distribution, but always fail when it deviates.
Through mechanistic analysis, we provide a complete explanation for these distinct generalization behaviors: in settings where models generalize successfully, performance is driven by the emergence of consistent intermediate representations for the same entities across contexts, whereas failures on settings where the second hop is out-of-distribution arise from a mismatch across layers: lower layers correctly construct these intermediate representations, but upper layers, while trained on corresponding atomic facts, primarily learn to map them to outputs rather than to reason over them.
Driven by this insight, we propose a recurrent-style training strategy, which enables transformers to reuse their reasoning circuitry across input forms and substantially improves generalization on out-of-distribution two-hop queries.

---


### 96. [Grammar Engineering Meets LLMs: Development of Cantonese and Irish ParGram Treebanks](https://arxiv.org/abs/2608.07283)

**<font color=#1a73e8>作者：</font>** Chit-Fung Lam, Elaine Uí Dhonnchadha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammar engineering requires expertise in linguistic formalism and computational implementation, especially in parallel grammar projects that balance cross-linguistic consistency with language-specific properties. This paper presents the development of Cantonese and Irish treebanks within the Parallel Grammar (ParGram) Project, where linguistic parallelism is maintained at an abstract functional level. We also investigate the methodological potential and limitations of using multilingual LLMs to support grammar engineering, focusing on Cantonese-Irish translation and the generation of formal syntactic structures using OpenAI's gpt-oss-120b model. The results show that translation performance was generally unsatisfactory and unaffected by prompt language. For syntactic structure generation, the model produced some structurally meaningful outputs, but performed poorly on tasks requiring cross-linguistic abstraction. Nonetheless, LLM-generated outputs may still offer some reference value by suggesting alternative analyses and (partially) capturing predicate-argument relations. Overall, our findings highlight both the potential and limitations of using LLMs in collaborative grammar engineering, while underscoring the continued importance of expert-driven analysis and verification.

---


### 97. [Foundation Models Adaptation for Multi-View Multi-modal Cardiac MRI Segmentation and Direct Ejection Fraction Estimation](https://arxiv.org/abs/2608.07291)

**<font color=#1a73e8>作者：</font>** Sina Amirrajab, Cian M Scannell, Volker Vehof 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have shown strong transferability in cardiac MRI (CMR), but their effectiveness for heterogeneous multi-view and multi-sequence CMR analysis remains unclear. In this work, we explore the effectiveness of fine-tuning and combining different CMR foundation models for the Universal Multi-Sequence, Multi-Center and Multi-View CMR Segmentation (CMR-Multi) Challenge. CineMA was fine-tuned for cine and late gadolinium enhancement (LGE) segmentation across short-axis and long-axis views. For direct left-ventricular ejection fraction (LVEF) estimation, we used two recent frozen CMR foundation models to extract embedding vectors that were then combined using attention-based multiple-instance learning for LVEF regression. In the challenge validation set, cine segmentation achieved Dice scores of 0.862, 0.883, and 0.902 for short-axis, two-chamber and four-chamber cine MRI, respectively. LGE segmentation achieved Dice scores between 0.621 and 0.846 across views. The direct LVEF regression model achieved an MAE of 4.96 percentage points and a Pearson correlation of 0.91. These results indicate that foundation models can be effectively adapted and combined for multi-view CMR analysis, while accurate LGE scar segmentation remains a challenging task.

---


### 98. [From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs](https://arxiv.org/abs/2608.07301)

**<font color=#1a73e8>作者：</font>** Neal Batra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study what can be recovered about the transition probabilities of a Markov decision process from optimal actions alone. This is closely related to the inverse problem considered by Letcher et al., who ask when the dynamics can be recovered from numerical \(Q\)-values. Here the numerical values themselves are not observed; only the optimal actions are known, for every reward in a given class.
For state-action rewards \(r(s,a)\), knowing the optimal actions for every reward also tells us how much better one action is than another when each is followed by the same fixed policy. This is still not enough to determine the transition probabilities uniquely. We prove that two kernels give the same optimal actions for every reward exactly when \[ Q_{s,a} =
\Bigl(P_{s,a}+\tfrac1\gamma e_s^{\mathsf T}(L-I)\Bigr)L^{-1} \] for one invertible matrix \(L\) satisfying \(L\mathbf 1=\mathbf 1\). Near a kernel with strictly positive entries, there is an \(n(n-1)\)-dimensional family of different kernels with this property. The result is unchanged if we consider only rewards having a unique optimal action at every state.
We then compare this with rewards of the forms \(r(s)\) and \(r(s,a,s')\). Rewards that depend on the next state can usually recover the transition kernel itself: every row at a state with at least two actions is determined, and we describe exactly when a row at a state with one action can remain hidden. State rewards reveal less: two kernels give the same optimal actions exactly when every deterministic policy is optimal for the same set of rewards. The results show how the form of the reward affects what can be learned about the dynamics from optimal actions alone.

---


### 99. [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](https://arxiv.org/abs/2608.07302)

**<font color=#1a73e8>作者：</font>** Zichuan Wang, Songlin Yang, Bo Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) often suffer from object hallucination, generating objects that are absent from the image. Prior work largely attributes this to insufficient visual attention. However, we find that both real and hallucinated objects receive equally strong visual attention in the model's mid-to-late layers, suggesting that the key issue may not be how much the model attends, but what it attends to and why. To this end, we decode the visual features of high-attention regions using Logit Lens, and observe that regions corresponding to real objects can be correctly decoded to the target object tokens, whereas those for hallucinated objects cannot. Building on this, we identify two hallucination mechanisms: (i) visual uncertainty, triggered by semantically similar or confusable regions; masking these regions eliminates the hallucination. (ii) contextual prior, triggered by strong co-occurrence priors; even when the initially attended region is masked, the hallucination persists and attention drifts to other regions. Based on these findings, we propose a simple yet effective training-free Detect-Mitigate framework comprising a Logit-Lens Consistency Check to detect hallucination and targeted remedies: High-Attention Regions Masking (HARM) for visual uncertainty hallucination, and Visual Evidence Enhanced Decoding (VEED) for contextual prior hallucination. Our approach achieves state-of-the-art results on multiple hallucination benchmarks. Code will be available.

---


### 100. [An End-to-End Agent Auditing Engine](https://arxiv.org/abs/2608.07346)

**<font color=#1a73e8>作者：</font>** Haoning Wang, Mingxun Zhang, Chenyue Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), harnesses have become essential infrastructure for deploying agents across a wide range of domains. The fast-evolving harness ecosystem has also made rigorous capability evaluation increasingly important. However, efficiently building an end-to-end, systematic, and comprehensive evaluation pipeline remains a significant challenge. To address this challenge, we introduce $A^2E$ (Agent Auditing Engine), an end-to-end evaluation engine designed for agent harnesses. $A^2E$ leverages our newly proposed Agent Task Protocol (ATP) to enable the rapid integration of evaluation tasks with different harnesses. Through an automatically instrumented Monitor, it captures and generates standardized execution traces during experiments. In the Evaluation stage, $A^2E$ systematically assesses harness capabilities using a suite of multidimensional metrics. Compared with correctness alone, these metrics provide a more fine-grained characterization of differences among harnesses in execution efficiency, tool use, task planning, and error recovery. Experiments conducted with $A^2E$ further reveal that model-harness combinations exhibit substantial performance variation across different types of tasks, and that no single combination consistently outperforms all others across every task. These findings not only demonstrate the necessity of systematic evaluation but also provide useful guidance for the co-evolving of models and harnesses. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-117](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
