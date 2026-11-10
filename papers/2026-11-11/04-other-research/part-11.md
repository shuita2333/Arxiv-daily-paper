# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-520**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-520**

---

### 501. [Smartphone-Enabled Depth-Aware Transillumination Imaging for Detection of Chicken Breast Fillet Myopathies in Chicken Fillets](https://arxiv.org/abs/2611.12796)

**<font color=#1a73e8>作者：</font>** Chaitanya Pallerla, Ramesh Bahadur Bist, Yihong Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Woody Breast (WB) myopathy is a major quality defect in broiler chickens characterized by fibrosis, increased tissue hardness, and altered structural properties that affect product quality. Conventional palpation is subjective and labor-intensive, while many non-destructive methods require specialized equipment or substantial computational resources. This study developed a smartphone-based transillumination and 3D point-cloud framework for non-destructive WB severity classification. A total of 267 chicken breast fillets, including normal breast (NB, n = 87), mild WB (MWB, n = 85), and severe WB (SWB, n = 95), were evaluated using RAW transillumination images and 3D point clouds acquired with an iPhone 16 Pro. A total of 91 features, comprising 14 image-derived, 76 geometric, and one physics-informed Beer-Lambert attenuation feature, were extracted. Partial correlation controlling for thickness revealed a significant association between image characteristics and WB severity (r = 0.413, p < 0.0001), indicating optical information independent of fillet geometry. SWB tissue exhibited approximately 26% greater light attenuation per unit thickness than NB. The 2D-only models achieved approximately 82% test accuracy, while the multimodal ensemble combining Fusion-DGCNN, XGBoost, and physics-guided logistic regression (PGLR) achieved approximately 90% accuracy. These findings demonstrate the complementary value of optical, geometric, and physics-informed features and establish the feasibility of smartphone-based, non-destructive WB severity assessment.

---


### 502. [Complementarity-Driven Dual-Teacher Hierarchical Alignment for Zero-Shot EEG-to-Image Retrieval](https://arxiv.org/abs/2611.12798)

**<font color=#1a73e8>作者：</font>** Lukun Wu, Jie Li, Ziqi Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decoding visual information from EEG is central to brain--computer interfaces and brain-inspired intelligence, and contrastive alignment with pretrained vision foundation models (VFMs) has become the dominant paradigm. However, existing methods align EEG solely with CLIP-family VFMs, leaving hierarchical visual information in neural responses under-exploited. To address this gap, we formulate a mechanism-paradigm correspondence view linking hierarchical visual processing (from appearance to semantics) to the complementary biases of cross-paradigm VFMs, with image-only models (e.g., DINO) and image--text models (e.g., CLIP) capturing distinct facets of this hierarchy. Guided by this view, we propose the Dual-Teacher Hierarchical Alignment (DTHA) framework. Concretely, a shared EEG encoder is supervised by frozen multi-blur CLIP and shallow DINOv2 teachers via dual-branch contrastive alignment, so each branch fully supervises the visual cues it emphasizes. A fused-retrieval objective learns adaptive weights to combine their complementary visual representations for zero-shot EEG-to-image retrieval. For the shared EEG encoder, we introduce the Attentive Modulated Scalp-Pattern Bank Encoder (AMSPBE), combining temporo-spatial attention with a learnable scalp-pattern bank for accurate, interpretable visual feature extraction, while modeling regional temporal dynamics and filter-bank topographies. On THINGS-EEG zero-shot retrieval, DTHA achieves 92.4% Top-1 accuracy, exceeding prior state of the art by 12.4 percentage points. Spatial, spectral, and representational-similarity analyses, together with THINGS-MEG evaluation, validate DTHA's effectiveness, biological plausibility, and cross-modality generalization. This complementarity-driven perspective shows that supervision from cross-paradigm VFMs enables more complete extraction of hierarchical visual information from brain activity.

---


### 503. [2D Gum-Net: Unsupervised Dense Elastic Image Registration via Symmetric Correlation and Spectral Pooling](https://arxiv.org/abs/2611.12805)

