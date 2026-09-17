# 🧠 大模型相关研究 | 2026年09月18日

> 本类共 **210** 篇论文：已确认 **198** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-210](./part-05.md)

---

### 51. [Apply-<x>Mag: One Tool to Support Many Inclusive Design Methods](https://arxiv.org/abs/2609.17948)

**<font color=#1a73e8>作者：</font>** Sadia Afroz, Rudrajit Choudhuri, Fatima A. Moussaoui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Doing inclusive design in HCI practice can be labor-intensive, a costly barrier that some companies and HCI practitioners may be unwilling or unable to overcome. Yet, not doing inclusive design is costly too, in the form of UX barriers that disproportionately disadvantage under-served user populations. To address this problem, we introduce Apply-<x>Mag, an LLM-powered tool to support HCI practitioners' work to design their products inclusively to wide ranges of users. Apply-<x>Mag is general, supporting any inclusive design method that can be expressed as <x>Mags (i.e., using attribute ranges and heuristics). It is also effective: Empirical results with researcher and practitioner teams using various combinations of two <x>Mags on 7 products showed Apply-<x>Mag precision averaging 90-99% and recall averaging 82-89%. Further, its environmental costs were reasonable, costing about the same resources as 2-4 ordinary Google searches.

---


### 52. [EDCT-Bench: Uncovering Faithfulness Gaps in VLMs via Explanation-Driven Counterfactual Testing](https://arxiv.org/abs/2609.17953)

**<font color=#1a73e8>作者：</font>** Sihao Ding, Santosh Vasa, Aditi Ramadwar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) can produce Natural Language Explanations (NLEs) that sound plausible yet remain inconsistent with the visual evidence they cite. We present Explanation-Driven Counterfactual Testing (EDCT), an intervention-based protocol that extracts visual concepts cited in a model's explanation, applies verified minimal edits to them, and tests whether the resulting answer and explanation remain consistent with the edited image. Using this protocol, we create EDCT-Bench, a comprehensive benchmark spanning three complementary domains: knowledge-intensive visual question answering (OK-VQA), safety-critical driving (DriveLM), and 3D spatial reasoning (3DSRBench). Across the evaluated VLMs, EDCT reveals substantial faithfulness gaps, with models frequently producing responses inconsistent with verified visual changes. Finally, our fine-tuning study suggests that EDCT-generated counterfactuals provide high-impact training signals.

---


### 53. [When to Call an LLM: A Confidence-Gated Hybrid for Cost-Effective Emotion Recognition in Conversational AI](https://arxiv.org/abs/2609.17977)

**<font color=#1a73e8>作者：</font>** Sai Babu Udayagiri, Arjun Chouhan, Ravisekhar Kanagala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion recognition in conversation (ERC) is a production capability behind agent-assist prompts, escalation routing, and post-call analytics in contact-center-as-a-service (CCaaS) platforms, where cost and latency constraints matter as much as accuracy. We report a systems-level comparison of three deployment options for dialogue-contextual ERC: a low-cost stacked ensemble (sentence embeddings, windowed context, RandomForest/XGBoost/logistic-regression stacking), off-the-shelf LLM prompting (GPT-4o-mini; zero-shot, few-shot, chain-of-thought), and a confidence-gated hybrid that escalates only the ensemble's least-confident predictions to the LLM - modeled on IVA-to-human-agent escalation policies used in production contact centers. On IEMOCAP, the ensemble significantly outperforms every LLM configuration (0.595 vs. 0.460-0.536 weighted F1, p < 0.0001) at a fraction of the cost and sub-10ms latency; on MELD and CMU-MOSI the ranking reverses, showing neither pure system is a safe default. The confidence-gated hybrid resolves this by Pareto-dominating both pure systems on all three datasets (0.620, 0.643, 0.824 weighted F1) while routing the majority of traffic through the near-zero-cost ensemble, translating to roughly $10-85 per million utterances versus $99-170 for an LLM-only pipeline. The escalation policy is not an opaque cost/accuracy dial: escalated turns disproportionately follow an emotion or sentiment shift, giving operators an interpretable, auditable routing signal, and the ensemble's confidence is well-calibrated and safely under- rather than over-confident. The pattern holds across three datasets and two LLM providers. Confidence-gated cascading is established in general ML systems; our contribution is showing it transfers cleanly to dialogue-contextual ERC, yielding a concrete deployment recipe for CCaaS and conversational-AI platforms deciding how to allocate LLM spend.

---


### 54. [Contiguity, Not Importance: Budgeted Repair of Stale KV Caches After Document Edits](https://arxiv.org/abs/2609.17983)

**<font color=#1a73e8>作者：</font>** Mingyang Mao, Wyatt Mackey, Xiaomin Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> KV-cache reuse can reduce inference cost in retrieval-augmented generation and agentic systems, but cached contexts may become stale when retrieved knowledge, working memory, or user state is edited. Under causal self-attention, even a local edit can affect downstream KV states. A full re-prefill reliably restores consistency but is costly, whereas refreshing only the edited span can leave downstream dependencies stale. We formulate in-place repair as budgeted recomputation and compare training-free position-selection policies on a factual RAG benchmark with matched direct and derived edits. Across three model families, all policies repair direct cases, but derived cases clearly separate them. At the primary budget, a contiguous edit-local window recovers at least 0.94 of the post-edit answer margin and substantially outperforms attention-based, KV-deviation, and structural selectors. Mechanistic analysis shows that position sets effective under clean-state transplantation can fail under actual recomputation because scattered positions inherit surrounding staleness. The edit-local advantage also depends on adjacency and largely disappears when the answer-bearing text moves downstream. Because answer-relevant edits almost always corrupt model behavior, failure severity is difficult to predict, and repair is 13-21 times faster than full re-prefill, our results support unconditional edit-local repair when the dependent text remains adjacent to the edit.

---


### 55. [TuiML: Machine Learning for AI Agents](https://arxiv.org/abs/2609.17984)

**<font color=#1a73e8>作者：</font>** Nilesh Verma, Nick Lim, Albert Bifet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine-learning libraries such as Weka and scikit-learn were designed for human programmers. Language-model agents now use these same libraries by recalling APIs from memory and writing code, an approach that hides what a library offers, delays errors until runtime, and loses experimental state between turns. We present TuiML, a self-contained machine-learning library built for AI agents, with native algorithms across supervised, unsupervised, time-series, data handling, tuning, and evaluation tasks. Every component describes itself through machine-readable metadata and parameter schemas, so an agent can search the library, inspect components, compose validated workflows, and register new ones that become discoverable in turn. Every call is validated, seeded, and traced, and sessions export as runnable notebooks, making experiments reproducible by construction. One specification layer drives the Model Context Protocol (MCP), agent-framework adapters, a Python API, a CLI, and local model serving, while data and models never leave the machine. Benchmarks show TuiML remains predictively competitive with scikit-learn and Weka. While looking like a conventional library to a human user, TuiML is designed for agents first, allowing them to read, extend, and operate machine learning autonomously. TuiML is open source, with documentation at this https URL.

---


### 56. [RideWay: Benchmarking Efficient Task Completion for Tool-Using Language Agents](https://arxiv.org/abs/2609.17985)

**<font color=#1a73e8>作者：</font>** Qingnuan Han, Boli Fang, Mingzhi Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are usually evaluated by whether they complete a task. In interactive service settings, a successful agent can still frustrate users by asking repeated questions, performing redundant searches, or making avoidable revisions. We introduce RideWay, an efficiency-centered benchmark for ridehailing agents in a stateful tool-calling environment, together with Efficiency Utility, a success-gated metric that discounts successful trajectories for excess tool calls and user-facing turns relative to task-specific reference effort. Human paired preferences calibrate the relative penalties, reflecting an aggregate service-workflow trade-off: extra dialogue often creates visible friction, whereas extra tool use can sometimes verify constraints or preserve user intent. Across 58 tasks and 24 models, the fitted penalty for excess turns is about twice that for excess tool calls. On task-disjoint held-out preferences, Efficiency Utility achieves 78.7% accuracy overall: 90.6% when trajectories differ in turns, but chance-level accuracy when they differ solely in tool calls - the axis on which human annotators agree least. RideWay therefore makes interaction efficiency measurable alongside task success, while exposing the boundary of count-based tool-use evaluation.

---


### 57. [Multimodal Conditioning of Fine-Tuned Stable Diffusion XL for Controllable and Culturally Faithful Ulos Motif Generation](https://arxiv.org/abs/2609.17987)

