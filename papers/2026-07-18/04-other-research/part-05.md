# 📦 其他研究 | 2026年07月18日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-221**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-221**

---

### 201. [Can We Trust Item Response Theory for AI Evaluation?](https://arxiv.org/abs/2607.15190)

**<font color=#1a73e8>作者：</font>** Han Jiang, Sunbeom Kwon, Jinwen Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI benchmarks increasingly leverage item-level statistical models, particularly item response theory (IRT), to estimate model capabilities, rank systems, select informative examples, and diagnose benchmark quality. However, AI benchmark data often departs from the data regime of human testing, for which standard IRT estimation tools were originally developed: benchmarks typically involve fewer evaluated models, far more items, and capability distributions that may be skewed, clustered, or multimodal. We examine how these regime mismatches challenge the reliability of IRT modeling for AI evaluation. Using item parameters and capability distributions derived from six widely used LLM benchmarks, we simulate response matrices under three common IRT models and compare four estimation tools used in recent benchmark studies: marginal maximum likelihood, Markov chain Monte Carlo, variational inference, and a neural pseudo-Siamese estimator. Across 18,000 simulation conditions, we systematically evaluate computational feasibility, scalability, and the reliability of IRT inferences about model rankings, predicted performance, and item characteristics. Results show that classical estimators can become infeasible in large benchmark settings, whereas scalable estimators can produce unreliable item-level and ranking inferences with small or nonnormally distributed model sets. This study identifies when latent trait models reliably support or risk distorting AI benchmarking claims, and what sample sizes and diagnostics are needed for trustworthy use.

---


### 202. [Plover: Steering GUI Agents through Plan-Centric Interaction](https://arxiv.org/abs/2607.15193)

**<font color=#1a73e8>作者：</font>** Madhumitha Venkatesan, Shicheng Wen, Jiajing Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) automation remains challenging in real-world environments, where dynamic layouts, unexpected dialogs, and evolving interface states can cause autonomous agents to drift from user intent. Recent vision-based multimodal agents improve flexibility by operating directly over screenshots and natural language instructions, but planning and adaptation often remain internal, limiting users' ability to inspect, supervise, or correct system behavior. We present Plover, a plan-centric vision-based GUI automation system that externalizes task plans and replanning as persistent, inspectable, and revisable artifacts. Through a planner--executor architecture, Plover supports explicit supervision of evolving execution, localized correction through editable plans, natural-language guidance, and screenshot-grounded interventions, while preserving prior progress during repair. A formative study with six participants informed the interaction design. We then evaluate Plover through benchmark failure-case repair and scenario-based workflow analyses. Our results show that many autonomous GUI-agent failures are structurally repairable when plans remain visible and interventions are localized, and that explicit replanning helps make GUI automation more transparent, controllable, and adaptable.

---


### 203. [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207)

**<font color=#1a73e8>作者：</font>** Qi Li, Xingyi Yang, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world prediction. This coupling is often viewed as a source of robustness, interpretability, and safety, as a robot's action can in principle be checked against its imagined future. In this paper, we show that this assumption is fragile. We introduce BadWAM, a unified framework for modeling and evaluating World-Action Drift Attacks: a new class of WAM-specific adversarial attacks that use small visual perturbations to break the alignment between what a WAM imagines and what it executes. BadWAM characterizes this attack surface along two natural criteria: attack strength and stealthiness. When the adversary prioritizes disruption, BadWAM instantiates an action-only adversarial attack, which directly drives the model toward task-failing actions. When the adversary additionally prioritizes stealth, BadWAM instantiates an imagination-preserving adversarial attack, which seeks to induce harmful action shifts while keeping the model's predicted future close to its clean imagination. Together, these two attacks capture a spectrum of WAM-specific failures: from overt action hijacking to stealthier cases where the model appears to imagine a plausible future but executes a desynchronized action. We evaluate BadWAM across different variants of WAMs. Results show that our attacks substantially reduce task success rates under closed-loop execution. For example, our action-only attack reduces the model performance from 96.5% to 43.1% success. The results of our imagination-preserving attack further exposes a WAM-specific vulnerability: moderate future-preserving regularization can maintain strong attack performance while reducing future imagination drift.

