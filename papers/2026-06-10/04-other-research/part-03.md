# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 101. [Beyond Individual Personas: Aligning Synthetic Dialogue to Population-Level Behavior Distributions](https://arxiv.org/abs/2606.07893)

**<font color=#1a73e8>作者：</font>** Xinyi Liu, Rinat Khaziev, Hooshang Nayyeri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic dialogue corpora are increasingly used as proxies for target dialogue data, yet persona-grounded generators optimize individual conversations rather than corpus composition, yielding locally plausible dialogues with distorted population-level behavior mixes. We introduce GroupPersona, a framework that aligns synthetic dialogue corpora to the behavior distribution of a reference corpus. GroupPersona turns population statistics into generation controls: it separates each dialogue's core behavioral signature from predictable side effects, and uses the resulting behavioral groups to condition user agents on the interaction patterns that define the reference population. We evaluate GroupPersona on four corpora crossing two dialogue sources, assistant-style and Reddit-derived, with two construction variants: structure-preserving and variation-enhanced. GroupPersona lowers Jensen-Shannon divergence between synthetic and reference distributions over 12 behavior attributes from 0.234 to 0.177 relative to the strongest average baseline, a 24.4% reduction, and is best or tied-best on all four corpora while preserving structural alignment. It also achieves the closest calibration to reference-conversation quality scores, reducing mean absolute deviation from the reference-conversation profile to 0.63 versus 0.91 for the next-best baseline.

---


### 102. [TBD-VLA: Temporal Block Diffusion Vision Language Action Model](https://arxiv.org/abs/2606.07895)

**<font color=#1a73e8>作者：</font>** Sung-Wook Lee, Xuhui Kang, Yen-Ling Kuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete Vision-Language-Action (VLA) models typically formulate action generation as next-token prediction over discretized action spaces, conditioning each token autoregressively on prior context. While effective, this paradigm incurs high inference latency and largely ignores the temporal structure inherent in action trajectories. Recent efforts introduce parallel decoding to improve efficiency, enabling faster inference, but lack explicit mechanisms for modeling token dependencies. We introduce TBD-VLA, a discrete token-based VLA framework that incorporates block diffusion to enable temporal action generation. We partition action sequences into temporal blocks and perform masked discrete diffusion within each block, while maintaining autoregressive generation across blocks. This design unifies temporal autoregression and parallel action decoding, achieving both strong temporal coherence and improved inference speed. In addition, the explicit temporal modeling enables asynchronous execution of action chunks (e.g., Real-Time Chunking) via temporal in-painting. TBD-VLA significantly outperforms prior VLA approaches in both simulation and real-world manipulation tasks, offering a scalable path toward fast, temporally aware, discrete VLA models. Project webpage: this https URL

---


### 103. [The AI Epistemic Deference Index: A Continuous Measure of Sycophancy](https://arxiv.org/abs/2606.07897)

**<font color=#1a73e8>作者：</font>** Alejandro Botas, Paul de Font-Reaulx, Luke Hewitt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current AI models frequently exhibit epistemic sycophancy, endorsing claims to agree with a user. Existing evaluations typically measure this either by assessing what it takes to make a model shift a binary endorsement or by eliciting an explicit probability in a proposition. However, much user-facing sycophantic behavior is demonstrated through shifts in graded support expressed through ordinary language. We propose the AI Epistemic Deference Index (AEDI): a continuous, unidimensional score representing how sensitive the support expressed in a model's output is to the attitude expressed in a user's prompt. To generate AEDI, we provide a new protocol for estimating probabilities from natural language outputs, using LLMs-as-judges validated for consistency and correlation to human judgment. We deploy it on a new curated database of 500 propositions across diverse topics and 16,000 prompts varying in user attitude, testing eight prominent models. Every model exhibits substantial deference, though with large and systematic differences across providers, with Claude models demonstrating the least, and Grok and Gemini models the most. The effect is amplified in prompts requesting a written artifact, and concentrated on propositions where models hold weaker priors. We release AEDI as an easy-to-update benchmark and measurement pipeline for output-level sycophancy evaluation.

---


### 104. [3D Oral Modelling with Improved Vertex Distribution Using Matching-Based Learning](https://arxiv.org/abs/2606.07907)

**<font color=#1a73e8>作者：</font>** Jihun Cho, Soo-Yeon Jeong, Eun-Jeong Bae 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In our previous work, a deep learning-based framework for 3D intraoral reconstruction was proposed. The model directly predicts explicit 3D point cloud coordinates from ten fixed-angle intraoral images, employing MobileNetV2 and Multi-head Attention for multi-view feature fusion, with a combined L1 Loss and Chamfer Distance as the loss function. Although the model achieved an accuracy of 77.49%, predicted vertices tended to concentrate in high-density regions of the ground truth, leaving other regions largely uncovered.
In this paper, an improved loss function is proposed to address this limitation. Hungarian matching with filtering and Repulsion Loss are introduced to enforce more uniform vertex distribution across the reconstructed model. The proposed model achieves an accuracy of 68.02%, which is numerically lower than the previous model. However, the vertex clustering issue observed in the prior work is substantially alleviated, with predicted vertices distributed more evenly across the entire reconstructed surface.

---


### 105. [Layer-wise Derivative Controlled Networks Achieve Competitive Accuracy and Gradient Stability Across Data Regimes](https://arxiv.org/abs/2606.07908)

**<font color=#1a73e8>作者：</font>** Rowan Martnishn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Derivative-controlled networks based on ChainzRule (CR) combine cubic polynomial layers with a lightweight forward-mode per-layer Jacobian penalty (DREG). In this second paper of a multi-part series, we evaluate the generalization properties of CR across data regimes.
We ablate the shape of the DREG coefficient schedule, demonstrating that the optimal annealing range depends on representation noise. On the Pima Diabetes dataset, CR achieves strong low-data performance and maintains a consistent accuracy advantage over baselines from 5\% to 100\% training data, supported by exceptionally stable gradient tail ratios ($\sim$1.01--1.02 vs. 1.07--1.09 for ReLU networks). Extensions to SST-5 show competitive or superior results in both frozen-embedding and BERT fine-tuned regimes, including outperforming prior BERT baselines despite substantially less training data. These results are statistically significant: CR achieves superior accuracy over the strongest published baselines we could identify on both datasets ($p < 0.05$).
These results establish that layer-wise derivative control induces a structural inductive bias toward low-frequency, stable representations that generalizes robustly across tabular and NLP domains, data volumes, and representation qualities. The gradient tail ratio serves as a reliable, label-free diagnostic of generalization capability.

---


### 106. [CAAL: Contextual Bandits based Online Hand-Craft Active Learning Strategy Selection](https://arxiv.org/abs/2606.07910)

**<font color=#1a73e8>作者：</font>** Shao-An Yin, Jiacong Li, Tianpei Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The challenge with active learning algorithms is the uncertainty of the statistical distribution of unlabeled data, making it difficult to choose the best hand-crafted strategy. To address this, we introduced Contextual Adaptive Active Learning (CAAL). In CAAL, each "arm" represents a hand-crafted strategy. Unlike existing frameworks that select strategies based only on feedback from labeled data, we dynamically choose strategies for labeling batches of data using reward prediction with external context information. This general framework allows for customization with domain knowledge to design more effective rewards and context candidates. In addition, we experimentally show that CAAL outperforms the existing baseline adaptive strategy on public datasets using our reward and context design. Our results are consistent regardless of batch size in each iteration.

---


### 107. [EditSR: Enhancing Neural Symbolic Regression via Edit-based Rectification](https://arxiv.org/abs/2606.07915)

**<font color=#1a73e8>作者：</font>** Da Li, Xinxin Li, Xingyu Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural symbolic regression models improve inference efficiency by shifting structural search to pretraining, but their one-pass autoregressive decoding is prone to error accumulation, which may lead to generating structurally incorrect expressions, especially in complex expression generation scenarios. Existing rectification strategies can alleviate this issue, but they often depend on restarting global search, thereby weakening the efficiency advantage of neural models, and remain susceptible to error accumulation. In this paper, we propose EditSR, a two-layer framework that combines a neural symbolic regression model in the first layer with an edit-based Rectifier in the second layer to achieve efficient prediction and post-hoc rectification. Instead of restarting the global search, we maintain rectification efficiency by pretraining the Rectifier. Specifically, we formulate the rectification process as a step-by-step state-transition chain starting from an incorrect expression, and develop a state-transition algorithm to construct supervised rectification chains for training the Rectifier. To ensure syntactic validity throughout rectification, each edit action is restricted to a syntactically valid space so that every edited expression remains parseable. In addition, because each edit decision is conditioned on the current state rather than the history, the Rectifier allows errors made in earlier steps to be rectified by subsequent edits, thereby reducing the risk of error accumulation. Extensive experiments and ablation studies show that EditSR substantially improves symbolic structure recovery with limited extra cost, with more pronounced gains on complex expressions, where one-pass autoregressive decoding is more susceptible to error accumulation.

