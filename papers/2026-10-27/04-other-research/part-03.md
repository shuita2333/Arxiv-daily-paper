# 📦 其他研究 | 2026年10月27日

> 本类共 **198** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-198](./part-04.md)

---

### 101. [FOCUS: A Lightweight Mamba-2 Model for EEG-Based Cognitive Workload Classification](https://arxiv.org/abs/2610.32361)

**<font color=#1a73e8>作者：</font>** Ioannis Kyprakis, Stefanos Gkikas, Chariklia Chatzaki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive workload estimation from physiological signals is increasingly relevant in high-risk environments, where continuous and unobtrusive monitoring can inform adaptive systems and safety interventions. This paper presents FOCUS (Frequency-band Optimized Cognitive-load Ultralight SSM), a compact Mamba-2-based model for EEG-based binary workload classification under constrained data conditions. Rather than learning frequency sensitivity from data, FOCUS encodes preprocessed multi-channel EEG using a fixed FFT decomposition that covers the five canonical EEG bands. The proposed model combines depthwise-separable convolution and a weight-shared encoder-bottleneck Mamba-2 pair, with 0.04 million parameters and 0.11 GFLOPs. Evaluated in a pilot study with 11 participants under leave-one-subject-out cross-validation across three cognitively distinct tasks, FOCUS achieves 74.75% accuracy on the full dataset at 0.08 ms GPU model-forward latency. In the weight-sharing ablation, the shared configuration achieves 4.55 percentage points higher accuracy on the full dataset than the non-shared variant while reducing the SSM parameter budget; however, this difference does not reach statistical significance under a two-sided Wilcoxon signed-rank test ($p=0.083$). Overall, the selected FOCUS configuration provides a favorable trade-off between classification performance and computational cost within this controlled pilot setting.

---


### 102. [Detection and Validation of Hidden Subgroup Disparities in Clinical AI](https://arxiv.org/abs/2610.32362)

**<font color=#1a73e8>作者：</font>** Alceu Bissoto, Trung-Dung Hoang, Tim Flühmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) models used in clinical workflows often perform systematically differently across patient groups, raising concerns about equity and patient safety. Traditional subgroup analyses can expose such disparities only when rich metadata (e.g., patient demographics) is available and captures the sources of performance variation, conditions rarely met in practice. Algorithmic subgroup discovery methods offer a solution by identifying coherent groups from learned feature representations, but because true underlying stratifications are unknown, these methods are hard to evaluate. As a result, subgroup discovery has not been systematically applied or assessed for performance monitoring. Our main objective is to evaluate algorithmic subgroup discovery for performance monitoring, assessing the discovered subgroups' performance gaps and semantic coherence. Investigating cardiomegaly classification in a dataset of 223,228 chest X-rays, we showed that the discovered subgroups exhibited larger performance gaps (accuracies of 0.61-0.90) than traditional metadata-based analysis (0.80-0.94) and were frequently interpretable using patient, acquisition, and model metadata. As a proof of concept, we also showed that annotations from learned subgroups can be used to mitigate the biases they expose. We conclude that subgroup discovery is a practical and effective tool to enhance the performance validation and monitoring of ML systems in healthcare.

---


### 103. [A Regularity Condition Under Which a CPAB Transformation is a Diffeomorphism](https://arxiv.org/abs/2610.32369)

**<font color=#1a73e8>作者：</font>** Amit Aflalo, Oren Freifeld  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous Piecewise-Affine Based (CPAB) transformations, introduced by Freifeld et al. (2015, 2017), are flows obtained by integrating continuous piecewise-affine (CPA) velocity fields. These expressive transformations have proven useful in applications including nonlinear temporal warping and trainable activation functions in 1D, as well as nonrigid spatial deformations in 2D and 3D. While computational costs were not an issue in 1D, they originally limited the practical expressiveness of CPAB transformations in higher dimensions, especially in 3D. Our recent work (Aflalo et al., 2026) removed this bottleneck, enabling efficient optimization with much finer tessellations and substantially greater expressiveness. There is, however, a mathematical subtlety that was overlooked in the original CPAB papers (Freifeld et al., 2015, 2017). CPAB transformations are always bi-Lipschitz homeomorphisms, implying that both the transformations and their inverses are differentiable almost everywhere. They are not, however, necessarily diffeomorphisms. This note remedies the omission by identifying sufficient regularity conditions under which a CPAB transformation is guaranteed to be a diffeomorphism. We explain how differentiability can fail and how the proposed conditions prevent this failure. In 1D and 2D, we show that these conditions can be easily enforced and, for commonly used tessellations, hold with probability one under standard sampling assumptions. We expect analogous behavior in 3D.

---


### 104. [Past as State, Present as Attention: Persistent-State Blockwise Flow Matching for Long-Horizon Co-Speech Motion Generation](https://arxiv.org/abs/2610.32373)

**<font color=#1a73e8>作者：</font>** Yi Liu, Xiangyue Zhang, Jianfang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-speech motion generation remains challenging over long horizons due to the need for temporal coherence and consistent style. Existing methods typically generate long motions segment by segment, either conditioning on a short seed of recent frames, which gradually drifts, or retaining ever-longer explicit histories, which are costly to maintain and hard to learn from limited data. We trace these limitations to a key asymmetry between past and present: past motion carries slowly varying style that should be compactly summarized, whereas the current segment exhibits fast-changing local dynamics that require fine-grained modeling. This asymmetry motivates a simple Past-As-State, Present-as-Attention principle for long-horizon co-speech motion generation. Following this principle, we propose PASPA, which summarizes past history with an inter-block persistent state and models the current segment with intra-block bidirectional self-attention. We instantiate PASPA within a blockwise flow matching framework, with multi-block supervision for effective training over variable histories, prefill-decode state caching for efficient rollout, and hybrid classifier-free guidance for enhanced history and speech conditioning. Extensive public-benchmark experiments show that PASPA achieves state-of-the-art FGD performance and preserves motion style across long-sequence generation.

---


### 105. [EigenGradCAM with AugSmooth: Enhancing Explainability and Precision in Multi-Stage Alzheimer's Disease Detection](https://arxiv.org/abs/2610.32374)

**<font color=#1a73e8>作者：</font>** Arsham Azam, Sagar Ashraf, Tayyaba Farhat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) is a progressive neurological disorder associated with memory loss, cognitive decline, and behavioral disturbances. Early and accurate diagnosis is essential, yet MRI-based deep learning models often lack interpretability, limiting their clinical use. This study presents an explainable deep learning approach for four-class AD staging using 2D axial MRI images. The method combines eigenvector-based Grad-CAM with gradient smoothing to improve saliency localization and heatmap stability. Principal component analysis is applied to gradient-weighted convolutional layers, while Gaussian noise is added to saliency weights before decomposition. To address class imbalance in the Moderate Dementia category, Wasserstein Generative Adversarial Network with Gradient Penalty (WGAN-GP) generates synthetic samples to balance the four-stage training distribution. Custom convolutional neural networks are trained on the Best Alzheimer MRI Dataset, achieving 97.2% test accuracy, 97.0% balanced accuracy, and a Matthews correlation coefficient of 0.944. The area under the ROC curve ranges from 0.96 to 0.99 across classes. Generated heatmaps highlight the hippocampus and entorhinal cortex, regions associated with Alzheimer's disease biomarkers. These findings suggest that the proposed approach combines strong classification performance with improved model interpretability, although further clinical validation is needed.

---


### 106. [Sam-Correction: Fully Adaptive Label Noise Reduction for Medical Image Segmentation](https://arxiv.org/abs/2610.32377)

**<font color=#1a73e8>作者：</font>** Takuro Shimaya, Masahiro Saiko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quality of the teacher label has a dramatic impact on the outcome of the machine learning process. Medical image segmentation often suffers from a noisy ground truth (GT) mask due to difficulties in consistent annotation. Although a recent study has proposed a promising method to curate the noisy GT mask, this requires additional well-curated GT masks that are not always accessible without the aid of multiple medical experts. As an alternative, we propose SAM-Correction, which utilizes a foundation model to correct the noisy GT mask in a fully adaptive manner instead of manually preparing well-curated masks. In our approach, we progressively mitigate label noise via the segment anything model (SAM), where prompts are given from another segmentation network that we train concurrently. Experiments with various types of label noise derived from actual human annotations demonstrate that SAM-C achieves precise noise reduction and high-performing segmentation models trained thereby. Our method paves the way for robust model training even when clean labels are entirely unavailable.

---


