# 🧠 大模型相关研究 | 2026年08月28日

> 本类共 **209** 篇论文：已确认 **195** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-209](./part-05.md)

---

### 151. [Closing the Gap: Automated Discovery of Secure Dockerfile Reference Standards via Semantic Clustering in Enterprise Inner Source](https://arxiv.org/abs/2608.25793)

**<font color=#1a73e8>作者：</font>** Jessica Hösl, Benedikt Hofmann, Patrick Stöckle  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Containerization dominates enterprise software delivery, yet Dockerfiles that assemble container images frequently harbor security misconfigurations and structural technical debt. This problem is poorly understood in corporate inner-source environments, where proprietary context and isolated governance prevent direct application of open-source findings.
We present an automated, six-stage pipeline that: (1) crawls an enterprise GitLab instance, (2) enriches each Dockerfile with static security and quality metrics (Hadolint, ShellCheck, Trivy) and lifecycle data, (3) groups functionally identical workloads using LLM-generated semantic descriptions and HDBSCAN, and (4) quantifies the optimization gap against cluster-internal reference implementations.
Applied to 11,470 Dockerfiles from over 6,200 repositories at a single large industrial company, we find a systemic deficit: 99\% of files contain at least one security misconfiguration, 80.8\% violate Dockerfile best practices, and the median artifact has not been revised for 838~days. Despite this, high-quality reference implementations already exist within 83\% of functional clusters. Adopting these internal standards would increase the average security posture score by 60.4\% without developing any new templates. These findings, grounded in one organization's inner-source ecosystem, provide a data-driven foundation for future automated, context-aware recommender systems targeting enterprise supply-chain security; whether the observed technical-debt distribution and optimization gap generalize to other enterprises remains an open question for future multi-organization study.

---


### 152. [Label-Free Foundational Model Selection for Medical Image Classification under Distribution Shift via Pseudo Label Discrepancy](https://arxiv.org/abs/2608.25810)

**<font color=#1a73e8>作者：</font>** Juan Iñaki Larrea, Lucas Mansilla, Enzo Ferrante  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly deployed for medical image analysis. However, under the inter-institutional distribution shift typical of deployment, their performance varies widely and cannot be known without target-domain labels, which are rarely available. This leaves a practical question unresolved: given several candidate foundational models and labeled-data from a source domain, which one to deploy in an unlabeled target domain? We propose a label-free selection criterion built on SUDO, a framework for evaluating clinical AI systems without ground-truth annotations. SUDO partitions the unlabeled target data by predicted probability and, for each region, measures a pseudo-label discrepancy reflecting class contamination; aggregated across regions, this yields a score (AURCC) requiring neither target annotation nor fine-tuning. We show that AURCC can be used to rank a variety of vision-language models (BioMedCLIP, CXR-CLIP, CheXzero, MedCLIP, MedImageInsight, CLIP) on chest X-ray classification across three inter-hospital shift scenarios, under zero-shot and MLP-probe regimes. The AURCC ranking recovers the ground-truth ranking with Spearman rho up to 0.943 (p<0.05). Against the natural baseline of ranking by held-out source accuracy, AURCC is competitive when the labeled source is large and yields a more accurate ranking once it is small; the regime of interest in resource-constrained settings.

---


### 153. [SkillShield: Prompt-Space Security Skills for LLM Coding Agents](https://arxiv.org/abs/2608.25817)

**<font color=#1a73e8>作者：</font>** Xiaodong Wu, Zhimin Zhao, Qi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A coding agent edits files and executes shell commands with its developer's privileges, allowing malicious requests to translate directly into harmful actions or functional malware. Existing defenses have complementary limitations: weight-level alignment is unavailable to API-only deployers, whereas input filters and execution-boundary monitors require auxiliary classification or checking components along the agent's trajectory. We therefore introduce SkillShield, a system-prompt defense that synthesizes security skills offline from known attacks or recorded agent failures. These skills are injected into the system prompt at session start and remain active throughout the tool-use loop. Unlike a reference monitor, they protect the system by defining the security policies the model should follow during execution. Due to the limited system-prompt space, we examine three fixed-budget provisioning scopes: all-classes, with one skill covering all threat classes, per-bundle, with one skill targeting a related subset, and per-class, with one skill dedicated to a single known class and used as the upper-bound reference. None requires runtime request classification or routing. Across six large language models on RedCode, the default all-classes skill reduces malware-generation severity from 3.37 to 0.58 and achieves a 43.6% execution attack success rate, comparable to Llama Guard 3's 42.7% without its separate 8B classifier. The per-bundle and class-fixed per-class settings further reduce this rate to 36.2% and 14.5%, respectively. Under two non-adaptive jailbreak families, SkillShield continues to outperform all baselines on malware generation. Across 731 benign task descriptions, SkillShield yields a mean safety-refusal rate of 0.14%. These results demonstrate the potential of prompt-space security skills to prevent harmful actions and malware generation for LLM coding agents.

---


### 154. [Localize-Then-Decide Guarantees for LLM Judgments](https://arxiv.org/abs/2608.25824)

**<font color=#1a73e8>作者：</font>** Xinyu Li, Yi Zhou, Guanqun Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as evaluators to assess output quality and preference alignment, yet providing reliable guarantees of agreement with human judgments remains challenging. Recent work introduces confidence-thresholding methods that provide such guarantees for pairwise comparisons, relying on the assumption that higher estimated confidence implies lower disagreement risk with humans. However, this assumption can break down when the number of candidate responses increases, since distributing probability mass across many alternatives can distort confidence estimates. To address this issue, we propose a Localize-Then-Decide framework. First, conformal prediction localizes a small shortlist that contains the human-preferred response with high probability. Then, a calibrated confidence-based rule selectively chooses a single response from this shortlist or abstains. This design restores the monotonic relationship between confidence and disagreement risk and enables high-probability agreement guarantees. Experiments with multiple candidate sizes across several datasets and judge LLMs demonstrate that our framework consistently achieves higher guarantee success rates and substantially higher coverage than single-stage baselines.

---


### 155. [Skill Issue: Are Skills Language-Invariant in LLMs?](https://arxiv.org/abs/2608.25832)

**<font color=#1a73e8>作者：</font>** Bobby Cheng, Adam Gaber, Zhengyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models access knowledge inconsistently across languages, but to what extent do they differ in their skill sets when interacting with different languages? This work quantifies cross-lingual skill inconsistency orthogonally from knowledge and general benchmark performance. We do this via multilingual self-play: two instances of the same model compete in a text-based game, each interacting through a different language interface. Since the model, opponent, rules, state space, and available actions remain fixed, this setting isolates the effect of language on the model's realized behavior. We build a multilingual extension to TextArena and evaluate three open-weight models across eight languages and six games covering spatial reasoning, imperfect information, resource allocation, and repeated interaction. We find that the same model can exhibit markedly different playing strength across languages, with systematic variation in win--loss margins, invalid actions, and strategic tendencies. Detailed analyses reveal language-specific failures in spatial reasoning, card-conditioned decisions, and optimal move selection. In some settings, changing only the intermediate reasoning language recovers much of the lost performance, suggesting that language can affect different stages of the decision process. These results show that skill discrepancies are a measurable major roadblock in the development of truly multilingual models. Better understanding these discrepancies can help us design models that perform more equitably across languages.

---


### 156. [THA-Flow Generative Model: Prosthesis Geometry Prediction from Preoperative CT](https://arxiv.org/abs/2608.25845)

**<font color=#1a73e8>作者：</font>** Yiping Wang, Jie Li, Jingyu Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preoperative planning for total hip arthroplasty (THA) is commonly framed as selecting a single prosthesis configuration and placement for a patient's osseous anatomy. In practice, however, the same anatomy may admit several clinically reasonable solutions, making planning inherently a one-to-many problem that is better represented by a conditional probability distribution. We present THA-Flow, a conditional flow-matching model that generates three-dimensional prosthesis geometry directly from preoperative CT. Separate AutoencoderKL models compress preoperative bone anatomy and prosthesis geometry, while a three-dimensional UNet learns a rectified flow from Gaussian noise to the prosthesis latent space under spatial bone conditioning and optional structured prosthesis parameters. The retrospective cohort comprised 1,355 hips from 1,149 patients undergoing primary THA. Following rigid registration of postoperative CT to preoperative CT, the actual postoperative prostheses were transformed independently according to the pelvic and femoral registrations and represented as a dual-channel truncated signed distance field. The prosthesis autoencoder achieved a peak signal-to-noise ratio of 47.11 dB and a structural similarity index of 0.9964 on the validation set. Complete acetabular and femoral geometries were generated across seven major stem models representing 93.4% of the cohort. Repeated bone-conditioned sampling preserved component position, alignment, and the principal bone-prosthesis interfaces while allowing limited local geometric variation. To our knowledge, THA-Flow represents the first application of generative AI to three-dimensional surgical planning for THA.