**<font color=#1a73e8>作者：</font>** Humasak Simanjuntak, Tamara Yunika Sianipar, Bronson T.M Siallagan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The traditional Batak Ulos weaving industry faces growing challenges in producing diverse, innovative motifs due to limitations in conventional, manually driven design methods. This study proposes a multimodal generative framework integrating a fine-tuned Latent Diffusion Model (Stable Diffusion XL v1.0 via LoRA) with a Multimodal Large Language Model (LLaMA 1.5-7B) to enable controllable, culturally faithful Ulos motif generation. Four complementary conditioning mechanisms: text, image, representation, and semantic map (via ControlNet) jointly guide the generation process, each governing a distinct aspect from semantic intent to spatial layout. A five level ablation study across three scenarios (shape transformation, colour variation, and high-complexity input) shows that conditioning effectiveness is not proportional to the number of mechanisms combined: Text + Image + Semantic Map achieved the best FID (270) and CLIP Score (0.65 - 0.70) but the weakest SSIM (0.65), while Text + Image + Representation offered the best overall balance, with stable SSIM (0.84) and competitive FID (280). Combining all four mechanisms yielded the weakest FID (330), indicating conflicting optimization signals. Qualitative evaluation by nine weavers and thirty public participants confirmed statistically significant positive acceptance (Wilcoxon, p=0.007 and p<0.001, respectively). A web-based prototype supporting text-to-image and image-to-image generation was also developed, offering a practical digital design tool for cultural heritage preservation.

---


### 58. [QuanText: Protecting Dataset-Level Secrets in Textual Data Sharing](https://arxiv.org/abs/2609.17995)

**<font color=#1a73e8>作者：</font>** Shuaiqi Wang, Zinan Lin, Giulia Fanti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural-language datasets support many downstream applications and research studies, but releasing text can reveal sensitive global properties of the underlying data source, such as the proportion of records associated with a particular gender, diagnosis, or political stance. Existing work has largely focused on property inference attacks that recover such global properties, while defenses for protecting these dataset-level secrets remain limited. Differential privacy, although effective for protecting individual records, provides only weak protection for aggregate properties. We propose Randomized Quantization for Text (QuanText), a training-free and large-language-model-agnostic data release mechanism that protects global secrets in textual datasets while preserving data utility. Given a dataset-level secret, such as the proportion of records with a particular diagnosis, and attributes whose utility should be preserved, such as topic and sentiment, QuanText perturbs both the secret distribution and the distributions of correlated attributes. It does so by constructing candidate release distributions over secret and non-secret attributes, randomly selecting a candidate sufficiently close to the private empirical distribution, and rewriting each private text sample to match the selected distribution using attribute-related snippets from the original text. QuanText is inspired by the Statistic Maximal Leakage (SML) framework, which bounds leakage about a secret function of a data distribution. Under idealized conditions, we show that QuanText satisfies an SML guarantee. Since these conditions may not hold exactly in practice, we also evaluate QuanText empirically on real-world datasets. Our results show that QuanText achieves a better empirical privacy-utility trade-off than competing data generation baselines.

---


### 59. [Modeling the Developmental Shift in Telicity Acquisition](https://arxiv.org/abs/2609.17996)

**<font color=#1a73e8>作者：</font>** Ellie Xia, Parisa Kordjamshidi, Alan Hezao Ke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Acquiring telicity, which is the distinction between bounded (e.g., ate an apple) and unbounded (e.g., ate apples) events, requires first language (L1) learners to map surface-level and semantic cues to abstract event structures, but the computational trajectory of this mapping is not well understood. We introduce a Difference in Surprisal method that uses GPT2 token surprisal over paired temporal adverbial diagnostics (in an hour versus for an hour) to automatically label telicity across English CHILDES corpora, validated against expert linguist judgments. Using these labels, we train diagnostic logistic regression classifiers on 12 syntactic and lexical semantic features to compare how child speech and child-directed speech encode telicity. The two models diverge: the child model reaches near perfect accuracy through a single deterministic cue, the presence of a post-verbal determiner, while the adult model relies more heavily on verb class and other lexical semantic features, with the determiner cue neutralized. This trajectory supports Syntactic Bootstrapping: learners first exploit high-frequency structural cues as a scaffold to bootstrap, before developing fully compositional, verb-based event structures.

---


### 60. [A Calibrated Instrument for Measuring How Inference Optimizations Affect Output Quality](https://arxiv.org/abs/2609.18005)

**<font color=#1a73e8>作者：</font>** Jerry Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model optimization is an active research area, spanning quantization of model weights, early-exit methods for skipping layers, and speculative decoding. Each track uses its own quality measures, typically an idiosyncratic benchmark score. Few approach the measurement precision required by other scientific disciplines.
We propose a rigorous methodology for measuring output quality, suitable for cross-system and cross-technique comparison. We score outputs with an LLM as a judge, but calibrate the judge formally: we compare its scores on two ordinary runs of a model given the same prompts, verifying that it shows no systematic preference between statistically equivalent outputs and measuring its per-sample noise. Each design also includes a 'null' condition, provably identical in distribution to the unmodified model, whose measured difference must be zero.
With this one instrument we measure several acceleration techniques on the same prompts, so their quality costs can be compared. Perceived quality proves highly dependent on the domain of discourse. A 4-bit model was indistinguishable from its 16-bit original down to our design's +/-0.3-point resolution, in English prose and Chinese alike. At 3-bit precision the same prompts lost 0.5 points in English prose, 0.9 in Chinese, and 1.1 on multi-step math; early exit that cost 0.7 points on prose cost 2.5 on math, cutting correctly solved problems from 19 of 27 to 6. The pattern held for models from Alibaba and from Meta, but not its magnitude: the same quantizer cost Meta's model 1.8 points where it cost Alibaba's 0.7.
A model's certainty about a token predicts how likely it is to differ from the full model's choice, but not how much that difference affects judged quality, so acceptance rules relying on certainty cannot distinguish errors that matter from errors that don't.

---


### 61. [Newer Is Not Fairer: Gender Stereotyping in Text-to-Image AI Across Model Generations](https://arxiv.org/abs/2609.18007)

**<font color=#1a73e8>作者：</font>** Shesh Narayan Gupta, Nik Bear Brown  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generative models are widely used in professional and creative settings, yet how they represent gender across occupations -- and whether newer models are fairer -- remains poorly understood across multiple generations. We evaluate gender representation across 20 occupations, 5 prompt templates, and 4 Stable Diffusion model generations (SD 1.5, SD 2.1, SDXL, SD 3 Medium), generating 8,000 images with n = 100 per occupation-model cell (5 prompts x 20 images), and classifying all with DeepFace. Across the 8,000 open-source images, 76.4% show male subjects (95% CI [75.1%, 78.7%], p < 2.2 x 10^-16, Benjamini-Hochberg adjusted). More strikingly, 57.6% of images for historically female-coded occupations show male subjects (raw p = 3.43 x 10^-22, BH-adjusted p = 1.71 x 10^-21). All nine significant tests reported in this paper survive BH correction across 10 tests. When compared against U.S. Bureau of Labor Statistics workforce data, models underrepresent women by 20-46pp on average, with particularly large deviations for near gender-balanced occupations: scientist (48% female in BLS, 82-99% male in model outputs) and cleaner (46% female in BLS, 80-92% male in outputs). Model generations do not improve steadily: bias worsens from SD 1.5 to SDXL before partially recovering in SD 3 Medium. A preliminary comparison with GPT-image-1 on five occupations suggests lower bias than open-source models, though the practical effect is small (Cramer's V = 0.080) and the comparison is exploratory. No model achieves gender parity.

---


### 62. [CoAtNet-DeepMoE: A Convolution-Attention Hybrid with DeepSeek Mixture-of-Experts for Parameter-Efficient Tomato Disease Classification](https://arxiv.org/abs/2609.18038)

**<font color=#1a73e8>作者：</font>** Md Nadim Mahamood, Md Arif Shahriar, Md Shafi Ud Doula 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The world population is growing rapidly, and technology is improving in parallel. Meeting the huge demand for food for these 7 billion people not only depends on increasing food production but also on reducing food loss. Crop losses due to disease affect both the food supply and the financial and economic stability of a country. Tomatoes are among the top food-producing crops globally, and a significant portion of this production is lost due to disease. People have used Machine Learning techniques for feature extraction and early diagnosis of tomato diseases, and nowadays, Deep Learning-based models are widely used for disease recognition. However, most existing models are highly parameter-intensive, which increases the time required for training and inference. As a result, while lightweight models are more suitable for user-friendly applications, they often show a reduction in performance. To balance performance and model size, we propose CoAtNet-DeepMoE, a Convolution-Attention hybrid architecture for rich feature extraction, further enhanced with a DeepSeek Mixture of Experts to substantially reduce the number of parameters without sacrificing accuracy. We evaluate our model on both balanced and imbalanced datasets from Kaggle and PlantVillage, demonstrating robustness and achieving 99.80% accuracy, 99.80% precision, 99.80% recall, and 99.80% F1-score on Kaggle, and 99.83% accuracy, 99.85% precision, 99.76% recall, and 99.80% F1-score on PlantVillage, representing state-of-the-art performance with only 2.47M parameters. The source code will be available at this https URL.