### 107. [UniWorld: A Unified World Model for Real-Time Visual World Simulation](https://arxiv.org/abs/2610.32381)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Yabo Chen, Shuaiwei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous visual world simulation requires coupling evolving scene geometry with temporally persistent appearance. We present UniWorld, a unified framework that integrates depth trajectories and reference appearance within a shared video generation model. The central design maintains visual and geometric histories on a common timeline. Noise-aligned overlapping continuation places generated history at the prescribed sampling noise level and commits only newly generated latents. Rolling depth latent state preserves the corresponding geometric controls, incrementally reads newly available geometry, and keeps the conditioning fixed within each sampling window. Together, these mechanisms ensure exact preservation of latent history while bounding the active depth state by the window size. We evaluate continuous generation, paired history interventions, and long-horizon behavior across diverse scene categories. The same generator supports estimated, native, and on-demand simulator depth, while cached and incremental execution paths produce bitwise-identical outputs. Appearance changes and geometric control branches operate through the same interface without modifying committed history. The measured steady-state DiT execution path achieves real-time generation throughput, demonstrating the efficiency of UniWorld for continuous visual world simulation.

---


### 108. [PASTA: Prompt-Aware Annealed Diffusion Sampling](https://arxiv.org/abs/2610.32390)

**<font color=#1a73e8>作者：</font>** Ren Ajiki, Ryugo Morita, Stanislav Frolov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Diffusion models produce high-quality images, real-world visual design requires intentionally preserving clean regions for headlines, logos, or UI elements. Existing layout-aware text-to-image methods struggle to strictly preserve reserved regions, often introducing unwanted content that complicates downstream editing. Existing approaches either manipulate attention to displace content or suppress conditioning via noise-level interventions. However, these methods sacrifice visual coherence, producing flat regions or noticeable style inconsistencies between reserved and non-reserved areas. To address this limitation, we propose a Prompt-Aware Shared-Latent Training-Free Annealed Diffusion Sampling (PASTA), a training-free framework that enforces reserved-region constraints by selectively applying semantic guidance to object-allowed regions during sampling. PASTA operates on a shared latent trajectory, where full-prompt and context-prompt guidance are fused through mask-guided sampling. An annealed schedule suppresses semantic leakage during early denoising stages while gradually restoring visual consistency in later stages. Extensive experiments demonstrate that PASTA improves reserved-region fidelity while preserving overall image realism and perceptual consistency.

---


### 109. [Interactive image diagnosis using test-time backpropagation from the auxiliary task](https://arxiv.org/abs/2610.32396)

**<font color=#1a73e8>作者：</font>** Takuro Shimaya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task deep learning has been developed to ensure explainability in computer-aided diagnosis (CAD) systems. These systems simultaneously predict interpretable characteristics of findings in auxiliary tasks to help radiologists assess the reliability of the diagnostic prediction. However, the CAD's opinion would not be referred to when the auxiliary task prediction deviates from the radiologist's expectation. To further leverage CAD's knowledge in the above situation, we proposed a multi-task gradient assist (MGA) method that brings interactivity to multi-task models without additional training. MGA allows radiologists to give feedback to the CAD and ask for additional diagnostic suggestions. Using two datasets of mammography and CT, we show that MGA successfully improves diagnostic accuracy upon feedback on various auxiliary tasks. Compared to an existing method using forward propagation only, MGA performs more robustly and can be combined to further improve accuracy. Our method paves a promising way for integrating artificial intelligence into image diagnosis.

---


### 110. [An Error Budget for Shuffled Multimodal Windows in the 3rd WEAR Challenge: Stacking, Count Constraints and Seam Matching](https://arxiv.org/abs/2610.32398)

**<font color=#1a73e8>作者：</font>** Soheil Kooklan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 3rd WEAR Dataset Challenge asks for an activity label for every one-second window of four unseen participants. Each window has 15 VideoMAEv2 frame embeddings, the accelerometer signal of one random limb, and the windows are shuffled. This report is an empirical analysis of one system built after the challenge deadline. Window classifiers are stacked with features averaged over per-participant graphs of video neighbours and scored successor candidates, and a mean-field style decoder with a soft count constraint per activity labels all windows of a participant together. The setting is offline and transductive, and the count constraint relies on each activity being performed once. In a participant-wise simulation with participant-level bootstrap intervals, stacking added 0.051 macro F1 over stage-1 fusion and the count constraint 0.011 (95% interval 0.006 to 0.017). A quadratic seam distance ranks the true same-limb successor first among about 720 candidates in 83.9% of cases, but adding it to the link model changed macro F1 by -0.0001 (-0.0006 to 0.0005). With the decoder settings and the mixing weight chosen inside the folds and the mislabelled spans left out of training, the system scores 0.936 in simulation (0.940 for participants who performed each activity once); the submitted configuration scores 0.938 (0.943). Per-participant scores range from 0.80 to 0.97. These results come from a non-nested stacking protocol that uses unlabelled features transductively, so they are not a fully inductive estimate. An oracle that averages the final unary scores over the true segments reaches 0.973, and 79% of the remaining errors involve the null class. On the private leaderboard, which no choice used, the selected Kaggle submission scored 0.9231 (public 0.9254, with bounds partly tuned there), and a later one with bounds chosen in simulation scored 0.9247 (public 0.9253).

---


### 111. [TIE: Training-free CLIP Embedding Guidance for Compositional Text-to-Image Alignment](https://arxiv.org/abs/2610.32407)

**<font color=#1a73e8>作者：</font>** Sujung Hong, Tae Eun Choi, Youngjun Jun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) diffusion models have advanced notably, but still fail to satisfy prompt conditions, resulting in attribute mismatches and missing objects. These errors normally fall into two categories: concept loss, when an object or attribute (i.e., concept) goes missing, and concept confusion, when an attribute is assigned to the wrong object or multiple objects blend together. Recent studies suggest that these challenges are caused by the limited capacity of CLIP text encoder to capture fine-grained semantic details. Although several methods have been proposed, concept loss and concept confusion persist in recent T2I models when handling multi-object, multi-attribute prompts. In this paper, we conduct an embedding-level analysis to develop a training-free, inference-time solution for concept loss and concept confusion across CLIP-based T2I models. We find that (1) concepts mentioned later exhibit higher embedding entropy, reflecting less concentrated representations that are more often associated with concept loss, and (2) the first CLIP attention layer captures the strength of binding between each object and its attribute. Guided by our findings, we introduce TIE, a method that improves semantic alignment through a single text-embedding update. TIE addresses concept loss via entropy-aware singular value amplification and resolves concept confusion through interpolation-extrapolation binding based on CLIP attention scores, all in a training-free manner. Extensive experiments demonstrate that TIE enhances semantic fidelity in multi-concept scenarios with minimal sampling overhead. The project page is available at this https URL.

---


### 112. [AlphaAnything: Extending Pretrained RGB Generators to RGBA](https://arxiv.org/abs/2610.32413)

**<font color=#1a73e8>作者：</font>** Qijie Wang, Zhixin Xu, Zhe Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing RGBA generation methods commonly learn a transparency-specific representation through reconstruction, introducing an additional training stage and potentially altering the RGB decoding function inherited from pretrained models. We present AlphaAnything, a lightweight framework that extends pretrained RGB generators to RGBA directly in their original latent space, without RGBA reconstruction pretraining. AlphaAnything inserts LoRA modules into the generative transformer and attaches an alpha branch to the frozen RGB VAE decoder. Unidirectional RGB-to-alpha feature sharing allows opacity supervision to shape the generative latent while guaranteeing that, for any fixed latent, RGB decoding remains identical to that of the pretrained decoder. We further introduce Endpoint-Aware Alpha Loss (EA Loss), which derives opacity supervision from the complementary foreground--background weights used in compositing. It supports exact opacity endpoints and continuous partial transparency while emphasizing localized alpha errors. Experiments on text-to-RGBA and image-to-RGBA tasks across multiple pretrained RGB backbones demonstrate competitive generation quality, and controlled ablations validate the shared-latent training design and EA Loss.

---


### 113. [When Does Dynamics Randomization Test Context Inference?](https://arxiv.org/abs/2610.32414)

**<font color=#1a73e8>作者：</font>** Oleg Smirnov, Sofiane Ennadir, John Pertoft 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Environments with randomized dynamics are widely used to ask whether world models need explicit context inference. However, randomization can leave little predictive information for a context encoder to add, because distinct latent parameters may produce similar transitions at visited states, or those states may already reveal the active context. We formalize the remaining one-step information as predictive headroom and compare kernels under fixed and visited state--action distributions to distinguish changes in query coverage from changes in context weights. We analyze discrete and continuous environments and find low headroom both when kernels differ little and when visitation reduces an otherwise large discrepancy. At the same time, resetting state components increases headroom, showing that context evidence accumulates in state. We propose reporting this headroom alongside the randomized parameters, so that gains from explicit context inference can be interpreted relative to the information missing from the current state and action.