---


### 157. [Key Point Analysis Needs Structure Recovery: Task Definition, Dataset Diagnosis, and a Structure-Aware Benchmark](https://arxiv.org/abs/2608.25854)

**<font color=#1a73e8>作者：</font>** Zhiqiang Shi, Oana Cocarascu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Key Point Analysis (KPA) aims to identify a concise set of key points that summarize a collection of arguments together with their prevalence. We argue that KPA is fundamentally a structured prediction problem that requires recovering semantic groupings, generating representative key points, ensuring coverage, and estimating prevalence. Under this formulation, we show that existing KPA benchmarks suffer from limitations in grouping quality, redundancy, coverage, and argument-key point mappings, causing ceiling violation and selection failure in reference-based evaluation. To support future research on true KPA, we introduce a structure-aware, distribution-sensitive benchmark built via a human-in-the-loop re-annotation. Human and LLM evaluations consistently show that the resulting structures yield more coherent groupings, higher-quality key points, better coverage, and more reliable prevalence estimates than existing annotations. We further release several annotation resources to support research on KPA evaluation, argument-key point matching, explainable KPA, and LLM-as-a-judge methodologies, and outline a research agenda for true KPA.

---


### 158. [LUTSeg: A Longitudinal Multi-Expert Dataset for Ulcer Tissue Segmentation](https://arxiv.org/abs/2608.25866)

**<font color=#1a73e8>作者：</font>** Karen Sanchez, Carlos Hinojosa, Albert A. Ávila 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantifying wound tissue composition is essential for monitoring chronic ulcer progression and guiding treatment decisions. However, pixel-level annotations are costly, and multi-tissue wound datasets remain scarce, particularly for neglected diseases such as leprosy. We introduce LUTSeg, a longitudinal chronic ulcer dataset comprising 141 images from 39 patients with wound masks and five tissue categories annotated by five expert clinicians, including a multi-expert gold-standard subset for inter-rater agreement analysis. To establish an initial benchmark for LUTSeg, we further propose TiSage, a semi-supervised tissue segmentation framework that integrates multi-scale semantic priors from a frozen medical vision-language model within a teacher-student architecture. We evaluate TiSage on LUTSeg and DFUTissue, showing improvements over supervised and semi-supervised baselines in most low-label settings. Code & data: this https URL

---


### 159. [Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence](https://arxiv.org/abs/2608.25869)

**<font color=#1a73e8>作者：</font>** Ante Kapetanovic, Kemal Altwlkany, Andro Mercep 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly assess generated content, giving rise to the LLM-as-a-Judge paradigm. These systems now score outputs, filter content, and gate iterative refinement in production pipelines, where each judgment is often assumed to be independent of earlier evaluations. We test this assumption using three prompt conditions: no metadata, revision framing, and anchored metadata containing revision, attempt, and prior-score fields. We show that prior scores, even when included only as context metadata, anchor judgments and systematically shift ratings toward their values. Across 192,000 attempted evaluations (185,271 successful), seven out of the eight evaluated models have 95% task-stratified bootstrap intervals below zero for the total anchored-metadata effect on 20 fixed texts. Cohen's $d$, a standardized measure of the difference between score distributions, reaches an absolute value of 0.71. Token-level analysis of selected model-task probes suggests a threshold-like response pattern: introducing anchored metadata produces a marked redistribution of output-score probabilities, while changing the anchor value within the tested below-threshold range produces comparatively little additional variation. On categorical industry data with human-labeled ground truth, anchored metadata blocks 48% of error corrections and flips 10.18% of correct judgments toward an assigned wrong label, demonstrating the bias extends beyond numerical scoring to categorical decisions. Neither Chain-of-Thought nor a metadata-disregard warning reduces the total effect, although the warning improves the paired accuracy effect relative to baseline in the industry experiment. Reliable LLM evaluation demands careful context engineering rather than an assumption of impartiality. Effective mitigation must be validated for the intended model and task or domain.

---


### 160. [CEDAR: Controlled and Event-Driven Demand Forecasting via Residual Decomposition](https://arxiv.org/abs/2608.25871)

**<font color=#1a73e8>作者：</font>** Junjie Meng, Ranxu Zhang, Zi-an Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting in large-scale e-commerce marketplaces is increasingly required to support planning: merchants need to evaluate sales outcomes under future action sequences such as budget schedules, rather than passively predicting what happens next. However, most existing time series forecasting (TSF) approaches remain inherently passive. Even when incorporating operational decisions as auxiliary covariates, they typically optimize for correlation-based extrapolation under historical policies. This design suffers from autoregressive inertia and conflates endogenous market evolution with decision-induced transitions, leading to policy-insensitive rollouts and unreliable counterfactual analysis. To bridge this gap, we propose CEDAR (Controlled and Event-Driven Demand forecasting via Action-aware Residual decomposition), a two-stage framework for robust decision-conditioned simulation. In Stage I, an Action-Interleaved Transformer learns controllable action-conditioned state transitions for rollout under planned interventions. In Stage II, a Residual Correction Module leverages external event signals and LLM-assisted text representations to align noisy event descriptions with product context and correct event-driven deviations. Our study is enabled by a large-scale real-world dataset from Alibaba 1688, comprising approximately 32 million product trajectories with paired state-action sequences and aligned event signals. Extensive offline experiments and online controlled experiments in production demonstrate that CEDAR consistently improves simulation accuracy over strong TSF baselines and delivers practical gains for real-world budget planning.

---


### 161. [Do Vision-Language Models Agree on the Affective Qualities of Shape? A Cross-Model Audit for Generative Design Interfaces](https://arxiv.org/abs/2608.25876)

**<font color=#1a73e8>作者：</font>** Luca Bux, Thiago Rios, Ingo Scholtes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative design interfaces increasingly expose semantic controls that let users steer output with concepts such as "more elegant" or "more minimalist," typically encoded by a vision-language model (VLM). A practical question is whether state-of-the-art VLMs represent objects consistently in terms of the same concept. We audit 6 VLMs by ranking untextured 3D objects along Kansei adjective pairs, where Kansei describes affective impressions of product form, with each axis defined as the difference between the text representations of its two poles. Geometric pairs serve as positive controls, and pairs of unrelated adjectives establish an empirical null. Across 10 categories of ShapeNet database, affective axes converge above the null (mean pairwise rank correlation 0.36 vs. 0.14) but below the geometric ceiling (0.44). The agreement between models is partial and highly uneven: on the three axes shared by all categories, mean convergence ranges from 0.21 for bookshelves to 0.51 for jars. Convergence depends primarily on whether a category's representational variation aligns with the semantic direction being evaluated, rather than simply on how much the objects vary in shape overall. Cross-model convergence does not imply agreement with human judgments. Based on our findings, we implement a UI prototype that shows how the audit can inform which Kansei descriptors to expose as controls for a given object class and which to withhold.

---


### 162. [From Passive Response to Proactive Correction: Enhancing LLM Robustness Against Input Fact Perturbations](https://arxiv.org/abs/2608.25894)

**<font color=#1a73e8>作者：</font>** Ping Wang, Xiangguo Sun, Bingbing Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently produce confident yet factually incorrect responses when user inputs contain misleading premises, a phenomenon we attribute to fact perturbations in the input. Existing approaches to hallucination mitigation typically assume reliable user inputs, overlooking how such factual errors can actively mislead model reasoning. To address this vulnerability, we propose DEDUCE, a three-stage framework that transforms LLMs from passive responders into proactive error correctors. DEDUCE operates in three stages: (1) detect errors through fine-grained fact extraction and verification; (2) devise correction strategies via multi perspective deliberation; and (3) correct misconceptions while delivering reliable answers. We also present MisFactQA, a dataset containing factual errors of varying degrees, and propose new metrics for evaluating model robustness. Experiments on TruthfulQA, FalseQA, and our MisFactQA benchmark demonstrate that DEDUCE significantly improves both accuracy and error correction capability. Consistent gains across Qwen, LLaMA, and Gemma families confirm its effectiveness and scalability.