---


### 108. [The CIFAR Synthetic Evidence Corpus for Detecting AI-Generated Evidence](https://arxiv.org/abs/2606.07916)

**<font color=#1a73e8>作者：</font>** Kelly McConvey, Jalehsadat Mahdavimoghaddam, Nima Jamali 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing ability of generative models to produce realistic documents poses a direct challenge to evidentiary workflows in the justice system and the courts, where decisions increasingly depend on the authenticity of evidence such as receipts, communications, and administrative records. Unlike social media or academic settings, evidentiary documents are often only subtly altered, with small, localized edits that preserve overall plausibility while changing legal meaning. Yet progress on automated detection remains limited, largely due to the absence of suitable training and evaluation data especially suited for the justice system requirements. Existing resources are either focused on photos of human faces or natural scenery or on narrowly scoped academic or social media document types, and do not capture the structure, diversity, or manipulation patterns characteristic of real-world evidentiary data. As a result, current detection systems do not necessarily learn meaningful signals appropriate for the justice system. We introduce the CIFAR Synthetic Evidence Corpus, a dataset designed to enable rigorous evaluation of evidence verification under realistic and controlled conditions. The corpus spans multiple document families and a spectrum of manipulation strategies, from small field-level edits to complete document fabrication, and is constructed using a diverse set of state-of-the-art generative tools. It is organized to systematically vary both manipulation complexity and generation method, while enforcing source-level separation between training and test data to reflect real-world generalization challenges.

---


### 109. [LEGS: Laplacian-Enhanced Gaussian Splatting with a Nonlinear Weighted Loss](https://arxiv.org/abs/2606.07932)

**<font color=#1a73e8>作者：</font>** Yongfei Guo, Qizhou Huo, Xuan Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has become an efficient explicit representation for radiance field reconstruction and real-time novel view synthesis. However, its standard photometric loss treats flat and structure-rich regions similarly, which may limit the recovery of sharp contours and fine details. Edge-Guided Gaussian Splatting (EGGS) improves structure awareness through edge-guided weighting, but mainly relies on first-order gradient responses and linear weighting. In this paper, we propose LEGS, a Laplacian-Enhanced Gaussian Splatting method with a nonlinearly weighted loss. LEGS replaces first-order gradient guidance with second-order Laplacian structural guidance and maps the normalized Laplacian response into pixel-wise weights through nonlinear response-to-weight functions. The proposed loss improves structure-aware Gaussian optimization while keeping the original 3DGS rendering pipeline unchanged. Experiments on the full Tanks\&Temples and Mip-NeRF360 datasets show that LEGS improves peak signal-to-noise ratio (PSNR) by up to 1.68 dB over 3DGS and up to 0.52 dB over EGGS. Incorporating the proposed second-order nonlinear weighting strategy into FastGS and FasterGS further improves PSNR by up to 1.69 dB, demonstrating its effectiveness as a general loss-level extension for Gaussian Splatting pipelines with potential applications in AR/VR, immersive visualization, and real-time 3D content generation.

---


### 110. [REACT 2026: The Fourth Multiple Appropriate Facial Reaction Generation Challenge: Personalised MAFRG and Appropriate EEG Reaction Prediction](https://arxiv.org/abs/2606.07935)

**<font color=#1a73e8>作者：</font>** Siyang Song, Micol Spitale, Zijian Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In dyadic interactions, various human facial reactions could be appropriate for responding to each human speaker behaviour. Following the successful organisation of the REACT 2023, 2024 and 2025 challenge series, a body of generative deep learning (DL) models have been developed for the problem of multiple appropriate facial reaction generation (MAFRG). This year, we propose the REACT 2026 challenge encouraging the development and benchmarking of Machine Learning (ML) models that can generate multiple personalised, appropriate, diverse, realistic and synchronised human-style facial reactions expressed by a specific human listener for responding to each given speaker behaviour. As a key of the challenge, we continuously provide challenge participants with MARS dataset introduced by REACT 2025 but additionally provide individual-level Big-Five personality labels and EEG recordings. This introduces a new one-to-many personalised facial reaction generation setting combining human expressive behavioural, affective and neurophysiological signals, which remains largely unexplored in current dyadic interaction modelling. This paper also presents the challenge guidelines and new baselines on the four proposed sub-challenges: Offline generic and personalised MAFRG as well as Online generic and personalised MAFRG, respectively, which are publicly available at this https URL.

---


### 111. [Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation](https://arxiv.org/abs/2606.07936)

**<font color=#1a73e8>作者：</font>** Katelyn Xiaoying Mei, Yi-Li Hsu, Minjoon Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human evaluation plays a critical role in assessing the quality of generated text. However, the reliability and reproducibility of these evaluations depend on transparent and well-documented protocols -- details that are frequently missing in current practice. In this work, we conduct a large-scale analysis of human evaluation protocols for evaluating long-form generation tasks in *CL conference publications from 2023--2025, including a full manual review of 284 papers and LLM-assisted analysis for another 1.8k+ papers. We define a set of 20 reportable criteria related to reproducibility of human evaluation studies, and apply these criteria to systematically examine reporting norms and practices within the community. We find widespread under-reporting of important aspects of human evaluation study design, leading to ambiguity about what was measured and how, who contributed judgments, and how judgments should be interpreted. Based on these findings, we outline actionable recommendations to support more transparent and reproducible reporting in future research. Our analysis code and annotated dataset can be found at: this https URL

---


### 112. [DAL-PCQA: Enabling Distortion-Level and Language-Driven Reasoning for Point Cloud Quality Assessment](https://arxiv.org/abs/2606.07938)

**<font color=#1a73e8>作者：</font>** Swarna Chakraborty, Gabriel De Castro Araújo, Syeda Tasmi Faria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point Cloud Quality Assessment (PCQA) methods typically predict scalar Mean Opinion Scores (MOS), which quantify overall perceptual degradation but do not reveal its causes. In contrast, human observers naturally reason in terms of specific distortions such as blur, color shifts, point density changes, missing regions, and geometric deformations. To close this gap, we introduce DAL-PCQA, a distortion-aware, language-annotated dataset for PCQA. DAL-PCQA augments benchmark point clouds with multi-level distortion severity labels, discrete quality categories, and structured natural language descriptions aligned with human perception. We define a point-cloud-specific distortion taxonomy that covers both photometric and geometric artifacts. Statistical analysis reveals characteristic degradation patterns across distortion types and quality levels. To assess the utility of these annotations, we compare zero-shot and fine-tuned multimodal models for generating perceptual quality descriptions. Experiments show that distortion-aware supervision substantially improves lexical and semantic alignment with ground-truth descriptions. By enabling interpretable, distortion-level reasoning, DAL-PCQA facilitates language-driven, explainable point cloud quality assessment. The dataset is publicly available at this https URL.

---


### 113. [EduMirror: Modeling Educational Social Dynamics with Value-driven Multi-agent Simulation](https://arxiv.org/abs/2606.07948)

**<font color=#1a73e8>作者：</font>** Jingzhe Lin, Hengbin Yu, Yongdan Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Understanding how educational social dynamics evolve is critical for informing effective educational policies and counterfactual interventions. However, traditional methods face a fundamental dilemma: observational studies often lack causal power, while controlled experiments are frequently constrained by ethical concerns. Although LLM-based multi-agent simulations offer a scalable in silico alternative, existing approaches remain limited by weak psychological grounding and insufficient measurement of latent psychological states. To address this, we introduce EduMirror, a multi-agent simulator for the scientific study of educational social dynamics. We provide configurable education-oriented agent forms, including value-driven agents grounded in psychological needs and social value orientation, together with a dual-track measurement protocol for quantifying observable behaviors and latent psychological states. We validate the realism and usability of EduMirror through case studies on school bullying and group cooperation, as well as broader evaluations across diverse educational scenarios. The results show that EduMirror generates educational social dynamics that are realistic, theory-consistent, and measurable by empirical criteria. These properties enable structured in silico educational research, providing a computational tool for hypothesis testing and counterfactual intervention analysis in educational science. Project page: this https URL.

---