---


### 63. [Anchoring What Matters: A Dual-Level Learning Framework for Visually-Grounded Multimodal Reasoning](https://arxiv.org/abs/2609.18057)

**<font color=#1a73e8>作者：</font>** Xinxin Song, Siyuan Li, Tingxiong Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has significantly improved the reasoning capabilities of large vision-language models (LVLMs). However, standard on-policy RLVR algorithms face a critical optimization bottleneck in preserving and reinforcing visually grounded reasoning behaviors: valuable visually-grounded reasoning trajectories are discarded after a single update, while uniform token advantage allocation prevents the model from reinforcing critical perception or reasoning steps. To bridge this gap, we propose PIVOT, a dual-level learning framework that anchors policy optimization around informative visual reasoning signals. Specifically, PIVOT introduces a self-calibrated experience replay mechanism, which selectively collects and replays visually-grounded historical experiences as stable reference anchors for policy optimization. Building upon this, we further design a vision-guided advantage allocation mechanism to allocate additional vision-aware advantages to tokens based on their local visual support and impact on downstream reasoning. Extensive experiments across diverse benchmarks demonstrate that PIVOT achieves highly competitive performance in enhancing the multimodal reasoning capabilities of LVLMs.

---


### 64. [The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://arxiv.org/abs/2609.18063)

**<font color=#1a73e8>作者：</font>** Yu Lin, Yiming Wang, Runyuan Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before layer N's output exists, so the reads cannot start early enough to hide behind compute. We present Edge0, a streaming MoE inference engine that closes the gap with a prerouter: a per-layer head predicts the next layer's routing one token ahead, and the prediction is consumed as the routing itself, so the staged expert set equals the routed set and nothing is dropped. An unmerged recovery LoRA, trained on the student path, pays back the quality lost to int4 quantization and routing replacement. On a single 24GB machine, Edge0
serves a 35B MoE at 20tok/s inside 3GiB of peak active memory, within a few points of its fp16 teacher on average across five public benchmarks. An 8B tier runs on the same framework, and the framework, checkpoints, and adapters are open source.

---


### 65. [From a River in Gilead to the Inference Distributions of Large Language Models: Covert Dialect Bias and Linguistic Profiling at Scale](https://arxiv.org/abs/2609.18068)

**<font color=#1a73e8>作者：</font>** Chowdhury Mohammad Abdullah, Rita Orji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in high-stakes domains such as housing screening. While alignment techniques mitigate explicit racial bias in generated text, they often leave covert attitudinal associations in internal probability distributions untouched. Adapting the matched-guise sociolinguistic paradigm, we examine covert dialect bias in housing-related social judgments across four varieties: Standard American English (SAE), African American Vernacular English (AAVE), Nigerian Standard English (NSE), and Nigerian Pidgin (NP). AAVE reflects the racialized dialect studied in prior covert-bias evaluations, whereas NSE and NP represent Black African, postcolonial varieties absent from this literature. Using 260 meaning-matched sentence quadruples and log-probability scoring over housing-relevant adjectives, we probe ten open-weight LLMs across three contexts varying in social proximity: tenant screening, neighbor acceptance, and roommate selection. Across all ten models, AAVE and NP are consistently associated with more negative adjectives than SAE, with NP penalized most severely. Crucially, each dialect is penalized via distinct stereotype clusters rather than a generic non-standard category. NSE, which carries institutional prestige, displays a context-dependent shift: favored over SAE in formal tenant screening but increasingly penalized as social proximity grows. Our findings reveal that LLMs inherit covert dialect bias along both racial identity and prestige dimensions, echoing documented human housing discrimination and demonstrating its reach across postcolonial English varieties.

---


### 66. [Decodability is Not Causality: Dissociating Probe Readouts from Behavioral Drivers via SAE Decomposition](https://arxiv.org/abs/2609.18080)

**<font color=#1a73e8>作者：</font>** Devesh Tiwari, Camille Davis, Shivank Sinha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear probes can decode safety-relevant concepts such as truthfulness from language-model activations, but probe accuracy may show only decodability, not that the features the probe weights causally drive model behavior. We demonstrate that this gap cannot be closed from the geometry of probe weights alone: the features geometrically aligned with probe direction need not be the ones the model uses, so causal relevance requires intervention. We introduce a feature-level diagnostic that decomposes a deployed True/False probe into sparse-autoencoder (SAE) features, ranks those features by both probe alignment and by gradient sensitivity of the model's behavior, and ablates the resulting shared, probe-only, and random feature sets under a coherence gate. On the truth probe of Buerger et al. (2024) (TTPD), applied in the instructed truth/deception setting of Long et al. (2025) for Gemma2-9B-Instruct, the two rankings overlap only weakly (about 12%, Spearman rho = 0.10), and ablation dissociates them sharply: features the probe shares with the model flip the output far more (up to 27%) than equally sized probe-only (6%) or random (1%) features at full coherence, while probe-only features instead perturb the probe's own readout. The dissociation holds across five seeds and a held-out split, and an activation-aware selection of features flips behavior nearly three times as often as the probe's geometric top features (17.6% vs. 6.1%). In this setting, therefore, the geometric projection of a probe's weight vector alone does not identify the features the model causally uses; however, combining probe information with feature activation statistics recovers substantially more behaviorally causal features, and coherence-gated SAE intervention is needed to separate them from probe readouts.

---


### 67. [Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Yunheng Zou, Shaokun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous research loops such as AutoResearch show that one coding agent can improve a training setup unattended. Run several of them and each session starts from scratch, so more agents tend to mean more duplicated search rather than more discovery. Agora is a shared memory for such agents: research is recorded as an append-only directed acyclic graph (DAG) stored in Git, so that every claim is a commit anyone can check out and rerun. Each result, insight, hypothesis, verification, and report is an immutable commit whose parent edges say what it builds on; a derived index exposes the frontier, the neglected branches, and the verification status of each claim, and a diversity-aware selection rule keeps the community from collapsing onto one leader. We describe the system and report its first sustained use: a run of nearly 12 days in which 13 language-model workers, with no assigned tasks and no central planner, worked on a weight-transfer problem. Given 141 pretrained donor models and a frozen 119.6M-parameter attention-SSM hybrid whose dimensions match no donor, the workers had to initialize the target without training data or gradient updates. They published 1,703 contributions and drove the evaluator from 3.39 to 1.899 bits per byte, closing 62% of the gap to a trained GPT-2 124M. The winning recipe compresses donor next-token statistics into the target's embedding and output head, then adds a short-range context signal through sparse edits to attention, feed-forward, and state-space blocks. Its 145-commit ancestry spans 15 accounts, and 165 independent reproductions were posted, none of which failed. We describe the single mid-run human intervention that pulled the community out of a monoculture, what the trace does and does not establish, and the controlled comparison that would settle whether shared research state improves discovery per unit of compute.

---


### 68. [When Is Graph Structure Worth Its Cost? The Case for Structure Pricing in Retrieval-Augmented Generation](https://arxiv.org/abs/2609.18099)

**<font color=#1a73e8>作者：</font>** Yuzhong Zhang, Haoyang Ma, Chao Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation (RAG) can help answer questions that require information from many documents. However, building a graph often requires many language-model calls during ingestion. It is therefore important to ask whether its quality gains justify the additional cost.
We present EffiRAG, a graph-based RAG system designed to reduce this cost. It uses the graph to locate relevant passages and generates answers from the original text. This design preserves source information while keeping graph construction and query processing lightweight.
We evaluate EffiRAG on UltraDomain, which contains 120 open-ended questions from four domains. Compared with LightRAG-hybrid, EffiRAG produces the preferred answer on 93 questions. LightRAG is preferred on 7, and the remaining 20 are splits. EffiRAG also reduces total system cost by 57 percent, from USD 0.952 to USD 0.408. The cost includes language-model calls during ingestion and querying.
The advantage remains as the corpus grows. At 10 and 20 documents per domain, EffiRAG uses a lightweight, non-LLM filter to skip low-salience chunks. It remains preferred over LightRAG-hybrid. It costs 4.2 times and 4.5 times less, respectively.
The comparisons identify different quality-cost trade-offs. Graph-based RAG systems should therefore be evaluated by both answer quality and cost. The results favor graph structure that locates and preserves source evidence.