---


### 163. [One Form to Transfer Them All: Pretraining Multilingual Language Models Beyond Native Orthography](https://arxiv.org/abs/2608.25904)

**<font color=#1a73e8>作者：</font>** Muge Zhang, Aaron Jencks, Krishna Badikela 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual language models transfer knowledge across languages through shared subword vocabulary, a mechanism that breaks down when related languages use different writing systems. Prior work addresses this via script equalization (romanization or IPA transcription), but direct comparisons are rare; the focus has been on encoder-only models, with most work adapting existing pretrained models. We systematically compare different input representations in autoregressive multilingual pretraining, comparing orthographic text, IPA, and romanization in a controlled setup across three scales (467M, 709M, and 1.03B) on eight languages in four typologically motivated pairs. Across a wide range of downstream tasks on seen and unseen languages, romanized pretraining yields the strongest cross-lingual transfer, and the advantage over text widens with scale. IPA improves over text in most settings but trails romanization. Surprisingly, finetuning a text-pretrained model on romanized data hurts performance on languages already covered by the base model, only marginally helping when the model lacks script coverage. Our results indicate that for multilingual models spanning typologically diverse scripts, to obtain maximum benefits, romanization should be treated as a core design choice applied at pretraining rather than a post hoc fix.

---


### 164. [Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems](https://arxiv.org/abs/2608.25920)

**<font color=#1a73e8>作者：</font>** Zhongwen Luan, Xiaoyu Zhang, Ming Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM)-based multi-agent systems (MASs) are increasingly applied to long-horizon complex tasks, their reliability has emerged as the core bottleneck hindering their real-world deployment. Existing MAS debugging and repair methods typically rely on rerunning and resampling the entire execution trajectory. However, a fundamental question remains to be answered: do these methods causally repair MAS failures or merely stochastically repair by leveraging the randomness of LLM sampling? To evaluate the effectiveness of MAS repair methods, we introduce SymTrace, a controlled evaluation framework that records the MAS execution trajectory and establishes intervention anchors. During replay, it effectively reconstructs the execution before the anchor using recorded logs and only regenerates the downstream trajectory, thereby enabling the reliable reproduction of MAS failures. We further construct the dataset SymFail, comprising 536 human-annotated failure trajectories with graph-linked locations, categories, and trace evidence. Based on these foundations, we conduct a large-scale empirical study across three mainstream MAS frameworks. Our findings reveal that existing unguided rerun methods are highly unreliable, exhibiting low failure reproduction and repair rates (only 67.97% and 6.90%, respectively). Building upon these findings, we further explore the effectiveness of a symptom-driven intervention method, which successfully repairs 20.15% of the failed cases (a 191.89% improvement to state-of-the-art repair methods). This study aims to provide actionable insights for MAS debugging and repair research, paving the way for the robust deployment of multi-agent systems.

---


### 165. [Visual General Intelligence: A White Paper](https://arxiv.org/abs/2608.25924)

**<font color=#1a73e8>作者：</font>** Hirokatsu Kataoka, Yoshihiro Fukuhara, Yonglong Tian 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper reconsiders intelligence from a vision-centered perspective and examines whether intelligence emerging from visual experience and learning may provide a pathway toward AGI. In the language domain, beginning with the introduction of the Transformer architecture, the GPT series has demonstrated transfer to unseen tasks through autoregressive language modeling on web-scale text combined with aggressive scaling. This raises a natural question, namely, what capabilities and forms of intelligence can emerge from visual modalities such as images, videos, and geometry? In this paper, we discuss whether visual intelligence can serve as a pathway toward AGI, referred to in this paper as visual general intelligence (VGI), by bringing together contributors from diverse standpoints and affiliations. Our aim is not to offer a single definition of visual intelligence, but to clarify the principles that computer vision should pursue in the AGI era, the visual input modalities, the benchmarks, the learning paradigms, and the relationship between vision, when taken as the core, and other modalities such as language.

---


### 166. [Code World Model: Coding Agent as World Brain](https://arxiv.org/abs/2608.25927)

**<font color=#1a73e8>作者：</font>** Yiwen Chen, Guosheng Lin, Chi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models aim to simulate how complex environments evolve under actions and events, yet existing video-based world models primarily learn dynamics from visual observations, which reveal outcomes rather than the underlying knowledge, rules, and mechanisms governing world evolution. This makes it difficult to maintain persistent consequences and support coherent, open-ended evolution. We introduce Code World Model, a framework that separates world evolution from visual realization by combining the reasoning and coding capabilities of language models with the generative priors of video models. A coding agent serves as the world brain, reasoning about events and their consequences and generating executable code to maintain persistent world state and perform rule-consistent evolution. To connect executable state with visual generation, we introduce a proxy representation that encodes frame-wise spatiotemporal constraints and is compiled into a proxy video, which conditions a video model to render high-fidelity visual observations. We further develop data pipelines for constructing aligned proxy-observation pairs from gameplay and real-world videos. After fine-tuning on paired gameplay data, MiniMax-H3 follows proxy-based spatiotemporal specifications from simple interactive worlds built by the coding agent while preserving rich visual details and dynamics. These results demonstrate the potential of combining code for persistent world evolution with video models for flexible visual realization, providing a new path toward open-ended world models.

---


### 167. [When Composition Doesn't Add Up: Humans Identifying Defects in AI-Generated Images](https://arxiv.org/abs/2608.25933)

**<font color=#1a73e8>作者：</font>** Ruoqi Hu, Chulin Zhao, Jiashuo Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> *Chulin Zhao and Ruoqi Hu contributed equally to this work.
State-of-the-art text-to-image (T2I) models exhibit pronounced and systematic defects when prompts involve intricate compositional factors such as multiple entities and multiple attributes. In this paper, we investigate how humans identify such defects. Specifically, we manually select 651 reference images from the four categories of people, hand, object, and scene that exhibit complex compositional characteristics, from which prompts emphasizing compositional factors are derived by manually editing ChatGPT-generated prompts. We then feed the prompts into three selected T2I models to generate AI images and conduct a comprehensive subjective study to identify their defects. For each image, 29 participants provide multi-label assessments specifying defect types and locations. The study yields the compositional AI-generated image defect (CO-AID) dataset, including reference images, prompts, AI-generated images, and information on defect locations and types. Experimental results show that training a deep model on CO-AID can both predict defects in AI-generated images and optimize AI image generation, demonstrating its usability and effectiveness. The database and supplementary materials are available at: this https URL .

---


### 168. [How Robust Are Automated Fact-Checking Systems? A Cross-Benchmark Evaluation](https://arxiv.org/abs/2608.25934)

**<font color=#1a73e8>作者：</font>** Aida Usmanova, Zangir Iklassov, Markus Leippold 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated fact-checking (AFC) systems retrieve evidence and predict claim veracity, yet evaluations omit simple baselines, systems are developed for a single benchmark and cannot be trusted to generalise across domains. No prior work cross-evaluates the full two-stage retrieve-then-verify pipeline across diverse datasets, complementing retrieval-only studies (Thakur et al., 2021) and single-stage benchmarking studies (Calamai et al., 2025). We benchmark nine models, ranging from random and sparse baselines to fine-tuned transformers, zero-shot LLMs, and the two highest-ranked systems from the AVeriTeC 2025 shared task, across four datasets spanning scientific, open-web, and climate domains. Three findings stand out: (1) on ClimateCheck claim-only and fine-tuned models outperform zero-shot LLM and top-performing AVeriTeC 2025 systems, highlighting that noisy evidence can degrade veracity prediction; (2) system rankings are strongly domain- and metric-dependent: the best model on SciFact (macro-F1 0.70) drops to 0.31 on ClimateCheck, while the AVeriTeC 2025 winner and runner-up swap rankings based on evaluation metrics and datasets; (3) replacing retrieved evidence with gold annotations improves veracity accuracy by 14-22 points across models, confirming retrieval remains primary bottleneck. We release code, pre-processed datasets, and all results to support reproducible AFC research.

---


### 169. [TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding](https://arxiv.org/abs/2608.25935)