---


### 114. [Tempo-Zero: Recursive Self-Play in Executable Worlds for Video Reasoning](https://arxiv.org/abs/2610.32433)

**<font color=#1a73e8>作者：</font>** Jingmin Zhu, Yanyan Zou, Xiuyu Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning requires understanding how events unfold over time, yet videos with accurate temporal annotations are expensive to collect. Self-play offers an alternative by letting a model generate and solve its own tasks without manual annotation. However, existing video self-play methods train on fixed sets of recorded videos, so they cannot alter the underlying event dynamics and rely on noisy pseudo-labels derived from the model's own outputs, such as majority voting, that risk reinforcing shared model errors. To overcome these limitations, we introduce Tempo-Zero, a self-improvement framework that closes a loop of executable environments, execution-verified self-play, and environment evolution, where executing a program renders a video with the ground-truth option and interval of every question. A single policy plays both Questioner and Solver, proposing questions and answering them with timestamped evidence lines, and is trained on execution-grounded rewards instead of model consensus. The Solver's performance steers a curriculum over tasks and difficulty levels, and the policy selects rule changes that enrich the event dynamics of later rounds. Despite being trained solely on simple programs, without supervised fine-tuning or external video data which prior methods typically require, Tempo-Zero outperforms the base models and recent self-play baselines on average across twelve real-world video benchmarks at different model scales, with particularly strong gains on temporal grounding tasks. Project page: this https URL

---


### 115. [Data Quality Audit and Bivariate Temperature-Humidity Analysis of a Long-Term LoRaWAN Network: Anomaly Detection, PCA, Clustering and Machine Learning](https://arxiv.org/abs/2610.32438)

**<font color=#1a73e8>作者：</font>** Mamadou Sow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term environmental IoT/LPWAN deployments often aggregate heterogeneous data streams from diverse devices without systematic auditing of each variable's actual coverage prior to analysis-an increased risk when multiple sensor types coexist within the same network. This work proposes a C++17 processing pipeline applied to the Tour Perret LoRaWAN dataset (421 937 frames, June 2021--June 2023, 5 devices). A systematic coverage audit integrated into the extraction phase reveals that CO2 is completely missing (0% coverage) and pressure is reported only by an isolated base module (Wyres, 4.24% of the corpus), invalidating the initial hypothesis of a joint four-variable analysis. The analysis is refocused on the Temperature--Humidity pair, jointly available across 205{,}005 frames (95.76%) from 4 Elsys EMS sensors. The pipeline sequentially performs anomaly detection (modified Z-score, Isolation Forest), bivariate Principal Component Analysis, clustering (K-means, DBSCAN), and a multilayer perceptron predicting humidity from temperature and time, whose residuals serve as a detector for slow drift. On real-world data: Temperature--Humidity correlation r=-0.662, two-component PCA (PC1 =83.1% of variance), Isolation Forest detects 2.12% multivariate anomalies while univariate Z-score detects none, calibrated DBSCAN isolates 0.17% noise across 13 clusters, and the MLP achieves $R^2=0.672$ (RMSE =10.54%) in cross-validation. This work demonstrates that per-variable coverage auditing prior to modeling is a necessary methodological step for heterogeneous multi-sensor IoT datasets.

---


### 116. [Learning Fine-Grained Visual Classification with Text as Privileged Information via Multimodal Distillation](https://arxiv.org/abs/2610.32442)

**<font color=#1a73e8>作者：</font>** Aishwarya Venkataramanan, Christian Ickler, Joachim Denzler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual classification (FGVC) requires distinguishing between highly similar categories by focusing on subtle, localized visual differences. Recent multimodal methods have demonstrated that textual attribute descriptions can provide valuable semantic supervision by explicitly describing discriminative object characteristics. However, these descriptions are typically unavailable at test time, limiting their direct use in deployment. We propose FG-LUPI, a Learning Using Privileged Information (LUPI)-based framework that leverages attribute descriptions during training. We train a multimodal teacher that integrates image patches and textual attributes via gated cross-attention, allowing semantic attributes to condition visual representations. We distill this knowledge into an image-only student using multi-level distillation at the prediction, patch, and attention levels, aligning global predictions, patch representations, and attention patterns with the teacher. This encourages the student to inherit attention structure learned from multimodal supervision while maintaining image-only inference. Experiments on multiple FGVC benchmarks show consistent improvements in classification accuracy over strong ViT-based baselines. Furthermore, evaluation using Expected Calibration Error (ECE) shows that FG-LUPI also produces better-calibrated predictions across all six benchmarks. These results suggest that textual attribute supervision can benefit not only fine-grained recognition performance but also the reliability of model confidence, while preserving the efficiency and practicality of image-only inference.

---


### 117. [DIGOM: Disentangled Interaction Graphs for Outcome prediction in Multimodal healthcare](https://arxiv.org/abs/2610.32451)

**<font color=#1a73e8>作者：</font>** Hakima Laribi, Olivier Lefebvre, Dan Poenaru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal healthcare data contain relational information that extends beyond individual patient observations. Effective clinical outcome prediction therefore requires not only integrating information from multiple modalities, but also modeling the relationships between them. Standard fusion approaches do not explicitly capture these interactions, while existing graph-based approaches typically model only a subset of them. We propose DIGOM (Disentangled Interaction Graphs for Outcome prediction in Multimodal healthcare), a graph-based framework that jointly models three complementary interaction types: Intra-patient cross-modal, Cross-patient same-modal, and Cross-patient cross-modal interactions. DIGOM learns a sparse multiplex graph with disentangled views, each encoding interactions between pairs of modalities across patients. Discrete adjacency matrices with patient-adaptive connectivity are sampled via a differentiable mechanism, enabling end-to-end learning and allowing the model to select informative relationships without imposing a fixed number of neighbors. A regularization objective maintains overall graph sparsity, while message passing integrates this relational context into patient representations for outcome prediction. We evaluate DIGOM on two multimodal healthcare datasets, MIMIC-IV and NIH-TB, across five clinical prediction tasks. DIGOM achieves the highest AUROC on all five tasks while using fewer connections than existing multi-interaction approaches. Ablation studies reveal that each interaction type's contribution varies across tasks, highlighting the need to adapt relational structures per task. DIGOM also demonstrates greater robustness to missing modalities, suggesting learned relationships provide complementary information when modalities are unavailable. Post-hoc analyses further reveal task- and outcome-specific connectivity patterns in the learned graphs.

---


### 118. [AutoMIL: Automated Multiple Instance Learning for Whole-Slide Image Classification](https://arxiv.org/abs/2610.32452)

**<font color=#1a73e8>作者：</font>** Jonas Waibel, Frank Kramer, Dominik Müller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing multiple instance learning pipelines for the classification of whole-slide images involves many interdependent design decisions and expertise in both pathology and machine learning. We present AutoMIL, an open-source framework that applies principles from the field of automated machine learning to tackle this task by automating integral pipeline steps, such as preprocessing, training and evaluation. In a benchmark evaluation with default settings, AutoMIL reached ROC-AUC scores of 0.94 on UBC-OCEAN, 0.99 on PCam and 0.93-0.96 on a TCGA-NSCLC subset, comparable to specialised pipelines in related work. Ensembling mainly improved performance on imbalanced data, showing that an automated pipeline must adapt to dataset characteristics. AutoMIL thus provides an accessible baseline for whole-slide image classification without manual pipeline configuration.

---


### 119. [Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation](https://arxiv.org/abs/2610.32453)

**<font color=#1a73e8>作者：</font>** Zifan Peng, Peng Huang, Jingyi Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents can inspect code and run tests to support smart contract security. SlowMist reports about $38.6 billion in losses across the broader blockchain ecosystem. Existing evaluations can reward memorized or copied answers, including attack code recovered from public blockchain transactions. Reconstructing contracts and validating tasks also require costly manual effort. To address these issues, we propose CONSTRAINTDIAL, a framework for lifelong construction of smart contract security tasks via protocol mutation. It automates local contract reconstruction and uses attack execution to select changes to the required calls or inputs. Execution checks guide revisions that make the original attack fail while preserving exploitability, the security objective, and normal functionality. New incidents and audit findings enter the same procedure. With CONSTRAINTDIAL, we construct 3,045 task inputs from 203 public cases, covering detect, exploit, and patch. Compared with reconstruction alone, protocol mutation reduces success with supplied public answers by 10.9 percentage points on average across detect, exploit, and patch. The fraction of tasks solved by copying online answers falls by 9.3 points.