### 114. [Demand-Driven Vulnerability Detection for Cloud Security Posture Management: Removing Human Rule Authoring from the Disclosure-to-Protection Critical Path](https://arxiv.org/abs/2606.07957)

**<font color=#1a73e8>作者：</font>** Prashant Kumar Pathak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud Security Posture Management (CSPM) systems detect known vulnerabilities by maintaining a rule set, distributing it to customers, and evaluating it against periodically-collected asset inventories. To our knowledge, in publicly documented architectures the rule set is environment-agnostic and curated centrally by the vendor; updates are batched into release cycles and shipped on a cadence ranging from hours to days depending on detection severity. The disclosure-to-protection window -- from a CVE being published to the customer's system being capable of detecting affected assets -- is therefore bounded by the vendor's release cadence for version-match detections, and by additional human authoring time for richer detections incorporating configuration predicates beyond the affected-software string. We propose an architecture in which the rule set is not vendor-distributed but continuously derived, within the customer's tenant, from the intersection of public catalogue feeds and the live asset graph. A rule comes into existence when a catalogue entry and an applicable asset are simultaneously present, and goes out of existence when either input ceases to support it. Derivation is bidirectional: new catalogue entries and new assets both trigger it. It incorporates the full structured-field content of catalogue entries, not only the affected-software predicate. The live rule set is bounded by environment diversity rather than catalogue breadth. Prior systems incrementally evaluate a static rule set; we incrementally derive the rule set itself. We present the threat model, the architecture, formal semantics with an equivalence theorem, complexity analysis, a worked example, and an evaluation methodology. The contribution is the architectural shift and its latency and resource consequences; rule correctness and alert prioritization are out of scope.

---


### 115. [What Does Debiasing Really Remove? A Geometric Study of PCA-Based Gender Debiasing in Word Embeddings](https://arxiv.org/abs/2606.07964)

**<font color=#1a73e8>作者：</font>** Alexey Kresin, Tchifou M. Dieffi, Tomer Caspi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Debiasing methods based on principal component analysis (PCA) are broadly used to reduce gender bias in word embeddings used in LLMs, yet it remains unclear what aspects of bias they actually remove and how destructive this process is. These methods are based on the understanding that bias resides in a low-dimensional subspace, with the assumption that most of it can be captured by a few principal components. In this work, we conduct a systematic geometric analysis of PCA-based gender debiasing and investigate what is actually removed from the embedding space. Our experiments across multiple embeddings show that direct gender bias is primarily concentrated in the first principal component, supporting the low-rank bias hypothesis. However, associative bias measured by WEAT does not align with these principal directions and is instead spread across multiple embedding dimensions. Furthermore, as expected, we demonstrate that removing an increasing number of principal components leads to a consistent degradation of the embedding geometry, affecting semantic structure and vector relationships. These results reveal that PCA-based debiasing operates as a trade-off: while it effectively reduces certain forms of direct bias, it fails to eliminate distributed associations and introduces geometric distortion. Moreover, there is no universal optimal level of debiasing, as the balance between bias reduction and semantic preservation depends on the chosen metric and embedding. Overall, our findings suggest that bias in word embeddings is not purely low-rank and that simple subspace removal methods may be insufficient for comprehensive debiasing.

---


### 116. [Zero-Shot Learning in Industrial Scenarios: New Large-Scale Benchmark, Challenges and Baseline](https://arxiv.org/abs/2606.07965)

**<font color=#1a73e8>作者：</font>** Zekai Zhang, Qinghui Chen, Maomao Xiong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Visual Language Models (LVLMs) have achieved remarkable success in vision tasks. However, the significant differences between industrial and natural scenes make applying LVLMs challenging. Existing LVLMs rely on user-provided prompts to segment objects. This often leads to suboptimal performance due to the inclusion of irrelevant pixels. In addition, the scarcity of data also makes the application of LVLMs in industrial scenarios remain unexplored. To fill this gap, this paper proposes an open industrial dataset and a Refined Text-Visual Prompt (RTVP) for zero-shot industrial defect detection. First, this paper constructs the Multi-Modal Industrial Open Dataset (MMIO) containing 80K+ samples. MMIO contains diverse industrial categories, including 6 super categories and 18 subcategories. MMIO is the first large-scale multi-scenes pre-training dataset for industrial zero-shot learning, and provides valuable training data for open models in future industrial scenarios. Based on MMIO, this paper provides a RTVP specifically for industrial zero-shot tasks. RTVP has two significant advantages: First, this paper designs an expert-guided large model domain adaptation mechanism and designs an industrial zero-shot method based on Mobile-SAM, which enhances the generalization ability of large models in industrial scenarios. Second, RTVP automatically generates visual prompts directly from images and considers text-visual prompt interactions ignored by previous LVLM, improving visual and textual content understanding. RTVP achieves SOTA with 42.2% and 24.7% AP in zero-shot and closed scenes of MMIO.

---


### 117. [Overcoming the Limits of Finite Difference Method; Physics-Informed Neural Network for Noisy High-Dimensional Heat Diffusion](https://arxiv.org/abs/2606.07982)

**<font color=#1a73e8>作者：</font>** Shreesh Bhattarai, Harish Chandra Bhandari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional transient heat diffusion under noisy boundary conditions exposes a fundamental limitation of classical numerical methods: accuracy degrades catastrophically where physical noise is unavoidable. This paper presents a Physics-Informed Neural Network (PINN) framework as a systematic solution to this problem across one, two, and three spatial dimensions, establishing clear operational regimes that redefine solver selection in noisy thermal systems. Under 20% boundary noise in 3D, PINN sustains approximately 91% accuracy while Finite Difference Method (FDM) collapses to 36%, a clear decisive advantage. This is further confirmed in a physical copper thermal system, where PINN reduces boundary reconstruction error by 3.3 times under realistic noise conditions. This noise resilience is accompanied by a dimensionality-driven efficiency crossover: PINN requires fewer spacetime nodes than FDM in 3D while achieving superior accuracy, exposing the true cost of classical discretization at scale. These findings reframe solver selection: the decisive axis is not accuracy alone, but noise exposure and dimensionality jointly. When noise and dimensionality are both high, the classical solver paradigm is insufficient; this work provides the foundation to justify PINN as the operational standard in such regimes.

---


### 118. [FMRFusion: Frequency-Aware Multi-View Representation Learning for Heterogeneous Image Fusion](https://arxiv.org/abs/2606.07985)

**<font color=#1a73e8>作者：</font>** Tao Zhoua, Yunlong Liu, Qinghui Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible image fusion aims to generate a composite image that retains significant target information and preserves detailed textures, integrating two heterogeneous modalities. Previous image fusion methods typically adopt a single-module stacking approach to extract features from the two modalities. However, these approaches may result in incomplete learning of their distinct characteristics, thereby limiting the fusion effectiveness and constrain ing robustness in real-world heterogeneous data scenarios. To address these challenges, we propose FMRFusion, a frequency-aware multi-view representation learning network for Heterogeneous Image Fusion. A Multi-Scale Struc tural Perception Module is introduced to effectively capture discriminative structures, extracting fine-grained local structures and essential contextual information. A bilinear frequency decomposition mechanism is employed to sepa rate features into high-frequency and low-frequency components, enabling joint modeling of local details and global representations across different frequency domains. Moreover, a Cross-View Complementary Interaction is incorpo rated to explicitly model and fuse the complementary characteristics between reflected light information and radiative intensity responses, facilitating effective cross-view interaction. We further improve the Performance of the fused results by flow matching, which progressively refines the fused features by learning the transformation from coarse data to high-quality representations. Extensive experiments conducted on multiple benchmark datasets demonstrate that FMRFusion achieves superior and consistent performance across a range of fusion tasks, especially in nighttime scenarios

---


### 119. [PAFO: Pareto Fairness Optimization for Personalized Reward Modeling](https://arxiv.org/abs/2606.07988)

**<font color=#1a73e8>作者：</font>** Xiaoyan Zhao, Haoting Ni, Yang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly rely on reward models to align their outputs with diverse user preferences. While personalized reward models aim to capture such heterogeneity, they are often trained on imbalanced user preference data and may therefore favor users whose preferences are more common in the training population. In this paper, we identify this failure mode as personalized reward bias, where reward modeling quality varies systematically with preference support rate. We formulate its mitigation as a Pareto fairness problem over group utilities, aiming to improve under-served users without degrading other user groups. To this end, we propose PAFO, a Pareto fairness optimization framework for personalized reward modeling. PAFO first trains group-specialized reward models for majority and minority preference groups, then constructs conditional margin-level supervision to distill their heterogeneous preference boundaries into a single unified model. The resulting model uses group information only during training and requires no explicit group labels at inference time. Experiments on Personal-LLM and DSP show that PAFO improves both minority-group and majority-group accuracy while reducing user-level unfairness across multiple metrics, demonstrating its effectiveness for fairer LLM personalization.

