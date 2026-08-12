# 📦 其他研究 | 2026年08月13日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

---

### 151. [Physics-informed Diffusion Generative Model for Time-Series Data Synthesis in Dynamic Systems](https://arxiv.org/abs/2608.10941)

**<font color=#1a73e8>作者：</font>** Haiteng Wang, Yunfei Zhu, Tao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial time-series signals, such as turbine temperature and rotational speed in aero-engines, are essential for monitoring the health and operational status of complex dynamical systems. However, collecting such data is often limited by harsh environments (e.g., high temperature and high pressure) and the high cost of experimental testing. To address this challenge, we introduce PhysDGM, a stepwise physics-embedded diffusion generative model for synthesizing time-series data that are consistent with the underlying physical laws of dynamical systems. PhysDGM embeds physical laws directly into each reverse diffusion step of the generative process, ensuring trajectory-level physical consistency, rather than enforcing constraints only at the final output. A large-scale AI-synthetic dataset (4.4 million samples, 20x scale-up) constructed by PhysDGM demonstrates strong fidelity across 34 datasets spanning turbofan engines, aero-engines, batteries, and chemical processes. After incorporating the synthetic data, the downstream task performance substantially surpassed that using real data alone by 48% for remaining useful life prediction, 15% for health indicator estimation, 22% for state-of-health assessment, and 20% for fault diagnosis. Moreover, it requires 10-20x less training data than existing approaches, substantially reducing the high cost of data collection in dynamical systems. We further demonstrate PhysDGM's potential in identifying early-stage faults in aero-engines by incorporating AI-synthesized data. In summary, PhysDGM provides a solid foundation for generating physically consistent industrial time-series, paving the way for expanding physics-guided AI into diverse data-scarce environments, including both industrial machinery and complex chemical reaction dynamics.

---


### 152. [Multiple Scale Latents for Learned Image Compression](https://arxiv.org/abs/2608.10952)

**<font color=#1a73e8>作者：</font>** Jonas Brenig, Radu Timofte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most learned image compression systems rely on a single latent representation combined with a hyperprior, which limits their ability to efficiently capture image structure across spatial scales. In this work, we propose a hierarchical latent representation to improve the efficiency of the entropy model. By using multiple latents at different scales, each with its own entropy model, we better capture the spatial structure of the latent representation. Our experiments show that this approach achieves a 17.9% BD-rate reduction over VVC on Kodak, demonstrating the effectiveness of multi-scale latent representations. Furthermore, the approach is orthogonal to other advances in learned image compression, making it a versatile addition to existing methods.

---


### 153. [GARLIC: Graph Attention-based Relational Learning of Multivariate Time Series in Intensive Care](https://arxiv.org/abs/2608.10969)

**<font color=#1a73e8>作者：</font>** Ruirui Wang, Yanke Li, Manuel Günther 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Healthcare data, such as Intensive Care Unit (ICU) records, comprise heterogeneous multivariate time series sampled at irregular intervals with pervasive missingness. However, clinical applications demand predictive models that are both accurate and interpretable. We present our Graph Attention-based Relational Learning for Intensive Care (GARLIC) model, a novel neural network architecture that imputes missing data through a learnable exponential-decay encoder, captures inter-sensor dependencies via time-lagged summary graphs, and fuses global patterns with cross-dimensional sequential attention. All attention weights and graph edges are learned end-to-end to serve as built-in observation-, signal-, and edge-level explanations. To reconcile auxiliary reconstruction and primary classification objectives, we developed an alternating decoupled optimization scheme that stabilizes training. On three ICU benchmarks (PhysioNet 2012 & 2019, MIMIC-III), GARLIC sets the new state of the art in outcome prediction, significantly improving AUROC and AUPRC over best-performing baselines at comparable computational cost. Ablation studies confirm the contribution of each module, and feature-removal trials validate the fidelity of importance attribution through a monotonic performance drop (full > top 50% > random 50% > bottom 50%). Real-time case studies demonstrate actionable risk warnings with transparent explanations, marking a significant advance toward accurate, explainable deep learning for irregularly sampled ICU time series data. Moreover, we demonstrated \proposed{}'s superiority in data imputation and classification on various time-series datasets beyond the ICU domain, showing its generalizability and applicability to broader tasks.

---


### 154. [A Dataset and Benchmark for Optical Music Recognition of String Quartet Scores](https://arxiv.org/abs/2608.10978)

**<font color=#1a73e8>作者：</font>** Dongmin Kim, Brian Liu, Jose J. Valero-Mas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical music recognition (OMR) transcribes music scores into digital formats. While the field has advanced significantly on monophonic and piano-form scores, multi-part score transcription remains underexplored, largely due to the absence of a suitable dataset. We introduce OpenScore String Quartet for Optical Music Recognition (OSSQ-OMR), the first dataset dedicated to multi-part OMR. Built on the OpenScore String Quartet corpus, OSSQ-OMR pairs digitally encoded scores with their original scanned editions from IMSLP, with all images visually aligned to their transcriptions. The dataset is released with score images at system and staff levels, and paired transcriptions in three encoding formats: Extended Linearized MusicXML (LMXE), **kern, and ABC. In total, OSSQ-OMR contains 24,544 system images and 98,172 staff images drawn from 116 string quartet scores. We accompany the dataset with a benchmark protocol and baseline results from two representative OMR models, evaluated across four random score-level splits with mutually exclusive test sets. Baselines reach OMR-NED as low as 3.6% on synthetic and 5.9% on scanned inputs; results reveal substantial effects of encoding and segmentation choices, with the LSTM-based baseline degrading on scanned inputs roughly 2.6 times less than the Transformer-based baseline.

---


### 155. [PEAK: Precise and Persistent Concept Erasure via k-Sparse Autoencoders](https://arxiv.org/abs/2608.10985)

**<font color=#1a73e8>作者：</font>** Man Jiang, Ouxiang Li, Weibao Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Erasing concepts from large-scale text-to-image (T2I) diffusion models has become increasingly crucial due to the growing concerns over copyright infringement, privacy violations, and offensive content. Existing approaches struggle to achieve both precise and persistent concept erasure: inaccurate localization of concept-related representations may cause unintended semantic interference, while incomplete removal of the underlying concept knowledge allows adversarial recovery. To address this dilemma, we propose PEAK, a \textbf{\textit{precise}} and \textbf{\textit{persistent}} concept erasure framework via k-Sparse Autoencoders (kSAEs). PEAK first trains a kSAE on internal activations of the diffusion denoising network to decompose dense representations into interpretable sparse features. By contrasting sparse activations induced by target and non-target prompts, PEAK identifies a compact set of target-specific features according to both activation strength and frequency. These localized features are then used for parameter optimization, where PEAK selectively suppresses target-related activations while preserving complementary non-target ones towards the original model. This feature-guided optimization embeds concept erasure directly into diffusion parameters, eliminating the need for additional inference-time intervention and facilitating effective persistence against adversarial attacks. Extensive experiments demonstrate that PEAK achieves effective and robust concept erasure. On the I2P benchmark, PEAK reduces NudeNet detections from 582 to 6, lowers the average attack success rate (ASR) from 96.52\% to 5.63\%, and preserves general generation quality on MS-COCO with a near-zero KID. Our code and models are available at: this https URL