---


### 69. [Linguistic Triggers of Gender and Racial Bias in Open-Weight LLMs Applied to Recruitment](https://arxiv.org/abs/2609.18106)

**<font color=#1a73e8>作者：</font>** Kosuke Kitahara, Nobuhiro Yamaguchi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models are rapidly entering hiring pipelines, yet their discriminatory failure modes -- and the regulatory exposure these create under the EU AI Act high-risk classification (Annex III) and U.S. EEOC adverse-impact analysis -- remain poorly understood. We present the first systematic, multi-model audit of open-weight LLMs that treats job-posting language as the primary experimental variable, evaluating six models (Llama 3.2, Mistral, Gemma 3, Qwen 3, Phi 3, DeepSeek-R1) across four controlled experiments that jointly probe recruiter-simulation and job-seeker-simulation tasks. We find that (1) agentic posting language depresses recruiter recommendation scores for female candidates (r_rb = 0.309, p_Bonf = 7x10^-5; model-fixed-effects r_rb = 0.448), while communal language partially reverses the penalty; and (2) coded-exclusion language suppresses non-White recruiter scores at large effect sizes (r_rb = 0.646-0.758) and, on the job-seeker side, selectively deters non-White personas from expressing interest -- operationalizing a chilling-effect mechanism at scale. A label-ablation experiment isolates the explicit demographic persona label as the primary causal driver, and Word Embedding Association Tests corroborate these findings at the representational level (d = 1.01-1.45 under Caliskan et al.'s multi-word gender attribute lists). We translate these results into a concrete pre-deployment audit protocol -- posting-vocabulary scoring, persona-conditioned LLM probing, and adverse-impact flagging against the four-fifths threshold -- that operationalizes the documentation and risk-management obligations Annex III imposes on high-risk AI in recruitment.

---


### 70. [PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs](https://arxiv.org/abs/2609.18120)

**<font color=#1a73e8>作者：</font>** Rushabh Vipulkumar Patel, Dipo Dunsin, Mohammed Almaiah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-driven penetration testing has been demonstrated with premium frontier models such as GPT-4, but the per-engagement token cost makes continuous, automated testing unaffordable for the smaller organisations that need it most. This paper presents PentestChain, a ten-phase automated penetration testing framework that couples a curated, deterministic exploit map with a cost-aware AI cascade-a local Ollama model (qwen2.5-7b) first, then free-tier OpenRouter and Cerebras, with a rule-based fallback that always produces output-and exposes the full pipeline through a Model Context Protocol (MCP) server with eleven tools. We make three contributions. First, we treat US-dollar cost per engagement as a measured, first-class evaluation metric and show that a 7B-parameter local model, kept off the critical path by a deterministic backbone, sustains end-to-end operation at zero measured paid-API cost. Second, we analyse the attack surface that an MCP-exposed offensive engine introduces, grounding a four-position threat model in the 2025 MCP incident record (the CVE-2025-6514 remote-code-execution flaw in mcp-remote, the postmark-mcp supply-chain backdoor, and the tool-poisoning-rug-pull-line-jumping class), and contribute four mitigations. Third, we specify a reproducible, containerised evalua-tion protocol aligned with the standardised testbeds now expected at top-tier venues-AutoPenBench, a Cybench subset, and the PentestGPT 182-sub-task benchmark-with multi-trial statistics (more than 10 trials per configuration, pass-at-k, non-parametric significance tests and effect sizes) and direct, same testbed reproduction of the PentestGPT and PentestAgent baselines rather than citation of their published numbers. On the legacy targets measured to date, the framework detected 26 services, enriched 34 CVEs, produced

---


### 71. [AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines](https://arxiv.org/abs/2609.18123)

**<font color=#1a73e8>作者：</font>** Li Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents tune GPU kernels and serving engines through a closed loop of propose, measure, and keep, but the measurements behind this loop are not trustworthy. We characterize four failure modes from a four-day pilot corpus of 619 model calls: strawman baselines manufacture speedups, absolute times do not transfer across machines, saturated tasks nullify comparisons, and infrastructure defects impersonate science. We present AutoTuneBench, a benchmark and measurement protocol that makes trust architectural. The protocol is frozen as code with test-enforced provenance; a database-level validator rejects out-of-protocol results; anti-cheat checks run outside the agent's modification surface; comparisons follow pre-registered readouts; and measurements anchor to externally published results, grounded in paired-seed statistics with a 5\% cross-run coefficient-of-variation cap. Honest measurement rewrites the headlines: our best kernel reads 10.6x against a naive baseline but 2.03x against the honest one; one configuration delivers 1.174x on one machine and 1.0049x on another; a pre-registered on/off comparison nulls at a shared wall (2.4840 vs 2.4957\,ms); and the KernelBench Level-1 suite admits 51\% of tasks with median speedup 1.0001x over PyTorch eager. The protocol, the two-engine corpus (vLLM and SGLang), and its audit trail are released as open artifacts.

---


### 72. [Symbolic Temporal Supervision of LLM Agents Using Contracts](https://arxiv.org/abs/2609.18128)

**<font color=#1a73e8>作者：</font>** Yifeng Xiao, Pierluigi Nuzzo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents augmented by tools can automate complex, multi-step tasks, such as web navigation, code generation, and workflow orchestration, by acting on external systems through tool calls. However, hallucinations, distributional instability, and adversarial manipulations in LLMs, and the irreversible consequences of certain tool calls can lead to harmful outcomes. Existing safeguards either grade recorded trajectories post hoc with stochastic LLM judges or block unsafe actions one call at a time, and no single deterministic artifact supports both roles. We present ContrAgent, a contract-based framework for symbolic temporal supervision of LLM agents. ContrAgent captures an agent's behavior as a sequence of tool calls and formalizes it as a trace over a fixed set of checkable predicates. It then specifies required behaviors using assume-guarantee contracts in linear temporal logic over finite traces (LTLf). Each contract is compiled to a deterministic finite automaton (DFA) that serves two roles: gating agent actions online and evaluating recorded traces offline. A contract library, acting as a reusable knowledge base, is maintained independently of the agent's model and can be applied across different agents within the same task domain. We show the effectiveness of our approach on four benchmarks spanning both roles, where ContrAgent matches state-of-the-art LLM-judge and rule-based guardrail baselines while producing deterministic, reproducible verdicts and, in the online mode, orders-of-magnitude lower per-call latency.

---


### 73. [Colla-Q: Toward Collaborative Experts in MoE Quantization via Minimax Precision Balancing](https://arxiv.org/abs/2609.18131)

**<font color=#1a73e8>作者：</font>** Eunju Shin, Jongbin Ryu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a Mixture-of-Experts (MoE) quantization method based on activation entropy. Although quantization reduces memory and computational costs, it can substantially degrade performance. In particular, performance decline is pronounced in quantized MoE models, where individual experts have a small number of parameters that are sensitive to low-bit representation. Considering that MoE operates as an ensemble model with collaborative contributions from routed experts, a significant performance decline of a particular expert due to quantization can harm model performance. Therefore, we propose Colla-Q, a bit-allocation framework to maintain balanced performance across experts through an activation-entropy-based bit-width allocation algorithm. This approach encourages each expert to operate collaboratively in the quantized model, thereby 1) improving the overall MoE performance and 2) reducing the dependence on the calibration dataset. Since uniformly adjusting each expert's performance facilitates robustness and stability of the MoE model, the proposed MoE quantization method can generalize more consistently across different calibration datasets. Our code is available at: this https URL

---


### 74. [Multi-View Mixture-of-Experts with Vision-Language Reranking for Cross-View Object Geo-Localization](https://arxiv.org/abs/2609.18139)

**<font color=#1a73e8>作者：</font>** Xuyu Fan, Qi Ming, Zhu Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view object geo-localization (CVOGL) locates a target in satellite imagery using drone or street-view queries. Existing methods train separate detectors for each viewpoint, leading to parameter redundancy and impeding cross-view knowledge sharing. Moreover, top-ranked satellite candidates are often visually similar, so visual appearance and categorical labels alone are insufficient to resolve such ambiguity. To address these, we propose MVLGeo, an efficient framework designed to unify multiple viewpoints and reduce model redundancy. First, we introduce environmental contextual text from the query view as cues to distinguish visually similar candidates via Vision-Language Reranking (VL-Rerank). Second, we design a multi-view Mixture-of-Experts architecture (MV-MoE) with a shared encoder and view-specific experts to reduce redundancy and promote knowledge sharing, while cross-view contrastive learning aligns their representations for consistency. Third, we introduce an adaptive elliptical prior (ESAM-Prior) as auxiliary positional encoding for anisotropic geometric perception. Extensive experiments on the CVOGL benchmarks confirm that MVLGeo, as a unified model for multiple query viewpoints, achieves state-of-the-art performance, demonstrating robustness to input degradation and generalization across viewpoints. Code and models will be available on GitHub to facilitate future work.