**<font color=#1a73e8>作者：</font>** Yuqiang Lin, Yan Shi, Sam Lockyer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic Anomaly Understanding (TAU) requires models and systems to detect, reason about, and explain anomalous events in transportation videos. To address this challenge, we propose TAU-Agent, an agentic retrieval-augmented framework for traffic anomaly understanding. Given a task query, a central retrieval agent orchestrates two visual perception tools, namely a Video Captioning Tool and an Open-Vocabulary Tracking Tool, to retrieve and select query-relevant evidence, including captions, temporal intervals, and object trajectories. The selected evidence, together with sampled video frames and the input query, is provided to a supervised fine-tuned vision-language model for final reasoning and answer generation. We evaluate TAU-Agent on both the in-domain and the out-of-domain benchmarks from the AI City Challenge 2026. TAU-Agent achieves scores of 0.6779 on Track 3, 0.3998 on Track 7, and 67.9275 on Track 8, ranking second, twelfth, and fifth, respectively. Code is available at: this https URL.

---


### 170. [One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation](https://arxiv.org/abs/2608.25936)

**<font color=#1a73e8>作者：</font>** Justin Robert, Raheel Qader  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation trains a language model on its own generations while a teacher scores them token by token. It combines the dense supervision of imitation learning with the on-policy sampling of reinforcement learning. But it requires a second, larger model to act as teacher. On-Policy Self-Distillation (OPSD) removes that cost. The teacher is the model itself, conditioned on privileged information the student will not have at test time, such as a reference solution, a plan, or environment feedback. The teacher is no stronger than the student, only better informed. Early results were promising, with accuracy comparable to reinforcement learning at a fraction of the generated tokens. But the same asymmetry that produces the signal also biases it. One failure mode now dominates the field: collapse, the progressive narrowing of the set of reasoning paths the model can produce. Collapse is not specific to OPSD, though privileged information aggravates it. This review treats collapse as a symptom governed by three levers: (i) where the signal is applied, that is, how tokens are weighted; (ii) what the teacher is shown, that is, the nature of the privileged information; and (iii) when the signal changes, that is, the teacher's dynamics and the decay of guidance. We restrict our scope to mathematical reasoning, where the method originated and where its failure modes are best documented. We report no new experiments. The contribution is structural: a shared vocabulary for phenomena named differently across papers, and a clear line between what is settled and what is still disputed.

---


### 171. [Candidate supply and answer selection shape the value of LLM judging in multi-agent systems](https://arxiv.org/abs/2608.25937)

**<font color=#1a73e8>作者：</font>** Jia-Hao Ji, Sijie Li, Jiabei Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.

---


### 172. [When Pruning Meets Interpretability: Preserving Sparse Autoencoder Robustness in LLMs](https://arxiv.org/abs/2608.25941)

**<font color=#1a73e8>作者：</font>** Suchit Gupte, Xueru Zhang, Mohammad Mahdi Khalili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are widely used to interpret the internal representations of large language models (LLMs), yet their reliability under post-hoc model compression remains poorly understood. We present a systematic study of how pruning affects SAE behavior and theoretically show that, for a fixed SAE, its impact is governed by perturbation energy, a covariance-weighted norm. This perspective exposes a key limitation of magnitude pruning: by ignoring activation geometry, it distorts the learned representation space and degrades SAE functionality. Activation-aware methods such as Wanda and SparseGPT, in contrast, implicitly control perturbation energy and are therefore substantially more robust at preserving SAE behavior. We further reveal a consistent structural vulnerability across all pruning methods: middle layers are significantly more sensitive to pruning than early or late layers. Guided by this insight, we propose a layer-wise sparsity allocation strategy, achieving lower perplexity under the same average pruning sparsity. Experiments across four model architectures validate our theoretical findings. Code is publicly available at this https URL.

---


### 173. [Unveiling Spectral Mechanisms in Training-Free LLM Text Detection](https://arxiv.org/abs/2608.25944)

**<font color=#1a73e8>作者：</font>** Haitong Luo, Xuying Meng, Weiyao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Large Language Models (LLMs) makes it increasingly difficult to distinguish human writing from machine-generated text. Training-free detection offers a scalable solution, yet common confidence-based metrics mainly measure average token probabilities and often miss the signal fluctuations that characterize human writing, which we call "generative vitality". Spectral analysis offers a way to capture this vitality, but its mechanism and practical boundaries remain underexplored. In this paper, we analyze spectral detection from both theoretical and empirical perspectives. We connect spectral energy to variance in proxy log-probability trajectories and explain how broader human token choices create the fluctuations used by frequency-domain indicators. We further show that the strength of this signal depends on text length and sampling range: spectral evidence is clearest for long, continuous, constrained generation, while short, fragmented, mixed, and edited settings require complementary confidence and fluctuation views. These findings clarify when frequency-domain detection works and provide guidance for future multi-dimensional detector design.

---


### 174. [Praxist: From Experimental Artifacts to Solution Lineages](https://arxiv.org/abs/2608.25955)

**<font color=#1a73e8>作者：</font>** Jin Li, Ahmed Murtadha, Zhiyu Wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous R\&D agents now write, run, and improve executable artifacts under automated evaluation---but largely as laboratory instruments: shown on curated benchmarks, with gains that are hard to trace to a cause and costs well above what sustained engineering practice absorbs. The limitation is structural. Most systems treat each attempt as nearly self-contained, so logs, memories, and search trees record what happened without establishing which design element produced an improvement, whether its evidence survived validation, or how it recombines with others. Long campaigns therefore keep re-learning the same lessons. We introduce Praxist, a lineage-centered generational system that converts reproducible artifacts and evaluator outcomes into a typed evidence graph of findings, lane-structured frontiers, and agendas. Separating local artifact construction from cohort-level evidence synthesis lets later attempts inherit validated mechanisms, unresolved claims, and useful constraints, and leaves results attached to an inspectable lineage. On the standardized 75-task MLE-bench suite, the finalized official-grader results give Praxist 60 medals (80.0\%), 49 of them gold, against 55 medals (73.3\%) and 34 gold for a Claude Code baseline on Claude Opus 4.8---at a recorded model spend of US\$3,054 versus US\$38,370, roughly a twelfth of the cost. Four case studies---quantitative trading, LiDAR-inertial-visual SLAM, tokamak magnetic control, and rocket landing---carry the same process into open-ended engineering problems, improving on each task-native baseline in headline accuracy, survival, or resource cost, with the discovery path on record. Stronger artifacts at an order of magnitude less spend, each backed by an auditable lineage, are, to our knowledge, first brought together here: the operating profile production research requires, not the one a benchmark demonstration establishes.

---


### 175. [LivingRAG: Augmenting Graph RAG with Experience](https://arxiv.org/abs/2608.25960)

**<font color=#1a73e8>作者：</font>** Yuzhuo Cui, Zongye Zhang, Qingjie Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based RAG improves multi-hop question answering by organizing evidence as a knowledge graph. However, most existing RAG systems process each query in isolation and discard useful reasoning from the LLM's response after inference. As a result, later related queries need to retrieve evidence and reason from scratch. We propose LivingRAG, a Graph RAG framework with writable and reusable reasoning experience. LivingRAG adds a writable experience store to a graph-based retrieval backbone, enabling verified experiences to be reused during inference in two ways. Stored graph signals help retrieval find entities and passages that were useful in earlier related queries. Stored summaries provide a reference reasoning pattern for answer generation. We analyze online QA streams and find reusable signals from shared entities, graph neighborhoods, and question templates. Experiments on multi-hop QA benchmarks show that LivingRAG improves accuracy over strong RAG baselines and reduces completion-token use when relevant prior experience is reused.

---


### 176. [SciMIF: Understanding Multimodal Instruction Following in Scientific Domains](https://arxiv.org/abs/2608.25973)

**<font color=#1a73e8>作者：</font>** Ye Shen, Yuting Zheng, Dun Pei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding instruction-following capabilities in scientific domains is essential for effectively leveraging Multimodal Large Language Models (MLLMs) to advance the development of scientific fields. In this work, we introduce SciMIF, a novel benchmark designed to evaluate the capability of MLLMs in following complex scientific instructions. Specifically, based on an extensive analysis of 22 distinct tasks across 5 representative scientific disciplines, we propose a comprehensive taxonomy comprising 10 constraint groups that captures both general functional requirements and discipline-specific characteristics. Guided by this taxonomy, we develop a high-fidelity instruction injection pipeline to systematically augment existing scientific datasets. We conduct comprehensive experiments on multiple state-of-the-art closed-source and open-source MLLMs. Our findings reveal significant performance disparities across different scientific disciplines, with chemistry posing greater challenges for current MLLMs. Furthermore, we observe that increasing the model scale does not yield corresponding improvements in constraint adherence, and current models still struggle severely with fine-grained constraints and instructions requiring the deep application of disciplinary knowledge. SciMIF fills the current void in evaluating multimodal instruction adherence within scientific domains, laying a crucial foundation for future enhancements of MLLMs in rigorous scientific applications. Data and code will be released at this https URL .