---


### 156. [Putting Registers to Work: Task Registers for Token Pruning in Vision Transformers](https://arxiv.org/abs/2608.10989)

**<font color=#1a73e8>作者：</font>** Hongsen Cao, Mona Jaber, Shanxin Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Token-pruning policies are usually designed for a single recognition pipeline, but pretrained Vision Transformers are reused across tasks with different spatial demands. We ask which parts of a pruning policy transfer across image classification, semantic segmentation, and object detection. For each pipeline, controlled probes freeze the no-pruning checkpoint and apply a series of parameter-free reduction criteria at one eligible layer at a time without retraining. The probes reveal three differences: segmentation and detection rank the criteria differently, classification is especially sensitive to attention-based pruning in the earliest layers, and the dense tasks prefer opposite recovery endpoints. These findings motivate Task-Adaptive Pruning (TAP). Existing register tokens serve as task-agnostic storage for feature artifacts. TAP instead introduces one task register per task and activates only the current one. Its evolving state ranks tokens, distributes an exact removal budget over depth, and sets the recovery scale for dense features. At a final keep rate of $\rho=0.5$, our jointly adapted model, TAP-J, reaches $47.0$ mIoU at $1.30\times$ encoder throughput on ADE20K and $53.7$ box AP at $1.32\times$ encoder throughput on COCO while remaining competitive on ImageNet-1K.

---


### 157. [HNDiff: Haze-Noise Diffusion for Image Dehazing](https://arxiv.org/abs/2608.10995)

**<font color=#1a73e8>作者：</font>** Jin-Ting He, Fu-Jen Tsai, Yan-Tsung Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing diffusion-based methods have recently made significant progress in image dehazing. However, they typically neglect the physics of haze formation and reconstruct clean images from pure Gaussian noise, thereby limiting their restoration potential. To address this issue, we propose Haze-Noise Diffusion (HNDiff), a novel diffusion framework that embeds the atmospheric scattering model as an inductive bias. By grounding diffusion in physical principles, HNDiff ensures that the restoration aligns more closely with underlying mechanisms of haze formation. In its forward process, we introduce joint haze-noise diffusion with a haze-aware noise scheduler, which progressively adds both haze and noise to an image. Essentially, the scheduler adapts noise levels according to haze density, meaning that regions with heavier haze receive stronger noise injection to encourage content generation, while clearer regions receive lighter noise to better preserve details, which directly links the forward degradation process with the physics of haze. In the reverse process, we then derive a physically consistent dehazing-denoising process that simultaneously removes haze and noise to restore a clean image in a manner aligned with the forward degradation process. To further enhance practicality, we propose Latent HNDiff, which compiles clean latent priors that can be seamlessly integrated into existing dehazing networks to boost performance. Extensive experiments show that our work significantly improves leading dehazing backbones and achieves state-of-the-art results on benchmark datasets. The project page is available at this https URL .

---


### 158. [On the Limitations of Cross-Lingual Consistency in Multilingual Text-to-image Generation](https://arxiv.org/abs/2608.11002)

**<font color=#1a73e8>作者：</font>** Sicheng Zhang, Zhonghao Yan, Binzhu Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) generation has achieved remarkable progress in recent years. However, existing research has largely focused on English-only settings, leaving cross-lingual performance gaps and language-specific effects insufficiently explored. To fill this gap, we introduce LingT2I, a benchmark covering 10 widely used languages with 33K prompts, designed to evaluate cross-lingual effects in both content generation and text rendering. Building on this benchmark, we conduct a comprehensive cross-lingual analysis, uncovering linguistic inequality and language-dependent trade-offs across evaluation dimensions. Beyond quantitative evaluation, we further reveal a range of language-dependent generation patterns, highlighting how linguistic factors and their corresponding cultural contexts systematically impact model outputs. Our benchmark and analysis provide a foundation for studying cross-lingual behavior in T2I generation and facilitate the development of more robust and inclusive models. Code and dataset are available at this https URL.

---


### 159. [R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video](https://arxiv.org/abs/2608.11017)

**<font color=#1a73e8>作者：</font>** Ke Ma, Yamin Mao, Weiming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon egocentric video is a rich substrate for wearable AI assistants, but object-centric questions such as where an item was moved, when it last changed state, or why it was relocated remain difficult because caption- and transcript-based memories rarely preserve persistent object identity or structured spatial change. Existing long-video QA methods mainly emphasize temporal grounding and clip retrieval, while prior 3D scene-graph methods typically assume stronger geometry than free-motion wearable RGB video provides, including point clouds, RGB-D input, posed views, sparse reconstruction, or reconstructed scenes. R4DSG introduces a relative 4D scene graph memory for long egocentric video. Instead of storing raw graph sequences, R4DSG converts video into compact queryable memory entries indexed by time, place, persistent objects, anchor-relative change, and local interaction context. The main idea is to separate stable anchors from dynamic objects, maintain persistent object identity across frames, and represent object state through anchor-relative transitions rather than a globally aligned world model. Built on recent RGB-only advances in promptable video segmentation, temporal propagation, and relative 3D lifting, the method produces a retrieval-ready memory directly usable for long-horizon question answering. Evaluation on a 255-question object-related subset from EgoLifeQA shows, under question-only retrieval, a 6.7-point overall gain over EgoRAG-Text and a 12.5-point gain on when questions, which highlights the value of temporally organized object memory. These results position relative 4D scene graphs as a practical memory substrate for wearable assistants, AR systems, and embodied multimedia agents. GitHub Page: this https URL.

---


### 160. [DEFT: Data-Efficient Frequency-domain Top-k Sampling via Inverse Discrete Fourier Transform for Spatiotemporal Dynamical Systems Modeling](https://arxiv.org/abs/2608.11019)