---


### 75. [LIGE-GR: A Smooth Leap from Ranking to Generative Recommendation in the LLM Era](https://arxiv.org/abs/2609.18148)

**<font color=#1a73e8>作者：</font>** Venkat Srinivas, Chenzhang He, Sam Woodmansee 等 62 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The remarkable success of large language models (LLMs) has provided important inspiration for the next generation of recommender systems. Structurally, recommendation and language generation share a similarity: both aim to produce an ordered sequence that optimizes the user's experience. However, how to precisely absorb the essence of the LLM paradigm into mature industrial recommender systems remains an open problem.
There are two challenges. First, it is unclear how to incorporate sequence-level generation and optimization from the LLM paradigm into recommendation. Second, real-world recommender systems are mature systems that have been iteratively customized for years around specific products, business constraints, serving infrastructure, and organizational ownership. Replacing such systems wholesale is often technically risky and organizationally disruptive.
In this paper, we propose LIGE-GR, a listwise generation and evaluation recommendation framework that upgrades from a traditional ranking system based on itemwise recommendation toward a generative recommendation paradigm. Instead of rebuilding the entire recommendation stack from scratch, LIGE-GR generalizes the existing pointwise recommendation system into a listwise generation system. This allows mature recommender systems to benefit from listwise optimization while preserving compatibility with existing models, value functions, and serving infrastructure.
We validate LIGE-GR in short-video recommendation on Instagram Reels and Facebook Video. On these recommendation surfaces, LIGE-GR improves time spent by 1.14 percent on Instagram Reels and 0.72 percent on Facebook Video, while requiring only modest additional inference resources.

---


### 76. [TeochewBench: A Human-Reviewed Benchmark for Teochew Hanzi Translation](https://arxiv.org/abs/2609.18156)

**<font color=#1a73e8>作者：</font>** Jianan Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Teochew has a substantial speaker community and exhibits distinctive lexical, syntactic, and pragmatic features, yet textual resources for evaluating large language models remain limited. We present TeochewBench, a human-reviewed benchmark comprising 300 Teochew Hanzi expressions for evaluating translation from Teochew Hanzi into Mandarin Chinese and English. The dataset covers five categories: basic vocabulary; everyday sentences; Teochew-specific expressions; tone, politeness, and context; and idiomatic, ambiguous, and culturally specific expressions. A primary Teochew-speaking reviewer examined all entries individually and revised them as needed, while two additional Teochew speakers verified selected items.
Our main evaluation covers 11 official general-purpose post-trained models on the reviewed dataset in both translation directions, yielding 6,600 predictions. Two official base checkpoints provide 1,200 predictions for supplementary diagnostics, bringing the total to 13 models and 7,800 predictions. We additionally include a Hanzi-copy control, which returns the source input unchanged, to assess how shared Hanzi affect automatic scores for translation into Mandarin Chinese. Qwen3.5-27B achieved the highest overall chrF-style score among the evaluated checkpoints, at 60.63, followed by Qwen2.5-72B-Instruct at 56.61, Gemma-3-27B-IT at 56.36, and GLM-4-32B-0414 at 55.82. Across the 11 main-evaluation models, the mean chrF-style score decreased from 69.25 for low-specificity items to 27.52 for high-specificity items. High-specificity expressions received lower scores and exhibited smaller cross-model differences, suggesting that they constitute a shared low-scoring region across the model families evaluated here. The Hanzi-copy control further indicates that surface overlap in low-specificity items can substantially affect automatic scores for translation into Mandarin Chinese.

---


### 77. [WFM: Wiki Foundation Model for Complex Agentic Reasoning](https://arxiv.org/abs/2609.18182)

**<font color=#1a73e8>作者：</font>** Junnan Dong, Linhao Luo, Senlei Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world agents fundamentally require persistent non-parametric knowledge for dynamic reasoning, i.e., long-term memory and retrieval-augmented generation. While graphs have shown reliable advantages in providing structured evidence, the sparse graph representations naturally restrict machine readability and semantic density required for complex agentic workflows. Driven by this limitation, the entire industry is witnessing a paradigm shift from traditional sparse graphs to LLM Wiki, an agent-native knowledge representation that couples dense document contexts with markdown files containing multi-layered topological linkages. However, parameterizing such rich semantics is challenging to encode dense textual contexts using traditional sparse graph embeddings. Moreover, learning LLM Wiki with existing graph encoders could overwhelm distributed system overheads that hinder deployment in large-scale commercial scenarios. To this end, we propose a novel paradigm Wiki Foundation Model, i.e., WFM, tailored for scalable, agent-native representation and retrieval. Specifically, (i) we formalize a Wiki Graph schema that seamlessly bridges fine-grained structures with dense contexts, maintaining explicit topologies alongside continuous semantics; (ii) A query-conditioned attentive aggregation is tailored for rich wiki message passing and explicit attention variance regularization; (iii) We engineer an infrastructural NCCL boundary exchange protocol that hoists static partition indices and leverages fixed-shape GPU-to-GPU collectives, bypassing CPU serialization and memory copy overheads. Extensive evaluations across five long-term agent memory and multi-hop reasoning benchmarks demonstrate the remarkable performance of WFM, while achieving a 10.5 times training acceleration on distributed clusters.

---


### 78. [Misgendering as Breakdown in Human-Machine Communication: How AI Companion Chatbot Users Experience and Repair Misgendering](https://arxiv.org/abs/2609.18186)

**<font color=#1a73e8>作者：</font>** Julia Liu, Qing Xiao, Leona Yinglang Pang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In recent years, large language model-based AI companion and role play chatbots have grown increasingly popular. People turn to these chatbots for emotional support and to engage in romantic and erotic role play. Although prior research suggests that digital role play can help people explore their gender and sexuality, LLM based technologies are also replete with gender and sexuality biases. In this study, we examine one way that AI chatbots can harm users: misgendering. In order to study chatbot misgendering we qualitatively analyzed 326 posts mentioning misgendering that were shared in AI companion or role play subreddits. We document how chatbot misgendering takes place and how, in response, users engage in ongoing work to curate their gender presentation to prevent and repair misgendering. We discuss how researchers and designers can mitigate chatbot misgendering and consider the implications of using AI chatbots for identity exploration.

---


### 79. [Behavior2Value: Benchmarking and Empowering LLMs for Consumer Value Measurement from E-commerce Behaviors](https://arxiv.org/abs/2609.18203)

**<font color=#1a73e8>作者：</font>** Peixuan Hou, Bin Chen, Li He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human values are deep motivational orientations that shape human behaviors. In e-commerce, they reveal the stable drivers behind users' purchase decisions. Compared with short-term interests, consumer values better explain how users evaluate products before purchase. However, consumer values are often implicit in complex and fragmented behavioral trajectories, leaving value measurement from e-commerce behaviors largely underexplored. To this end, we propose the Behavior-to-Value (B2V) task, which aims to identify consumer values from e-commerce behavioral trajectories. Centered on this task, we first construct the E-commerce Consumption Value Taxonomy (ECVT) and introduce B2V-Bench, the first B2V dataset and benchmark, based on anonymized Taobao behavioral logs. B2V-Bench consists of real-world purchase decision episodes, covering 25 types of purchase behaviors, along with corresponding consumer value orientations manifested in each episode. To improve consumer value measurement accuracy, we further present B2V-Verifier, a behavior-to-value measurement model based on Value Verification Tuning, which learns to assess whether behaviors provide sufficient evidence for each value inference. Experiments show that B2V-Verifier outperforms strong LLM baselines, improving multi-label classification by 34\%. The dataset and code will be publicly released upon acceptance.

---


### 80. [Beyond Accuracy: How Procedural Traces Shift the Decision Criterion of LLM Overseers](https://arxiv.org/abs/2609.18204)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Di Zhu, Lei Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizations increasingly use oversight loops where one large language model (LLM) audits another's outputs alongside procedural traces of claimed steps. A common concern about such LLM-as-a-judge pipelines is that detailed traces make overseers gullible. Using signal detection theory, we audit five LLM overseers on 19 compliance tasks (4,551 analyzed judgments), varying only trace detail and evidence labeling. With disconfirming evidence always visible, error detection remains near ceiling. Instead, elaborate traces shift the decision criterion toward rejection, increasing false alarms in susceptible overseers. Without option labels, human-validated reason coding shows about 60% of false alarms cite an inability to tie evidence to its option. Labels eliminate this stated reason, yet residual rejection of correct work persists in those overseers and rises with trace detail. Procedural traces thus act as governance artifacts that shape oversight decisions. AI auditors should be evaluated by their decision criterion and false-alarm behavior, alongside accuracy.