---


### 120. [MDMR-Bench: A Multi-Dimensional Benchmark for Multi-Reference Image Generation](https://arxiv.org/abs/2610.32459)

**<font color=#1a73e8>作者：</font>** Bowen Zheng, Jintao Lin, Changheng Yi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image generation models have rapidly advanced, with many models now supporting generation conditioned on multiple reference images and textual instructions. Such models enable a wide range of applications, including entity fusion and attribute transfer across images. However, existing benchmarks for multi-reference image generation rely on limited evaluation dimensions and fail to capture the diverse challenges of the task. To address this limitation, we propose MDMR-Bench, a Multi-Dimensional benchmark for Multi-Reference image generation. MDMR-Bench is organized around representative capability settings and consists of multiple evaluation subsets spanning diverse dimensions of multi-reference image generation, including (1) common entity fusion and attribute transfer, (2) multi-element extraction from a single image, (3) infographic manipulation, and (4) visual reasoning-intensive generation. This design enables systematic analysis of model capabilities and failure modes across different challenge dimensions. Furthermore, to achieve more reliable and interpretable evaluation, we introduce a checklist-based evaluation protocol that decomposes generation quality into fine-grained evaluation aspects. Instead of relying solely on holistic scoring, our framework uses structured checklists composed of both global-level and atomic-level queries, enabling more diagnostic assessment of model performance. By benchmarking both open-source and proprietary models, we demonstrate that MDMR-Bench provides fine-grained insights into model performance across different dimensions. The dataset and code are publicly available.

---


### 121. [DualGSL: Prior-Guided Graph Structure Learning with Node-Adaptive Prediction Fusion](https://arxiv.org/abs/2610.32462)

**<font color=#1a73e8>作者：</font>** Yuxia Sun, Yutszyuk Wong, Huihong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph structure learning (GSL) adapts propagation graphs to prediction tasks, but the relative predictive value of feature-derived priors and learned relations can vary across nodes. We propose DualGSL, a prior-guided framework for transductive node classification that learns node-specific weights for combining predictions from separate prior and task-adaptive propagation paths. The prior branch augments a feature graph with virtual class nodes to incorporate training-label information, while the structural branch combines learned affinity graphs with the feature-graph prior. The two branches share encoder parameters while preserving distinct representations and classification logits. A node-adaptive gate fuses the branch logits based on their projected representations, element-wise absolute difference, and prediction confidence. A joint objective integrates fused and branch-specific classification losses with prior-branch class-anchor alignment, coordinating graph construction, representation learning, and prediction fusion. Experiments against seven baselines on the AMG18 malware attribution dataset and the widely used 20News text classification and USPS handwritten-digit recognition benchmarks show that DualGSL achieves the highest cross-dataset average accuracy and Macro-F1 among the evaluated methods. Ablation studies on AMG18 further demonstrate the benefit of combining prior and learned propagation through logit fusion.

---


### 122. [Online Continual Learning in Edge-Cloud Applications](https://arxiv.org/abs/2610.32472)

**<font color=#1a73e8>作者：</font>** Charalampos Davalas, Dimitrios Michail, Christos Diou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployed machine learning models in real-world IoT and edge/cloud systems face a critical reliability bottleneck: the requirement for online adaptation to non-stationary data streams while operating without access to the full original training dataset. Performance is severely degraded when models encounter Out-of-Distribution (OOD) inputs or suffer from catastrophic forgetting. Addressing these challenges requires adaptation mechanisms capable of learning from evolving data streams while preserving previously acquired knowledge. This paper proposes an edge-cloud methodology for integrating Continual Learning (CL) with Out-of-Distribution (OOD) Detection and Concept Drift Detection in IoT applications. The methodology incorporates ODIN and ECDD as alternative mechanisms for identifying informative samples for annotation and triggering rehearsal-based model updates. Experimental results across automotive, healthcare, and agricultural datasets demonstrate the applicability of the proposed methodology and its potential to support model adaptation while mitigating catastrophic forgetting.

---


### 123. [From Perception to Pixels: Human-Derived Visually Distinct Colors for Improved Dominant Color Extraction](https://arxiv.org/abs/2610.32473)

**<font color=#1a73e8>作者：</font>** Uldana Shyndali, Nurdaulet Toleugaliyev, Kuat Zharykbayev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dominant color extraction is a fundamental task in computer vision, with applications in design, image retrieval, and content recommendation. However, conventional algorithms based on device-oriented color spaces (e.g., RGB) and fixed quantization often fail to capture how humans perceive color differences. In this study, we propose a human-perception-based framework for dominant color extraction, built on a novel Human Color Dictionary (HCD) derived from a perceptual experiment. Participants (n=110) were sequentially shown 120 colors and asked to identify those they perceived as unique. Based on their responses, we constructed a 120 by 120 co-occurrence matrix and applied a greedy selection algorithm to derive 64 perceptually distinct colors, forming the HCD. This dictionary was integrated into RGB color histogram and K-means color extraction algorithms by initializing centroids and mapping pixel values to their nearest perceptual color using the deltaE 00 distance. Evaluation on a dataset of 4,562 images paired with expert-designed palettes demonstrated that our method improves perceptual alignment, as measured by Earth Mover's Distance (EMD) and best-match distance. Our findings suggest no meaningful gender differences in the number of uniquely perceived colors, indicating that sex does not significantly influence color perception in this task. Another key finding is that highly saturated colors are perceived as the most distinguishable, whereas dark and deep colors tend to perceptually collapse and are less reliably differentiated. The results confirm that incorporating experimentally derived human color representations ensures the generated color clusters align more closely with human perception, thus improving the usability of color palette generation in practical applications.

---


### 124. [A curated multi-endpoint drug-protein bioactivity dataset with construct-aware protein targets](https://arxiv.org/abs/2610.32490)

**<font color=#1a73e8>作者：</font>** Lina Abou-Abbas, Nour Mhanna, Hasan Bazzi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public drug-protein bioactivity resources commonly identify targets by UniProt accession, although one accession may represent distinct experimental sequences. We present Curate-DTI, a construct-aware dataset derived from the 1 July 2026 BindingDB export, with IC50, Ki, Kd and EC50 processed independently. The release contains 2,919,717 measurements, 1,291,872 standardized ligands, 9,668 sequence-defined protein entities and 2,275,683 endpoint-specific interactions spanning 8,336 reviewed UniProt accessions. Protein entities combine the accession with the reported experimental sequence, preserving constructs that accession-only processing would merge. Across the four endpoints, 4,204 endpoint-specific ligand-accession groups showed different classification labels across sequence-defined protein entities. Exact and inequality-qualified observations provide relation-aware classification evidence, whereas regression targets use exact values only. Connected Parquet tables preserve individual measurements, standardized structures, protein sequences, aggregated interactions and available assay and source provenance. The resource supports endpoint-specific classification and regression while allowing users to select molecular representations, protein representations and evaluation splits. Preprocessing code, a column dictionary, exclusion reports and validation summaries accompany the release.

---


### 125. [L0-Norm-Based CycleGAN for Unpaired Brain CT-to-MR Synthesis](https://arxiv.org/abs/2610.32491)

**<font color=#1a73e8>作者：</font>** Yunxiao Zhang, Shouqiang Du, Zexian Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) and magnetic resonance (MR) imaging provide complementary information for the brain, but acquiring both modalities is not always possible. The cycle-consistent adversarial network (CycleGAN) enables unpaired CT-to-MR synthesis, but because the standard L1-norm cycle?consistency penalty grows linearly with the residual magnitude, the network tends to focus on large residuals. This paper introduces an L0-norm-based cycle?consistency term, in which the L0-norm is approximated by a smooth and bounded function. This approximation not only increases sensitivity to small residuals but also effectively suppresses the influence of large residuals. The proposed model and an otherwise identical L1-norm baseline were trained on 102 images and evaluated on 9 test images. The proposed model achieves a lower mean squared error (0.02746 versus 0.03464, a 20.7% reduction), a higher mean peak signal-to-noise ratio (15.80 versus 14.77 dB), and a higher mean structural similarity index (0.5689 versus 0.5407). It also has a lower maximum MSE and higher minimum PSNR and SSIM than the baseline. These results indicate that modifying the cycle-consistency penalty can improve reconstruction accuracy on this dataset.

---