**<font color=#1a73e8>作者：</font>** Hengbo Xiao, Jiale Liu, Jiahao Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling spatiotemporal dynamical systems governed by partial differential equations (PDEs) poses two major challenges: it either requires expensive physics-based simulators that entail iterative numerical solving at high computational cost, or it depends on abundant training data, yet purely data-driven models often generalize poorly to downstream dynamic operating conditions. We propose DEFT, a frequency-domain data sampling method that identifies the dominant Fourier modes of a physical system and systematically varies the corresponding amplitudes and phases to generate physically consistent training data via the inverse discrete Fourier transform. In addition, we derive a generalization bound of this method. We note that it also provides a theoretically principled criterion for selecting $K$. We evaluate the proposed method through three sets of experiments, each targeting a distinct aspect of its utility. First, we validate the framework on canonical PDEs solving demonstrating that it outperforms traditional methods when the system is dominated by a few prominent frequency components. Second, we employ DEFT as a data-value filter on the diffusion--sorption and Burgers equations of PDEBench, showing that it reduces data requirements by $40\%$ while sacrificing less than $2\%$ in predictive accuracy. Third, to evaluate DEFT for more challenging and practically relevant problems, we validate it in the battery degradation PDE system, achieving consistently high predictive accuracy across various test datasets with $R^2$ values exceeding $0.99$. Moreover, the learned frequency-domain features transfer to other battery chemistries with only $20\%$ of the fine-tuning data. These results demonstrate that DEFT is an effective data-sampling method for efficient operator learning.

---


### 161. [Derivative Computation in PINNs: Automatic Differentiation, Finite Differences and Beyond](https://arxiv.org/abs/2608.11020)

**<font color=#1a73e8>作者：</font>** Maciej J. Mikulski, Tadeusz Uhl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We systematically investigate finite-difference (FD) derivative computation in Physics-Informed Neural Networks (PINNs) as an alternative to automatic differentiation (AD). On three benchmark PDEs we show that, with a properly calibrated step size, FD matches AD in accuracy on every problem while running faster across the full tested batch-size range and using substantially less GPU memory, and that a stochastic variant we propose outperforms AD on a stationary problem. We further show that for neural architectures with inter-sample dependencies (e.g. BatchNorm, self-attention) the standard PyTorch autograd idiom is silently incorrect; the correct per-sample alternative is computationally infeasible at PINN-relevant batch sizes, while FD provides a forward-only approximation that is empirically an order of magnitude closer to the true per-sample derivative.

---


### 162. [myMediWhisper: Construction of Burmese Medical Speech Corpus and Whisper Fine-Tuning for Clinical Dialogue ASR](https://arxiv.org/abs/2608.11036)

**<font color=#1a73e8>作者：</font>** Ye Kyaw Thu, Ye Bhone Lin, Thura Aung 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Whisper models benefit from large-scale multilingual pre-training, their performance on Burmese medical speech remains limited. This work presents a Burmese medical speech recognition framework built on a high-quality 28-hour corpus recorded and validated by native speakers. We fine-tune Whisper models using full fine-tuning (FFT) and parameter-efficient fine-tuning (PEFT) with LoRA. To evaluate robustness, we apply waveform- and spectrogram-level data augmentation under controlled noise and simulated room acoustics. While augmentation reduces performance on clean speech, it significantly improves robustness in noisy and reverberant environments across FFT and PEFT settings. Our best-performing system, fully fine-tuned myMediWhisper-Medium without augmentation, achieves a state-of-the-art Word Error Rate (WER) of 23.44%, outperforming much larger general-domain fine-tuned models. Dataset and other resources can be found at the Huggingface repository: this https URL.

---


### 163. [Multi-Level Evidence Aggregation for Robust Facial Phenotype Retrieval in Rare Genetic Disorder Prioritization](https://arxiv.org/abs/2608.11037)

**<font color=#1a73e8>作者：</font>** Alexander Hustinx, Carolin Kaffiné, Behnam Javanmardi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-assisted facial phenotyping supports rare genetic disorder prioritization by retrieving visually similar diagnosed cases from facial image reference databases such as the GestaltMatcher Database (GMDB). Existing GestaltMatcher-based retrieval frameworks compare each test image with individual gallery images in a facial phenotype embedding space. However, this pointwise formulation does not fully exploit available evidence, because patients may have multiple images and disorders may be represented by multiple diagnosed gallery patients.
We propose an inference-time multi-level evidence aggregation framework that improves facial phenotype retrieval without modifying the underlying GestaltMatcher-Arc encoder. The framework combines embedding-level patient aggregation of multiple images from the same individual, patient-weighted disorder centroids, and hybrid individual-centroid scoring to integrate test-patient observations, disorder-level gallery evidence, and local nearest-neighbor evidence.
We evaluated the approach on GMDB v1.1.4 across disorders represented during training (GMDB-Freq), unseen disorders (GMDB-Rare), and multi-image patient subsets, using a unified gallery containing both GMDB-Freq and GMDB-Rare disorders. Multi-level evidence aggregation improved mean per-disorder top-$N$ retrieval accuracy across all evaluation subsets. Top-1 accuracy increased from 38.52% to 48.82% on GMDB-Freq and from 19.38% to 23.79% on GMDB-Rare. On multi-image subsets, top-1 accuracy increased from 46.12% to 60.94% on GMDB-Multi-Freq and from 18.54% to 26.71% on GMDB-Multi-Rare.
These findings show that inference-time aggregation can improve next-generation facial phenotype retrieval without retraining the encoder, supporting a shift from isolated single-image matching toward multi-level aggregation of patient and disorder evidence for rare-disorder prioritization.

---


### 164. [Multiclass Sentiment Analysis for Identifying Political Viewpoints](https://arxiv.org/abs/2608.11049)

**<font color=#1a73e8>作者：</font>** Girma Yohannis Bade, Olga Kolesnikova, Jose Luis Oropeza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of social media has created vast amounts of political discourse, which provides valuable opportunities to analyze public opinions and identify different political perspectives. Sentiment Analysis (SA) is a core task in Natural Language Processing (NLP) that allows the computational study of attitudes and opinions in textual data, and has become increasingly important for understanding political discourse. In this work, we investigate multiclass sentiment analysis of political view- points on social media, that is to automatically discriminate multiple sentiment classes over political issues and figures. To solve this task we design and evaluate two machine-learning approaches based on XGBoost and BERT. We train and evaluate the models on a labeled dataset of political social media posts using standard classification metrics. The experimental results show that the XGBoost model reaches an F1-score of 0.2835 and the BERT- based model reaches an F1-score of 0.2806 on the test set. These results demonstrate the challenge of classifying complex and contextualized political discourse sentiment and provide a baseline for future research in multiclass political sentiment analysis.

---


### 165. [3D Weighted Geometric Graph Neural Networks for Sheep Facial Pain Assessment](https://arxiv.org/abs/2608.11050)