**<font color=#1a73e8>作者：</font>** Aarya Bhave, Anushka Ajay Bhave  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense non-rigid registration, the recovery of a pixel-wise deformation field that warps one image into geometric agreement with another, is fundamental across medical imaging, structural biology, and correspondence estimation, yet learning-based approaches face a severe bottleneck: ground-truth deformation fields are notoriously difficult to obtain for real data. We present 2D Gum-Net, an end-to-end architecture that predicts dense elastic deformation fields fully unsupervised. We transfer the Geometric Unsupervised Matching Network (Gum-Net), originally developed for 3D subtomogram alignment in cryo-electron tomography, to 2D elastic registration: all three modules are redesigned in 2D, and the rigid transformation head is replaced by a Dense Spatial Transformer that regresses a sparse control-point grid, lifted to a full-resolution field $\Phi$ by bicubic interpolation. Downsampling uses DCT spectral pooling, implemented as frozen-basis matrix multiplications ($\approx 50\times$ GPU speedup), preserving the fine, quasi-periodic structure that max and average pooling destroy. We evaluate on contact-based fingerprints, a challenging testbed for this task: locally self-similar ridge patterns make correspondence maximally ambiguous, skin pressed against a sensor generates authentic large-displacement elastic distortion, and minutiae act as precise landmarks through which an independent matcher externally verifies the topological correctness of predicted fields. Trained purely on synthetic impressions and evaluated zero-shot on real benchmarks, our method improves structural correlation by up to 15.7% on FVC2004 and raises genuine match scores under an independent matcher while leaving imposter scores essentially unchanged. This suggests that the predicted deformations restore true structure without fabricating correspondences.

---


### 504. [Inversion-Free High-Dimensional Counterfactual Inference](https://arxiv.org/abs/2611.12815)

**<font color=#1a73e8>作者：</font>** Saketh Vishnubhatla, Pingchuan Ma, Shu Wan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual inference is the task of answering hypothetical "what-if" queries about a unit, given an observational dataset, modeling assumptions, and a causal graph. This enables a modeler to reason about hypothetical scenarios that cannot otherwise be answered without assumptions or a causal graph. The simpler case involves a causal graph with scalar 1-D variables that denote different attributes in the data-generation process. While the literature is clear in the 1-D case, extending this to settings with high-dimensional nodes (e.g., images) remains challenging. Conventionally, in the literature, methods recover the latent state from the factual image (inversion), generate counterfactual attributes from the graph, and render the counterfactual image from the latent state using the updated attributes. In our work, we investigate the necessity of the inversion step in computing high-dimensional counterfactuals. We first discuss moving from the scalar 1-D case to the higher-dimensional case. Secondly, we discuss the relevance of the inversion step and evaluate an inversion-free counterpart repurposed from the image-editing literature. Finally, on image datasets such as CelebA and ADNI, we benchmark our approach using two measures: namely, effectiveness and identity preservation. While effectiveness is a measure of how faithfully the counterfactual attribute is rendered, identity preservation measures whether the same unit (image) is being rendered, both of which are crucial for high-dimensional counterfactual inference. We present the tradeoffs of using inversion-based and inversion-free approaches in our work.

---


### 505. [How Well Does AI Peer Review Work? A Benchmark Built from 100 Planted Errors](https://arxiv.org/abs/2611.12820)

**<font color=#1a73e8>作者：</font>** Paul Litvak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One hundred known errors were planted into 10 open-access psychology papers, and the modified papers were then run through frontier models and two commercial AI review tools. The best single system caught 71 of the 100 errors, while the worst caught 30. Pooling every system's output caught 93. Models are only partly correlated in the errors they find, which makes ensembling a big lever for finding issues in papers. Seven errors could not be caught by any system, and all seven were omissions: information deleted from a paper rather than mistakes inserted into it. this http URL contributes more unique catches than any other single system, though it is expensive on a per-error basis. False positives were not measured, and how this error distribution compares to the distribution of errors in real papers remains unknown. The papers, errors, model outputs, and full experiment log are public, so that others can build on this toward a comprehensive evaluation benchmark across disciplines.

---


### 506. [MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning](https://arxiv.org/abs/2611.12825)