### 126. [K-CLUE: A Segmentation-to-Clustering Framework for Ki67 Cell Typing](https://arxiv.org/abs/2610.32493)

**<font color=#1a73e8>作者：</font>** Ana Beatriz Vieira, Sara P. Oliveira, Diana Montezuma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ki67 is a key marker of tumor proliferation in breast cancer, but its quantification from immunohistochemistry images normally depends on supervised classifiers trained per dataset. We examine the role of frozen pretrained visual representations in annotation-free Ki67 cell typing. To this end, we use K-CLUE, a framework that segments individual nuclei, represents each nucleus with a pretrained encoder, reduces the resulting embeddings with principal component analysis, and separates Ki67-positive from Ki67-negative nuclei using k-means clustering, without task-specific training or manual annotations. Clustering the raw components is highly sensitive to the choice of encoder: across seven encoders, the Ki67-positive F1-score on matched MIST nuclei varies by 44 points, although Ki67 status remains linearly decodable from every representation, with supervised probe AUCs above 0.98. Analysis of the embedding spaces shows that clustering succeeds when DAB-related variation occupies the leading directions of variance. Whitening the retained principal components removes this dependence, reducing the spread across encoders to 1.00 F1-score point. Handcrafted color representations are also competitive, confirming that Ki67 status is strongly reflected in chromatic information, but they require an explicit choice of color space. In end-to-end evaluation, K-CLUE reaches F1-scores of 85.00% and 81.91% for Ki67-positive and Ki67-negative nuclei on MIST, and 79.59% and 81.16% on BCData, outperforming DeepLIIF and IHCScoreGAN on both datasets. These results show that pretrained representations can support annotation-free Ki67 typing when their variance structure is accounted for.

---


### 127. [Distortion-Aware Spatiotemporal Learning for Real-Time Wide-Angle Video Rectification](https://arxiv.org/abs/2610.32500)

**<font color=#1a73e8>作者：</font>** Lang Nie, Yihan Yang, Wenbo Nie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While wide-angle lenses provide an expanded field of view (FoV), they exhibit severe nonlinear distortion near image boundaries, unnaturally stretching people in these regions. Existing methods mostly focus on facial regions, require high computational costs, and lack temporal modeling, resulting in incomplete full-body rectification, impractical real-time deployment, and noticeable inter-frame shakes. To tackle these issues, we propose \textbf{FastVC}, an efficient full-body video rectification framework driven by distortion-aware spatiotemporal learning. Grounded in lens physics, FastVC introduces a distortion-aware thin-plate spline (DA-TPS) module that nonlinearly remaps control points into a peripheral-dense layout, enabling more accurate geometric fitting without additional computational cost. We further develop a dual-level spatiotemporal learning scheme for causal and stable video rectification. At the model level, neighborhood spatiotemporal attention (NST) aggregates local context and selectively fuses historical features with low overhead. At the optimization level, sparse spatiotemporal supervision applies spatial alignment only to anchor frames, decoupling frame-wise accuracy from temporal stability. Besides, we contribute the first benchmark dataset for wide-angle full-body video correction. Extensive experiments show that FastVC achieves state-of-the-art rectification fidelity and visual stability at 57.0 FPS.

---


### 128. [DRIVE: Fine-tuning via Data Contribution- and Diversity-aware Weighting with Prior Regularization](https://arxiv.org/abs/2610.32501)

**<font color=#1a73e8>作者：</font>** Qing Liu, Xinrui Chen, Yi Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-stage fine-tuning is pervasive, yet catastrophic forgetting persists when the source pre-training data is inaccessible. Data weighting affords a natural lever to modulate sample influence. Yet existing weighting methods lack a principled mechanism to explicitly arbitrate knowledge retention against new-task adaptation, and provide no unified differentiable objective to accommodate auxiliary signals such as sample diversity and sample characteristics. This is because current schemes privilege one goal over the other, and no explicit gradient-compatible encoding exists for such signals. To address this, we propose DRIVE, a principled and efficient weight assignment framework. It derives per-sample weights via a unified differentiable objective where three coupled signals co-evolve: Shapley additivity splits contribution into anti-forgetting and adaptation components, which are reshaped by a covariance-based diversity term and stabilized by a sample-characteristic prior. Far from a mere combination, this yields an end-to-end gradient-based scheme balancing stability against plasticity. Theoretically, we prove that DRIVE enjoys superior stability-plasticity guarantees over existing weighting schemes and enhances parameter estimation robustness. Empirically, it attains superior overall performance, faster convergence, and stronger robustness. Code at this https URL.

---


### 129. [BAARC: Uncertainty-Driven Adaptive Partial Spectral Measurement to Full Reconstruction for Material Classification](https://arxiv.org/abs/2610.32505)

**<font color=#1a73e8>作者：</font>** Adithya Ashok Chalain Valapil, Aishwarya Venkataramanan, Joachim Denzler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectroscopic instruments with limited wavenumber coverage require accurate scan positioning or multiple measurements to complete the material analysis. This often requires prerequisite knowledge about the material under diagnosis to measure the spectral regions with distinguishing peaks. In our study, we simulate a Bayesian Adaptive Acquisition with Reconstruction-driven Classification (BAARC) framework for Raman spectral measurements, using masked training to learn spectral features that dynamically drive laser channel selection until the material is identified. We present a jointly trained two-level framework that takes progressive partial measurements of small wavenumber patches across the complete spectral range and, at each step, first attempts to reconstruct the full spectra until the model uncertainty is low. Secondly, material classification is performed at each reconstruction step until stoppage. Uncertainty quantification during reconstruction steps helps determine the measurement position of our next patch, while combining it with classification uncertainty determines measurement termination. By closing the loop between hardware acquisition and deep probabilistic modeling, the proposed system minimizes physical measurement steps while maintaining both spectral fidelity and diagnostic accuracy. Experimental evaluations demonstrate that our framework achieves high-accuracy sample identification using only a fraction of full-spectrum channels, offering a scalable solution for real-time, high-throughput spectroscopic instruments.

---


### 130. [Augmentation Strategy for DINO in Glaucoma Classification](https://arxiv.org/abs/2610.32511)

**<font color=#1a73e8>作者：</font>** Ashish Kumar Meena, Chandra Sekhar Seelamantula  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) offers a promising approach to medical image representation learning, yet augmentation strategies of SSL frameworks validated on natural images do not reliably transfer to specialized medical imaging domains. We analyze DINO, a knowledge-distillation based SSL framework, and empirically demonstrate that its default augmentation strategy produces unreliable representations for retinal fundus images, degrading downstream glaucoma classification performance. Guided by the principle that effective cropped views should share minimal redundant information while retaining clinically relevant signal, we redesign DINO's augmentation strategy. Our approach biases the learned representations toward diagnostically critical features rather than low-level image statistics. We evaluate our method for glaucoma classification by training a linear classifier on the frozen representations, achieving strong generalization across seven benchmark datasets. URL for code and weights: this https URL

---


### 131. [The Punjabi Geet Toxicity Dataset (PGT-FG): Fine-Grained Multimodal Annotations for Toxic Content in Punjabi Songs](https://arxiv.org/abs/2610.32513)

**<font color=#1a73e8>作者：</font>** Lakhjeet Kaur, Jaspreet Kaur, Komal Rani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Resources for toxicity detection in Punjabi remain limited, particularly for musical content that combines linguistic and multimodal information. We present the Punjabi Geet Toxicity Dataset (PGT-FG), a segment-level resource developed to support research on toxicity detection in Punjabi musical content. The dataset was constructed from publicly available Punjabi songs collected from YouTube. An initial collection of 620 songs resulted in 465 successfully downloaded songs and 3,402 preliminary segments from 450 songs. After quality control and annotation, the final dataset contains 2,396 unique segments from 392 songs. Four native Punjabi annotators produced 2,870 annotation records, including a shared subset of 158 segments annotated by all four. Each annotation includes binary toxicity, eight fine-grained toxicity categories, severity, sentiment, mode, and an uncertainty flag. Inter-annotator agreement was measured with Fleiss' kappa on the shared subset, and majority-based resolution produced the final segment-level labels. Of the 2,396 segments, 705 (29.42%) were labelled toxic and 1,691 (70.58%) non-toxic. Violence was the most frequent category, occurring in 539 toxic segments (76.45%), followed by gang references (227, 32.20%) and drug references (133, 18.87%). The overall toxicity label achieved substantial agreement (kappa = 0.6521). PGT-FG provides a fine-grained resource for Punjabi toxicity detection and multimodal content analysis. The resolved dataset, with one final record per segment, is publicly available on Zenodo (this https URL). Original lyrics, lyric excerpts, and copyrighted audio or video content are not redistributed.