**<font color=#1a73e8>作者：</font>** Alam Noor, Luis Almeida, Mohamed Daoudi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning systems perform mainly within the 2D for a single image domain and take the face as a single-dimension representation, losing sight of the 3D anatomy of sheep and cross-landmark spatial relationships that are intrinsic to the clinically proven Sheep Pain Facial Expression Scale (SPFES). This paper presents the \textbf{3D Sheep Pain Facial Expression System (3D-SPFES)}, a novel, monocular depth-aware geometric graph neural network system that integrates each SPFES facial landmark, such as the ears, eyes, and nose, into 3D Euclidean space estimated from a single RGB camera by using VideoDepthAnything, thus preventing the need for specialized depth hardware. Each landmark node includes a feature vector containing its 3D spatial coordinates, estimated surface normal, and facial attribute class embedding. Edges linked to nodes are assigned weights based on an aggregate metric that combines both Euclidean distance and surface co-planarity in a 3D space. A Weighted Geometric Graph Neural Network (WG-GNN) studies this graph using $\mathcal{K} = 3$ geometry-aware message-passing layers enhanced by a scaled dot-product attention method that selectively enhances anatomically relevant inter-landmark messages. The resultant node embeddings are combined into $\mathcal{O} = 3$ pain-level clusters and integrated into a Normalized Pain Score (NPS) within the range of $[0, 100%]$ a confidence-weighted, SPFES-derived scoring method.

---


### 166. [HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation](https://arxiv.org/abs/2608.11051)

**<font color=#1a73e8>作者：</font>** Raphael Lorenzo-Louis, Fabio Amadio, Bertrand Luvison 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As robots increasingly operate in human-populated environments, anticipating human intentions is essential for enabling proactive and socially aware behavior. Automatic anticipation of human-robot interactions is thus emerging as a crucial perception challenge for embodied agents. To this end, we introduce HUI360, the largest dataset for human-robot interaction anticipation in the wild and its set of baselines. The dataset was collected from a mobile robot, in the wild, over multiple days within a 3-month period, and in several environments, capturing natural, spontaneous behaviors from both passersby and users, and encompassing a diverse range of individuals. This variety enables evaluating and improving the generalization capabilities of interaction anticipation models. We designed a pipeline and share code for automatic interaction annotation in arbitrary 360-degree equirectangular videos, along with interfaces for manual refinement. Using this pipeline, we release the HUI360 open set of 1M pre-processed annotations, including detailed 2D poses, facial keypoints, and segmentation masks, obtained using state-of-the-art computer vision methods and manually curated to ensure high-quality tracking and interaction annotation. Additionally, we release the raw panoptic 360-degree images captured from the robot's egocentric viewpoint (on demand, for research purpose only in compliance with GDPR). Finally, we establish benchmark baselines for interaction anticipation, including the first cross-dataset evaluations for this task: to this end, we also release 6M annotations for another existing in-the-wild outdoor dataset collected from a mobile robot (SSUP-HRI). Dataset and code can be found at this https URL.

---


### 167. [Efficient Hypergradient Descent for Inverse Reinforcement Learning](https://arxiv.org/abs/2608.11052)

**<font color=#1a73e8>作者：</font>** Nikita Sevriukov, Anna Barabanova, Uliana Gagarina 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse reinforcement learning (IRL) aims to recover a reward function under which the resulting policy reproduces the behavior observed in expert demonstrations. A natural approach is to formulate IRL as a bilevel optimization problem, in which the inner level corresponds to policy optimization under the learned reward and the outer level measures the discrepancy between the induced policy and expert data. However, this formulation is computationally challenging in practice because the outer update requires a hypergradient involving an inverse-Hessian-vector product for the inner objective. We address this challenge by showing that, at the inner optimum, the Hessian of the inner objective is proportional to the Fisher information matrix of the policy, yielding a structured Fisher-based hypergradient closely related to Natural Hypergradient Descent. To address the resulting scalability bottleneck associated with large Fisher matrices, we approximate the required inverse-Fisher-vector product using a streaming spectral sketch, avoiding explicit construction of the Fisher matrix. We evaluate our approach against a first-order stochastic bilevel baseline across discrete- and continuous-control environments. The results demonstrate competitive policy performance and strong reward-ranking quality, while Fisher sketching reduces curvature-storage complexity and can improve computational efficiency relative to an explicit Fisher solver.

---


### 168. [A Comparative Evaluation of Deep Learning Object Detection Models on a Real-World Multi-Plant Dataset from Africa](https://arxiv.org/abs/2608.11053)

**<font color=#1a73e8>作者：</font>** Ismail Ismail Tijjani, Sunusi Muhammad Ibrahim, Amina Ibrahim Khaleel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The application of computer vision in agriculture has shown significant potential for improving crop monitoring and precision farming. However, many existing approaches rely on controlled datasets that do not adequately represent realworld farming conditions, particularly in underrepresented regions such as Africa. This study presents a comparative evaluation of six object detection models YOLOv5, YOLOv8, YOLO11, YOLO26, Faster R-CNN, and RT-DETR using a real-world dataset, AgriAISeg 1 , collected manually from Nigerian farms. AgriAISeg comprises 3,382 images of sesame, cabbage, and tomato crops captured under varying environmental conditions, including changes in illumination, occlusion, and viewing perspectives. Models were trained, and performance was assessed using precision, recall, mAP@0.5, and mAP@0.5:0.95. The results show that RT-DETR achieved the highest overall performance with a precision of 0.768 and mAP@0.5:0.95 of 0.624, while YOLOv8 and YOLO11 also demonstrated strong and consistent performance. In contrast, Faster R-CNN recorded significantly lower accuracy, with an overall mAP@0.5 of 0.466, indicating reduced effectiveness under complex field conditions. In addition, YOLO-based models exhibited superior training efficiency compared to Faster this http URL findings demonstrate that modern one-stage and transformer-based detectors provide more reliable and efficient solutions for plant detection in realworld agricultural environments.

---


### 169. [Uncertainty-Aware Deep Learning for Genomics Applications: Insights from an Empirical Study](https://arxiv.org/abs/2608.11054)

**<font color=#1a73e8>作者：</font>** Sepideh Saran, Mahsa Ghanbari, Uwe Ohler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models have emerged as the standard computational tool for a wide range of applications in genomics. Yet, uncertainty quantification (UQ) -- and more specifically, the reliability of different uncertainty estimates in this domain -- has received little systematic attention. This work presents an empirical analysis of UQ in deep learning models, focusing on genomics applications. In a series of experiments, we contrast Deep Ensembles, Bayesian Neural Networks, and Monte Carlo-dropout methods. We assess their ability to quantify uncertainty in different scenarios, accounting for common dataset characteristics in two genomic application areas and modalities: sequence-to-activity models, and single-cell expression analysis. Our systematic comparison framework provides guidelines for the applicability and reliability of UQ methods in genomics, highlighting their strengths and limitations in different scenarios. We show that Bayesian Neural Networks are better at capturing uncertainty caused by strong class imbalance and out-of-distribution data in genomics, despite their computational disadvantages. Moreover, we show how uncertainty scores can be used to select high-quality predictions in protein-RNA interactions.