---


### 120. [Summarization is Not Dead Yet](https://arxiv.org/abs/2606.08000)

**<font color=#1a73e8>作者：</font>** Dongqi Liu, Chenxi Whitehouse, Zheng Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The progress of large language models (LLMs) has fueled claims that model-generated summaries rival or even surpass human-written references, raising questions about whether summarization remains an open research problem. We re-examine this narrative through a multi-track evaluation covering five diverse datasets and five state-of-the-art LLMs, combining controlled human assessment, bias-mitigated LLM-as-Judge protocols, factuality verification against external knowledge, and corpus-level linguistic analysis. Our findings reveal a more nuanced landscape in which human reference summaries continue to demonstrate advantages in informativeness and faithfulness, whereas LLM outputs are preferred mainly for surface-level coherence and fluency. Factuality verification indicates that human references remain more reliable, particularly for claims involving reasoning or synthesis, and linguistic analysis uncovers a pattern of stylistic homogeneity across different models. These observations suggest that current LLMs have raised the floor of summarization quality, but the ceiling of their performance remains below human capabilities.

---


### 121. [Learning a Semantic Calibration Network for Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2606.08001)

**<font color=#1a73e8>作者：</font>** Yang Sun, Tao Wang, Anastasia Ioannou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic image segmentation assigns a predefined category label to each pixel, has achieved significant progress lately. Open-Vocabulary Segmentation (OVS) extends the segmentation task from a fixed set to an open set, enabling the identification and segmentation of novel concepts based on arbitrary text inputs, such as category names or descriptions. In this paper, we propose a novel Semantic Calibration Network (SCN) for open-vocabulary semantic segmentation. Different from prior approaches that focus on feature aggregation or simple fine-tuning of pre-trained models, SCN refines the mask classification process by explicitly modeling the semantic correlations between classes, aiming to enhance the model's discriminative power while effectively preserving the generalization abilities of the pre-trained CLIP model. Specifically, SCN comprises two core components: Class Disambiguation (CD) and Logits Fusion (LF). First, a cross-attention mechanism is utilized to transform the text embeddings into visually aware pseudo-text embeddings, in order to derive an enhanced similarity score that complements the original mask-text similarity score. Subsequently, the Class Disambiguation module captures implicit inter-class dependencies through a residual architecture to effectively resolve semantic ambiguities. Finally, the Logits Fusion module dynamically integrates multifaceted semantic evidence to ensure that the model achieves a robust semantic consensus while maintaining CLIP's inherent generalization capability. Comprehensive experimental results on mainstream benchmarks demonstrate that the proposed method achieves significant performance improvements compared to state-of-the-art algorithms.

---


### 122. [Aqua Boundary-Saliency Attention Module for Lightweight Underwater Salient Instance Segmentation Detection Transformer](https://arxiv.org/abs/2606.08002)

**<font color=#1a73e8>作者：</font>** M. Fazri Nizar, Julian Supardi, Muhammad Naufal Rachmatullah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater instance segmentation integrates pixel-level mask prediction and instance-level discrimination for marine resource exploration, ecological monitoring, and underwater robotic perception. Recent prompt-based and auxiliary-modality methods improve mask quality, but their reliance on large foundation models, prompt generation, or extra modality estimation complicates efficient deployment. This work introduces Lightweight Underwater Salient Instance Segmentation Detection Transformer (LUSIS-DETR), a compact detection-transformer framework built around the Aqua Boundary-Saliency Attention Module (AquaBSAM). AquaBSAM embeds underwater boundary, contrast, attenuation, chroma, dark-channel, and center-prior cues into DINOv2-initialized multi-scale features through bounded residual modulation, while auxiliary mask supervision and small-object copy-paste are training-only. Extensive evaluation on four recent underwater instance segmentation datasets, UIIS, UIIS10K, USIS10K, and USIS16K, shows competitively leading performance against previous state-of-the-art works across category-aware and salient-instance protocols. TensorRT half-precision (FP16) benchmarking on an NVIDIA T4 graphics processing unit (GPU) achieves 4.31-6.34 milliseconds (ms) latency, supporting real-time inference under an accessible reproduction setting.

---


### 123. [Rewrite to Translate, Translate to Reward: Reinforcement Learning for Source Rewriting in Machine Translation](https://arxiv.org/abs/2606.08011)

**<font color=#1a73e8>作者：</font>** Boxuan Lyu, Haiyue Song, Zhi Qu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although directly prompting off-the-shelf Large Language Models (LLMs) to generate meaning-preserving source rewrites can effectively enhance Machine Translation (MT) quality, doing so requires manually tuning prompts for different MT models. In this work, we propose RLSR (Reinforcement Learning for Source Rewriting), a novel RL-based framework for training a source rewriting model without tuning prompts for each MT model. RLSR optimizes the rewriting model by directly using the improvement in downstream translation quality yielded by each rewritten source as the reward. Extensive experiments across six MT models and 16 language pairs demonstrate that our 4B rewriting models trained via RLSR significantly outperform the no-rewriting baseline and existing same-scale prompt-based rewriting baselines, while achieving competitive performance against prompt-based baselines based on the 235B LLM.

---


### 124. [The Dodona Protocol: A Living Design Science Experiment in Oracle Design](https://arxiv.org/abs/2606.08012)

**<font color=#1a73e8>作者：</font>** Giulio Caldarelli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The oracle problem, broadly understood as the difficulty of reliably incorporating external information into blockchain-based systems, has been widely examined by scholars and practitioners. Recent comparative research has shown that several challenges of modern blockchain oracles, including attributability, accountability, integrity, and query design, mirror procedural and epistemic constraints already present in ancient oracular institutions such as the Delphic Oracle. Yet the translation of these insights into applied oracle design remains largely unexplored. This paper introduces the Dodona Protocol, a modular, chain-agnostic oracle service inspired by procedural patterns identified in ancient and modern oracle systems. Named after the Oracle of Zeus at Dodona, one of the oldest oracular sanctuaries in ancient Greece, the protocol operationalizes principles such as structured consultation, access control, attributable resolution, constrained query formats, reputational accountability, and tiered service availability. Its first module implements a query and dispute resolution mechanism in which a named expert resolver provides binding answers to structured questions submitted by petitioners. The oracle does not claim to reveal objective truth; rather, it produces outcomes that parties have agreed in advance to accept. The paper presents the design rationale, architecture, and comparative positioning of the Dodona Protocol. It frames the protocol as a living research experiment within the Design Science Research tradition, where the deployed system functions as the research artifact and operational data support structured analysis, iterative refinement, and peer-reviewed dissemination. In doing so, the paper seeks to bridge the gap between oracle theory and oracle practice.

---


### 125. [Evaluating the Impact of Task Granularity on Catastrophic Forgetting in Continual Learning](https://arxiv.org/abs/2606.08013)

**<font color=#1a73e8>作者：</font>** Emre Alyamac, Himanshu Janmeda, Shashwat Krishna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting, the abrupt loss of previously acquired knowledge upon learning new information, remains the central challenge in Continual Learning. This project investigates whether the order in which a model learns information affects how well it retains knowledge. Specifically, we ask: does learning general categories first (like "animals" vs "vehicles") before learning specific classes (like "dog" vs "cat") reduce forgetting compared to learning all classes at once?
We test three approaches on CIFAR-100: (1) Coarse-to-Fine: train on 2 super-classes, then expand to 10 specific sub-classes, (2) Fine-to-Coarse: train on 10 sub-classes, then group into 2 super-classes, and (3) Flat: train on all 10 classes from the start. We use Elastic Weight Consolidation (EWC) to prevent forgetting during transitions. Our hypothesis is that learning general patterns first creates a stable foundation that helps the model retain knowledge when learning more detailed distinctions. We evaluate using standard metrics (accuracy, precision, recall, F1) plus continual learning metrics like backward transfer and forgetting rates. This work could inform how we design learning sequences for real-world systems that need to learn incrementally.

---


### 126. [GVC-Seg: Training-Free 3D Instance Segmentation via Geometric Visual Correspondence](https://arxiv.org/abs/2606.08014)