---


### 204. [Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya](https://arxiv.org/abs/2607.15209)

**<font color=#1a73e8>作者：</font>** Hailay Kidu Teklehaymanot, Debela Desalegn Yadeta, Wolfgang Nejdl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual pre-trained language models (PLMs) exhibit degraded performance on low-resource, non-Latin-script languages, driven by high out-of-vocabulary (OOV) rates and excessive subword fragmentation that result from Latin-script-centric tokenizer training. We introduce VEXMLM, a vocabulary-extended variant of XLM-R targeting the two highest-resource Ge'ez-script languages, Amharic and Tigrinya, and further evaluated on 17 additional low-resource African languages (19 total). We train a language-specific SentencePiece tokenizer on curated Amharic and Tigrinya monolingual corpora, extend XLM-R's vocabulary with 30,000 Ge'ez-script subwords derived from this tokenizer, and initialize their embeddings by averaging the embeddings of their constituent subwords under XLM-R's original tokenizer. VEXMLM is trained in two stages: (1) continued masked language modeling over the extended vocabulary on the curated corpora, and (2) supervised fine-tuning on question answering (QA), named entity recognition (NER), and sentiment analysis (SA). On Amharic/Tigrinya QA, VEXMLM achieves 87.0 EM /90.0 F1, versus 66.0 EM/78.0 F1 for XLM-R and 74.0 EM/ 78.0 F1 for Glot500. On SA, VEXMLM reaches 80.0\% accuracy versus 77.0\% (XLM-R) and 46.0\% (Glot500). On NER, VEXMLM raises OOV-token entity accuracy from 81.4\% to 94.3\%, averaged over 11 of the 19 evaluated languages for which OOV analysis was possible. Our contributions are: (i) a vocabulary-extension and embedding-initialization procedure tailored to Ge'ez script; (ii) a two-stage training strategy under which vocabulary and continued-pretraining gains on Amharic/Tigrinya transfer to 17 typologically related, unaugmented African languages; and (iii) an evaluation spanning both intrinsic tokenization metrics (vocabulary coverage, fertility, OOV rate) and extrinsic task performance across all 19 languages.

---


### 205. [MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos](https://arxiv.org/abs/2607.15211)

**<font color=#1a73e8>作者：</font>** Ziren Gong, Xiaohan Li, Fabio Tosi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents MAGiSt3R, a multi-agent 3D reconstruction framework performing reconstruction and camera tracking for monocular RGB videos at almost 10 FPS. MAGiSt3R relies on a feed-forward model from the 3R family to process RGB videos and regress local point maps, and on a merging model, MAGMA, that combines local maps at both intra-agent and inter-agent levels to obtain the final global point map. Furthermore, MAGiSt3R performs pose graph optimization to mitigate cumulative camera drift occurring along the feed-forward pipeline. We evaluate MAGiSt3R on both synthetic and real-world datasets, demonstrating its superior reconstruction and camera tracking accuracy compared to state-of-the-art approaches.

---


### 206. [Structural-Semantic Reciprocal Learning for Unsupervised Visible-Infrared Person Re-Identification](https://arxiv.org/abs/2607.15220)

**<font color=#1a73e8>作者：</font>** Moyao Tian, Shijia Liu, Yan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised visible-infrared person re-identification (USVI-ReID) is challenging due to the large modality gap and the lack of cross-modal identity annotations. Progressive association paradigms have been proposed to gradually bridge the gap, but they suffer from two critical bottlenecks: reliance on ambiguous global representations and unchecked propagation of pseudo-label noise in an open-loop manner. To address these issues, we propose Structural-Semantic Reciprocal Learning (SSRL), a framework that transforms open-loop association into a self-correcting closed-loop system. Structurally, we introduce Fine-grained Structural Decoupling (FSD) to extract discriminative body-part primitives as reliable spatial anchors, complementing ambiguous holistic silhouettes with spatially consistent structural details. Semantically, we design a Closed-loop Semantic Calibration (CSC) mechanism that reconstructs shared semantic prototypes at each epoch and feeds them back into the training loop, effectively filtering pseudo-label noise before the next clustering cycle. Through the reciprocal interaction between structural and semantic learning, SSRL achieves robust cross-modal representation. Extensive experiments demonstrate the competitive performance of SSRL against state-of-the-art USVI-ReID methods on both SYSU-MM01 and RegDB, notably surpassing several supervised counterparts on RegDB.