---


### 170. [Batch Size or Negatives? A Selection Rule for Memory-Constrained Recommender Training](https://arxiv.org/abs/2608.11061)

**<font color=#1a73e8>作者：</font>** Artyom Sabitov, Daniil Volkov, Alexey Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale neural recommender systems are typically trained with a softmax cross-entropy objective over the full item vocabulary. For a typical large number of possible items $K$, the final classification layer dominates memory, requiring $O(nK)$ logits and gradients to materialize for a batch of $n$ examples. Sampled softmax reduces this cost by restricting the objective to only $k \ll K$ candidate negative items, resulting in an $O(nk)$ memory. However, for a fixed budget $B = n k$, it remains unclear whether one should prioritize larger batches or the inclusion of more negative items.
We address this question by analyzing sampled-softmax training under a fixed memory constraint. Under standard smoothness and variance assumptions, our theoretical evidence suggests that the fastest convergence arises from an $ n \sim B, k \sim 1$ allocation. So, an actionable rule is to include as many objects as possible given computational constraints.
Our theory is supported by controlled synthetic and synthetic and four real sequential recommendation benchmarks, including MovieLens-20M. The suggested configuration achieve faster convergence and better final recommendation quality than imbalanced alternatives within the same memory constraint. These findings provide a theoretical and empirical foundation for configuring memory during the training of recommender systems. Code, reproducibility materials, and all scripts for generating figures are available at this https URL

---


### 171. [Entropy-Centric Explainable AI for Remote Sensing Image Segmentation](https://arxiv.org/abs/2608.11064)

**<font color=#1a73e8>作者：</font>** Ali Saleh, Abdul Karim Gizzini, Mohamad Ghassany 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has become a powerful approach to solving complex problems in critical domains. Many concerns arise regarding the decision-making process of its models, mainly due to deep neural networks outperforming their peers at the cost of ambiguity in feature extraction and prediction. Consequently, in critical domains such as remote sensing, where high-resolution imagery must be analyzed using black-box models, the lack of transparency limits trust in these models and, thus, their adoption. In light of this reality, explaining and understanding the complex decision-making process of AI models has become essential. Explainable AI (XAI) aims to bridge this gap by providing insights into how and why certain decisions are made. While significant progress has been achieved in explaining image classification tasks, image segmentation still offers considerable room for improvement. In this context, this paper proposes an entropy-centric XAI method for semantic segmentation. Moreover, a new XAI evaluation methodology is proposed to efficiently measure the relevance of the regions highlighted by the proposed XAI method. Experimental results demonstrate the superiority of the proposed XAI method compared with recently adapted XAI methods for semantic segmentation.

---


### 172. [Static in Frames, Dynamic in Events: Rethinking Features in Event Cameras as Motion Cues](https://arxiv.org/abs/2608.11075)

**<font color=#1a73e8>作者：</font>** Hesam Araghi, Jan van Gemert, Nergis Tomen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras capture intensity changes asynchronously with high temporal resolution, requiring novel preprocessing methods for downstream tasks. Unlike static intensity snapshots, event data inherently encode information about scene dynamics and object motion, meaning that features derived from events can exhibit behaviors with no direct analogue in frame-based vision. In this paper, we analyze two features used in event-based corner detection---the eigenvalues of the structure tensor and the spatiotemporal density values---and show that they are \emph{motion cues}. We hypothesize that these features, combined with local geometric information, can enhance motion estimation tasks. To validate this, we first theoretically analyze how the eigenvalues of the structure tensor at moving corner points relate to the direction of motion. We then design controlled experiments on a synthetic dataset, confirming that extending local geometric features with eigenvalues and density values provides complementary motion information and is robust to texture and shot noise. Finally, we integrate the proposed features into a state-of-the-art event-based optical flow network and evaluate on the real-world DSEC benchmark, where the added features consistently improve accuracy, with the largest gains in data-scarce scenarios and for lower-capacity models. The code for this paper can be found at: \href{this https URL}{this https URL}.

---


### 173. [Learning Gaussian Structure: Intervention-Guided Density Control for Feed-Forward Driving Reconstruction](https://arxiv.org/abs/2608.11077)

**<font color=#1a73e8>作者：</font>** Hang Li, Jiahe Li, Meiying Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward Gaussian reconstruction has recently emerged as an efficient approach for driving scene reconstruction. However, prevailing LiDAR-based methods preserve the initial correspondence between observed points and Gaussian primitives, treating the initialized primitive set as the final representation. Unlike optimization-based 3DGS, these methods cannot accumulate gradients during training to determine how the scenes representation should be densified. Meanwhile, the shared sparse backbone only fuses observations from different timestamps implicitly, without explicitly aggregating cross-time evidence for individual primitives. In this paper, we present Learning Gaussian Structure (LGS), a framework that enhances both Gaussian structure and primitive attributes. Our key observation is that changes in local gradient responses induced by a prune or add intervention reveal whether the corresponding structural adjustment benefits reconstruction. Based on this observation, our Gaussian Densify Policy learns a Densify Map comprising Prune and Addition Scores from controlled interventions, and directly adjusts the Gaussian structure during inference. We further develop a compact Cross-Time Point Query that explicitly retrieves and aggregates neighboring features from Gaussian primitives at other timestamps for reliable attribute prediction. Extensive experiments on the Waymo Open Dataset and PandaSet demonstrate that LGS consistently outperforms existing methods.

---


### 174. [SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure](https://arxiv.org/abs/2608.11079)