---


### 132. [Amortized Thompson Sampling and Efficient Information-Directed Sampling for Simulator-Based Design](https://arxiv.org/abs/2610.32514)

**<font color=#1a73e8>作者：</font>** Michal Kobiela, Michael U. Gutmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thompson sampling is a widely used strategy for sequential decision-making under uncertainty, offering a principled way to balance exploration and exploitation. This strategy involves maximizing a target objective under a single sample drawn from the current belief over unknown quantities. Conventionally, this optimization is performed once the belief has been inferred from data, and it becomes computationally burdensome when many Thompson samples are required, especially in continuous action spaces. In this work, we introduce an approach that amortizes this process ahead of time, before any data is collected, so that an approximation of the full Thompson sampling distribution is available immediately once observations arrive. We employ this approach to solve the multi-round setting, involving sequential data acquisition and Thompson-sample recommendation across rounds. Beyond accelerating Thompson sampling, our approach enables efficient estimation of expected information gain about the optimal action. This can be used to select more informative Thompson samples or to obtain maximally informative designs with optimization. Combining this estimate of expected information gain with immediate regret supports information-directed sampling (IDS), which can outperform Thompson sampling by explicitly balancing these two quantities. We demonstrate our approach on two simulator-based design problems in synthetic biology, where the simulators have intractable likelihoods.

---


### 133. [Analysing Austrian Parliamentary Speeches by Predicting Party Affiliations](https://arxiv.org/abs/2610.32515)

**<font color=#1a73e8>作者：</font>** Sarah Sulollari, Vanja Karan, Benjamin Roth  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper examines speech characteristics of the Austrian National Council members (CMs). We introduce analysis methodology based on a fine-tuned BERT-Model which assigns to every speech a probability distribution over Austrian parties. These are then aggregated at the speaker and party level. We perform an extensive evaluation to ensure the quality of the generated distributions prior to further analysis. Instead of considering mis-assignments of predicted parties as a performance issue, we leverage them to derive insights about the CMs and political developments. Our findings show that parties that govern together become more similar in their speech characteristics, while, analogously, parties that are in opposition move further away from governing parties. Moreover, CMs who switch party usually adapt their speech characteristics only after the switch occurs. Finally, we publicly release a data set containing party affiliation predictions for the speeches of the Austrian National Council from 1996 to 2018.

---


### 134. [VERA-Hand: A Verified Multidimensional Benchmark for 2D Hand Pose Estimation in Third-Person Dynamic Gesture Videos](https://arxiv.org/abs/2610.32517)

**<font color=#1a73e8>作者：</font>** Gibran Benitez-Garcia, Hiroki Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand landmarks serve as input for gesture recognition, sign language understanding, and touchless human-computer interaction. Yet hand pose estimators are typically evaluated with frame-wise localization metrics such as PCK or MPJPE, which are computed over matched predictions and overlook missed or spurious hands, handedness errors, and temporal instability. To address these limitations, we present VERA-Hand, a benchmark that evaluates estimators using manually verified, frame-level 2D annotations for 10,690 hands across four complementary dimensions (detection, localization, identification, and temporal stability), as well as a joint Pose-F1 metric that requires both correct detection and accurate localization. Evaluating six estimators spanning hand-specific, whole-body, reconstruction-based, and foundation-model paradigms, we find that no estimator dominates: rankings reorder sharply across dimensions. VERA-Hand also exposes failures that localization-only and downstream evaluations may not reveal, including cross-hand overlap in over 85% of frames for a recent foundation model. A post-hoc cleanup case study demonstrates how the benchmark can validate corrective interventions, while stratified analyses show that robustness varies across motion-blur classes and hand regions. We release the verified annotations, protocol, and code at this https URL

---


### 135. [HEALPix-Based Implicit Neural Compression of Omnidirectional Images](https://arxiv.org/abs/2610.32561)

**<font color=#1a73e8>作者：</font>** Yulong Cheng, Youneng Bao, Junfeng Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time decoding of omnidirectional images is essential for immersive virtual reality (VR) experiences. Compared with conventional transform-based learned image compression (LIC), overfitted codecs offer lower decoding complexity by representing each image with a lightweight implicit neural representation (INR). However, existing approaches typically operate on the equirectangular projection (ERP), which introduces nonuniform spherical sampling and spatial distortion, leading to redundant sampling near the poles and latitude-dependent receptive fields. To address these limitations, we propose a spherical overfitted codec based on a multi-scale Hierarchical Equal Area isoLatitude Pixelization (HEALPix) representation, which enables equal-area sampling and efficient hierarchical modeling of spherical signals. Building on this representation, we develop a Spherical Inter-Scale Conditional entropy model that exploits spatial dependencies and cross-scale correlations among HEALPix latents to improve coding efficiency. We further introduce a Multi-Ring Spherical Convolution that aggregates neighboring pixels over a nearly uniform spherical receptive field across latitudes. Experiments on a public omnidirectional image dataset demonstrate BD-rate reductions of 16.3%, 26.5%, and 19.5% over VVC in terms of V-PSNR, V-MS-SSIM, and V-LPIPS, respectively. Our method also achieves a 13.1% BD-rate reduction over ERP-based Cool-Chic 5.0 in terms of V-PSNR, while providing 2.6-3.6x faster decoding than the evaluated learned autoencoder codecs.

---


### 136. [Shared Is Not Enough: Predictor Width and Factor Readability Under Masked Latent Prediction](https://arxiv.org/abs/2610.32562)

**<font color=#1a73e8>作者：</font>** Nilotpal Kakati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked latent prediction methods such as I-JEPA aim to learn predictable features, but what determines which information they retain is less clear. We built a simulator in which every factor behind an image is known, so a probe can measure how readable each factor remains after training. We trained small encoders (0.7M parameters) with I-JEPA, SimCLR and BYOL on the same pairs of views and probed a factor that both views share. I-JEPA had a predictor with half the encoder's width and depth, the proportions it uses for ViT-B. Its median score was about 40% of SimCLR's. Widening the predictor to the encoder's width reversed this ordering at every training seed, against both other methods. We release the simulator and the trained models.

---


### 137. [Standing on Open Shoulders: Regional Fine-Tuning of Open-Weight Camera-Trap Models for UK Wildlife with Modest Data and Compute](https://arxiv.org/abs/2610.32573)

**<font color=#1a73e8>作者：</font>** Paul Fergus  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-trap species classification is dominated by large models from well-resourced organisations, which often lack the species-level distinctions regional conservation needs, such as native red versus invasive grey squirrels in the UK. We ask whether open weights let a small team with a modest dataset and a single GPU take a real part in AI development. We fine-tuned the open DeepFaune classifier on 28 UK classes, paired it with the unmodified MegaDetector v6, and compared the resulting DeepFaune-UK v1.2 with DeepFaune v1.5.0 and SpeciesNet on 20,212 hand-verified MammalWeb citizen-science images, after removing sequences sharing any of 1,039 images with our training archive. DeepFaune-UK achieved a strict image-level accuracy of 88.8%, including empty frames, against 56.5% and 59.0% for the baselines, but at DeepFaune's coarser label resolution DeepFaune v1.5.0 was more accurate, though not significantly under contributor resampling (91.4% vs. 88.8%). As DeepFaune v1.5.0 uses a newer DINOv3-based classifier, we applied the identical recipe, without new data, to that classifier. The resulting DeepFaune-UK v1.3 reached 90.6% strict accuracy, narrowed the like-for-like gap to 0.8 points and reduced roe deer misclassified as fallow deer by 69%. On 1,850 images from the 26 contributors with no overlapping images, the three DeepFaune-based models did not differ significantly (90.5%, 90.6%, 89.9% like-for-like). Fine-tuning on 10% of the training crops (about 150 per class) gave out-of-distribution accuracy similar to using all of them, and a DINOv2 run on this subset took about 22 minutes with under 4 GB of GPU memory. Open weights thus make regional model development feasible for small teams, but the largest like-for-like gain came from a newer base model trained by others, so this democratisation depends on large actors continuing to release open weights, under licences that may change.

---


### 138. [Contextual Decision Making: Predictive or Generative](https://arxiv.org/abs/2610.32584)