**<font color=#1a73e8>作者：</font>** Jihwan Jeong, Guy Tennenholtz, Yinlam Chow 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems must often maintain bounded memory of unbounded interaction histories. However, optimizing the memory representation, and its updates, for downstream task utility is difficult for standard reinforcement learning (RL) due to severe credit assignment bottlenecks induced by sparse, delayed rewards. We introduce MaxIM (Maximally Informative Incremental Memory), a framework that formulates incremental summarization as a capacity-constrained, information-theoretic reward-shaping problem. Grounded in value suboptimality bounds, we show that bounding sequential information loss motivates maximizing the predictive log-likelihood of future, task-relevant targets, a variational lower bound on predictive sufficiency. We introduce a recursive consistency condition to ensure summaries are grounded by maximizing mutual information (MI) with the observed history. We mitigate credit assignment issues with a parameterized asymmetric critic that computes step-wise variational MI bounds for dense reward shaping. Empirical evaluation on long-horizon scientific reading and multi-turn dialogue benchmarks shows that MaxIM outperforms RL, supervised fine-tuning, and prompt-focused baselines on factual grounding, comprehensive autorater metrics, and downstream task utility across strict token budgets and extended horizons, without the need for expensive human preference labels.

---


### 507. [What the Loss Curve Misses: FP4 Pretraining Slows the Acquisition of Rare Facts](https://arxiv.org/abs/2611.12832)

**<font color=#1a73e8>作者：</font>** Chang Lu, Mengjiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision pretraining is usually judged by validation loss. We ask whether matching loss also means learning rare facts as efficiently. We train transformers from scratch with emulated 4-bit matrix multiplications on synthetic biographies with controlled exposure counts, on their own and mixed into web text. NVFP4 needs 1.32$\times$ and 1.52$\times$ as many exposures as BF16 to match its recall while validation loss differs by only 0.5% and 2%, and 1.26$\times$ and 1.30$\times$ when both models are evaluated with BF16 matrix multiplications. Under our primary readout, the exposure cost is about 1.2$\times$ at matched loss. Zero-mean gradient noise reproduces the cost of quantizing only the backward pass, which barely moves the loss. In a controlled experiment at twice the NVFP4 error, noise fed only to Adam's second-moment estimate acts like a lower learning rate and its cost fades, whereas noise in the update lowers its signal-to-noise ratio and carries about two thirds of the cost through the end of training. Raising the learning rate to offset the smaller average step does not recover the cost, either for this noise or for NVFP4. Gradient statistics of BF16 checkpoints rank the costs of formats, partial quantizations and noise controls without fitting (Spearman 0.96). We suggest measuring rare-fact acquisition alongside loss when evaluating low-precision recipes.

---


### 508. [Programming Prescience: Issues in Human Construction of Forecasting Bots](https://arxiv.org/abs/2611.12834)

**<font color=#1a73e8>作者：</font>** Priya Dhawka, Benjamin Wilson, Andrew Head  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI models' growing capacity for complex reasoning has made them attractive tools for forecasting, or the systematic prediction of the future based on past and present data. However, should AI forecasting systems be adopted, human builders will shoulder the work of building and evaluating them. In this paper, we explore what this work looks like with a qualitative interview study with 15 builders of forecasting bots, sampled from among successful participants in a recent AI forecasting competition. Our analysis surfaces the challenges around (1) tuning a bot to acquire factual research, (2) implementing coherent reasoning, and (3) understanding how well one's bot actually does. During their work, builders frequently introduced complexity that did not pay off, and tested in ways that were opportunistic and piecemeal. Our detailed account of their challenges helps clarify what problems should be targeted in upcoming innovations in process, tools, and human-AI teaming for forecasting.

---


### 509. [What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching](https://arxiv.org/abs/2611.12852)