---


### 207. [Divergent Gaze Patterns in Artistic Viewing: Spatial and Temporal Signatures of Attention Across Autistic Individuals, Artists, and Neurotypical Observers](https://arxiv.org/abs/2607.15227)

**<font color=#1a73e8>作者：</font>** Mohammed Amine Kerkouri, Daphné Senggaran, Renaud Jusiak 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How different populations visually explore artworks bears on cognitive science and on accessibility design, yet most eye-tracking work in autism has used social scenes rather than art, and has analysed where the eyes land while ignoring when and in what order. We present a comparative free-viewing study across three groups, autistic adults (ASD), trained artists, and neurotypical observers, who each viewed 30 paintings for 15s. We introduce a directed, metric-grounded framework that compares groups along two complementary axes: a spatial axis, in which one group's fixation-density map predicts another's fixations under six saliency metrics (AUC-Judd, NSS, CC, SIM, KL, Information Gain); and a temporal axis, in which individual scanpaths are compared with MultiMatch, ScanMatch, a foveal-disc IoU score (FDISS), and dynamic time warping (DTW). Fixations are extracted uniformly for all groups with a dispersion-threshold algorithm. Three results converge. (i)Artists and neurotypicals are almost indistinguishable in both space (density-map correlation CC=0.96) and time (they form the most alignable scanpath pair), whereas ASD gaze diverges from both. (ii)ASD attention is dissociated: it matches artists' wide spatial exploration (dispersion, explored area) but carries a distinct temporal signature, shorter fixations, less dwell, and the most idiosyncratic (least self-consistent) scanpaths of any group. (iii)ASD gaze is not selectively artist-like on any metric; if anything it is marginally closer to neurotypical. Together these findings indicate that autistic viewing of art is a distinct, group-specific attentional profile in both space and time, and they motivate population-conditioned models of aesthetic attention. We release all analysis code and per-stimulus results.

---


### 208. [Data Driven Block Replacement Scheduling](https://arxiv.org/abs/2607.15229)

**<font color=#1a73e8>作者：</font>** Aniruddhan Ganesaraman, VIdyadhar Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop data-driven algorithms for maintaining $N$ independent identical machines under a \textit{block replacement policy}, in which each machine is replaced upon failure and all machines are jointly replaced at regular intervals of length $k$. The goal is to learn the cost-minimizing interval $k^*$ from operational data when the lifetime distribution is unknown. At each decision epoch, the operator selects $k \in \{1, 2, \ldots, K\}$, observes the resulting failure history (a mixture of complete and right-censored lifetimes) and incurs a per-unit-time cost governed by the renewal function. We formulate this as a stochastic multi-armed bandit and propose Hoeffding- and Bernstein-based lower-confidence-bound algorithms achieving $O(K \log T)$ regret, matching the Lai--Robbins lower bound. Exploiting a nested observation property unique to block replacement, correlated variants attain $O((K-k^*)\log T)$ regret and require only $O(1)$ direct pulls of suboptimal arms $k < k^*$. A complementary Kaplan--Meier renewal algorithm estimates the lifetime distribution nonparametrically from censored data, achieving almost-sure policy consistency and empirically near-zero incremental regret at long horizons. We additionally analyze two average-cost MDPs: a time-elapsed formulation establishing that block replacement is optimal within its policy class for any lifetime distribution, and an age-vector formulation proving a monotone threshold structure under increasing failure rate distributions and providing a gold-standard cost benchmark. Numerical experiments confirm the theoretical ordering and reveal structural cost gaps between optimal block and age-dependent replacement.

---


### 209. [CRISP: Constrained Refinement via Iterative Squeezing Process for Robust Medical Image Segmentation under Domain Shift](https://arxiv.org/abs/2607.15231)