**<font color=#1a73e8>作者：</font>** Xiaofan Bai, Hongqiang Lin, Chao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents accumulate reusable skills by appending successful procedures and failure fixes. Over time, the same requirement is often restated in several branches, examples, and warnings, while common action sequences are copied rather than reused. The resulting skill becomes expensive to inject and difficult to maintain. Generic prompt compression is ill-suited to this setting because a skill is not a flat passage: its name and description define when it applies, its workflow controls execution, its tool and output contracts constrain validity, and rare exceptions may remain essential even when no sampled task activates them. Evaluation-guided compression can test these behaviors, but it introduces rollouts, cost, and dependence on the compression-time evaluation set. We present SkillZip, an evaluation-free method that compresses a skill by finding its shortest faithful structural explanation. The intuition is explain once, reference many: state a repeated rule once at the scope where it applies, factor a repeated action sequence into a shared procedure, and keep only the differences as explicit exceptions. We formalize this intuition as a typed minimum description-length objective over a skill contract and a residual, subject to a hard coverage constraint for every extracted trigger, workflow edge, tool requirement, obligation, and output field. The formulation provides simple sharing thresholds, preserves unique rare rules by construction, and supports efficient local updates. SkillZip has a one-shot mode with one structured extraction call and deterministic optimization, and a continual Zip-on-Write mode that integrates each self-evolution patch without replaying tasks or reparsing the full history. Through comprehensive experimental evaluations, we demonstrate the effectiveness and superiority of SkillZip in compression performance, generalizability, and cost overhead.

---


### 175. [RTSKG: Building a Rail Transit Station Knowledge Graph Dataset](https://arxiv.org/abs/2608.11080)

**<font color=#1a73e8>作者：</font>** Shutong Zhu, Tianxing Wu, Runfeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rail transit systems play a vital role in urban mobility and economic development. As key components of such systems, rail transit stations function as critical transport hubs that enhance urban accessibility and stimulate development in surrounding areas. City-level rail transit station related tasks (e.g., ridership prediction) require large-scale urban data, but current studies often neglect complex interactions among various urban entities in terms of data organization. In this paper, to address the above issue, we build a Rail Transit Station Knowledge Graph (RTSKG) dataset which explicitly models the spatial and semantic interactions among different kinds of urban entities, to benefit city-level rail transit station related tasks. RTSKG integrates heterogeneous urban entities, such as rail transit stations, road segments, and points of interest, with a specially designed unified schema, and is accessible as Linked Data at this https URL. Evaluations on station-area store recommendation and knowledge-enhanced ridership prediction demonstrate the effectiveness of RTSKG, highlighting its potential to support city-level rail transit station analysis.

---


### 176. [Every Packet Counts: Dispersing Information for Loss-Resilient Learned Image Compression](https://arxiv.org/abs/2608.11096)

**<font color=#1a73e8>作者：</font>** Yuhang Wei, Chuqin Zhou, Yibo Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image compression (LIC) has achieved impressive rate-distortion performance. However, existing methods remain highly vulnerable to packet loss, a common challenge in satellite and emergency communications. This vulnerability stems from non-uniform information distribution at the packetization stage and sequential decoding dependencies at the entropy coding stage. We propose an end-to-end loss-resilient image compression scheme that addresses both. Before packetization, we introduce an Inter-Channel Redistribution (ICR) mechanism to redistribute channel energy, preventing critical information concentrating in a small subset of channels. Then, an Interleaved Channel Grouping (ICG) strategy partitions latent channels in a strided manner to disperse information across packets, with each packet kept within constrained sizes. To limit cascading errors from lost packets, we adopt a two-layer dual-branch autoregressive structure to shorten the dependency chain. Extensive experiments demonstrate that our method consistently outperforms existing approaches in both reconstruction quality and stability. At 20% packet loss, it achieves an average PSNR gain of 1.84 dB over LossResilientLIC while reducing PSNR variance by an order of magnitude. Notably, trained under uniform random loss only, our model generalizes to bursty loss modeled by the Gilbert-Elliott channel, outperforming methods explicitly trained for such conditions.

---


### 177. [Two-stage Odd Residual Flows for Mean-Preserving Probabilistic Time Series Forecasting](https://arxiv.org/abs/2608.11114)

**<font color=#1a73e8>作者：</font>** Kiran Madhusudhanan, Christian Klötergens, Lars Schmidt-Thieme 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic forecasting plays an essential role in risk-sensitive decision-making, particularly in long-horizon settings. However, existing approaches often face a fundamental trade-off between distributional flexibility and accurate mean prediction. Traditional parametric methods, such as Mean Variance Estimation (MVE), can suffer from degraded point accuracy when trained under joint Negative Log-Likelihood (NLL) objectives, while modern-flexible generative models, including Normalizing Flows and Diffusion Models, typically rely on costly Monte Carlo sampling and may yield suboptimal mean estimates. To address this limitation, we propose Two-stage Odd Residual Flows (TORF), a framework that decouples mean forecasting from uncertainty estimation. In the first stage, a pre-trained deterministic model is used to produce an accurate mean prediction. In the second stage, a Restricted Normalizing Flow, with strictly odd functions learns flexible residual distributions around the point forecast, guaranteeing mean preservation from the first stage without sampling. Experiments show that TORF achieves state-of-the-art deterministic accuracy (NMAE) while providing strong density estimation performance (CRPS) on short and long-horizon forecasting.

---


### 178. [AlbumentationsX: One Augmentation Pipeline for Images and Related Annotations](https://arxiv.org/abs/2608.11123)

**<font color=#1a73e8>作者：</font>** Vladimir Iglovikov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Augmentation can corrupt a training example when an image and its annotations receive different random changes. A crop must use the same coordinates for the image, mask, boxes, keypoints, stereo views, video frames, or volume. Code paths that choose these values separately can silently misalign the data.
AlbumentationsX keeps the transform list, probabilities, annotation settings, and random seed in one Compose object. Each call chooses random values once and applies them to every supported part of the training example. The library keeps each object's mask, box, and label together and lets projects add their own transforms. It can also save the pipeline definition, show what happened in one call, and run that call again.
The examples place Compose after files have been decoded into arrays and before PyTorch groups examples into a batch. AlbumentationsX executes the declared transforms. Practitioners still decide whether a flip, crop, color change, or other operation preserves the correct label for their task.

---


### 179. [Is There Really a Camouflaged Object? Towards Realistic Camouflaged Object Detection](https://arxiv.org/abs/2608.11135)

**<font color=#1a73e8>作者：</font>** Huafeng Chen, Yueming Lyu, Chenyang Si 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged object detection (COD) aims to segment objects that are visually concealed in their surroundings and has attracted increasing attention in recent years. However, most existing COD methods are developed under a closed-world assumption, where each input image is assumed to contain a camouflaged object. This assumption ignores realistic scenarios with pure backgrounds or non-camouflaged objects, causing existing models to produce severe false positives when deployed in open-world environments. To address this limitation, we propose OPC16K, a large-scale benchmark for realistic COD. OPC16K contains 16,245 images from 14 sources and is carefully organized into camouflaged-object images, pure background images, and non-camouflaged-object images, enabling comprehensive evaluation of both segmentation quality and negative-sample rejection. Based on this benchmark, we further propose OPCNet, a presence-aware camouflage network that reformulates COD from a pure segmentation task into a joint problem of object localization and camouflage existence reasoning. Specifically, OPCNet introduces hierarchical existence reasoning to distinguish CO, BG, and NOCOD scenarios, similarity-aware camouflage relation modeling to capture foreground-background camouflage cues, and existence-aware feature refinement to regulate segmentation features with existence predictions. Extensive experiments on OPC16K demonstrate that OPCNet achieves superior performance under the proposed realistic COD evaluation protocol, significantly reducing false positives on negative samples while maintaining accurate camouflaged-object segmentation. Code and dataset will be released at this https URL.