**<font color=#1a73e8>作者：</font>** Tianze Luo, Haofeng Huang, Yuan Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent Diffusion Models dominate generative modeling but face two-stage training complexity and the inherent reconstruction limits of pre-trained autoencoders. Pixel-space Flow Matching offers a simplified end-to-end alternative yet often encounters training difficulties when using the standard $v$-prediction objective. Recent research attributes this difficulty to the off-manifold nature of noised targets, motivating a shift toward $x$-prediction. In this paper, we investigate this explanation through patch-wise Principal Component Analysis (PCA) and identify a bandwidth bottleneck. The velocity in minor components is largely determined by the raw noisy input, requiring deep backbones to preserve information that competes with principal-component modeling. Through controlled experiments and representation analysis, we further examine why $x$-prediction remains effective: its parameterization provides a raw-input bypass, while its learned input representation can spontaneously concentrate on principal directions. Under low-rank observations, our analysis of the induced flow characterizes $x$-prediction as an implicit conditional-mean decoder, reconstructing discarded components from the retained information. These observations motivate the Raw-injected Transformer (RiT), which combines a lightweight raw-conditioned decoder with an output-side shortcut to separate semantic modeling from raw-state propagation. Our method restores effective $v$-prediction and achieves competitive performance on ImageNet $256\times256$, providing a perspective on the interaction between prediction objectives and architectural bandwidth.

---


### 510. [TUTTI: Parallel CKKS Bootstrapping in under 3 ms on CPU](https://arxiv.org/abs/2611.12854)

**<font color=#1a73e8>作者：</font>** Robin Köstler, Antonio Guimarães  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper introduces TUTTI, a new CKKS bootstrapping procedure that outperforms previous low-latency solutions in multi-threaded latency for any number of messages and, most notably, has a lower latency than TFHE when bootstrapping a single one. Our bootstrapping builds upon SPRU (CK, TCHES 2027), improving it with new methods for exploiting parallelism and increasing the number of messages, as well as with a refined security analysis, of independent interest, of the block-binary secret keys of LMSS (AsiaCCS 2023). TUTTI bootstraps 4096 real-number messages in 46 to 83.4 ms on 192 threads to restore 1 to 9 multiplicative levels, outperforming SHIP (CHKS, Eurocrypt 2025) by a factor of up to 3 on the same machine. Unlike SHIP, TUTTI gains immediately from bootstrapping fewer messages, with a 256-message bootstrapping taking just 15 to 34 ms on 32 threads. For a single message, TUTTI takes 4.6 ms on 32 threads, whereas TFHE-rs needs 7.3 ms for a 4-bit bootstrapping on the same machine and thread count. We show that this advantage persists across different architectures: on an Apple M5 Pro laptop (ARM), TUTTI takes 2.4 ms on 14 threads, against 4.5 ms for TFHE-rs. Differences between CKKS and lightweight schemes such as TFHE remain on several fronts, from functionality to key sizes and security assumptions, but our work shows that multi-threaded latency is no longer one of them, closing a long-standing gap in the practical FHE literature.

---


### 511. [AI-based characterization of lymphoid structures and the tumor microenvironment reveals lower mature tertiary lymphoid structures, lymph-node follicles, and plasma cells after neoadjuvant therapy in lung squamous cell carcinoma](https://arxiv.org/abs/2611.12855)

**<font color=#1a73e8>作者：</font>** Arne Schmidt, Justin Nieder, Cornelius Boehm 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mature, germinal centre-bearing tertiary lymphoid structures (TLS) and mature lymph node follicles (secondary lymphoid structures, SLS) sustain the plasma cell response that shapes outcome and immunotherapy benefit in lung cancer. How this loco-regional axis differs between neoadjuvant-treated and therapy-naive tumors is poorly defined. We analyzed H&E whole-slide images of resected tumors and paired proximal and distal lymph nodes from matched neoadjuvant-treated (neoLUSC, n=20) and therapy-naive (naivLUSC, n=20) lung squamous cell carcinoma (LUSC) patients. Aignostics Atlas H&E Tissue Analysis (HETA) models quantified cell densities per tissue compartment and cell-cell co-localization; a dedicated deep-learning model validated against pathologist annotations detected TLS and SLS and graded their maturity. Prognostic value was tested in an independent cohort (n=458; 46 treated). In neoLUSC tumors, stromal plasma cell density was 72% (p=0.004) and stromal lymphocyte density 48% (p=0.015) lower than in naivLUSC; macrophages and granulocytes did not differ significantly. Total and immature TLS did not differ, whereas mature TLS in the tumor (p=0.034) and mature SLS in the tumor-distal lymph node (p=0.003) were lower in neoLUSC patients. Peri-TLS plasma cell density correlated with tumor lymphocyte density in naivLUSC (rho=0.54, p=0.017) but not in neoLUSC tumors (rho=0.07). In the validation cohort, stromal plasma cell density (HR 0.69, p=0.011) and lymphocyte-plasma cell co-localization (HR 0.66, p=0.004) were associated with longer survival, and neoadjuvant status with shorter survival (HR 1.50, p=0.026). Neoadjuvant therapy is thus associated with fewer mature lymphoid structures and weaker coupling of the humoral compartment to the tumor rather than uniformly lower immune readouts. The stromal plasma cell/co-localization axis is a candidate prognostic biomarker.