---


### 177. [When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized LLMs](https://arxiv.org/abs/2608.25977)

**<font color=#1a73e8>作者：</font>** Yao Fu, Lijia Huang, Xiaomin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences. While the Myers--Briggs Type Indicator (MBTI) has emerged as a common framework for assessing LLMs' personality, existing studies focus primarily on full-precision models and evaluate only final outputs. They overlook the widespread deployment of quantized LLMs requiring low memory footprints, whose personality traits remain underexplored. In this work, we present a systematic MBTI analysis of open-source LLMs across multiple precisions, including mainstream 4-bit methods (GPTQ, AWQ) and extreme 2-bit settings (AQLM variants). Beyond output-level evaluation, we examine how personality emerges across layers through option-level entropy and confidence-gap dynamics, and introduce Uncertainty-Amplified Layer Decoding (UALD) to study decoding-induced personality drift at inference time. Our results reveal a key insight: LLMs' personality is not a static property, but an emergent, layer-dependent decision process sensitive to quantization, prompting, and decoding. Specifically, we find that (1) ENFJ remains dominant across model families and precisions; (2) 4-bit quantization largely preserves coarse personality structure, while 2-bit quantization disrupts fine-grained prompt consistency and cross-precision agreement; (3) personality decisions emerges in upper layers, following substantial ambiguity in early layers; and (4) inference decoding can shift personality, while personality-aligned conditioning improves robustness. These findings provide a new perspective on the behavioral reliability of quantized LLMs and highlight the importance of considering internal dynamics and inference strategies in personality-sensitive chatbot applications.

---


### 178. [Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs](https://arxiv.org/abs/2608.25986)

**<font color=#1a73e8>作者：</font>** Zongyu Wu, Yilong Wang, Xiaochen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph (KG)-based RAG leverages structured knowledge to provide (M)LLMs with high-quality external information. Building on these works, recent studies have explored multimodal knowledge graphs (MMKGs) as knowledge bases for GraphRAG. This enables Graph RAG to integrate knowledge across multiple modalities, thereby further enhancing its performance. However, existing MMKG-based RAG methods generally follow a common pipeline in which different modalities are largely processed independently before being fusion. As a result, textual context is only used to a limited extent during visual information extraction and subsequent multimodal knowledge fusion. This brings a semantic gap between images and text which limits the multimodal GraphRAG performance. To address this issue, we propose a novel framework for constructing a Context-Enhanced MMKG (CEMMKG) to better support multimodal GraphRAG. The proposed CEMMKG enriches each image with complementary textual context at both local and global scopes. Local context goes beyond the surrounding text by incorporating sentences that are semantically related to the image, while global context provides a summary of the entire passage. We further introduce a multi-granularity design for the local context, allowing it to capture semantically relevant information at different levels of detail. Extensive experiments on the selected vision-centric dataset validate that CEMMKG is effective in leveraging contextual information to improve MMKG-based RAG performance. Moreover, its effectiveness across different MMKG-based RAG methods demonstrates its broad applicability.

---


### 179. [Spectral Allocation: Why Muon Outperforms Adam, and How to Improve Muon](https://arxiv.org/abs/2608.25990)

**<font color=#1a73e8>作者：</font>** Xiaodong Wu, Wenyi Yu, Chao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Orthogonal optimisers such as Muon can substantially accelerate large language model pretraining relative to Adam, yet the mechanism remains incompletely understood. We investigate this through an out-of-sample spectral probing analysis of Transformer loss landscapes. At checkpoints along real training trajectories, we decompose each momentum buffer into its singular directions and estimate the loss-optimal step size along each direction on held-out data. The resulting spectral profile is anisotropic yet stable across batches and training stages, and consistent across the optimisers and model scales: a volatile head operating at the Edge-of-Stability supports a much smaller step size than the tolerant bulk, which permits substantially larger steps. This profile provides a unified spectral allocation account of why Muon outperforms Adam, which outperforms SGD. It also exposes a limitation of Muon's uniform scaling: it still underutilises the bulk. Guided by this finding, we introduce Spectral-Aware Muon (SAMuon), which holds the head at the Muon scale and amplifies the bulk using a static spectral prior. We provide two variants: the complete SAMuon follows the measured profile using a low-rank randomised SVD and the simplified SAMuon-lite uses a two-level approximation via rank-one power iteration. Neither method adds persistent optimiser state or notable extra FLOPs beyond Muon at scale, and the idealised exact-whitening versions of both retain Muon's asymptotic convergence rate under standard assumptions. Across "modded-nanogpt" models from 124M to 1B parameters, both variants outperform tuned AdamW and Muon (Scion implementation) baselines in all evaluated model-scale and batch-size configurations. SAMuon requires 13.3% to 24.0% fewer training tokens to reach the same validation loss as Muon, while SAMuon-lite retains most of this gain with near-zero wall-clock overhead.

---


### 180. [ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs](https://arxiv.org/abs/2608.25992)

**<font color=#1a73e8>作者：</font>** Songyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur substantial operating costs due to repeated LLM invocations and long-horizon context accumulation. Existing cascade routing methods make one-shot, query-level decisions and cannot adapt to the dynamic, state-dependent nature of multi-step workflows, in which the right LLM at each step depends on evolving task progress, remaining task difficulty, and cost-efficiency requirements. We present ProgRouter, an online progress-guided routing framework that adaptively selects LLM agents across workflow steps to preserve task-solving quality while adhering to time and cost budgets. ProgRouter introduces a multi-view task progress scorer that combines coarse workflow outcome regimes with fine-grained signals on subtask completion, progress trends, and workflow state quality. Then, a dual-path task progress predictor and an adaptive meta-gating mechanism estimate the progress gain for each candidate routed LLM. ProgRouter makes online step-wise routing decisions that balance progress gain, task time budgets, and long-term operating cost efficiency. Experiments on HumanEval Plus, MBPP, MATH-500, and ASQA, spanning agentic code generation, mathematical reasoning, and retrieval-augmented long-form question answering, demonstrate that ProgRouter reduces the operating cost relative to key baselines while maintaining strong task-solving performance.

---


### 181. [Distinct dynamics of conceptual and referential disruptions in human reading and large language model processing](https://arxiv.org/abs/2608.25999)

**<font color=#1a73e8>作者：</font>** Rui He, Nihal Altay, Wolfram Hinzen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic meaning is grounded in conceptual content, from which reference to particular entities emerges as words enter discourse. To examine the processing dynamics associated with these two dimensions of meaning, we selectively disrupted conceptual or referential information in short narratives and traced the resulting effects in human self-paced reading and in the predictive and representational processing of large language models. In human reading, conceptual disruptions produced a strong but localized processing cost, emerging immediately after the distorted word, reaching an early maximum, and then declining rapidly. Referential disruptions produced weaker effects, which decreased more gradually across subsequent words, and were more strongly modulated by sentence boundaries. In the language model, both disruptions emerged immediately at the manipulated word. Contextual model surprisal showed a pattern closely paralleling human reading: conceptual disruption produced a larger, more locally concentrated effect that decayed rapidly, whereas referential disruption produced a smaller and more gradual downstream effect. Output-layer representations showed a different pattern: referential disruption produced a larger initial displacement, while both distortions were subsequently characterized by power-law decay. Together, these results provide convergent evidence for distinguishable processing dynamics of two types of meaning: conceptual information imposes a more locally concentrated integration cost, whereas referential information engages a more distributed process of maintaining discourse-level identity.

---


### 182. [AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs](https://arxiv.org/abs/2608.26004)