---


### 81. [Understanding Dynamic Scenes at Gigapixel Scale: Wide-Area Spatio-Temporal Perception from UAVs](https://arxiv.org/abs/2609.18210)

**<font color=#1a73e8>作者：</font>** Yuhang Zhu, Meiyi Zhu, Yunkai Dang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV-borne imaging has advanced from megapixel to gigapixel sensors, shifting aerial perception from recognizing individual targets to understanding entire dynamic scenes. We characterize this demand as Wide-area Spatio-temporal Scene Understanding (WSTU), which requires wide-area coverage, per-target resolution, and temporal continuity at once, a combination existing datasets lack. To fill this gap, we introduce an ultra-High-resolution (12768x9564) Airborne Remote-sensing Dataset (HARD) annotated at three levels for object detection, multi-object tracking, and scene-level visual question answering. Ultra-high-resolution imagery raises per-frame processing time to seconds. At that scale latency can no longer be ignored in evaluation. Thus, we propose a latency-aware metric for multi-object tracking called streaming-HOTA (s-HOTA). Extensive baseline experiments show how ultra-high-resolution processing reshapes each task. For detection, the end-to-end pipeline affects accuracy and speed as much as the detector itself does. For tracking, high latency charges the association axis far more unevenly than the detection axis, and association is where pipelines diverge. As a result, the pipeline that performs best offline can lose its lead under s-HOTA. For VQA, vision-language models remain weak at cross-frame identity binding and cannot transfer their single-frame gains to it. Together these findings show that the baselines we evaluate fall short of WSTU. HARD provides the data and the systematic baselines to advance it.

---


### 82. [Measuring and Exploiting Implicit Trust in LLM Tool-Calling Pipelines](https://arxiv.org/abs/2609.18217)

**<font color=#1a73e8>作者：</font>** Murali Ediga, Sudipta Chattopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) enables LLMs to invoke external tools, but every tool interaction exposes the model to attacker-controlled text through multiple input channels (tool descriptions, tool results, sampling messages) that share a single context window without privilege separation. In this paper, we present a framework to measure the trust profile of an arbitrary LLM based on a variety of payload framings sent through different channels. Following this assessment, we devise cross-channel fragmentation attacks that distribute seemingly benign payloads across two or three channels; no individual channel carries a complete injection, yet the LLM compiles the fragments into credential exfiltration. We evaluated our attacks across 12 frontier models, three production clients, and six payloads, totalling over 15,000 trials. Our evaluation reveals that cross-channel attacks are an unexplored attack surface: models that fully resist single-channel injection (0% compliance) exfiltrate sensitive data at up to 100% under two-channel fragmentation (e.g., GPT-4o, Llama 70B, Composer 2, Haiku 4.5). We further demonstrate value-aligned exploitation, where a tool's stated purpose requires the data the attacker targets, and a sampling system prompt override that injects persistent instructions via VS Code's MCP implementation. Finally, we evaluated our attacks against seven third-party MCP security tools and three prompt-based defenses. All tools failed to detect fragmented payloads, and prompt defenses proved model-specific rather than universal.

---


### 83. [REPAIR: Resolving Long-Tail Confusion in Scientific Retrievers via Fact-Verified Iterative Refinement](https://arxiv.org/abs/2609.18262)

**<font color=#1a73e8>作者：</font>** Yerim Oh, Gunhee Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Precise retrieval of scientific information is fundamentally constrained by long-tailed concepts and high fact-sensitivity of scientific corpora. These challenges often limit the effectiveness of dense retrievers and hallucination-prone LLM augmentation. To address this, we present REPAIR, a self-evolving data augmentation framework for scientific dense retrievers. REPAIR iteratively synthesizes training data to address knowledge gaps by cycling through diagnosis of long-tail concepts, API-guided evidence expansion, and differentiation via hard negative mining. This process effectively grounds retrieval in factual reality to resolve fine-grained distinctions. Extensive experiments demonstrate that REPAIR significantly outperforms 19 strong baselines on nine materials science and biomedical benchmarks. Our work highlights that diagnosing and factually augmenting data to long-tail deficits is essential for robust scientific retrieval.

---


### 84. [BENCHCOMPASS: From Scores to Signals for Training and Harness Decisions in Payment-Domain LLMs](https://arxiv.org/abs/2609.18270)

**<font color=#1a73e8>作者：</font>** Sijie Dong, Wei Ren, Xuanwei Hu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Payment operations are a critical financial infrastructure, but the value of large language models in this domain remains unclear because payment rules change quickly, evidence is fragmented, and decisions depend on transaction state, participant role, region, and payment rail. Existing benchmarks do not isolate whether failures come from missing payment-rule knowledge, poor use of supplied evidence, or brittleness under imperfect harness inputs. We introduce BENCHCOMPASS, a payment-domain benchmark whose construction pipeline builds scenario-grounded tasks from typed evidence packs, applies LLM-based quality checks, creates task-input attack variants, and reserves final item admission for domain experts. The release contains an expert-reviewed Pro benchmark covering payment knowledge, context-grounded scenario reasoning, and Attacked Open robustness, plus a lower-assurance Normal pool for inspection and future curation. Across 16 model variants, BENCHCOMPASS shows qualitatively different failure modes: missing parametric payment knowledge, incomplete reasoning over supplied rules, and failure to reject plausible but invalid workflows. The benchmark remains unsaturated: the best frontier model reaches 89.6% on Open Context-Grounded Reasoning and 81.7% under attacked inputs, while a representative 32B open-weight model reaches 69.8% and 42.6%. Benchmark data and code are available at this https URL.

---


### 85. [Behavioral Fingerprinting and Navigation Prediction in Web Browsing](https://arxiv.org/abs/2609.18273)

**<font color=#1a73e8>作者：</font>** Ralph Elsaghbini, Omran Berjawi, Walid Fahs 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web browsing often appears ephemeral: users visit a few websites, complete a task, and move on. However, even short fragments of browsing activity can contain rich and structured behavioral signals. In this work, we conduct a comparative empirical study of two complementary behavioral inference tasks: session-level user identification and next-domain prediction. Both tasks are derived from the same cleaned event stream and evaluated on large-scale anonymous browsing traces, with sessionization and splitting adapted to the temporal requirements of each task. For user identification, we evaluate classical and neural models operating on session-level behavioral and domain features. For next-domain prediction, we combine graph-based modeling with Large Language Models (LLMs). Experimental results show that short browsing sessions are highly identifiable, while future navigation actions are highly predictable from long-term interaction structure combined with recent behavioral context. Furthermore, LLM-derived semantic features yield only marginal gains over purely structural and sequential models, indicating that repeated interaction patterns remain the dominant predictive signal in the evaluated web-browsing setup. These findings highlight the extent to which interaction history substantially contributes to both user identifiability and navigation predictability in browsing traces.

---


### 86. [I code or AI code: A comparative evaluation of AI-rated scores in classroom observations](https://arxiv.org/abs/2609.18274)

**<font color=#1a73e8>作者：</font>** Y. Fong, J. Xiang, T.Y.D. Chan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Classroom observations are widely recognized as a key tool for establishing benchmarks of education quality and guiding pedagogical improvement, yet they remain resource-intensive and dependent on trained observers. This study evaluated the feasibility of using a LLM (GPT-5 model) to score teacher-child interactions in early childhood classrooms, benchmarked against human raters. The study analyzed 87 video-recorded observations from 38 classrooms across 30 kindergartens in Hong Kong. Using observation transcripts, the AI model was configured to apply the full Classroom Assessment Scoring System (CLASS) framework. AI-rated scores were then compared with human ratings by examining correlations and differences in mean scores of the CLASS domains and dimensions. The results showed greater convergence between AI and raters for the Emotional Support domain and, in particular, the Quality of Feedback dimension, which captures how teachers use feedback to extend children's learning. Greater divergence emerged for interactions that were more procedural or context-dependent, particularly within the Classroom Organization and Instructional Support domains. These findings suggest that transcript-based AI scoring may capture some of the relative variation in teacher-child interactions but cannot yet reproduce calibrated human judgements consistently across the full CLASS framework. AI-assisted observation may therefore be more appropriate as a preliminary screening tool rather than as a replacement for trained observers, providing teachers with evidence for reflection rather than high-stakes evaluation. Future research should examine whether domain-specific training and incorporation of contextual and visual information can improve alignment between AI and human rated scores.