---


### 512. [Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning](https://arxiv.org/abs/2611.12865)

**<font color=#1a73e8>作者：</font>** Xinjie Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) can improve an agent's task capability while reinforcing behavior that violates contextual execution requirements. We study this reward-driven misalignment, including reward hacking, through verifiable reward--context conflicts, where compliant task completion remains feasible while some executable shortcuts earn more reward than every compliant strategy. Encoding these conflicts in task dynamics lets us generate diverse interactive environments at scale and derive compliance feedback from execution histories. In resource and reporting workflows, task optimization increases real productivity through unauthorized resource use or raises reported scores while actual work declines. Controlled changes in the training distribution show that minority conflict exposure can still lead to widespread shortcut acquisition, reaching 97.9\% certified profitable violations on an API task under a 25\% conflict mixture after 128 updates. The same contextual checks supply a simple binary penalty that supports joint capability and compliance gains and partially mitigates acquired violations. Learned safety adapts to expanded authorization and transfers across mechanisms into workflows with evolving evidence and approval requirements. On 32 unseen changing-evidence tasks, resource-trained safety increases safe completion from 53.1\% to 89.1\% relative to task-only training, while both policies achieve full real work. These results connect a verifiable account of reward-driven misalignment with scalable task construction and safety learning that remains useful under changing execution requirements.

---


### 513. [SWAM: Scaling World Action Models with Cross-Modal Alignment](https://arxiv.org/abs/2611.12870)

**<font color=#1a73e8>作者：</font>** Yu Zhou, Xinyuan Xia, Xuankun Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment acquired through video pretraining as an established foundation. However, introducing action learning may impair this alignment. Principled guidance on data and supervision design for maintaining language-video alignment during action learning remains limited. To investigate this, we curate a pool of approximately 47,000 hours of general videos, egocentric videos, UMI demonstrations, and robot demonstrations. Building on this, we systematically study how language-video supervision, language-video-action supervision, and the joint use of these two forms affect WAM performance. In particular, we examine how language annotation quality affects pretrained language-video capabilities, and how action supervision from UMI and robot demonstrations extends these capabilities to language-video-action modeling. To better scale the model, we further conduct detailed studies on joint training recipe and model architecture. Under a fixed training budget, mixing egocentric videos and UMI demonstrations improves control generalization. Model architecture affects how effectively these experiences are used, while scaling pretraining under the selected configuration brings further gains. The resulting recipe, post-trained on RoboTwin Clean demonstrations only, achieves success rates of 88.10% and 61.56% under Easy (Clean-to-Clean) and Hard (Clean-to-Random) conditions, respectively. Our model achieves 40.00% SR across three real-world tasks, compared with 23.33% for the strongest baseline, indicating better generalization under unseen conditions. We release the curated data, training code, and model weights.

---


### 514. [Vendi Anomaly Scores for Efficient and Accurate Anomaly Detection](https://arxiv.org/abs/2611.12871)