**<font color=#1a73e8>作者：</font>** Sheng Liang, Yongyue Zhang, Nathanael Brian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions. To control latency, deployments routinely compress inputs, but this degrades task accuracy. Speculative decoding (SD) accelerates generation losslessly, yet it assumes the drafter and verifier share an identical context, preventing SD from resolving the accuracy-overhead trade-off. We propose AsymSpec, an asymmetric speculative decoding framework that breaks this symmetry: a lightweight drafter reads the full input while the large verifier operates on the compressed view. The drafter steers the verifier via a contrastive $\delta$-fusion of logits, modulated by a divergence-aware acceptance gate that preserves verification stability and high draft acceptance rates. Evaluated across four agentic capabilities and two end-to-end agent benchmarks, AsymSpec reaches $\approx 90\%$ of full-context accuracy on average, delivering $1.3$--$1.7\times$ throughput speedups at $0.2$--$0.3\times$ the compute cost on isolated text capabilities. These results show that asymmetric context access yields substantial gains precisely when compression discards critical reasoning signals.

---


### 183. [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](https://arxiv.org/abs/2608.26013)

**<font color=#1a73e8>作者：</font>** Min Zeng, Guanxin Tan, Libin Cen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal instruction-following models require training data that is accurate, diverse, verifiable, and challenging. Existing synthesis pipelines typically follow a one-pass generate-and-filter paradigm, discarding feedback from failed samples, verifier outcomes, and target-model errors. We present VISA (Visual Instruction Synthesis Agent), an agentic framework that reformulates multimodal instruction synthesis as a self-evolving loop. At each round, VISA analyzes an image to filter incompatible constraints and discover new verifiable ones, samples diversity- and difficulty-aware constraint sets from persistent memory, generates candidate instructions, and verifies the resulting samples with executable tools and structured large language model judges. Failed samples trigger diagnostic-guided recovery, while accepted samples are probed against the target model to estimate difficulty. The resulting verifier signals and target-model failure profiles are written back to memory, allowing subsequent rounds to adaptively expand the constraint space, reduce template repetition, and focus on unresolved model weaknesses. The same verifier contracts further provide reward signals for reinforcement learning without a separately trained reward model. Experiments on MM-IFEval show that VISA consistently improves multimodal instruction following over strong baselines, while preserving general multimodal capability across seven public benchmarks.

---


### 184. [DualOPSD: Adaptive Privileged Teachers for On-Policy Self-Distillation](https://arxiv.org/abs/2608.26019)

**<font color=#1a73e8>作者：</font>** Yutong Chen, Guangfu Guo, Zhichao Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) uses a privileged copy of the student model to provide dense supervision without an external teacher. OPSD keeps this privileged teacher fixed, even though the student distribution and output style change during training. We propose DualOPSD, an asymmetric alternating framework that adapts both policies. The student first learns from the privileged teacher. The teacher then moves toward the updated student distribution on the same student trajectory. This update makes later supervision responsive to the learner and does not require another rollout. On Qwen3-8B in non-thinking mode, DualOPSD improves avg@12 over OPSD by 23.61, 13.89, and 10.00 points on AIME 2024, AIME 2025, and HMMT 2025. Results at 1.7B and 4B show that the accuracy gain depends on model scale. Across all three scales, DualOPSD reduces truncation. The 4B diagnostic also shows lower KL in both directions between the teacher and student.

---


### 185. [Trace Integrity for LLM Data Agents: A Vision for Auditable Structured Reasoning in Real-World Systems](https://arxiv.org/abs/2608.26036)

**<font color=#1a73e8>作者：</font>** Srimonti Dutta, Akshata Kishore Moharir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Answer accuracy is an insufficient reliability signal for LLM data agents. In structured-data tasks, a benchmark-correct answer can be produced by an invalid trace. This paper introduces Trace Integrity, a deployment reliability criterion for evaluating whether the computation recorded behind an answer is explicit, executable, schema-valid, operator-faithful, replayable, answer-consistent, and auditable. We identify the Structure Gap as the deployment failure mode that makes Trace Integrity necessary: natural-language reasoning and free-form rationales do not reliably specify the operator-level programs required by real-world systems. We operationalize Trace Integrity with execution contracts, structured artifacts that bind user intent to schema elements, operator plans, assumptions, executable queries, verification status, and final-answer linkage. We also introduce CAIT (Correct Answer / Invalid Trace) Rate, which measures how often answer-only evaluation counts computationally unsupported outputs as successes. In an empirical demonstration on BIRD Mini-Dev, Direct SQL, Operation Summary + SQL, and Contract-First SQL achieve answer accuracies of 20%, 22%, and 24%, while their Trace Integrity Pass Rates are 39%, 43%, and 40% and their CAIT Rates remain high at 55%, 59.1%, and 45.8%, showing that answer accuracy, trace validity, and silent-failure risk are distinct evaluation signals. Real-world LLM data agents should, therefore, be evaluated not only by whether their outputs match a reference answer, but by whether those outputs are backed by auditable computation.

---


### 186. [Robust CurveMoE: Multi-Norm Adversarial Defense for Mixture-of-Experts Models via Mode Connectivity](https://arxiv.org/abs/2608.26043)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Ren Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-norm adversarial defense aims to protect neural networks against perturbations defined by different norm constraints, but existing methods typically optimize competing robustness objectives within a single parameter configuration, leading to substantial training cost and unfavorable robustness trade-offs. We propose Robust CurveMoE, an efficient mixture-of-experts framework that connects models specialized for different perturbation norms through a low-loss path and exploits the complementary robustness profiles of models along this path. Robust CurveMoE derives clean and norm-specialized experts from robustness-constrained curve locations and selectively expertizes only influential layers, while sharing the remaining parameters across routing paths. To further reduce curve-construction cost, we introduce contribution-guided partial updating, which selects influential curve parameters using initialization-based gradient scores. We also theoretically bound the objective gap between partial and full curve optimization. Experiments on CIFAR-100 and ImageNet-100 with WideResNet and Vision Transformer architectures show that Robust CurveMoE consistently improves clean, norm-specific, and Union accuracy over MSD and ERMC. In particular, it improves Union accuracy by 2.37 and 2.13 percentage points over the strongest baseline on CIFAR-100 and ImageNet-100, respectively. Extensive ablations further validate the effectiveness of partial updating, selective expertization, and robustness-constrained expert selection.

---


### 187. [RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models](https://arxiv.org/abs/2608.26049)

**<font color=#1a73e8>作者：</font>** Mahshid Rezakhani, Kimia Azar, Hadi Kamali  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models (LLMs) is driving a shift toward automated register transfer level (RTL) code generation, enabling designers to translate high-level specs. into synthesizable hardware. However, this reliance on pre-trained (3rd-party) fine-tuned models may introduce critical trust issues, as the training data and adaptation process of these models are often opaque. Thus, adversaries (even model providers) may embed hidden backdoor threats during fine-tuning, allowing malicious behavior, e.g., hardware Trojans, to be triggered by seemingly benign prompts given by victim user at inference time. In this paper, we introduce RTLGuard, to mitigate such a trust issue in AI-enabled IC supply chain. Rather than prohibitive computational cost of full-parameter retraining, RTLGuard leverages a teacher-student framework designed to sanitize compromised RTL generation models by (1) fine-tuning a small-scale, "clean" teacher model on a limited set of trusted RTL data, (2) guiding the poisoned target model via a composite teacher-student objective, and (3) incorporating feature alignment and knowledge distillation to suppress malicious behaviors. Our experiments across various LLM architectures demonstrate that RTLGuard significantly reduces the Attack Success Rate (ASR) while preserving the functional correctness and synthesizability of the generated RTL code.

---


### 188. [StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.26067)

**<font color=#1a73e8>作者：</font>** Zhe Liu, Jinghua Hou, Yuxiang Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored temporal modeling. It treats each (visual observation, language instruction) pair as an atomic temporal unit: bidirectional attention within each pair enables cross-modal fusion, while causal attention across pairs preserves autoregressive streaming inference. This ensures the language instruction serves as a persistent semantic anchor throughout task execution. To bridge the gap between synchronous training and asynchronous real-robot deployment, we introduce a andom-interval streaming training strategy: a proper inter-frame interval (e.g., every 3 frames) enables faster and smoother action execution. Beyond this, randomizing the interval further improves robustness to frame-timing perturbations, supporting asynchronous deployment in practice. Furthermore, by leveraging the length extrapolation capability of the LLM backbone, StreamPI seamlessly inherits pretrained single-frame weights and supports flexible single-frame and multi-frame inference. Experiments on real-robot tasks spanning memory-dependent and precise perception scenarios, as well as the simulation benchmark LIBERO, demonstrate that StreamPI outperforms pi0.5 across diverse tasks.

---