**<font color=#1a73e8>作者：</font>** Yizhou Fang, Pujin Cheng, Yixiang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution shift in medical imaging remains a central bottleneck for the clinical translation of medical AI. Failure to address it can lead to severe performance degradation in unseen environments and exacerbate health inequities. Existing methods for domain adaptation are inherently limited by exhausting predefined possibilities through simulated shifts or pseudo-supervision. Such strategies struggle in the open-ended and unpredictable real world, where distribution shifts are effectively infinite. To address this challenge, we adopt the "Rank Stability of Positive Regions" as a working assumption under distribution shift, and use it to derive robust spatial hints for source-only segmentation. Guided by this assumption, we propose CRISP, a model-agnostic framework that, unlike deployment-time adaptation, requires no test-time parameter updates and no target-domain data--a target-free, plug-in refinement framework that segments with frozen weights. Rather than using ranking to directly output masks, CRISP exploits the stability of probability rankings under distribution shift to derive robust spatial priors. Via latent feature perturbation, perturbation-invariant high-grade regions define a high-precision (HP) core, while voxels that remain potentially foreground under at least one perturbation define a high-recall (HR) support; these dual priors are then recursively refined under perturbation. We then design an iterative training framework that progressively squeezes HP and HR toward the final segmentation. Extensive evaluations on multi-center cardiac MRI and CT-based lung vessel segmentation demonstrate CRISP's superior robustness, significantly outperforming state-of-the-art methods with striking HD95 reductions of up to 0.14 (7.0% improvement), 1.90 (13.1% improvement), and 8.39 (38.9% improvement) pixels across multi-center, demographic, and modality shifts, respectively.

---


### 210. [Language Identification via Compositional Data Analysis: A Linear-Time Classifier Based on Log-Ratio Geometry](https://arxiv.org/abs/2607.15238)

**<font color=#1a73e8>作者：</font>** Paul-Andrei Pogăcean, Sanda-Maria Avram  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language identification is commonly addressed using either neural architectures or statistical n-gram models. Neural approaches typically require substantial computational resources, whereas classical frequency-based methods offer efficient linear-time performance, but rely on distance metrics that are not always appropriate for compositional data.
This work models character and bigram frequency distributions as compositional vectors constrained to the simplex and mapped via the centered log-ratio (CLR) transformation bijectively onto the $(D-1)$-dimensional zero-sum subspace of $\mathbb{R}^D$, where Euclidean distances correspond to Aitchison distances. A pipeline is proposed, combining CLR-transformed unigram and bigram features with Laplace smoothing to address sparsity. The method is evaluated on six languages.
Experimental results show that the proposed approach achieves robust accuracy across different text lengths, with strong performance for longer sequences. These findings indicate that compositional representations provide a deterministic and computationally efficient alternative for language identification, particularly in settings where interpretability and low resource consumption are essential.

---


### 211. [Mutable Low-Rank Sketches for Retrain-Free Recommendation](https://arxiv.org/abs/2607.15242)

**<font color=#1a73e8>作者：</font>** Hector J. Garcia, Nick Clayton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A common bottleneck in two-stage recommendation is embedding staleness: when a user rates a new item, their embedding remains fixed until the next retrain cycle. We propose mutable sketches, which store each user's preferences in a KP-tree (a sparse segment tree with sum aggregation), fit a low-rank projection once, and recompute embeddings on-the-fly as ratings arrive. We prove that each new observation monotonically tightens the prediction error envelope (Theorem 1), a guarantee that FunkSVD and eALS lack. On KuaiRec, the mutable sketch achieves 0.810 RMSE at 1.8% data read vs. ALS 0.822 at 100%, with 8x faster per-batch updates. A new user receives personalized recommendations in <1 ms after their first rating, with no model retraining required. A comparison of sampling strategies across density regimes shows that the KP-tree's norm-proportional sampling provides 40-130% better item coverage on sparse data (<1% density), while uniform sampling suffices on dense matrices.

---


### 212. [HoloGeo: Mitigating Landmark Bias in Geo-localization via Evidence-Driven Reasoning](https://arxiv.org/abs/2607.15255)