**<font color=#1a73e8>作者：</font>** Amey Pasarkar, Adji Bousso Dieng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection (AD) is a critical for trustworthy machine learning and scientific discovery. Existing methods typically define anomalies through local density, isolation heuristics, or distance from a fitted distribution, making them sensitive to neighborhood scale, partitioning choices, or restrictive distributional assumptions. In this work, we introduce a new paradigm by formulating anomaly detection from a diversity perspective. We propose the $\textit{Vendi Anomaly Score}$ (VAS), which detects anomalies by quantifying how much a sample changes the diversity of the dataset, as measured by the Vendi score, when removed. VAS captures both local redundancy and global data structure without relying on density estimation or partitioning heuristics. Moreover, VAS requires no hyperparameter tuning, instead adapting automatically to the spectral structure of the data. VAS is non-parametric and scales linearly with dataset size. Across 148 benchmark embedding datasets derived from 10 source datasets and 4 embedding architectures, VAS achieves state-of-the-art AD performance. We further validate VAS on large-scale ImageNet experiments, where it remains robust as both contamination rate and dataset scale increase.

---


### 515. [HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](https://arxiv.org/abs/2611.12872)

**<font color=#1a73e8>作者：</font>** Haozhen Zhang, Bohan Liu, Jianzhu Bao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined representations, which may miss relevant memories and overlook heterogeneous evidence needs across queries. We introduce \textbf{\hivemem}, a multimodal memory framework that interleaves \textbf{\textsc{H}}or\textbf{\textsc{i}}zontal Memory Expansion with \textbf{\textsc{Ve}}rtical Evidence Composition. For horizontal memory expansion, \hivemem organizes memory episodes into a relational graph using textual and visual anchors, expanding semantically retrieved seeds with related neighbors to recover complementary information. For vertical evidence composition, each retrieved memory retains multiple evidence forms, including compact summaries, captions, grounded visual views, raw images, and interaction history. A lightweight trainable selector independently composes an evidence subset for each retrieved memory, enabling query-adaptive utilization of heterogeneous multimodal information. This two-dimensional design jointly broadens memory coverage and adapts the evidence contributed by individual memories. Experiments across three multimodal memory benchmarks show that \hivemem consistently improves task performance across base models while reducing token consumption by about 90\% compared with the most efficient competing multimodal baselines.

---


### 516. [Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks](https://arxiv.org/abs/2611.12875)

**<font color=#1a73e8>作者：</font>** Hao Gu, Jin Yao, Zezhou Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite impressive progress, existing feed-forward large 3D reconstruction models produce a single, irrevocable prediction. When these models fail, there is no mechanism to correct their mistakes. To address this limitation, we introduce Click3R, a framework for interactive geometric correction of feed-forward models using sparse human correspondence clicks. Given an image pair and a small set of cross-view point correspondences provided by a user, Click3R injects geometric constraints into the 3D reconstruction networks through a lightweight point correspondence adapter, enabling the model to resolve ambiguities in challenging scenarios such as repetitive textures, symmetric structures, large viewpoint changes, or textureless regions. To evaluate interactive reconstruction, we curate a challenging benchmark specifically designed to expose failure modes of existing feed-forward 3D reconstruction methods. Experiments show that Click3R reduces reconstruction error with as few as a single correspondence click, improving performance on both standard and our curated benchmarks. Our results highlight that sparse human interaction provides an effective and practical mechanism for correcting geometric reconstruction errors.

---


### 517. [Adaptive Quantization Preserves Fast Rates for TD Learning over Rate-Limited Channels](https://arxiv.org/abs/2611.12878)

**<font color=#1a73e8>作者：</font>** Sreejeet Maity, Aritra Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by reinforcement learning subject to communication constraints, we study a policy evaluation problem with linear function approximation over a rate-limited channel. In our setup, an agent interacting with an unknown environment (modeled as a Markov Decision Process) transmits quantized estimates of a temporal-difference (TD) learning update direction to a server over a finite-capacity channel. Our goal is to investigate to what extent one can preserve the statistical convergence rates achievable when the channel has infinite capacity. To that end, we propose a new algorithm called Batched Adaptively Quantized TD (BAQ-TD), which uses batching to reduce the variance of the transmitted information, and adaptive quantization to encode innovations. We prove a high-probability finite-time error bound for BAQ-TD, and show that, above a certain finite channel capacity, BAQ-TD preserves the convergence rate of unquantized TD up to logarithmic factors. Specifically, for a $d$-dimensional value function parameter, we establish that transmitting a total of $\mathcal{O}(d \log(T))$ bits over a horizon of length $T$ suffices to achieve the order-optimal rate of $\tilde{\mathcal{O}}(1/T)$, marking an exponential improvement in communication-complexity over prior work.