---


### 180. [sLTN: Structural Logic Tensor Networks](https://arxiv.org/abs/2608.11136)

**<font color=#1a73e8>作者：</font>** Davide Rinaldi, Luciano Serafini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logic Tensor Networks (LTN) provide a neurosymbolic framework in which first-order logic is interpreted through tensor operations, enabling logical constraints to be integrated with differentiable learning. However, the original formulation of LTN is primarily suited to data represented as flat collections of individuals, and does not explicitly capture structural organization such as temporal order, sequential position, or graph connectivity. We introduce sLTN, an extension of LTN that makes structural dimensions first-class elements of the language. Structural dimensions represent named tensor axes associated with domain-specific organization, such as time steps, sequence positions, or graph nodes. They can be quantified explicitly, related through structural relations, and used to express temporal, sequential, and relational constraints directly at the logical level. We formalize the syntax and fuzzy tensor semantics of sLTN and show that, in the absence of structural dimensions, the framework recovers the original LTN semantics as a special case. We further describe a PyTorch implementation based on a declarative signature, formula parsing, and tensorial interpretation. The framework is illustrated on representative temporal and sequential reasoning examples. This paper serves as a companion to the sltn library, available at this https URL.

---


### 181. [SAR2Agri: Learning SAR Intensity Representations for Agricultural Monitoring](https://arxiv.org/abs/2608.11142)

**<font color=#1a73e8>作者：</font>** Moti Rattan Gupta, Anupam Sobti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural monitoring faces unique challenges, arising from the landscape's complex temporal, phenological, and climate dynamics, yet monitoring them is critical for ensuring food security. Synthetic Aperture Radar (SAR) satellites offer all-weather day-night imaging capability supporting key monitoring tasks including crop type mapping, yield prediction and phenological event detection. Existing multimodal remote sensing foundation models including TerraMind and CopernicusFM learn SAR representations by grounding them in optical imagery using joint encoding and contrastive learning techniques, while SAR-specific foundation models such as SAR-JEPA, SARMAE, and SAR-W-MixMAE primarily focus on target detection, flood mapping, and land cover classification applications. Recent work has introduced phenology inspired temporal pretext tasks with optical imagery which has shown strong performance on agricultural downstream tasks. In this work, we propose the first self-supervised learning pipeline focused on using only SAR intensity imagery for agricultural applications. We improve the temporal pretext tasks through masking and curriculum learning to enhance the pretraining pipeline's ability to capture phenological features from SAR. On the SICKLE benchmark, our final model achieves 84.9% IoU on crop type mapping, outperforming optical baselines (by 15.3 pt) and existing SAR baselines (by 2.2 pt), demonstrating the effectiveness of our proposed pipeline for pretraining SAR intensity encoders for agricultural monitoring.

---


### 182. [A Recommendation System Approach for Interference-Robust Sensor Subset Selection](https://arxiv.org/abs/2608.11143)

**<font color=#1a73e8>作者：</font>** Kaan Buyukkalayci, Kyle Pak, Merve Karakas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a method for sensor-subset selection for tracking. Prior work showed that low-cost acoustic Received Signal Strength Indicator (RSSI) measurements can be used to recommend subsets of sensor nodes whose expensive sensing modalities, such as cameras, can achieve high tracking accuracy. While efficient, RSSI-based approaches are challenged by acoustic interference. We propose a recommendation-system-inspired framework that instead leverages frequency-band acoustic features and a Two-Tower Multi-Layer Perceptron (MLP) architecture to efficiently score candidate sensor subsets. Experimental results on outdoor vehicle-tracking deployments show that the proposed method can improve accuracy by around 20\% over the RSSI baseline while maintaining the low computational overhead required for real-time selective sensing.

---


### 183. [Strategies to Avoid Illegal Data Access](https://arxiv.org/abs/2608.11153)

**<font color=#1a73e8>作者：</font>** Muhammad Mubeen, Arslan Bisharat, Giri Anandhi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> For companies of all sizes, data security is a top priority. The chance of unauthorized data access increases as technology develops. To prevent unwanted access to their data, businesses must be proactive. This study examines technology solutions, personnel training, and policy enforcement as methods to prevent unauthorized data access. Data may be protected from illegal access using technological solutions like firewalls, intrusion detection systems, and encryption. Intrusion detection systems notify the administrator when suspicious behavior is found, while firewalls serve as a protective border between the internal network and the internet. Even if data is intercepted, encryption makes sure it is safe. Another effective method of avoiding unauthorized data access is employee education. Employees must be taught how to spot hazards like phishing emails and shady websites and react to them. Additionally, they should be taught the right way to utilize passwords and other security precautions. To secure data, organizations should create and implement policies. Policies should set out appropriate data and system use guidelines and provide repercussions for noncompliance. Policies should be evaluated regularly to ensure that they are current and useful. Businesses may prevent unwanted access to their data by installing technology solutions, training staff, and enforcing regulations. Organizations may reduce data breach risk and maintain regulatory compliance by taking these precautions. ...

---


### 184. [DACRI: Decision-Aware Causal Intervention Ranking for Critical Supply Chains](https://arxiv.org/abs/2608.11154)

**<font color=#1a73e8>作者：</font>** Shiqi Huang, Jiani He, Dingyan Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting or attributing a supply-chain disruption is not the same as selecting the intervention that maximizes recoverable net value. We present CriticalSCM-Bench v1, a controlled synthetic benchmark with causal ground truth, paired factual/counterfactual rollouts, and an explicit net-value objective. Relative to a full-information train-selected static benchmark, LambdaMART improves median normalized net value by 5.7--16.2\%, with paired statistical support on the semiconductor and critical-material archetypes but not on digital infrastructure. On digital infrastructure, a domain-informed constant-buffer policy remains stronger, showing that greater model complexity is not uniformly justified. Across partial and delayed settings, LambdaMART retains 33--75\% of full-clamp value. Stress tests further show that intervention fidelity, timing, cost, and held-out disruptions can alter policy ordering. Critical materials show the weakest out-of-distribution retention. Separately, a guarded explanation study over 540 generations preserves every fixed intervention decision after deterministic validation and template fallback, although exact wording remains unstable. Within this controlled setting, the results identify regimes in which adaptive ranking adds value and those in which simpler structural policies remain preferable.