**<font color=#1a73e8>作者：</font>** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models (VLMs) have significantly improved image geo-localization, yet existing models remain susceptible to landmark bias, causing them to overlook geographical cues or form spurious correlations, ultimately resulting in inaccurate localization. To systematically investigate this issue, we first design two quantitative metrics, Bias Intensity (BI) and Bias Harmfulness (BH), to characterize the impact of landmarks exerted on model reasoning, and establish a comprehensive benchmark, LandmarkBias-3K. To mitigate landmark bias, we further propose an evidence-driven reasoning framework, HoloGeo, to improve the reliability of geo-localization. HoloGeo is supported by a high-quality dataset, BF-30k, annotated with structured multi-evidence bias-free reasoning chains. By incorporating multi-dimensional rewards, HoloGeo explicitly encourages balanced attention over diverse visual cues and achieves evidence-driven joint reasoning. Extensive experiments demonstrate that HoloGeo not only maintains excellent performance on IM2GPS3K and YFCC4k but also significantly outperforms existing open-source VLMs on LandmarkBias-3K, validating its effectiveness for robust geospatial reasoning.

---


### 213. [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257)

**<font color=#1a73e8>作者：</font>** Yuyao Zhang, Junjie Gao, Zhengxian Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents. However, as interaction histories grow, agents increasingly struggle to track task progress. When search attempts fail to yield useful evidence, current single- and multi-agent systems can become trapped in repetitive loops, wasting search budgets and ultimately compromising the quality and completeness of the final output. We introduce SearchOS, a system-level multi-agent framework that turns fragile, implicit search progress into explicit, persistent, and shared state. First, we formulate open-domain information seeking as relational schema completion with grounded citations, where agents discover entities, populate attributes across linked tables, and anchor each value to source evidence. Then we design Search-Oriented Context Management (SOCM), which externalizes the evolving state into Frontier Task, an Evidence Graph, a Coverage Map, and Failure Memory. Built on SOCM, SearchOS applies a pipeline-parallel scheduling mechanism that overlaps the execution of sub-agents and continuously refills freed slots with tasks targeting unresolved coverage gaps to improve utilization and throughput. To schedule and control the execution of search agents, SearchOS introduces a Search Tool Middleware Harness that intercepts model and tool interactions to record grounded evidence and react to stalls or budget exhaustion, and provides a reusable hierarchical skill system comprising strategy and access skills to augment the agents' search process and avoid repeating failed search patterns across runs. On WideSearch and GISA, SearchOS leads all metrics among the evaluated single- and multi-agent baselines, paving the way toward robust information-seeking collaboration.

---


### 214. [Decoding Market Emotion from Blockchain Activity: A Data-Driven Sentiment Classifier](https://arxiv.org/abs/2607.15258)

**<font color=#1a73e8>作者：</font>** Arthur G. Bubolz, Abreu Quevedo, Giancarlo Lucca 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing use of Bitcoin as a decentralized digital asset and investment tool has sparked strong interest in understanding its market behavior. This study presents a new approach to analyze Bitcoin market sentiment by combining on-chain and financial data with social media posts. Unlike models that aim to predict prices, this work focuses on explaining market sentiment using blockchain transactions, historical price data of Bitcoin, and daily Twitter sentiment classifications. The method merges sentiment trends with on-chain and financial metrics, normalized into a dataset for detailed market analysis. Multiple machine learning models were tested using cross-validation, with Gradient Boosting (XGBoost) emerging as the most reliable model for classifying sentiment, achieving an average F1-score of about 0.84. SHAP (SHapley Additive exPlanations), a game theory-based method for model interpretability, was used to quantify the contribution of on-chain features to the model's predictions, improving transparency. The results indicate that this data combination yields meaningful predictive signals and insights, supporting data-driven cryptocurrency analysis and future improvements with deep learning.

---


### 215. [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263)