### 189. [Prefix Sliding for efficient test-time scaling](https://arxiv.org/abs/2608.26070)

**<font color=#1a73e8>作者：</font>** Niklas Muennighoff, Zhengyang Wang, Zeyi Chen 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling uses extra test-time compute to improve performance, such as letting language models reason longer when solving a problem. As models keep the entire reasoning trace in memory via full attention, hard tasks that need long thinking can be prohibitively expensive. However, we find most intermediate reasoning tokens lose importance as the model continues reasoning. This calls into question whether retaining them is worth the cost. Based on this insight, we propose Prefix Sliding, which discards tokens during reasoning that are not part of the prefix or the window of the last few thousand tokens. The prefix has key instructions and tools available to the model, while the most recent tokens are the current reasoning the model is working on. This caps the total memory requirement regardless of how long the model reasons, allowing for efficient long-horizon test-time scaling. Without training, Prefix Sliding can make existing models 3x faster while maintaining performance. Training with Prefix Sliding using reinforcement learning can achieve better performance by enabling scaling to reasoning traces beyond a hundred thousand tokens. Ablations show Prefix Sliding outperforms summarizing intermediate tokens or vanilla sliding window. Our code is at this https URL

---


### 190. [SwarmWorld: Stigmergic technological evolution in societies of language-model agents](https://arxiv.org/abs/2608.26081)

**<font color=#1a73e8>作者：</font>** Subhadeep Pal, Fiona Y. Wang, Markus J. Buehler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collective intelligence can emerge when individuals coordinate through a shared environment, allowing local actions to accumulate into durable social organization. Language-model agents offer a new substrate for this process, yet most multi-agent systems rely on direct conversation, predefined roles, or centralized workflows. It remains unclear whether decentralized agents can build functional technologies and outperform independent search. Here, initially homogeneous LLM agents in SwarmWorld self-organize without assigned roles or recipes into evolving technological societies. Agents explore a spatial environment, process resources, test materials, construct persistent artifacts, and write executable controllers evaluated by a deterministic simulator under unseen disturbances after the agents are removed. SwarmWorld splits cognition from consequence: agents propose architectures and controllers within fixed action and material schemas, while the simulated world determines function. Shared societies develop broader, more resilient technological portfolios than a strong best-of-N isolated-search baseline, although isolated search remains competitive for the strongest artifact. Agents differentiate into exploration, construction, maintenance, and coordination behaviors, transitioning as the world matures. Technologies accumulate through collaborative construction, executable inheritance, and persistent agent-artifact networks, with most reuse beginning through physical observation rather than communication. Explicit cultural mechanisms amplify collaboration and organization, but functional benefits depend on outcome and timescale. Physical stigmergy alone supports capable societies, while interaction drives persistent technological ecologies rather than universally superior individual inventions.

---


### 191. [TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development](https://arxiv.org/abs/2608.26086)

**<font color=#1a73e8>作者：</font>** Jiarui Yan, Weiwei Sun, Sijie Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models write correct code for isolated problems but remain far weaker at autonomous machine-learning development, where an agent must revise data pipelines, models, and validation over hours of feedback, and on most competitions still finishes below strong human competitors. Outcome-based benchmarks record this gap but not its cause, because they grade the final submission and discard the development process behind it. We introduce TraceML, which pairs human and agent work on the same competitions under one version-level schema: 4,465 human Kaggle trajectories across 134 competitions, seven of which are also worked by two agent scaffolds, giving 430 paired human and 207 agent trajectories. Every code version carries its score, its timestamp, and labels for the action taken, its intent, the edit size, and the score effect. Read this way, the gap becomes concrete. Experts alternate data work, validation, model changes, and ensembling, and return to approaches they had set aside. Each agent scaffold instead collapses into a narrow loop: Codex spends its steps re-weighting ensembles and tuning submissions, MLEvolve mutates its model in place, and neither pivots at the human rate nor reopens abandoned work. A short planning prompt distilled from human practice moves the behaviors it names toward the human profile and lifts scores, but the effort profile stays agent-shaped: instruction closes only the part of the gap that reduces to instructions. We release the corpus, the schema, the labelers, and the extraction pipeline at this https URL.

---


### 192. [From Producing to Validating: How AI Is Deskilling Freelancers](https://arxiv.org/abs/2608.26089)

**<font color=#1a73e8>作者：</font>** Nakul Rajpal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is promoted as a way to enhance knowledge work, yet its benefits and drawbacks fall unevenly across the workforce. Freelance and gig workers, who commonly lack the upskilling pathways available to traditional employees, face heightened risks to both skill development and job security as AI adoption advances. We review empirical evidence on AI's impact on knowledge-worker workflows and upskilling, then predict the primary and downstream effects of AI adoption among clients and workers in the freelance economy. We anchor this in two cases of the same shift, machine-translation post-editing and software development. We argue that freelancers are the leading edge of a change that also reaches salaried HCI practitioners, and we close with questions for the platforms and clients that mediate this work, and for HCI researchers.

---


### 193. [Agentic Autoresearch for Cell-Edge Power Control: Radically Redefining the Researcher's Role](https://arxiv.org/abs/2608.26093)

**<font color=#1a73e8>作者：</font>** Ahmad Khan, Akram Bin Sediq, Sara Azadegi Naeini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing machine learning algorithms for wireless resource management is labour-intensive: the architecture, the loss function and the training recipe are all specified by hand. We demonstrate that this design layer can be surrendered to an autonomous agent in its entirety. We adopt the autoresearch protocol, in which an AI coding agent edits a training script, runs a fixed-budget experiment, and retains or discards the change according to a single immutable metric. We grant the agent authority over the architecture family, the input representation, the output parameterization, the loss function and the task-sampling law, and set it a target chosen for its difficulty: sum-least-percentile-rate power control across a multicell network. The formulation targets cell-edge throughput and is non-convex, non-smooth and strongly NP-hard away from its max-min vertex. Safeguards render the results trustworthy: a hash-pinned evaluator, an enforced inference contract and a pre-registered falsifier per experiment. In eighty-one unattended experiments over twenty-six hours, the agent reached $99.5\%$ of a converged minorization-maximization reference in one fixed-cost inference pass, at roughly $600\times$ lower inference cost, closing $94\%$ of the gap from its first working architecture, with one parameter set serving every network size and percentile target. It recovered provable structure rather than tuned constants: the output parameterization it discovered reproduces the exact max-min-optimal allocation at the minimum percentile, for every value of the trained weights.

---


### 194. [A Visual Dependence-Aware Framework for Multimodal Unsupervised Continual Post-Training](https://arxiv.org/abs/2608.26095)

**<font color=#1a73e8>作者：</font>** Kaichen Li, Zhilin Zhu, Jianhao Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we explore a novel task of Multimodal Unsupervised Continual Post-Training (MU-CPT), enabling deployed MLLMs to continually evolve from streaming unlabeled data. Existing unsupervised post-training methods for MLLMs typically optimize target tokens uniformly, overlooking their heterogeneous visual dependence (VD). However, we reveal that token-level VD is crucial for MU-CPT. Specifically, its structural distortion serves as an indicator of cross-modal catastrophic forgetting, and its inherent heterogeneity acts as a compass to guide new-task learning. Leveraging this property, we propose a Visual Dependence-Aware (VDA) framework with two main components. First, Visually Constrained Optimal Transport (VC-OT) formulates the VD structural distortion of old-task VD during new-task learning as an optimal transport problem to mitigate cross-modal forgetting. By designing a region-aware ground cost and a dependence-stratified transport penalty, it prevents global shifts in visual focus while strictly prohibiting visual reliance from degenerating into language bias. Second, Visually Modulated Adaptation (VMA) exploits VD heterogeneity to emphasize visually grounded new-task learning, promoting new-task plasticity. Together, our method simultaneously maintains old-task stability and new-task plasticity during challenging MU-CPT. Extensive experiments under our MU-CPT setting validate the effectiveness of VDA.

---


### 195. [VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning](https://arxiv.org/abs/2608.26105)