**<font color=#1a73e8>作者：</font>** L. Jeff Hong, Weihuan Huang, Xinyao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual decision making uses observed covariates to guide decisions under uncertainty. Two natural approaches are predict-then-optimize (PtO), which learns the conditional expected objective, and generate-then-optimize (GtO), which learns conditional uncertainty and optimizes using generated scenarios. We study when each approach is preferable by examining how the choice of learning target affects statistical accuracy and optimization tractability. Although PtO learns a narrower target, our regret bounds show how differences in smoothness can offset GtO's additional dimensional burden. Exploiting smoothness also raises an optimization tradeoff: within the class of nonnegative-weight PtO methods studied, a lower bound limits the gains from additional smoothness, while more flexible methods may introduce signed weights and lose the guarantee of preserving convexity. GtO preserves scenario-wise convexity, but requires learning a richer object and generating scenarios for optimization. Synthetic experiments and a real case study illustrate how these tradeoffs vary with data availability and problem structure. Together with the scope for reusing a model across tasks, our findings provide practical guidance for choosing between the approaches without identifying a universal winner.

---


### 139. [Trajectory Matching: Discrete Flow Matching with Structured Actions](https://arxiv.org/abs/2610.32602)

**<font color=#1a73e8>作者：</font>** Niklas Kemper, Marten Lienen, David Lüdke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The natural units of structured discrete generation are often not independent single-component edits but richer actions: attaching a fragment to a molecule, inserting a node together with an incident edge, or growing a hierarchy by adding a child. Yet most existing discrete flow matching methods (DFM) are restricted to independent component-wise edits over fixed-size states. This restriction stems from endpoint conditioning: endpoints fix the source and target during training but not the action sequence between them, making tractable conditional rates hard to define for complex actions that cannot be factorized component-wise. We propose trajectory matching, which conditions the flow on a full sequence of actions connecting the endpoints. This yields principled, simulation-free training targets for user-defined action spaces, including actions that change state size, modify multiple components, or depend on earlier actions. We prove that the resulting objective recovers the marginal flow and that trajectory matching strictly subsumes factorized DFM, while additionally capturing actions with prerequisite structure such as hierarchy growth or fragment-based molecule generation. Empirically, on tree and molecular graph generation, trajectory matching with domain-aligned actions matches or surpasses factorized DFM baselines (lifting MOSES validity from 92.8% to 99.2%) and transfers without retraining to substructure extension and linking. Trajectory matching enlarges the design space of discrete flow matching by turning the action vocabulary into a modeling choice. An interactive explanation of trajectory matching is available at this https URL.

---


### 140. [Hair Segmentation and Skin Characterization on Macroscopic Dermatological Images for Laser Treatment Parameterization](https://arxiv.org/abs/2610.32609)

**<font color=#1a73e8>作者：</font>** Alex Navarro Navarro, Marc Arriaga Hidalgo, Carlos Moreno Rubio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current light-based devices, such as laser hair removal, intense pulsed light (IPL), vascular laser therapy, and dermatologic phototherapy, are widely used in clinical dermatology but rely heavily on subjective manual parameterization or uncalibrated point-based colorimeters. To overcome these limitations, this work presents a unified system for hair segmentation and skin characterization in macroscopic dermatological images. Unlike most existing literature that relies on dermoscopic datasets captured under highly controlled conditions, our approach is specifically designed for macroscopic images that replicate real clinical laser treatments. The proposed pipeline integrates a custom-trained variant of the YOLOv9 deep learning architecture for instance segmentation and classical image processing within a single workflow to extract objective skin and hair parameters such as phototype, hair density, color, and thickness. A color calibration stage using spectrophotometric measurements ensures accurate feature estimation regardless of illumination conditions. Experimental results show competitive segmentation metrics (mAP@50 $\approx$ 0.80) on a custom dataset featuring short, shaved hairs, typical of pre-treatment scenarios. These findings demonstrate the feasibility of the proposed pipeline in providing the objective, foundational skin and hair features required for future automated laser parameterization, paving the way for its extension to broader light-based medical therapies.

---


### 141. [Interpreting Supervised Pairwise Graph Representations: Local Evidence, Confounding, and Provable Post-hoc Correction](https://arxiv.org/abs/2610.32611)

**<font color=#1a73e8>作者：</font>** Ilya Brekin, Ariela Moldavskaya, Elina Sidorova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised pairwise graph representations convert pairwise predictive relations into sample-specific graphs, but graph-level accuracy does not by itself show that higher-order topology carries the signal. In a controlled Transformer error-detection task, supervised pairwise graphs outperform attention-as-adjacency (ROC-AUC $0.839$ versus $0.559$; the comparable no-confidence pair is $0.687$ versus $0.559$), but their apparent advantage over model confidence disappears after controlling for sequence length, which is almost perfectly recoverable from the pooled hidden state ($R^2=0.9995$). On published HCP Emotion ensemble graphs, signed node aggregation already acts as an ensemble of supervised pairwise predictions. Edge magnitude alone is near chance; topology-aware augmentations change ROC-AUC by at most $0.004$, with only sign-separated degree showing small positive changes across all tested graph sizes, while a validation-tuned three-layer GCN provides no measurable improvement over the signed node-summary baseline. A Fisher post-hoc corrector satisfies its distribution-agnostic guarantees across the evaluated feature representations and remains stable under reduced labelled budgets; in a near-error-free fMRI calibration regime the bound correctly becomes statistically uninformative. A separate cross-attention analysis identifies a redundant reversal circuit and downstream EOS-timing and copy failures. Higher-order topology should therefore be credited only after local supervised evidence and recoverable nuisance variables have been excluded.

---


### 142. [DriveOSS: Dataset and Benchmark for 3D Anomaly Segmentation and Open-set Semantic Segmentation in Autonomous Driving](https://arxiv.org/abs/2610.32612)

**<font color=#1a73e8>作者：</font>** Zhiran Yan, Savankumar Bhanderi, Sourabh Lolge 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D semantic segmentation have significantly improved scene understanding in autonomous driving. However, existing methods are typically developed under a closed-set assumption and evaluated under standard driving conditions, where all categories are known in advance. In real-world driving, autonomous vehicles inevitably encounter previously unseen objects, making closed-set perception insufficient for safe deployment. To address this challenge, we introduce DriveOSS, which, to the best of our knowledge, is the first real-world multimodal dataset and benchmark specifically designed for 3D anomaly segmentation and open-set semantic segmentation. It contains 12,661 synchronized and annotated frames captured using six surround-view RGB cameras, a 128-beam LiDAR, and a GPS/IMU unit. The dataset comprises 52 real-world driving scenes collected under clear, nighttime, cloudy, rainy, and snowy conditions and is organized into ID (in-distribution) and OOD (out-of-distribution) subsets. The ID scenes contain only known classes and are used for training, whereas the OOD scenes additionally contain unknown objects annotated as the outlier class and are used for validation and testing. Extensive experiments show that unseen objects remain a major challenge for current 3D perception systems. The dataset, benchmark protocols, and code are available at this https URL.

---


### 143. [Earth embeddings are decomposable records of the land surface](https://arxiv.org/abs/2610.32617)

**<font color=#1a73e8>作者：</font>** Robin Young, Srinivasan Keshav  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ecological monitoring, carbon accounting and biodiversity assessment increasingly rely on annual Earth embeddings--learned vectors that compress a year of satellite observation for every ten-meter pixel on Earth, consumed in place of the imagery itself. What these vectors mean has not been established. Here we decompose two widely used embedding products and show that they contain individual ecological features, including fire, forest clearing and crop type, validated against independent reference data on events across six continents. The recovered concepts date abrupt canopy loss to the first post-disturbance growing season and resolve severity well enough to separate prescribed fire from wildfire. Small fires that recover quickly are detectable in one product but not the other, which instead separates crops more strongly.

---


### 144. [Privacy-Preserving Federated Loss Exploration for Vision-Based Perception under Non-IID Data](https://arxiv.org/abs/2610.32626)

**<font color=#1a73e8>作者：</font>** Nergiz Yuca, Christian Internò, Nikolay Matyunin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-based image classification models benefit from Federated Learning (FL) across vehicles, however learning accurate models from distributed vehicular cameras is challenging due to data heterogeneity and privacy concerns. To improve performance on non-IID data, advanced FL optimization approaches have emerged that share auxiliary insights, such as client gradient behaviors. While these gradient-guided optimized FL methods improve the model accuracy, their reliance on sharing additional gradient information introduces a previously unexplored privacy vulnerability. In our empirical privacy-leakage experiment, we show that a malicious server can infer clients' label sets from shared guidance matrices under heterogeneous client label distributions (simulated via Dirichlet-based label partitions), between 50% and 84% accuracy. To address this privacy leakage, we propose PPFLex that replaces the central server with three Secure Multi-Party Computation (MPC) servers to securely compute the global guidance matrix and perform federated averaging under semi-honest and malicious MPC server assumptions. We evaluate PPFLex on widely used traffic-sign classification datasets (e.g., GTSRB and BTSC) as representative autonomous vehicle perception benchmarks, comparing against baselines. Our results show that PPFLex achieves accuracy comparable to the plain-text FedLEx pipeline while preventing privacy leakage, incurring acceptable MPC overhead.