---


### 185. [Hierarchical Empirical-Bayes Naive Bayes: Minimax Smoothing and Calibration with AODE Extension](https://arxiv.org/abs/2608.11162)

**<font color=#1a73e8>作者：</font>** Nguyen Thai Anh, Truong Viet Vu, Tran Thien Thanh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Naive Bayes (NB) classifier remains a standard choice for categorical data, yet its widely used smoothing rules, such as Laplace, Lidstone, Krichevsky-Trofimov, and the $m$-estimate, all prescribe a fixed smoothing strength that ignores feature cardinality, sample size, and class imbalance, inducing a non-vanishing bias on modern high-cardinality tabular data. We propose hierarchical empirical-Bayes Naive Bayes (HEB-NB), in which each class-feature conditional probability is smoothed by a Dirichlet prior whose concentration is learned data-adaptively via Type-II maximum likelihood, enabling principled information sharing across classes while retaining closed-form inference. We further introduce HEB average one-dependence estimators (HEB-AODE), showing that the adaptive smoothing transfers cleanly to structural relaxations of NB. Theoretically, we establish a non-asymptotic $\ell_1$ error bound for HEB-NB matching the empirical-distribution minimax rate plus a vanishing data-adaptive bias, together with a matching Laplace-tight lower bound that yields a finite-sample, risk-level strict separation from Laplace. We further derive a plug-in excess Bayes-risk bound via total-variation tensorization and a population top-1 expected calibration error (ECE) corollary. Empirically, across 31 UCI and OpenML benchmarks, HEB-NB attains the best average Friedman rank on probabilistic metrics, with up to 22.1% log-loss reductions on high-cardinality datasets and consistent improvements of HEB-AODE over vanilla AODE. Combining HEB-NB with mutual-information weighting reduces top-1 ECE by 41%-70%, demonstrating substantial gains in probabilistic accuracy and calibration.

---


### 186. [From Interpretability to Control: Insights from Six Years of the TrustNLP Workshop](https://arxiv.org/abs/2608.11171)

**<font color=#1a73e8>作者：</font>** Rahul Gupta, Abhinav Mohanty, Anaelia Ovalle 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Workshop on Trustworthy Natural Language Processing (TrustNLP), co-located with major ACL conferences since 2021, has grown from 8 proceedings papers to 41 over six editions, documenting a field-wide transition from post-hoc interpretability of static models to mechanistic understanding and proactive control of generative systems. We synthesize insights from all 144 proceedings papers, classifying them along six trust dimensions grounded in established frameworks (TrustLLM, DecodingTrust). We observe co-occurrences with capability emergence. The release of the first high-impact chat models activated all trust dimensions simultaneously, while subsequent model generations shifted focus toward truthfulness and safety alignment. Analysis from the classification study reveals that truthfulness is the fastest-growing dimension (absent in 2021-2022, comprising 37% of papers by 2025-2026), fairness remains the most consistent theme, and explainability exhibits a U-shaped trajectory; declining as post-hoc methods lost relevance but resurging in 2026 through mechanistic interpretability. A cross-venue comparison with ACL, NAACL, EACL, and EMNLP (~2K papers) in the same period shows that TrustNLP's topical distribution closely follows the field average. We identify four structural insights and conclude with actionable directions for the research community.

---


### 187. [Long-Horizon AI Research for Grothendieck Constant: A Case Study in Human-AI Mathematical Collaboration](https://arxiv.org/abs/2608.11195)

**<font color=#1a73e8>作者：</font>** Alan Li, Rahul Saha, Anton Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly used in mathematics research, but it is often unclear how to use them effectively. Towards this, we present an extensive case study of how AI was used to improve bounds on the Grothendieck constant $K_G$, which captures the hardness between combinatorial problems and their continuous relaxations. Specifically, while the precise value of $K_G$ is not known, we recently tightened the best known bounds to \[
\frac{6\pi}{11}
\;\le\;
K_G
\;\le\;
\frac{\pi}{2\log(1+\sqrt2)} - 10^{-4}. \] Crucially, these improvements were achieved using an AI research system that could arrive at insights deemed novel by domain experts. We give a detailed discussion of our experience using AI for mathematics research, particularly touching upon its strengths and weaknesses, as well as our experience with creating ideal conditions for AI to arrive at breakthrough insights.

---


### 188. [Capturing Uncertainty in Human Motion for Representation Learning in Soccer](https://arxiv.org/abs/2608.11203)

**<font color=#1a73e8>作者：</font>** Yizhou Xu, Lars Bretzner, Tiesheng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a self-supervised representation learning framework for understanding 3D skeleton-based human motion in soccer, using future motion prediction as the learning objective. Since human motion is inherently uncertain, accounting for multiple plausible futures is essential for capturing the underlying motion dynamics and learning effective representations. To this end, we introduce a conditioning module for motion prediction that models a probabilistic distribution over discretized future motions in 3D Euclidean space, learning multimodality with explicit supervision from future trajectories. Experiments on large-scale soccer player tracking data show that our approach substantially improves motion prediction accuracy. Moreover, the learned representations effectively transfer to multiple soccer downstream applications, demonstrating strong cross-task generalization.

---


### 189. [AdvFD: Boosting Visual Generation via Adversarial Fr'echet Distance Loss](https://arxiv.org/abs/2608.11205)

**<font color=#1a73e8>作者：</font>** Mingju Gao, Jingkai Zhou, Kun Gai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fréchet distance has recently emerged as an effective distribution-level objective for generator post-training, complementing the conventional sample-level diffusion and flow-matching losses. However, directly optimizing Fréchet objectives can cause Fréchet hacking. The target metrics keep improving, but visual quality and Fréchet alignment in other feature spaces may stagnate or deteriorate. We attribute this failure to the static pretrained feature spaces used by existing Fréchet losses. These feature spaces provide incomplete and fixed views of the differences between real and generated distributions. To address this limitation, we propose Adversarial Fréchet Distance (AdvFD), which complements the static representation targets in FD-Loss with a calibrated adversarially learned representation. AdvFD augments the original static Fréchet objective with a learnable representation that adversarially maximizes the Fréchet discrepancy between real and generated samples, while the generator minimizes the same discrepancy in the resulting adaptive feature space. To prevent the adversarial representation from trivially increasing the objective through feature amplification, we further introduce real-feature whitening, which normalizes its scale and covariance geometry and stabilizes the min--max optimization. Extensive experiments show that AdvFD consistently improves one-step generator post-training across both JiT and pMF backbones and across different model scales.

---


> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