**<font color=#1a73e8>作者：</font>** Liang Xu, Fangjing Wang, Jinyu Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D instance segmentation in point cloud data is critical for machine vision applications. Recent advancements leverage multiple pre-trained foundation models to generate 3D proposals, followed by the application of proposal aggregation methods, which significantly enhance performance. However, they often produce sub-optimal results due to inherent variations in confidence levels across different segmentation models, resulting in a bias toward the model with higher confidence. This bias is inherently model-dependent and is influenced by factors such as data preprocessing techniques and training strategies. To address this bias, we propose a novel, training-free 3D instance segmentation approach via Geometric Visual Correspondence (GVC-Seg), which exploits the correspondence between 3D geometric cues and 2D visual cues to mitigate the confidence bias. Additionally, a 3D proposal generation module and a mask-aware CLIP feature extraction module are introduced during the instance mask generation and instance semantic reasoning, respectively. In this way, GVC-Seg enhances proposal quality assessment, ensuring unbiased ensemble learning across different models. Extensive experiments demonstrate that our method achieves state-of-the-art performance on several challenging benchmarks, while also exhibiting strong potential in open-vocabulary semantic segmentation settings.

---


### 127. [UniQL: Towards Dialect-Universal Benchmarking for Text-to-SQL](https://arxiv.org/abs/2606.08018)

**<font color=#1a73e8>作者：</font>** Jianling Gao, Chongyang Tao, Jiayuan Bai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing text-to-SQL benchmarks are largely centered on SQLite, making it difficult to evaluate whether models can generalize across heterogeneous SQL dialects. However, real-world database systems differ substantially in syntax, functions, type systems, and execution semantics, so the same natural language intent often requires dialect-specific SQL realizations. We introduce UniQL, a human-verified benchmark for cross-dialect text-to-SQL evaluation. UniQL aligns 1,534 natural language questions with executable SQL annotations across 16 SQL dialects, yielding 24,544 dialect-specific queries. All dialects share the same intents, aligned schemas and database contents, enabling controlled evaluation of dialect generalization. UniQL is constructed through a hybrid pipeline combining database migration, SQL translation, execution-guided verification, iterative rule summarization, and human validation. Experiments on both open-source and closed-source LLMs show that current models remain far from dialect-universal, with substantial performance variation across database systems and limited transfer from SQLite success to other dialects. These findings highlight the need for aligned cross-dialect benchmarks and more dialect-aware text-to-SQL methods. Code and data are available at this https URL

---


### 128. [Arabic Sentence Segmentation Across Genres and Punctuation Conditions](https://arxiv.org/abs/2606.08025)

**<font color=#1a73e8>作者：</font>** Mohammed Elkholy, Khalid N. Elmadani, Nizar Habash 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentence segmentation in Arabic is challenging due to ambiguous and inconsistent punctuation, with many texts lacking reliable sentence boundary markers. Existing approaches rely heavily on punctuation cues and are typically evaluated on well-formed text, limiting their robustness in realistic Arabic settings. To address this, we introduce AraSEG, a genre-diverse sentence segmentation corpus spanning eight genres and a wide range of punctuation and document structure conditions. Using AraSEG, we evaluate LLMs, lightweight encoder models, and dependency parser-based models under increasingly challenging segmentation settings. Our experiments show that lightweight encoders, and even dependency parser-based models, outperform LLMs in the most challenging settings. We further investigate the effects of training data size and genre diversity, finding that performance eventually saturates and cross-genre generalization remains challenging. We also demonstrate that accurate sentence segmentation substantially improves downstream dependency parsing. We make our code, data, and models publicly available.

---


### 129. [CausShield: Sample Reconstruction-Resilient Vertical FL via Causal Representation Learning](https://arxiv.org/abs/2606.08027)

**<font color=#1a73e8>作者：</font>** Yongqi Jiang, Yansong Gao, Siguang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vertical federated learning (VFL) is a distributed learning paradigm that leverages vertically partitioned features across isolated parties without sharing raw samples; however, it remains vulnerable to active sample reconstruction attacks. Existing defenses fail to achieve a satisfactory trade-off between model utility and privacy protection, due to either suppressing task-relevant information alongside privacy-sensitive features or relying on end-to-end supervised training to converge the defense module, which exposes the model to early-epoch vulnerability. To address this challenge, we adopt a structural causal model (SCM) insight and construct CausShield. From a task-learning standpoint, causal features within a raw sample are those that are directly relevant and contributory to the learning objective, whereas non-causal features are task-irrelevant but often encode sample-specific private information, thereby facilitating reconstruction. Importantly, we lay a theoretical foundation to prove this insight. CausShield thus decomposes the shared representations between the client and the coordinating server in VFL into task-relevant and task-irrelevant components to ensure full-cycle privacy protection. Nonetheless, the decomposition is inherently challenging due to the dual objectives of preserving model utility while mitigating privacy leakage. We address this via a carefully formulated optimization problem, which is solved through unsupervised representation learning. We further theoretically prove that CausShield preserves the convergence behavior of standard VFL. Extensive experiments compare CausShield against seven SOTAs, including InvL (USENIX Security'25), and evaluate robustness against advanced reconstruction attacks such as URVFL (NDSS'25). Results demonstrate that CausShield consistently outperforms in privacy protection, model utility, and computational efficiency.

---


### 130. [Noise-Adaptive High-Probability Regret Bounds for Online Convex Optimization](https://arxiv.org/abs/2606.08028)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Yutong Zhang, Wentao Mo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study high-probability regret bounds for online convex optimization (OCO) with strongly convex losses and establish three results that resolve open questions at the intersection of noise adaptivity, feedback structure, and constraint satisfaction. For the full-information setting with sub-Gaussian stochastic gradients, we prove a noise-adaptive high-probability regret bound in which the martingale deviation term scales with the noise level $\sigma$ rather than the gradient bound $G$, yielding a multiplicative improvement of $G/\sigma$ over the classical Azuma-Hoeffding baseline. Our analysis introduces an exponential supermartingale argument that bypasses the bounded-difference requirement of Freedman's inequality, enabling direct treatment of unbounded sub-Gaussian noise without truncation artifacts. For bandit feedback, we prove a minimax lower bound: the high-probability regret scales linearly in $\log(1/\delta)$, in contrast to the $\sqrt{\log(1/\delta)}$ confidence cost under full information. This constitutes a formal separation in the confidence cost of strongly convex OCO across feedback models. Regarding constrained OCO with stochastic constraints satisfying a Slater condition, we provide simultaneous high-probability guarantees for both cumulative regret and long-run constraint violation, achieving $\mathcal{O}(\sqrt{T\log(m/\delta)})$ regret and $\mathcal{O}(\sqrt{T}/(\zeta\delta) + m\sqrt{T\log(m/\delta)})$ violation. Synthetic experiments corroborate all theoretical predictions.

---


### 131. [Voting Protocols as Coordination Mechanisms for Role-Constrained Multi-Agent Tutoring Systems](https://arxiv.org/abs/2606.08030)

**<font color=#1a73e8>作者：</font>** Eric S. Qiu, Joyce Gill  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic tutoring systems introduce a coordination challenge: multiple agents may propose different but reasonable interventions, yet only one response can be delivered to the learner. In this paper, we study how voting protocols shape cooperation among four role-constrained pedagogical agents responsible for scaffolding, misconception, motivation, and metacognition. We compare four voting protocols -- simple, ranked, cumulative, and approval voting -- across two simulated tutoring environments on SciQ and HumanEval benchmarks. Rather than using voting as a simple aggregation step, we use it to analyze how collective decision rules shape coordination under partial pedagogical conflict. Across 1,200 simulated interactions, we find that agent deliberation and voting protocol type frequently change which response ultimately wins, showing that both meaningfully shape the collective decision. Different voting rules also produce distinct coordination behaviors, and even brief tutoring turns show measurable learning gains in simulated students. Overall, we show that protocol choice is associated with distinct coordination patterns among role-specialized pedagogical agents.

---


### 132. [Vision-Language Asymmetry in Bistable Image Captioning](https://arxiv.org/abs/2606.08031)

**<font color=#1a73e8>作者：</font>** Arohan Agate  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wittgenstein's duck-rabbit poses a question for vision-language models: when a model captions an ambiguous image, where in the model is the commitment to one aspect made? We address this with a 3,320-generation behavioral baseline over 83 bistable stimuli that surfaces three regimes (default-dominant, force-dominant, force-balanced) under neutral vs forced-choice prompting, then probe the underlying representations using a TopK sparse autoencoder we train on the CLIP layer that LLaVA-1.6-7B actually consumes (validation EV 0.93). Across 69 bistable stimuli with both per-aspect feature pools available, 72% (50/69) show simultaneous activation of both pools at the vision tower, including 12/12 default-dominant duck/rabbit and 7/8 force-balanced young/old. Causal steering at CLIP layer 22 flips captions on default-dominant stimuli (33% rabbit-flip rate under a fluency guard) but cannot flip captions on force-balanced young/old at any tested coefficient, despite their vision-side superposition. The dominance bottleneck lives downstream of the vision tower; the gap between vision-side representation and language-side commitment is an empirical handle on the seeing/seeing-as distinction. We also flag a methodological note: rank-based statistics on TopK SAE outputs require tie-corrected ranking to avoid silent row-order bias.