---


### 145. [The Standard Deviation in VICReg Buys a Safety Margin](https://arxiv.org/abs/2610.32630)

**<font color=#1a73e8>作者：</font>** Hawar Dizayee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> VICReg prevents collapse with a hinge on the standard deviation of each embedding dimension, and its authors argue from the gradient that a hinge on the variance would fail. To our knowledge, this claim has not been tested experimentally. We test it in a controlled setting (ResNet-18, CIFAR-10 and CIFAR-100), changing only the hinge and sweeping its weight $\mu$ over five orders of magnitude. At the default weight ($\mu = 1$), the two hinges reach the same linear-probe accuracy on CIFAR-10 (about 89.5%). Both collapse below a threshold weight, but the standard-deviation hinge's threshold is 35-130$\times$ lower. CIFAR-100 shows a consistent gap. In training, the variance hinge's gradient fades as the feature variance shrinks, while the standard-deviation hinge's does not until that variance is very small. The standard-deviation hinge therefore buys a safety margin: it keeps training at weights far below the point where the variance hinge collapses.

---


### 146. [EditJev: System One Routing for Image Editing Models](https://arxiv.org/abs/2610.32635)

**<font color=#1a73e8>作者：</font>** Zhile Guan, Xu Jiang, Yule Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing models exhibit pronounced sample-specific performance variation: different models can produce substantially different results for the same source image and editing instruction, and the best-performing model often varies across requests. These models also differ substantially in inference latency, making fixed-model deployment inefficient. We therefore study image editing model routing, which dynamically selects an editor from a candidate pool given an input image and editing instruction. We introduce EditJev, a System One routing model that directly predicts sample-level preference scores over candidate image editing models in a single forward pass. A lightweight preference head on a vision-language backbone produces a fixed-dimensional score vector without autoregressive model-name generation or response parsing. To train EditJev, we construct pairwise preferences from offline candidate outputs and optimize a pairwise ranking objective to learn relative model suitability. At inference time, EditJev combines the predicted preference scores with model-level speed scores to balance editing quality and generation latency. Experiments on ImgEdit and GEdit-En show that EditJev improves aggregate quality over the strongest fixed editor, from 4.540 to 4.592 and from 8.194 to 8.255, respectively, while reducing estimated end-to-end latency by 60.8% and 31.7%. These results demonstrate the effectiveness of direct, structured model routing for efficient image editing.

---


### 147. [Residual Expert Routing for Text-Only Domain Adaptation of Factorized Transducer ASR](https://arxiv.org/abs/2610.32637)

**<font color=#1a73e8>作者：</font>** Shashi Kumar, Esaú Villatoro-Tello, Thibault Bañeras-Roux 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning the non-blank predictor of a factorized transducer on target-domain text improves recognition on that domain but degrades performance on the source domain. A single interpolation weight between base and adapted predictors cannot resolve this: the adapted predictor helps at some prefixes and hurts at others, often within one utterance. We propose conservative residual routing: the adapted predictor becomes a residual correction to the base, and a 16k-parameter gate decides at each prefix how much of it to admit. Closing the gate reproduces the base exactly. On a 40-hour conversational corpus, routing retains essentially all of the text-only gain on two held-out domains (19.89 to 16.74, 20.91 to 16.21 WER) while leaving source-domain WER unchanged (12.90 to 12.93); the adapted predictor alone costs 1.08 WER. Routing needs no per-domain tuning on target-domain audio. Analysis reveals the gate does not behave as a simple domain-level switch: it modulates intervention through the disagreement between the two predictors, suppressing it in-domain and amplifying it out-of-domain.

---


### 148. [WL-SeqVAE: Sequence-Based Graph Generation Using Variational Autoencoders and Weisfeiler-Leman Colors](https://arxiv.org/abs/2610.32650)

**<font color=#1a73e8>作者：</font>** Iakovos Evdaimon, Giannis Nikolentzos, Achilleas Tsimichodimos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce WL-SeqVAE, a sequence-based variational autoencoder for generating graphs. The key observation behind WL-SeqVAE is that node colors induced by the Weisfeiler-Leman (WL) algorithm provide compact discrete summaries of local graph structure and can therefore serve as structural tokens for generation. Rather than learning a distribution over adjacency matrices directly, our method maps each graph to a sequence of WL colors and employs a variational autoencoder that encodes this sequence into a Gaussian latent distribution, from which an autoregressive decoder reconstructs the graph. During generation, compatibility constraints derived from the WL colors guide node and edge predictions, combining global information from the latent representation with local structural consistency. This formulation turns graph generation into a sequence generation problem and avoids directly parameterizing a quadratic adjacency matrix. We evaluate WL-SeqVAE on molecular and general graph generation tasks. Across the evaluated datasets, WL-SeqVAE is competitive with established baselines on several local structural and molecular quality metrics. Code is available at this https URL

---


### 149. [DT-JEPA: Learning to Predict Future Representations for Decision-Making](https://arxiv.org/abs/2610.32657)

**<font color=#1a73e8>作者：</font>** Changxu Ni, Yiyang Ni, Jun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision Transformer (DT) has demonstrated strong performance in various offline reinforcement learning (RL) tasks by conditioning action generation on expected future returns and historical trajectories. However, treating expected future returns as the condition provides an incomplete description of the future, as trajectories with different state transitions and behaviors may share similar returns. Moreover, expected future returns inherently depend on task-specific reward functions, which makes policy learning reliant on reward-labeled datasets and restricts its scalability to tasks with similar but unseen rewards. Recently, Joint Embedding Predictive Architectures (JEPA) have emerged as a promising paradigm of self-supervised learning-based world models, which learn predictive representations of future dynamics in latent space rather than reconstructing future states in the original space. Inspired by JEPA, we propose DT-JEPA, an offline pretraining and online fine-tuning framework that learns general knowledge from reward-free offline trajectories and achieves excellent adaptation to unseen tasks. Instead of predicting a single deterministic future embedding, we design a novel probabilistic predictor to model the conditional distribution of future representations in the latent space, thereby capturing both predictive information and uncertainty about future dynamics. Theoretically, we show that 1) the JEPA objective seeks to maximize a variational lower bound on the mutual information between historical representations and future trajectories; and 2) predictive future-conditioned policy learning admits a finite-sample performance bound with an O(N-1/4) estimation term. Experiments on D4RL benchmarks demonstrate that DT-JEPA achieves efficient adaptation across varying offline RL tasks, outperforming traditional DT-based and other offline RL methods.

---


### 150. [WiMoT: Replay-Free Continual Wi-Fi Sensing via Moment Transport](https://arxiv.org/abs/2610.32660)

**<font color=#1a73e8>作者：</font>** Chunchun Yang, Yang Cao, Zhitang Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual Wi-Fi sensing must balance plasticity, learning new rooms or users, against stability, keeping earlier ones, yet nodes often cannot retain channel state information (CSI) for privacy and storage reasons. We propose WiMoT (Wi-Fi Moment Transport), which stores the per-class feature mean and covariance of every earlier domain instead of samples. When the representation changes, stored statistics become stale. WiMoT restricts the change to an affine map on a frozen feature basis and applies the same map to the statistics, so they stay valid without old samples. Supervised contrastive learning learns the new domain, a closed-form loss on the stored statistics keeps earlier classes separable, and a Gaussian discriminant classifier, refitted from the transported statistics with equal weight per domain, predicts without domain identity. On 3DO, WiMANS, and Widar3.0, WiMoT's average final accuracies are 94.02%, 89.61%, and 95.16% with at most 0.58 percentage points (pp) of forgetting. On 3DO and Widar3.0, it also has the highest balance of new- and earlier-domain accuracy and is 3.77 and 13.11 pp ahead of the strongest of 21 baselines, which uses replay, staying ahead across domain orders and label budgets. On WiMANS, it matches the strongest replay baseline in accuracy (+0.41 pp) while reducing forgetting from 2.78 to 0.00 pp, and has the highest six-order average accuracy. Because full covariances dominate the memory, storing them as rank-32 factors shrinks the moment memory to 6.4%, losing at most 0.49 pp of accuracy, within edge-node storage budgets.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-198](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