**<font color=#1a73e8>作者：</font>** Junxiang Xu, Ruisi Wang, Fanyi Pu 等 52 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Native visual reasoning treats visual generation as the medium of reasoning itself: visual states (i.e. images and videos) are not merely inputs to be understood or outputs to be rendered, but first-class substrates for problem solving beyond language. Yet progress remains bottlenecked by the lack of scalable training tasks, reliable feedback, and controlled comparisons across generative substrates. In this work, we introduce VBVR-Pro, a closed-loop testbed that makes native visual reasoning through generation trainable, verifiable, optimizable, and experimentally controllable. 1) Task scaling. VBVR-Pro turns visual reasoning into a controlled task space of 300 procedurally generated tasks. Models trained on VBVR-Pro show strong transfer beyond the proposed suite across seven external visual reasoning benchmarks such as RISE-Video, MME-CoF-Pro, and BabyVision. 2) Verifiable rewards. VBVR-Pro provides verifiable reward scorers for task-grounded evaluation. Through a systematic study of leading MLLMs as judges, we identify recurring failure modes of the prevalent VLM-as-a-judge paradigm. In contrast, the proposed scorers are grounded in deterministic, task-specific rules, achieve fine-grained alignment with human judgments. Importantly, they serve as reliable reward signals for large-scale multi-task reinforcement learning and demonstrate stronger post-RL performance across visual reasoning tasks. 3) Mechanism study. VBVR-Pro enables controlled modality studies across more than 30 image, video, and interleaved generators. Our analysis shows that video generation remains strongest for tasks requiring persistent spatiotemporal state tracking, while interleaved generation provides a compute-efficient alternative. Critically, ablations and probing suggest the presence of vision-native trajectories that are crucial to visual reasoning. We release all data, models, scorers, and code.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 196. [Unsupervised Post-Training of Foundation Models: A Survey](https://arxiv.org/abs/2608.24982)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yijie Xu, Qianyi Cai, Huizai Yao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundation-model post-training usually relies on human labels, preference data, stronger teachers, or executable verifiers. We study Unsupervised Post-Training (UPT): update-bearing adaptation on unlabeled inputs whose learning signal is derived from same-lineage model artifacts rather than an external oracle. We catalog 80 strict UPT methods and organize them by the object that supplies the update signal: a prediction statistic, a sample relation, a self-generated target, or an internal evaluator. Beyond inventory, we show how the choice of internal signal and task structure determines whether post-training improves the model or recursively amplifies error. An orthogonal Input Visibility $\times$ Update Persistence view maps deployment regimes and defines a unified framework for UPT selection and evaluation.

---


### 197. [Flower Hub: A Reproducible Benchmarking Platform for Federated Learning in Simulation and Deployment](https://arxiv.org/abs/2608.25114)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yan Gao, Mohammad Naseri, Javier Fernandez-Marques 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) has emerged as a key approach for training models across decentralized data, yet benchmarking in FL remains difficult to reproduce, compare, and extend. Existing evaluations are often tied to custom infrastructure, released as incomplete research code, and conducted primarily in simulation, which limits portability and practical relevance. We present Flower Hub, a platform for publishing, discovering, and executing decentralized and federated applications. We show how it enables reproducible benchmarking by packaging benchmarks as executable, versioned applications with standardized metadata, pinned dependencies, and explicit evaluation workflows. We instantiate this approach with a multi-domain benchmark suite spanning cross-silo and cross-device settings, and including tasks in medical imaging, financial tabular learning, legal instruction tuning, phishing URL detection, and audio tagging. We further demonstrate that the same benchmarking application can run across both simulation and deployment runtimes without changing the application code, enabling unified evaluation across varying learning environments. Beyond model quality, our benchmark design supports system-aware reporting, including runtime and communication metrics. This work advances benchmarking in FL settings from ad hoc code artifacts towards portable, executable, and reusable benchmark applications.

---


### 198. [When Does Context Routing Help? A Systematic Study of Multi-Modal Fusion in Time Series Forecasting](https://arxiv.org/abs/2608.25128)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruizhe Zhou, Gaoyuan Du, Xiaoyang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-modal time series forecasting methods integrate auxiliary context into temporal predictions through increasingly sophisticated fusion mechanisms. A growing body of work reports substantial gains, yet it is often unclear whether they reflect genuine use of the context or incidental architectural effects. We ask a narrower, checkable question: when can auxiliary context help a forecaster at all?
We identify two dataset-level conditions that must both hold: (1) the target is not dominated by a last-value shortcut (low autocorrelation rho_h), and (2) the context carries information about the target beyond history (non-zero conditional mutual information delta; when delta=0 no predictor can benefit---a distribution-free result). Through controlled experiments on MoME (a 14.3B-parameter mixture-of-experts model, 6 datasets, 10 seeds) and four additional fusion mechanisms implemented within a single-backbone testbed (5 datasets), we find that when both conditions hold, text-conditioned expert modulation contributes a sizeable MSE reduction; when either fails, the contribution collapses to the capacity floor of the modulation pathway and carries no context-attributable signal.
We establish causality through two interventions: adding a shortcut to MoME suppresses routing contribution by 77-93% across 3 datasets; progressively corrupting context quality drives the context-specific benefit from +44% to negative. We validate the autocorrelation component of our diagnostic on 27 Monash Archive datasets. We provide a calibrated pre-training diagnostic that, on the datasets we test, yields no false positives in well-powered settings. We are explicit about the asymmetry of our evidence: the negative arm is broadly reliable, while the large positive magnitudes come from a single model family (MoME) and are corroborated only in direction by the testbed.

---


### 199. [Can You Trust Frozen Hematology Foundation Models under Acquisition Shift?](https://arxiv.org/abs/2608.25148)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jai Kumar Sharma, Peeyush Tapadiya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen hematology foundation-model (FM) embeddings reach near-saturated in-domain white-blood-cell (WBC) accuracy, but clinical deployment demands reliability across scanners, sites, stains and preparation pipelines. We audit 15 frozen encoders (hematology, pathology, and general vision) across four public single-cell acquisition domains along two axes: accuracy robustness and calibration. In-domain linear-probe macro-F1 is saturated (0.98-0.997), yet cross-dataset macro-F1 drops 34-72% and rankings re-order: DinoBloom-L, the in-domain best, falls to 10th of 15 on the most-shifted target (MLL23) at the benchmark's shared 224-px input, behind RedDino and several general and pathology encoders. Rank transfer is probe-dependent: 1-NN retrieval is more stable on average than a source-fitted linear head (median $\rho$ 0.65 vs 0.45), but neither probe universally predicts target robustness. Calibration also collapses: source-trained probes are nearly calibrated in-domain (expected calibration error, ECE, 0.004) but confidently wrong off-domain (ECE 0.35), and source-fitted temperature scaling transfers poorly. We further audit pretraining exposure and identify MLL23 as DinoBloom's internal cohort; because DinoBloom's only held-out dataset is also our source domain, this benchmark cannot isolate exposure from scanner-associated shift. Label-free adaptation and marginal-entropy-based model selection appear safe under balanced evaluation but fail under realistic WBC class-prior shift. Class-Balanced Re-standardization (CBR), a training-free pseudo-label-balanced feature normalization, improves all evaluated target-prior scenario means and partially improves calibration, although encoder-level exceptions and residual miscalibration remain. Hematology FM benchmarks must therefore jointly audit accuracy, calibration, exposure, and class-prior robustness.

---


### 200. [Bootstrapping a 4D LiDAR Annotation Tool from Video Foundation Models](https://arxiv.org/abs/2608.25418)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jihun Kim, Hyun-Kurl Jang, Hyemin Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in 4D LiDAR segmentation is bottlenecked by data. Assigning temporally consistent labels across sparse point cloud sequences is costly and hard to scale, and every new task or domain tends to demand fresh dense annotation. This motivates a simple question of whether high-quality LiDAR training data can be produced automatically, without any human labeling. To this end, we introduce LiDAR-SAM2, a framework that turns a 2D video foundation model, SAM2, into a scalable source of supervision for the 4D LiDAR domain. On the data side, it automatically generates temporally coherent LiDAR-level labels from SAM2 video masks through multi-view projection and spatio-temporal aggregation. On the modeling side, a tailored modality interface and a two-stage learning objective adapt SAM2's video segmentation kernel to spatio-temporal LiDAR structure, so that a single click per object yields a consistent mask track across the sequence. Trained with no human LiDAR annotation, LiDAR-SAM2 produces semantic and panoptic labels on SemanticKITTI that approach the quality of full human annotation from only a few points, and models trained on these labels approach the performance of full ground-truth supervision. This positions LiDAR-SAM2 as a scalable labeling tool that substantially reduces the annotation burden for 3D and 4D scene understanding.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-209](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