---


### 518. [Grasping the Future: Joint 3D Hand-Object Forecasting From Internet Videos](https://arxiv.org/abs/2611.12879)

**<font color=#1a73e8>作者：</font>** Rustin Soraki, Matthew Wallingford, Ryan Aby 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To interact with an object, we need to anticipate both how it will move and how our hands should move with it. Human videos capture these relationships across everyday activities, offering a natural source for learning to predict future interactions. Learning from them requires recovering motion from completed interactions and using it to anticipate what could happen next. We present $\textit{Grasping-the-Future}$, a unified generative model of joint 3D hand-object motion, including wrist motion, finger articulation, and object position and orientation. Through masked spatiotemporal completion and flow matching, we train a single model for several prediction tasks: forecasting future interactions, predicting hand motion given object motion or vice versa, generating both trajectories toward a desired final object pose, and completing partially observed interactions. We explicitly model hand-object relations and incorporate contact constraints to help preserve grasp relationships during motion. To obtain 3D supervision from internet videos, we develop a scalable pipeline that combines pretrained perception models with joint geometric optimization to reconstruct completed interactions. We combine these recovered trajectories with annotated interaction datasets as training data for all tasks. We demonstrate strong performance across all tasks, outperforming released forecasters on datasets with 3D annotations. Moreover, we show geometric and physical plausibility of the predicted trajectories by retargeting them to a robotic embodiment. Videos are available at this https URL.

---


### 519. [Kolmogorov-Chapman Maps: Trajectory-Free Learning for Simulating Molecular Dynamics](https://arxiv.org/abs/2611.12880)

**<font color=#1a73e8>作者：</font>** Majdi Hassan, Marta Skreta, Dominique Beaini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic differential equations (SDEs) describe stochastic processes across a wide range of scientific domains, including physics, biology, and finance. Although individual numerical integration steps are inexpensive, observing meaningful events or transitions can require millions of sequential steps, resulting in substantial wall-clock simulation time and poor hardware utilization. Deep learning offers an alternative by amortizing many integration steps into a single neural network forward pass, potentially enabling much faster simulation. However, existing supervised approaches typically require long simulated trajectory data, which restricts their applicability. In this work, we introduce Kolmogorov-Chapman Maps (KC-Maps), a method for learning the transition kernel of an SDE that relies only on the trajectory-free marginal samples together with the known drift and diffusion coefficients. Given an initial time and state of a process, KC-Maps models its distribution integrated to any given time, corresponding to the weak solution of the SDE. To recover the correct dynamics, KC-Maps satisfies two key properties: (i) it satisfies the boundary conditions, which we incorporate directly into the neural network architecture, and (ii) it respects the Kolmogorov--Chapman equation, which provides an efficient training objective. We empirically demonstrate that KC-Maps learns to integrate the dynamics of peptide molecular systems and outperforms classical molecular dynamics in terms of GPU-hours.

---


### 520. [Guiding Data Allocation for Robust Subpopulation Generalization](https://arxiv.org/abs/2611.12884)

**<font color=#1a73e8>作者：</font>** Zhaoying Pan, Yipei Wang, Shenyu Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models often achieve high average accuracy in the training data while performing poorly on test data due to subpopulation shift. A common data-centric solution is to enforce balanced subgroup proportions, but full balance can be costly, infeasible, and not always necessary. In this work, we study whether balanced training data is the unique optimal configuration for robust subpopulation generalization. We extend a Gaussian feature-model framework to theoretically characterize the performance landscape across general training subgroup distributions. We show that multiple configurations, including substantially imbalanced ones, can perform comparably to the balanced one. We further derive gradient-based directions for adjusting subgroup proportions to improve adjusted accuracy and worst-group accuracy more efficiently. These findings suggest that strategically allocating data offers a more flexible and principled path to robust performance than simple balancing. The code is available at this https URL.

---


> [!TIP]
> 当前位于：**501-520**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-520**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