**<font color=#1a73e8>作者：</font>** Paul Kassianik, Blaine Nelson, Yaron Singer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security-agent evaluations commonly measure peak offensive capability under generous inference budgets, emphasizing vulnerability discovery, exploit development, penetration testing, and CTF completion. Such measurements are useful but incomplete: in operational security, every reasoning step, tool call, telemetry query, and enrichment request consumes budget. We evaluate language-model security agents through this cost-success lens on offensive Cybench challenges and defensive Splunk BOTS v1 investigation challenges. Instead of reporting only best-case success, we compare models at fixed cost levels and decompose performance by inference spend and tool spend. Our results show distinct scalingregimes for red- and blue-team tasks. Offensive CTF performance improves with additional test-time compute, and scaled open-weight models can approach frontier proprietary systems while remaining cost-competitive. Defensive SOC investigation does not scale in the same way: success depends more heavily on disciplined tool use, telemetry navigation, and selective enrichment than on raw reasoning budget alone. We argue that security-agent benchmarks should measure economic efficiency and operational fit alongside task success. Cost-aware, SOC-native evaluations provide a clearer picture of which models are practically useful today and where defensive agents still need to improve. We present an interactive website with our results this https URL.

---


### 216. [SceneBind: Binding What and Where Across Vision, Audio and Language](https://arxiv.org/abs/2607.15265)

**<font color=#1a73e8>作者：</font>** Mingfei Chen, Zijun Cui, Ruoke Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SceneBind, an omni-modal representation of realistic scenes with joint semantic and 3D spatial understanding across vision, audio and language. Existing omni-modal encoders excel at instance-level semantics (i.e., what is present), but often lack explicit spatial structure (i.e., where it is). SceneBind addresses this gap by representing each scene as a semantic-spatial entity, combining a global semantic embedding with object-centric semantic-spatial slots. This representation explicitly captures object-level semantics, spatial attributes, and uncertainty. We further propose SceneBind Matching, a semantic-spatial matching scheme that integrates global scene similarity with object alignment, supporting cross-modal scene retrieval and object grounding. To train and evaluate SceneBind, we curate a novel real-world binaural audio-visual dataset with structured semantic and spatial annotations, and propose a training protocol for aligning semantic and spatial signals across modalities. SceneBind is compatible with large-scale pretrained semantic encoders, adds lightweight spatial modeling with only a few additional tokens. It achieves state-of-the-art scene and spatial retrieval while enabling strong zero-shot transfer to downstream tasks such as audio-visual localization.

---


### 217. [Pretraining Data Can Be Poisoned through Computational Propaganda](https://arxiv.org/abs/2607.15267)

**<font color=#1a73e8>作者：</font>** Victoria Graf, Hannaneh Hajishirzi, Noah A. Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Poisoning pretraining data can introduce harmful behaviors to LMs that are difficult to detect and mitigate. Prior work on poisoning pretraining data has largely exploited established data sources such as Wikipedia, which do not represent the large scale and heterogeneity typical of pretraining corpora, and has ignored the interaction between poisoned data and data curation pipelines. We demonstrate that poisoning attacks on pretraining data are feasible beyond this limited setting through an existing web-scale content injection mechanism: public discussion interfaces. Additionally, to measure whether malicious content is included after web crawling and data curation, we introduce HalfLife, a novel analysis for estimating adversarial content inclusion in web-crawl based LM training data. We use HalfLife to explore the feasibility of poisoning pretraining corpora at web scale through open discussion interfaces. Our analysis demonstrates the importance of estimating whether poison injections are included in pretraining data, and establishes third-party webpage content as a possible vector for attacking language model pretraining.

---


### 218. [Motion-Conditioned Multi-View Fusion for Myocardial Infarction Localization from Echocardiography](https://arxiv.org/abs/2607.15268)

**<font color=#1a73e8>作者：</font>** Guang Yang, Wentian Xu, Siyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Myocardial infarction (MI) remains a leading cause of mortality worldwide. Echocardiography (Echo) is a widely available modality for MI assessment, where regional wall motion abnormality is a key indicator. Prior learning based methods for myocardial motion analysis often use handcrafted descriptors or densely supervised estimation, but the need for extensive annotation limits applicability. Foundation models have recently improved vision-based Echo analysis; however, most methods operate on single views and segment-level localization remains unreliable under view-dependent ambiguity, especially in apical views. To address this, we propose MCF-Net, a novel motion-guided multi-view fusion framework that fuses myocardial motion cues with foundation model representations to localize infarction. Visual features are extracted using EchoPrime, a pretrained Echo foundation model shared across dual views. Cardiac motion is modeled with extremely sparse supervision: a single annotated template frame is transferred across videos to initialize point tracking, avoiding dense labels. Motion-derived segment-aware soft masks provide coarse spatial priors that selectively enhance features for challenging myocardial segments. A motion-conditioned fusion mechanism then integrates motion and vision across views, refining predictions without overriding strong appearance cues. On segment-level MI localization, MCF-Net achieves 72.4\% F1 and 84.9\% accuracy, outperforming state-of-the-art motion-only, vision-only, and fusion baselines.