---


### 133. [Balancing Real and Synthetic Data for CNN-based Masonry Crack Detection](https://arxiv.org/abs/2606.08033)

**<font color=#1a73e8>作者：</font>** Mattia Forlesi, Alfonso Esposito, Ivan Zyrianoff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cracks are a critical indicator of building health, and early stage identification is fundamental to prevent harmful damages. Advances in deep learning (DL), particularly convolutional neural networks (CNNs), have enabled scalable solutions for automated crack detection. However, CNN performance strongly depends on the availability of large and diverse datasets, which is particularly challenging for complex surfaces such as masonry. Collecting sufficient real data is time-consuming, while publicly available datasets may not be adequate. To address this limitation, we explored generating synthetic crack data, which complements real data and improves training effectiveness. The real dataset consists of masonry crack images collected from buildings in Bologna and surrounding areas. In contrast, the synthetic dataset was generated using a crack overlay tool that adds cracks to background images in a controlled orientation and placement. The real dataset was used to train several DL architectures, to identify the best-performing model (InceptionV4) employed for experiments with generated data. Six training scenarios were tested in InceptionV4 by varying the ratio of real and synthetic data, with evaluation performed on a test set composed of real images using the F1-score and mean Intersection over Union (mIoU) metrics. Results show that training on synthetic data plus a modest addition of 20% real data achieves results comparable to training on real data only. Moreover, the 20/80 scenario (synthetic/real) achieved an 76% F1-score and 80% mean IoU, outperforming the real-only case. As can be seen, the method demonstrates the potential of synthetic data to reduce collection efforts while enhancing crack detection accuracy.

---


### 134. [Sci-Rho: A Multilingual Visually-Grounded Symbolic Benchmark for STEM Problems](https://arxiv.org/abs/2606.08034)

**<font color=#1a73e8>作者：</font>** Muhammad Falensi Azmi, Ikhlasul Akmal Hanif, Vallerie Alexandra Putra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Symbolic benchmarks have emerged as a key approach to assess model robustness under minor modifications to STEM-related questions. However, existing symbolic benchmarks mostly remain limited to mathematical reasoning, lack visual grounding, and are predominantly in English. In this work, we introduce Sci-Rho (Science Rhobustness), a dynamic benchmark for visually-grounded STEM problems spanning five subjects and seven languages, comprising 4,242 problem templates (606 per language) crafted by domain experts, including Olympiad medalists. Each template is implemented as executable Python code that generates diverse but equivalent problem instances by varying numerical values, visual patterns, geometric shapes, color schemes, and function types, resulting in 42,420 instances in total, each paired with reasoning steps and ground-truth solutions. We evaluated 17 state-of-the-art VLMs and discovered a noticeable gap between worst-case accuracy (defined as the proportion of problem templates that a model answers correctly across every generated variation) and average accuracy. We also discovered that smaller models show noticeable performance degradation across languages, whereas proprietary and larger models remain robust. Step-level evaluation reflects this same trend, revealing a significant gap between average F1 and worst-case F1 scores. Finally, our inspection of attention heads of a VLM reveals substantial cross-lingual variation in the relative attention allocated to image tokens compared to text tokens. Our work highlights the importance of evaluation beyond static benchmarks as a metric to measure the quality of VLMs.

---


### 135. [SafeECGMatch: Calibration-Aware Joint Frequency and Time Space Semi-Supervised Learning for Open-Set ECG Classification](https://arxiv.org/abs/2606.08037)

**<font color=#1a73e8>作者：</font>** Hongkyu Koh, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) classification models often suffer from severe label scarcity, making semi-supervised learning (SSL) an attractive strategy for reducing annotation costs. In clinical settings, however, unlabeled pools frequently contain out-of-distribution (OOD) anomalies or diagnostic groups absent from the labeled set. Standard SSL forces incorrect pseudo-labels onto these unseen classes, producing overconfident predictions. To address this, we propose SafeECGMatch, a calibration-aware safe SSL framework for single-label ECG classification under label distribution mismatch. Methodologically, SafeECGMatch employs a dual-branch architecture extracting time-frequency latent representations via ECG-specific augmentations. Crucially, it dynamically aligns confidence with empirical accuracy through adaptive label smoothing and temperature scaling, calibrating both the multiclass classifier and the OOD detector across temporal and spectral domains. This joint optimization allows trustworthy OOD rejection and reliable pseudo-labeling. Evaluated on the PTB-XL and PhysioNet/CinC Challenge benchmarks, SafeECGMatch achieves state-of-the-art accuracy and calibration, advancing reliable knowledge discovery in physiological time-series. Code is available at this https URL.

---


### 136. [OSMGraphCLIP: Learning Global Location Representations from OpenStreetMap Graphs](https://arxiv.org/abs/2606.08046)

**<font color=#1a73e8>作者：</font>** Dimitrios Michail, Eleni Saka, Ioannis Giannopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present OSMGraphCLIP, a CLIP-style geospatial representation model that learns global location embeddings from freely available OpenStreetMap (OSM) data. OSMGraphCLIP represents geographic environments as heterogeneous graphs of typed OSM features, preserving the topological and semantic relationships among roads, buildings, land-use regions, and points of interest. A multi-scale graph encoder captures both fine-grained local structure and broader landscape composition, and supervises a spherical-harmonics location encoder through a contrastive alignment objective. We evaluate OSMGraphCLIP across a diverse suite of downstream geospatial regression and classification tasks spanning climate, ecology, socioeconomic indicators, public health, land cover, biodiversity, and wildfire forecasting, and show that structured OSM data alone supports strong global location representations across domains. OSMGraphCLIP matches or exceeds satellite-based baselines on the majority of benchmarks, with the most pronounced advantage on socioeconomic and public-health tasks, where OSM's explicit semantic annotation of the built environment encodes patterns of human activity that satellite pixels can only capture indirectly. On ecological and environmental tasks, the model remains closely competitive with imagery-based methods despite using no Earth observation data. Qualitative analysis confirms that the learned embeddings organize geographic space coherently, recovering biome boundaries, urban gradients, and tropical--temperate distinctions from map topology alone.

---


### 137. [SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows](https://arxiv.org/abs/2606.08049)

**<font color=#1a73e8>作者：</font>** Amine El Hattami, Nicolas Chapados, Christopher Pal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly turn past experience into reusable artifacts such as code, workflows, and procedural memories. Reuse can improve efficiency, but it also creates a lifecycle reliability problem: artifacts that succeed once may fail under environment drift, underspecified tasks, or changing task distributions, especially in web automation. We introduce this http URL, a framework for governing reusable agent workflows with evidence-calibrated lifecycle policies. this http URL uses selective formalization: execution evidence decides which workflow steps should become executable code, which should remain natural-language guided, and when those choices should be revised. Workflows are stored as auditable, versioned notebooks that interleave natural-language guidance, multi-language executable cells, validation gates, fallback paths, and multimodal evidence such as outputs, screenshots, and error traces. At runtime, gate-conditioned execution lets each step run code when its gates validate, or fall back locally when drift invalidates the executable realization. On WebArena-Verified, this http URL achieves 53.7% single-round success, improving over the strongest baseline by 3.9 percentage points. Across three re-executions, it retains 91.7% of initially successful tasks, 15.5 points above the next best method. Under bounded repair, it recovers 72.9% of subsequent failures while limiting post-repair regressions to 4.2%, compared with 15.0% to 17.0% for persistent baselines. It also leads on Mind2Web cross-website and cross-domain splits. In a GitLab migration test, this http URL preserves performance when reusing frozen state learned on GitLab 15.7, with frozen-versus-fresh target-version gaps of -1.7 points on GitLab 16.11 and +0.6 points on GitLab 18.9. These results identify lifecycle governance and gate-conditioned execution as reliability axes beyond one-shot task success.

---


### 138. [What's the Point? Spatial Grammar & Index Resolution for Sign Language Processing](https://arxiv.org/abs/2606.08056)