---


### 87. [Too Good to Be Real? Diagnosing and Reducing the Gap Between AI Preference and Real User Engagement](https://arxiv.org/abs/2609.18282)

**<font color=#1a73e8>作者：</font>** Xinglang Zhang, Yuanmeng Xiang, Yunyao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to generate and evaluate online content, yet it remains unclear whether the qualities they associate with higher engagement match what real users respond to. We study this question using 1.17 million answers to 25,978 questions from Zhihu, Quora, and Reddit, comparing real platform answers and AI-generated answers across four within-question engagement levels. We introduce Ontological Preference Measurement, which represents answers along three dimensions: logic, affect, and expression. We find a systematic gap between AI preference and real user engagement: as target engagement increases, LLMs add more explicit logical structure, while real user engagement is more strongly associated with affective and expressive salience. We call this tendency logic overbinding. Based on this diagnosis, we propose Ontology-Masked Reasoning Autoencoding (OMRA), a controlled intervention that masks and reconstructs over-explained spans while preserving stance, factual content, and coherence. Across four LLM families, OMRA reduces the measured gap by an average of 54.4%. In human evaluation, OMRA wins 62.4% of pairwise preference judgments against matched real platform answers, even though the real answers are more often judged to be human-written.

---


### 88. [Where Should Agents Live? Energy-Memory Characterization of Agentic AI for the Edge-Cloud Continuum](https://arxiv.org/abs/2609.18283)

**<font color=#1a73e8>作者：</font>** Carolina Fortuna, Vid Hanžel, Tim Strnad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As telecommunication networks evolve toward autonomous 5G-Advanced and 6G operations, agentic artificial intelligence (AI) workflows, where large language models (LLMs) execute multi-step reasoning, invoke diagnostic tools, retrieve domain knowledge, and coordinate across agent teams, are increasingly embedded across the edge-cloud continuum. While the biological brain accomplishes complex cognition on an exceptionally modest metabolic power budget of approximately 20W contemporary LLMs are profoundly energy- and memory-intensive, making sustainable lifecycle orchestration a critical operational priority. However, existing AI lifecycle metrics evaluate only isolated, single-model inferences or overlook multi-agent execution graphs entirely. Consequently, network operators lack foundational models to determine whether distributed agent communication incurs meaningful energy costs and where across edge-cloud tiers agent teams should physically reside. To address this gap, we introduce agentic-eCAL, generalizing the Energy Cost of AI Lifecycle (eCAL) metric to directed multi-agent workflows by coupling a closed-form two-rate single-call energy model (compute-bound prefill and memory-bound decode) with 7-layer OSI data transport. Grounded in hundreds of GPU benchmark configurations on NVIDIA A100 and H100, 16 open-weight models and 8 orchestration topologies, we validate components of the metric and study workflow placement implications. Our findings demonstrate that inter-agent text transport incurs 0.25% of workflow energy across 5G RAN, metro, and optical links. Therefore in edge-cloud agent placement the dominant energy cost of distribution is often not the transmission of inter-agent text itself, but the additional inference and context processing induced by that communication.

---


### 89. [Made in Hungary: Comments on the performance of generative language models](https://arxiv.org/abs/2609.18284)

**<font color=#1a73e8>作者：</font>** Mátyás Osváth, Enikő Héja, Noémi Ligeti-Nagy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, three initiatives have emerged to develop generative language models in Hungary. The motivation behind them is the same. For Hungarian, no model with the given capability existed, or existing English-centric models offered limited proficiency. A detailed examination of the corresponding studies, however, reveals several methodological limitations. First, the reliability of the evaluation protocols is questionable. Contrary to the findings of Csibi et al. [2026], evaluation under the recommended inference settings shows that Qwen3-4B achieves higher scores than Racka-4B, its Hungarian-adapted version. Data contamination is evident in the work of Yang et al. [2025d] and Szentmihályi et al. [2025], potentially biasing the reported results. Second, the training pipelines fall short of current best practices in corpus curation and data mixture, which risks wasting substantial compute on low-quality data. The lack of controlled ablations prevents reliable assessment of these choices. Third, none of the three papers assessed forgetting or capability loss. Testing the adapted models on a subset of the original benchmarks indicates performance decline in all three cases, especially Racka-4B. These observations emphasize the importance of rigorous experimental design in language model development, given the significant computational and financial costs involved.

---


### 90. [What Counts as Strategic Reasoning? A Systematic Mapping of Chess Research on Humans, Engines, and Language Models](https://arxiv.org/abs/2609.18286)

**<font color=#1a73e8>作者：</font>** Paolo Ciancarini, Remo Pareschi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chess has long served as a model domain for studying search, expertise, decision-making, and artificial intelligence. The emergence of large language models (LLMs) has renewed the relevance of chess as a controlled environment for investigating strategic reasoning and comparing human and artificial decision-making. We present a systematic mapping study of recent research spanning human players, classical chess engines, neural and reinforcement-learning systems, LLMs, and hybrid approaches. The final map comprises 84 core study families, classified according to agent type, strategic-reasoning stages, and evaluation dimensions.
The map reveals a literature strongly concentrated on situation assessment, evaluation, and action selection, while explicit planning, explanation, metacognition, and human--AI collaboration remain less explored. LLM research places particular emphasis on state representation and generalization, whereas grounded explanation appears more frequently in hybrid approaches combining language models with engines, expert knowledge, or other external structures. Two distinctions emerge that the map aggregates rather than resolves: hybrid systems differ in where and when heterogeneous capabilities combine, and evaluations that show improved human performance do not thereby establish human--AI synergy. We propose both as extensions of the mapping framework.
We argue that chess provides a useful bridge between cognitive and computational perspectives on strategic reasoning, and identify explicit planning, grounded and faithful explanation, metacognitive calibration, and human--AI complementarity as directions for future research.

---


### 91. [Rollback the World, Keep the Reflection: Rollback-Induced Reflection for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.18304)

**<font color=#1a73e8>作者：</font>** Yi Yu, Liuyi Yao, Yaliang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly tackle long-horizon tasks through multi-step environment interaction, yet a single erroneous action can alter subsequent states and observations, causing errors to compound over time. Existing methods either correct the context without repairing altered environment states or restore earlier states while discarding useful experience, making it difficult to both eliminate failure conditions and avoid repeating past mistakes. We argue that reliable recovery should instead be treated as a rollback-boundary control problem that jointly determines when to intervene, where to resume, and what information should survive recovery. Based on this view, we propose Rollback-Induced Reflection (RIR), a unified recovery framework that restores execution to a selected prior state while carrying forward reusable knowledge distilled from the abandoned trajectory to guide subsequent decisions. We further characterize recovery through a unified operator over rollback depth and retained memory, providing a general view of state restoration and knowledge retention. Experiments on three long-horizon benchmarks demonstrate that RIR consistently improves task performance across multiple LLM backbones, with structured reflection memory preserving useful experience and selective rollback enabling efficient recovery.

---


### 92. [Bias Amplification in Multi-Agent Network: How Biased Agents Shape Opinions and Rhetoric](https://arxiv.org/abs/2609.18306)

**<font color=#1a73e8>作者：</font>** Omran Berjawi, Giuseppe Fenza, Rida Khatoun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in applications involving interaction between agents, where their output plays a role in collective reasoning and decision-making processes. Despite significant research into the functioning of LLMs in such multi-agent systems, the processes of bias propagation in such systems are still a challenge. This work studies how biased opinions are propagated in the form of textual interaction in an environment of LLMs, in which a minority of agents maintain persistent extreme opinions, while the remaining agents iteratively update their beliefs through structured textual interactions. The findings show that even the presence of a small percentage of biased agents in such a system leads to significant shifts in the opinions of non-biased agents. It suggests that for the same percentage of biased agents, the shifts occur more quickly for the Llama~3.2 model when compared to a classical Friedkin-Johnsen (FJ) model. Further semantic analysis demonstrates that rhetorical consistency in textual explanations increases systematically with biased exposure and, importantly, is partially decoupled from numerical convergenumericalutral agents adopt the vocabulary employed by the biased agents even in configurations where their numerical opinion shifts remain moderate. The research helps explain how bias and language develop together in multi-agent language model ecosystems.

---


### 93. [SEA-LION-v4.8: A Technical Report](https://arxiv.org/abs/2609.18310)