---


### 219. [Online Neural Space Time Memory for Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.15271)

**<font color=#1a73e8>作者：</font>** Baback Elmieh, Lynn Tsai, Zeman Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes. The computational cost of heavy memory updates precludes real-time application and can lead to instability over long contexts. Given that memory updates are more demanding than memory application and video content is largely redundant, we propose to decouple the frequencies of these two processes. Our approach performs periodic memory updates while applying the memory on a per-frame basis, using cross-view attention to manage deformations between the prior memory state and the current frame. To lock in the historical context, we introduce two critical mechanisms: an auxiliary Memory Loss that forces persistent internalization of the scene, and a Memory Caching strategy that regularizes active weights against catastrophic drift. Our method demonstrates real-time, state-of-the-art performance on scenes with dynamic human motion as well as minute-scale online memorization.

---


### 220. [SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions](https://arxiv.org/abs/2607.15272)

**<font color=#1a73e8>作者：</font>** Yasheng Sun, Zezi Zeng, Yifan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Editing the figures in a research paper is a routine and time-consuming part of everyday research practice: authors relabel components, rearrange panels, and restyle visuals as they revise their manuscripts. Automating this editing workflow under a natural-language instruction, however, is challenging, because a scientific figure is a dense infographic in which heterogeneous visual elements such as schematics, plots, photos, captions, and arrows are composed under a tight visual grammar to advance a specific argument. To address this, we present SciDiagramEdit, a benchmark and skill-evolution framework that learns from natural paper revisions and operates on the figure's editable vector source, where users can inspect and co-edit individual primitives alongside the agent. Our benchmark mines before/after figure pairs from arXiv version histories, each grounded in the authors' own revision intent. To accommodate the diversity of editing instructions, we adopt agentic learning via skill evolution: an agentic proposer continually refines the agent's skill specification from execution traces over multiple epochs. The resulting skill progressively lifts edit accuracy on a held-out validation set, providing evidence that natural paper revisions are an effective training signal for instruction-driven figure editing.

---


### 221. [Hierarchical Denoising For Multi-Step Visual Reasoning](https://arxiv.org/abs/2607.15278)

**<font color=#1a73e8>作者：</font>** Zezhong Qian, Xiaowei Chi, Chak-Wing Mak 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning. Streaming autoregressive diffusion models are efficient but limited in reasoning, while bidirectional diffusion enables global revision with high inference costs due to dense frame-level denoising. Both paradigms struggle to achieve logical consistency and low-latency streaming for complex reasoning tasks. We propose HDR (Hierarchical Denoising for Visual Reasoning), a unified framework that integrates hierarchical latents into causal video generation for multi-step reasoning. HDR organizes video latents into a tree-structured hierarchy, enabling coarse-to-fine reasoning before streaming output. Coarse denoising layers preserve uncertain hypotheses for global planning, while finer layers progressively refine them into concrete visual states. A sparse hierarchical attention pattern (SHAP) further reduces temporal attention costs. We introduce a level-stratified multi-step video reasoning benchmark with out-of-distribution cases, covering six tasks: maze navigation, Tower of Hanoi, one-line drawing, sliding puzzle, Sokoban, and water pouring. Compared with streaming autoregressive diffusion baselines, HDR improves success from 34.22 to 60.29 (76.2% relative gain) and increases average progress from 76.00 to 89.56, demonstrating more consistent reasoning trajectories. HDR maintains low-latency streaming at 0.70 seconds per latent, achieving 54.2 times faster inference than bidirectional diffusion. It also retains 82.9% of full-data performance with only 2% training data, compared with 52.0% for bidirectional diffusion. Real-world robot experiments further demonstrate HDR's potential for physical interaction and world modeling. Project demo: this https URL.

---


> [!TIP]
> 当前位于：**201-221**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-221**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