**<font color=#1a73e8>作者：</font>** Oline Ranum, Simon Hadfield, Richard Bowden  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language models are predominantly trained with gloss-sequence or text supervision, thereby under-modeling non-lexical and productive constructions. One comparatively tractable instance is spatial indexing: pointing gestures that assign discourse entities to spatial loci for subsequent co-reference, which lexicon-centric objectives largely fail to capture. We present a targeted evaluation of indexing in Sign Language Recognition, showing that despite comprising 10-15% of signing content, indexing is poorly recovered. We introduce a framework for training and evaluating indexing experts, establishing a baseline for index-aware sign language modeling. Our approach decomposes spatial reference resolution into index detection and discourse entity linking. The resulting mention representations enable automatic annotation and non-lexical structure modeling, and serve as an auxiliary indexing expert that augments a frozen SLR model at inference time.

---


### 139. [Beyond Homophily: Towards Generalized Graph Reconstruction Attack and Defense](https://arxiv.org/abs/2606.08067)

**<font color=#1a73e8>作者：</font>** Zhanke Zhou, Bo Han, Xuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are widely deployed on relational data, yet they can leak sensitive or proprietary information about the training graph adjacency, e.g., social ties, transactions, and interactions. This work studies graph reconstruction attacks (GRA), a form of model inversion that reconstructs the training adjacency from a trained GNN, given different levels of attacker-side information. We first provide a systematic characterization of when and why adjacency becomes recoverable through features, labels, embeddings, and predictions, with leakage modulated by graph homophily, heterophily, and the model's inductive bias. Motivated by these findings, we view GNN inference through a Markov chain approximation lens, treating the layered forward computation as a chain of topology-dependent representations. Building on this view, we develop complementary attack and defense methods. On the attack side, we propose MC-GRA (+), which reconstructs the adjacency by optimizing a surrogate adjacency whose GNN-induced representations align with those of the target model at each layer. On the defense side, we propose MC-GPB (+), which suppresses adjacency-dependent information throughout the representation chain while aiming to preserve classification accuracy under a privacy-utility trade-off. Experiments across homophilic/heterophilic graph benchmarks and GNNs show that our attacks improve reconstruction fidelity over prior methods, while our defenses reduce reconstruction success with only minor accuracy loss.

---


### 140. [Support Vector Rubrics: Closing the Gap Between Self-Generated and Human Rubrics](https://arxiv.org/abs/2606.08077)

**<font color=#1a73e8>作者：</font>** Mengyuan Sun, Yu Li, Zhuohao Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluation is a promising paradigm for judging large language model (LLM) outputs, yet self-generated rubrics lag human-annotated criteria on hard instances. We argue this discriminative gap reflects an objective mismatch: self-generated rubrics describe good responses, whereas effective criteria must discriminate between close candidates. To close this gap, we introduce SVR (Support Vector Rubrics), a framework that recasts rubric construction as max-margin boundary learning over preference data. SVR mines contrastive features from preference pairs into a rubric bank, learns a prompt-conditioned selector together with global rubric weights, and iteratively refines the bank through support-pair selection and adversarial probing of hard negatives. At inference, given only the prompt, SVR retrieves the top-rubrics from the bank and scores responses. On RubricBench, SVR narrows the gap to human reference rubrics from 24.1 to 0.3 points and outperforms strong self-rubric and judge baselines, and the learned bank transfers across judges without retraining. On RewardBench 1&2, and RM-Bench, it remains competitive with dedicated reward models, demonstrating broader reward modeling capability. Overall, boundary-defining rubrics offer a principled route to closing the discriminative gap in LLM evaluation.

---


### 141. [Constraint-Aware Optimization for Robust Protein Stability Prediction](https://arxiv.org/abs/2606.08100)

**<font color=#1a73e8>作者：</font>** A Shivram, Aneesh S. Chivukula, Manik Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal $\Delta\Delta G$ predictors integrating protein language models with inverse-folding representations achieve strong in-distribution accuracy on the Megascale dataset but exhibit limited robustness on out-of-distribution (OOD) proteins, persistent forward-reverse bias on paired-mutation benchmarks, and under-representation of rare stabilizing mutations. Existing approaches address these limitations primarily through additional architectural components, leaving optimization-level intervention comparatively underexplored. We introduce a constraint-aware optimization framework combining Balanced Mean Squared Error, a Siamese anti-symmetric regularizer, and a novel OOD-margin consistency loss on the per-position feature representation, requiring no architectural changes to the SPURS backbone. Across eleven benchmarks and three random seeds, the framework improves Spearman correlation on S669 from 0.486 to 0.540 ($\sigma=0.002$ across seeds), matching the published SPURS baseline (0.50) without architectural modification, and on S461 from 0.653 to 0.711, with consistent smaller gains on five additional OOD datasets. A controlled diagnostic on Ssym reveals that anti-symmetric training does not eliminate systematic forward-reverse bias, indicating that gains arise through implicit regularization rather than exact thermodynamic constraint enforcement.

---


### 142. [A Unifying View of Attention Sinks: Two Algorithms, Two Solutions](https://arxiv.org/abs/2606.08105)

**<font color=#1a73e8>作者：</font>** Lukas Fesser, Mozes Jacobs, Thomas Fel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When attention concentrates on a single token, a sink, what is the model actually computing? Attention sinks are ubiquitous in softmax transformers, yet this shared visual signature can hide fundamentally different algorithms. We show that visually similar sink patterns can reflect two distinct mechanisms: {i} adaptive nop, where a head suppresses its update by routing to a null token, and {ii} broadcast, where a sink aggregates and redistributes global information. In that case, sinks serve an analogous role: a safe destination when there is nothing useful to compute. Proposed interventions like gating or registers work because they implicitly target one or the other, revealing a duality between method and assumed mechanism: gating implicitly assumes nop; registers implicitly assume broadcast. Each mechanism leaves distinct traces (nop sinks exhibit negligible value norms; broadcast sinks induce low-rank outputs) which we formalize on synthetic tasks and use to derive practical diagnostics. Applied to pretrained vision transformers, these diagnostics reveal that both mechanisms exist at scale: sinks transition from CLS in early layers to patches in deeper layers, and concentrate in specialized heads. Strikingly, register tokens, designed for broadcast, are repurposed to also serve nop, confirming that neither intervention alone suffices. Combining gating with registers yields complementary gains in stability and performance. Overall, we find that the same attention pattern can reflect two very different computations and effective intervention requires first asking what the model is actually computing.

---


### 143. [PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents](https://arxiv.org/abs/2606.08106)

**<font color=#1a73e8>作者：</font>** Zayx Shawn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve by repeatedly proposing changes to their own prompts, skills, or workflows and keeping those that score higher on a small held-out set. Almost all effort has gone into the proposer that generates candidates; we argue the weak point is the acceptor, the rule that decides whether to commit a change. Applied hundreds of times against the same noisy dev estimate, the ubiquitous "keep it if the score went up" rule is uncontrolled adaptive multiple testing: the agent effectively p-hacks itself, accumulating false commits that make it churn and drift rather than improve.
We recast committing as a sequential hypothesis test and propose PACE (Paired Anytime-valid Commit Evaluation), a training-free, anytime-valid commit gate. Each candidate is compared to the incumbent on identical instances and committed only when a testing-by-betting e-process accumulates decisive evidence, stopping early to save evaluations and controlling each candidate's false-commit probability at a user-set level even under optional stopping (a per-decision guarantee).
On Qwen2.5 agents (0.5B-3B) self-evolving at the prompt level on GSM8K, SVAMP, and ARC-Challenge, greedy acceptance commits 30-42% false and 10-33% harmful edits when a genuine improvement is hidden among noisy proposals, while PACE commits the real one and essentially nothing else, matching greedy's held-out accuracy at sharply lower variance and about 18% lower evaluation cost. With no real gain available, greedy commits 13-21 spurious self-modifications per run (72-100% false) and degrades the most fragile agent by 4.9 points, while PACE holds at baseline. Reliability of self-evolution depends on the acceptor, not only on the proposer.

---


### 144. [Conditional Random Ordered Transport Spaces](https://arxiv.org/abs/2606.08113)