**<font color=#1a73e8>作者：</font>** Ahmed Mohammad Dabeer, Ahn Jeongmi, Anocha Sutaveephamochanon 等 48 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Nemotron-SEA-LION-v4.8, a family of Southeast Asian Languages in One Network (SEA-LION) built upon NVIDIA Nemotron 3. The family includes 30B-A3B and 120B-A12B models, with both continued-pretrained base checkpoints and post-trained variants. We adapt the models using Southeast Asian, reasoning, code, and multilingual parallel datasets, followed by post-training with supervised fine-tuning and online on-policy distillation. On SEA-HELM, the 30B-A3B model improves the overall SEA score from 46.06 to 51.57, while the 120B-A12B model improves from 49.30 to 63.44. The strongest gains are observed in instruction following, natural language reasoning, and natural language understanding across seven Southeast Asian languages.

---


### 94. [Knowledge-Graph Based Augmentation versus Retrieval Augmented Generation for Cultural-Related Question Answering](https://arxiv.org/abs/2609.18317)

**<font color=#1a73e8>作者：</font>** Pablo Poulenard, Yannis Karmim, Valentin Barrière  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) suffer from a long-tail deficit: culturally specific facts, particularly those concerning underrepresented regions such as Latin America, appear too rarely in pretraining corpora to be reliably memorized. Retrieval-Augmented Generation (RAG) addresses this by grounding generation in external text, but structured alternatives such as Knowledge Graphs (KGs) offer tighter control over what enters the context, along with potential gains in explainability and updatability. We benchmark Graph-RAG against standard RAG on LatamQA, a culturally grounded multiple-choice dataset spanning eight thematic categories. The graphs are built end-to-end from Wikipedia articles with KGGen, a recent open-domain extractor, without manual curation in our main setting. G-Retriever is competitive with RAG and reduces the error of the base LLM by 72\% with a standard KG and 78\% with a benchmark-aware variant, the gap to RAG narrowing further as the graph is oriented toward task-relevant content. The trained projection transfers zero-shot to Portuguese without target-language fine-tuning, indicating multilingual reach.

---


### 95. [Attention Dispersion as a Diagnostic Signal for Hallucination in Large Language Models](https://arxiv.org/abs/2609.18320)

**<font color=#1a73e8>作者：</font>** Shardul P. More, Tanuja S. Pawar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) frequently exhibit hallucinations, presenting a major barrier to reliability in complex reasoning tasks. While traditional detection methods rely on output-based confidence metrics, these logits are often miscalibrated by modern alignment techniques. In this paper, we investigate the temporal volatility of internal attention mechanisms as an alternative diagnostic signal for hallucination that does not depend on output calibration. By introducing an unsupervised metric for attention dispersion, we show that epistemic uncertainty leaves a measurable trace within intermediate layers, where spikes in attention entropy are associated with reasoning breakdowns. We evaluate our approach on mathematical reasoning benchmarks (GSM8K and MATH-500) using the Qwen2.5 model family (1.5B and 3B parameters), finding statistically significant AUC improvements of up to +0.076 over output-based baselines across all tested conditions. These findings suggest that attention dispersion is a promising complement to traditional hallucination detection methods, requiring further investigation across broader model families and task domains.

---


### 96. [Trajectory Learnability for Offline On-Policy Distillation with Imperfect Teachers](https://arxiv.org/abs/2609.18321)

**<font color=#1a73e8>作者：</font>** Yihao Ai, Weilong Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline on-policy distillation gains efficiency by collecting student trajectories and teacher supervision once and reusing them throughout optimization. The same reuse makes imperfect supervision persistent. Since even strong teachers can fail, we ask \emph{what remains learnable from imperfect teacher supervision?} Teacher failure is only a coarse problem-level signal and does not imply that all supervision along the associated student trajectory is unhelpful. A natural alternative is to estimate teacher recoverability along the trajectory, but repeated continuations largely erase the efficiency advantage of offline distillation. We instead use teacher-successful problems to define a cheap reference for what the student can learn. We train on teacher-successful problems and measure how the likelihood of each observed token in trajectories from teacher-failed problems changes. We use these signed likelihood changes as an operational \emph{learnability signal}: larger increases indicate behavior more strongly promoted by successful-only learning. We aggregate this signal into trajectory-level weights for the original distillation loss. Unlike continuation-based estimates, our learnability requires no additional generation and can be computed once from stored trajectories and model checkpoints. Across mathematical reasoning and code generation, our method improves an offline OPD baseline by up to 2.7 percentage points and matches or outperforms online OPD variants on multiple benchmarks. Despite the additional successful-only distillation stage, it uses 2 GPUs and about 22 GPU hours, compared with 3 GPUs and 36--48 GPU hours for representative online OPD methods.

---


### 97. [Visual Compliance via Executable Safety Rule Entailment](https://arxiv.org/abs/2609.18328)

**<font color=#1a73e8>作者：</font>** Jisoo Kim, TaeYoon Kwack, Jinwoo Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLMs and VLMs have enabled safety systems to reason beyond simple risk patterns toward more contextual and semantic safety concerns. However, as risk patterns continue to evolve and safety rules become more complex, existing training-based end-to-end safeguards face persistent challenges in adaptability and explainable reasoning over complex safety rules. To address these challenges, we propose GuardEn (Guarding by Safety Rule Entailment), an executable safeguard framework that decomposes safety policies into atomic propositions through Safety-Rule Compilation, modeling their composition as executable code. At test time, Scene-Grounded Execution instantiates these atomic propositions with contextual visual information derived from scene graphs, enabling rule-grounded and interpretable safety reasoning. Experiments on SafetyVisionBench demonstrate the effectiveness of programmable safeguard for complex visual safety assessment, achieving an average improvement of 9.8 F1 points over the strongest baseline.

---


### 98. [Autonomy in Check: Governor-Mediated Adaptive Security at the Edge](https://arxiv.org/abs/2609.18338)

**<font color=#1a73e8>作者：</font>** Ijaz Ahmad, Ijaz Ahmad, Flavio Esposito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adaptive security at the network edge increasingly relies on automated planners, including rule-based controllers, learned policies, and LLM-assisted agents, that translate observations into enforcement actions. Once such a planner can influence live policy state, syntactic validity is not enough. A semantically wrong action, produced from incomplete or manipulated observations, can be faithfully executed by an enforcement substrate that cannot judge mission context. We address this problem by treating the boundary between planner output and kernel enforcement input as the primary security object. We propose a split-control architecture in which an untrusted planner emits typed security intents, a deterministic governor checks each intent against safety, resource, temporal-stability, and proportionality invariants, and only admitted actions are bound to signed receipts and compiled into pre-installed eBPF map updates. The paper formalizes this trust-boundary problem, defines three threat classes, develops the governor admission predicate, and reports an end-to-end prototype. Across rule-based and LLM-assisted planners on a Raspberry Pi 5 testbed connected to the university 5G Test Network, the governor admits, rejects, and bounds intents at microsecond cost without disrupting protected-flow regularity. The contribution is conceptual as much as empirical: adaptive security does not need to trust the author of an action. It needs a mediation boundary that decides whether the action is admissible.

---


### 99. [Visual Input and Its Framing Affect Attribute-based Descriptions Produced by Large Vision-Language Models](https://arxiv.org/abs/2609.18345)

**<font color=#1a73e8>作者：</font>** Xiaomeng Wang, Martha Larson, Zhengyu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) are commonly used with only a single text prompt as the input, or plus an image. In this paper, we demonstrate that when the image exists, even if the text prompt is not about the specific instance (but only the concept it belongs to) in that image, the response would still be affected. For example, when the text prompt only asks for the attribute descriptions of a dog breed, an image depicting a specific dog from that breed would shift the response. Further, how the specific instance is framed in that image would determine towards which the response shifts. Detailed analyses also reveal that in the response, physical terms increase from 18% for text-only to 45% (40%) for subject-focused (subject-in-situation) framings. Overall, the unexpected effects of visual cues on LVLMs highlight the need to understand the presence of an image and its framing when evaluating the robustness of LVLMs.

---


### 100. [Faithful yet Collusive: Why Chain-of-Thought Monitoring Cannot Detect Collusion in LLM Pricing Agents under Oligopolistic Competition](https://arxiv.org/abs/2609.18346)

**<font color=#1a73e8>作者：</font>** Dohun Lee, Hyunwoo Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLM) deployed as autonomous pricing agents may sustain supracompetitive prices through tacit coordination. We develop a causal graph divergence framework that separately measures structural faithfulness and intent faithfulness of LLM pricing agents in Bertrand competition. Across nine LLMs under duopoly and triopoly conditions, collusive behavior and chain-of-thought (CoT) faithfulness dissociate along both dimensions: the most collusive model accurately reports cooperative intent yet reasons structurally unfaithfully, while the most structurally faithful model sustains supra-Nash pricing under both market structures. These findings establish that CoT monitoring alone cannot serve as a standalone safeguard against algorithmic collusion.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-210](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