**<font color=#1a73e8>作者：</font>** Lei Luo, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A small Wasserstein distance does not certify that a transformation is admissible. In evidence-constrained, semantic, causal, physical, monotone, or risk-sensitive learning, one must ask not only how far two probability laws are, but whether mass has moved in a direction allowed by available information. We introduce conditional random ordered transport spaces (CROTS), a class of \(L^0\)-valued spaces of random probability measures equipped with a Wasserstein ambient metric, a closed stochastic order, hard and soft ordered transport discrepancies, and a conditional risk functional for evaluating order violation under an evidence sigma-field. The central object is an order-admissible transport geometry for random measure-valued dynamics, distinct from cone-valued metrics, ordered Kantorovich constructions, random Wasserstein spaces alone, and model-specific residuals for generative paths. We develop the foundations of CROTS as a space theory for reliable distributional learning. The results include well-posedness and duality for hard and soft ordered transport, soft-to-hard variational convergence, measurability and completeness of the random lifted space, reductions to classical Wasserstein and ordered geometries, ordered geodesics, constrained barycenters and projections, conditional risk-transport duality, and separation of order-violating distributions. The main stability theorem shows that random learning dynamics may converge in the ambient Wasserstein metric while its local admissibility leakage follows a separate conditional order-risk recursion. The resulting asymptotic order-risk floor provides a mathematical language for evidence overreach, ordered distribution shift, robustness failure, and admissible distributional dynamics.

---


### 145. [Policy Description Language for Authorization using Logic-Based Programming](https://arxiv.org/abs/2606.08119)

**<font color=#1a73e8>作者：</font>** Masaki Hashimoto, Mira Kim, Hidenori Tsuji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recently, with the impossibility of eradicating the vulnerabilities of information systems, we must prepare for the occurrence of the security incident by the multi-layer defense called the Defense-in-Depth strategy. In the multi-layer defense, it is important to authorize accesses in fine-grained granularity to compose each layer effectively, and many access control models are proposed to follow them. However, policy description languages proposed so far cannot express the models appropriately in proper granularity. In this paper, we propose a policy description language which can designate many kinds of conditions for access control, such as the dynamic status of an application process, as an element of decision data, and implement it in Datalog. Using the proposed language, we compose the policy of SELinux, which is a major implementation achieving the multi-layer defense, and we confirm the advantages of the proposed language by evaluating its validity and expressiveness.

---


### 146. [Trustworthy Visual Predicates for Robust Manipulation Understanding under Degradation](https://arxiv.org/abs/2606.08121)

**<font color=#1a73e8>作者：</font>** Fatemeh Ziaeetabar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manipulation understanding requires reliable relational evidence, such as contact, support, containment, motion coupling, grasp, release, and active-hand involvement. Although these visual predicates are widely used in event-chain, graph-based, and neuro-symbolic models, their reliability under visual degradation is rarely analyzed directly. This paper introduces a predicate-level reliability framework for robust manipulation understanding under blur, occlusion, illumination change, low resolution, frame dropping, and detection noise. The framework defines a structured predicate vocabulary, confidence-aware predicate estimation, and reliability metrics for predicate preservation, degradation sensitivity, temporal consistency, confidence-weighted stability, and downstream impact. Experiments on controlled manipulation videos and public egocentric or bimanual datasets, including VISOR/EPIC-KITCHENS, H2O, and ARCTIC, show that predicate failures are structured rather than uniform. Static spatial predicates remain comparatively robust, whereas contact-sensitive, dynamic, and derived predicates such as grasp and release are more fragile. Under severe degradation, detection noise, occlusion, and frame dropping cause the strongest reliability losses. Downstream analysis shows that degraded predicates reduce manipulation-understanding accuracy from 0.89 to 0.58, while removing confidence weighting under moderate degradation reduces accuracy from 0.74 to 0.64. These results show that predicate reliability provides a diagnostic layer between visual perception and structured manipulation reasoning.

---


### 147. [Human-Centered Benchmarking of Driver Monitoring Models](https://arxiv.org/abs/2606.08123)

**<font color=#1a73e8>作者：</font>** Ruben Dario Florez-Zela  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based driver monitoring systems are increasingly deployed in safety-critical intelligent transportation settings, yet they are almost always compared on classification accuracy alone. This paper argues that accuracy is insufficient to characterize a model's fitness for real-world deployment, and proposes the Human-Centered Benchmarking Framework (HCBF), which evaluates models across four dimensions: accuracy, explainability, efficiency, and robustness. The framework is applied to four representative lightweight architectures, MobileNetV3, ShuffleNetV2, EfficientNet-B0, and DeiT-Tiny, on the MRL Eye Dataset for eye-state classification. While the models are nearly indistinguishable on clean-set accuracy, each leads in exactly one dimension, and all four lie on the Pareto frontier. A Human-Centered Score computed under three deployment-oriented weighting scenarios ranks ShuffleNetV2 first throughout. However, this aggregate winner retains less than half of its performance under sensor noise and fails by classifying closed eyes as open, whereas the transformer remains robust. These findings show that aggregate ranking can mask dimension-specific vulnerabilities that are operationally decisive, underscoring the value of multi-dimensional, human-centered evaluation.

---


### 148. [One Stone, Three Birds: Self-adaptive Optimal Transport for Multi-VLM Selection, Adaptation, and Ensembling](https://arxiv.org/abs/2606.08126)

**<font color=#1a73e8>作者：</font>** Qiyu Xu, Zhanxuan Hu, Yu Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) enable visual recognition from semantic class descriptions, which makes them attractive when target annotations are scarce or unavailable. Most deployment pipelines, however, first choose a single VLM and then adapt that model to the unlabeled target set. This single-backbone paradigm hides a critical assumption: the selected VLM is already compatible with the target domain. In realistic cross-domain deployment, several general-purpose and domain-specialized VLMs may be plausible, yet no instance-level target labels are available to identify the reliable ones. Deployment therefore requires a coupled solution for model selection, target adaptation, and prediction integration. We revisit this problem from a system-level multi-VLM perspective. Our central observation is that the three decisions above depend on the same latent object: a trustworthy sample-class structure in the target set. Different VLMs may encode different transfer biases and produce conflicting predictions, but their outputs can still provide complementary evidence for estimating this structure. We propose One Stone, Three Birds, a training-free framework based on self-adaptive optimal transport. Given a pool of frozen candidate VLMs, OSTB estimates a consensus sample-to-class transport plan without updating VLM parameters. The learned transport structure is then reused for all deployment objectives: model selection is performed by ranking the combined semantic and visual reliability induced by the consensus plan; target adaptation is obtained by fitting transport-conditioned visual classifiers; and ensembling is implemented through reliability-aware probabilistic integration. Extensive experiments on natural-image, remote-sensing, and medical-pathology benchmarks show that OSTB improves model ranking, adaptation stability, and ensemble robustness under heterogeneous candidate pools.

---


### 149. [How to be Non-Human : A Thematic Analysis of Animal Embodiment in VR Games](https://arxiv.org/abs/2606.08130)

**<font color=#1a73e8>作者：</font>** Siqi Yu, Shuai Liu, Yiqing Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study employs a reflexive thematic analysis to systematically examine the design patterns of 48 first-person Virtual reality (VR) animal avatar games. The research identifies four primary design themes: Animal Biomimicry, Limited Animal Simulation, Hybrid HumanAnimal Features, and Human Behavior with Animal Avatar. The analysis reveals that approximately 77 percent of the games remain grounded in human-centered interaction logic, with animal forms primarily serving as visual representations. The study highlights the core tension between authenticity and usability in current VR animal avatar design, and points toward design opportunities for achieving more authentic animal avatar's interactive experience through directions such as controller innovation, unconventional body mapping, and dynamic feedback. This research provides a thematic classification framework for understanding the representation of non-human perspectives in VR games.

---


### 150. [Phase Marginalization for Patch-Grid Instability in Vision Transformers](https://arxiv.org/abs/2606.08132)

**<font color=#1a73e8>作者：</font>** Oğuzhan Ercan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers operate on fixed patch grids, which can introduce phase-dependent instability for dense prediction: changing the patch partition can change the token evidence available to a pixel, especially near boundaries. We formalize patch-grid phase as a nuisance variable and propose Phase Marginalization, a post-hoc marginalization method that evaluates structured patch-grid phases, inverse-aligns dense outputs, and aggregates them in the original image coordinate system. The central variant, Uniform Phase Marginalization with K = 4, is training-free and improves over the canonical K = 1 baseline across measured segmentation, depth, and local matching settings. In a controlled Cityscapes experiment, Uniform Phase Marginalization provides a modest compute-matched advantage over generic shift-based four-forward test-time augmentation (TTA) (+0.31 mean Intersection-over-Union over the strongest tested generic row). A scaling study further shows that K = 4 is a practical cost-accuracy trade-off: K = 8 is essentially unchanged and K = 16 adds little accuracy at much higher latency. These results position patch-grid phase as a measurable nuisance variable and Phase Marginalization as a simple diagnostic and post-hoc marginalization baseline for dense ViT prediction.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
