# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 151. [Frequency-Domain Membership Inference Does Not Beat Confidence Thresholding: A Band-Resolved Analysis of Why](https://arxiv.org/abs/2610.24643)

**<font color=#1a73e8>作者：</font>** Mohammad Zare, Pirooz Shmamsinejadbabaki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A widely repeated account of membership inference holds that models lean on fine-grained detail for samples they have memorized, so degrading an input's resolution should expose membership through how quickly a prediction falls apart. We test that account band by band. A monotone family of zero-phase low-pass filters is applied to each query image, the target's confidence on its original prediction is read at every step, and the resulting decay is scored in a dozen ways. Two federated ResNet-18 targets are studied, one trained normally and one pushed to a 45.1-point generalization gap. The account does not survive. On the normally trained target the best profile score reaches an AUC of 0.513 against 0.537 for a single confidence threshold, and on the overfit target 0.735 against 0.943. A search over 1206 candidate scores, with direction chosen on a held-out half and a fitted combination as an upper bound, produces no score that beats the threshold in either regime. The failure has a mechanism: the mean confidence gap between members and non-members grows as detail is removed, exactly as the hypothesis predicts, but the spread grows faster, so discriminability falls from the first step onward. Decomposing each image into phase and magnitude shows why no band-localized operation can work, since the advantage travels with image structure, surviving at 0.567 when the phase is kept and collapsing to 0.492 when only the magnitude is. Membership is a whole-image identity effect rather than an accumulation of spectral energy in any band, and defenses aimed at high-frequency reliance are aimed at the wrong target.

---


### 152. [Modeling Uncertainty Propagation in 3D Morphable Models](https://arxiv.org/abs/2610.24646)

**<font color=#1a73e8>作者：</font>** Megh Shukla, Edo Collins, Prashanth Chandran 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the problem of mapping parameter-space variance of a 3D Morphable Model (3DMM) to per-vertex variance. Traditionally, per-vertex variance has been used to visually interpret the learnt parameter uncertainty. However, mapping parameter-space variance to per-vertex using sampling or error propagation is computationally expensive. We address this limitation with Closed-form Local Uncertainty Estimation (CLUE), which transforms the parameter-space distribution of 3DMMs to per-vertex through a closed-form approximation. CLUE emerges from applying the law of total variance to the 3DMM formulation and is modular, computationally inexpensive, and accurate. Subsequently, we study integrating CLUE for in-the-wild human mesh recovery training and inference. We note that CLUE uses the geometry of the mesh as an inductive bias when predicting the variance, leading to improved accuracy. Through extensive qualitative and quantitative experiments, we show that when used in training, CLUE (1) outpeforms probabilistic and deterministic baselines on metrics evaluating joints, mesh and uncertainty, and (2) has the highest uncertainty-to-error spearman correlation, with applications including data mining and interpretable uncertainty. Finally, we share SAM 3D Body (CLUE) which augments the regressor with high resolution uncertainty maps. We make our code available at this https URL

---


### 153. [From Prediction to Action: Population Health World Model for Digital Medicine](https://arxiv.org/abs/2610.24662)

**<font color=#1a73e8>作者：</font>** Xike Xie, Yu Li, Weizhong Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital medicine now captures data that traces individual health trajectories and reveals population health dynamics through electronic health records, claims, remote monitoring, wearable devices, mobile devices, social sensing data, medical images, etc. But much of its modeling still centers on task-specific, outcome-specific, and prediction-specific estimation. The next frontier is not simply better prediction, but action in an evolving health world shaped by multiple decision-makers, heterogeneous populations, resource constraints, and feedback in care delivery. This is why digital medicine now needs world models: not only to estimate what will happen, but to represent how actions change what can happen next -- whom to prioritize, how to allocate scarce resources, how to adapt care across subgroups, and how interventions reshape future health trajectories and population dynamics.
We call such a model population health world model (PHWM): a more foundational representation of an evolving health world in which health states, individual trajectories, population health dynamics, interventions, constraints, and feedback are intrinsically coupled. Building a PHWM endows three unmet structural gaps in current digital medicine: dynamic health-state modeling, population-level intervention intelligence, and validation, equity, and governance for action-oriented use. We argue that addressing these gaps requires three minimal capabilities: representation learning under action-dependent observation, multi-scale intervention intelligence, and validation with explicit decision boundaries, while highlighting the importance of social, contextual, and public-health sensing data for action-oriented digital medicine.

---


### 154. [Knowledge Diversion: A Novel Paradigm for Pre-training Decomposable Image Generation Models](https://arxiv.org/abs/2610.24664)

**<font color=#1a73e8>作者：</font>** Yucheng Xie, Fu Feng, Ruixiao Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale pre-trained models have become foundational to modern machine learning, yet conventional pre-training objectives primarily optimize source-domain performance without explicitly considering downstream requirements. Consequently, transferable and task-specific knowledge remains entangled within a shared parameter space, limiting selective knowledge reuse and efficient downstream adaptation. This limitation is particularly consequential for image-generation models, which must accommodate diverse conditions and domains. To address this challenge, we introduce Knowledge Diversion (KDiv), a condition-aware pre-training paradigm for learning inherently decomposable generative models. Before pre-training, KDiv factorizes randomly initialized weights into rank-one Knowledge Units, which are organized into learngenes and tailors. During pre-training, continuous condition-aware routing consolidates knowledge shared across conditions in learngenes while directing condition-dependent variations to tailors. This structured organization enables learngenes to capture transferable generative priors and tailors to develop condition-specific expertise, allowing the resulting model to be selectively recombined for diverse downstream conditions. Extensive experiments across class-, text-, and image-conditioned generation demonstrate that KDiv consistently matches or surpasses dense baselines at comparable pre-training cost and achieves the strongest average downstream performance with a trainable parameter budget comparable to low-rank adaptation methods.

---


### 155. [MESS: Multi-Exposure Sequence Synthesis for Generalizable Image Enhancement](https://arxiv.org/abs/2610.24680)

**<font color=#1a73e8>作者：</font>** Ruodai Cui, Shuaizheng Liu, Rongyuan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the significant progress in image enhancement under adverse illuminations, such as low-light image enhancement, exposure correction, and backlit image enhancement, existing models show limited generalizability to different scenarios. A major bottleneck lies in the lack of large-scale and diverse training data, as these tasks typically rely on manually captured, precisely aligned image pairs that are expensive to scale up. Although synthetic data have been explored as an alternative, existing synthesis methods are limited in modeling complex adverse illumination conditions and camera imaging pipelines. To address this issue, we propose a novel framework to synthesize realistic training pairs for generalizable image enhancement in the wild. Specifically, we first derive multi-exposure sequences (MES) from high-bit RAW images by rendering them under different exposure settings through an emulated ISP pipeline. Using these RAW-derived MES as supervision, we train a diffusion-based RGB-to-MES generator to synthesize plausible exposure sequences from a single 8-bit RGB image, extending the synthesis pipeline from limited RAW collections to large-scale in-the-wild RGB data. For each source image, we randomly sample one synthesized exposure variant as the degraded input and use the original high-quality RGB image as the target. With the proposed MES Synthesis (MESS) approach, we construct a dataset of 500K training pairs and train a lightweight network, which demonstrates significantly better generalization performance than existing models across various image enhancement tasks. Code and data are available at this https URL.

---


### 156. [MM-LeJEPA: Correlated Gaussian Regularization for Multimodal Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2610.24681)

**<font color=#1a73e8>作者：</font>** Haowen Bai, Rui Gong$, Meichen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LeJEPA derives an isotropic Gaussian embedding target by minimizing, under its task assumptions, a Fisher information criterion that controls the task-averaged squared prediction bias. This enables unimodal self-supervised learning without reconstruction decoders, exponential-moving-average teachers, or contrastive negatives. However, its isotropic task prior does not account for the cross-modal structure of multimodal tasks that read shared content. We introduce MM-LeJEPA by extending LeJEPA's task assumptions to multimodal learning. Specifically, we model multimodal tasks as strength-weighted combinations of components that read independent information from the two modalities and components that read the same content from both. Under explicit gradient-moment, correspondence, and symmetry assumptions, we derive a correlated Gaussian target that minimizes a weighted Fisher information functional under a fixed total variance constraint. An analytic transform adapts Sketched Isotropic Gaussian Regularization (SIGReg) to this target, yielding a two-term objective that combines distributional regularization with local-to-global prediction. The extension adds a single scalar hyperparameter, the target cross-modal correlation, and retains the simplicity of LeJEPA. On public audio-visual classification benchmarks, our results are competitive with representative open-source methods. Code will be released.

---


### 157. [Contrastive Adversarial Training for Robust Graph Neural Networks under Label Poisoning](https://arxiv.org/abs/2610.24685)

**<font color=#1a73e8>作者：</font>** Manshika Charvi Bissessur, Melis Ilayda Bal, Michael Muehlebach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are effective for modeling relational data but are vulnerable to label poisoning, where a small number of corrupted training labels can propagate errors across the graph via message passing. Despite this risk, defenses against label poisoning remain underexplored: existing methods are primarily designed for label noise and often rely on robust losses or heuristic data cleaning that fail to distinguish adversarial poisoning from naturally hard examples. In this paper, we propose CoLAT (Contrastive Label-flipping for Adversarial Training), a novel contrastive adversarial training framework tailored for robust node classification on graphs. The core of our approach is a structure-aware detection model that uses contrastive learning to identify label-structure inconsistencies. Unlike prior contrastive methods that focus on representation learning, CoLAT leverages contrastive embeddings to select high-risk nodes that guide adversarial label-flipping during training. This alternating optimization not only performs structure-aware adversarial training but also implicitly sanitizes some corrupted labels, improving robustness against diverse attacks from the literature. Extensive experiments on multiple benchmarks show that CoLAT consistently outperforms existing defenses under various poisoning intensities while scaling efficiently to large graphs.

---


### 158. [Geometry-Aware Interpolation for Inverse Problems](https://arxiv.org/abs/2610.24687)

**<font color=#1a73e8>作者：</font>** Pourya Shamsolmoali, Masoumeh Zareapoor  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering missing visual information from incomplete or degraded images remains a challenging problem, particularly when spatial variations and complex image structures affect reconstruction accuracy. Although Spatial Transformer Networks (STNs) facilitate spatial feature alignment, their reliance on conventional linear or bilinear interpolation limits their ability to capture the underlying geometric characteristics of image data. Furthermore, interpolation based on a restricted set of neighbouring pixels can introduce inconsistencies in gradient propagation, potentially affecting optimisation stability. To address these limitations, we propose a Geometry-Aware Interpolation Network (GAIN), a variational autoencoder-based framework that incorporates manifold geometry into spatial transformation and image reconstruction. Rather than estimating pixel intensities solely from fixed spatial neighbours, GAIN exploits the local tangent structure of the data manifold to construct geometry-informed intensity approximations. An entropy-based regularisation mechanism further guides the estimation of spatial transformation parameters, promoting more adaptive interpolation. In addition, a convolutional normalisation strategy is introduced to regulate the magnitude of non-zero activations and improve gradient stability during training. Extensive experiments on challenging image completion and classification benchmarks demonstrate the effectiveness of GAIN in improving predictive accuracy while reducing computational cost compared with existing methods.

---


### 159. [Spherical Physics-informed Neural Operator with Multi-scale Coupling for Meteorological Downscaling](https://arxiv.org/abs/2610.24708)

**<font color=#1a73e8>作者：</font>** Yiqiang Ye, Yichi Wang, Haodi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Meteorological downscaling is crucial for high-resolution regional climate forecasting and disaster early warning. While neural operators have emerged as a promising paradigm for modeling complex spatiotemporal mappings, existing frameworks often struggle with spherical manifold geometric distortions, inherent atmospheric multi-scale coupling mismatches, and lack of explicit atmospheric laws. We propose the Spherical Physics-informed Neural Operator, which utilizes a Spherical Laplacian Decomposition to partition atmospheric fields into hierarchical frequency components, maintaining exact point-wise correspondence across scales. To evaluate these representations at arbitrary locations, we introduce a localized spherical integral operator that approximates continuous kernel transforms via geometry-aware attention. Dynamical consistency is further enforced by embedding differentiable constraints into the learning process. Extensive experiments demonstrate that our framework attains superior accuracy and zero-shot generalization across various meteorological variables and unseen queries, representing a robust and interpretable solution for global-to-regional meteorological downscaling.

---


### 160. [SQuIREL: A Context-Relative Framework for Measuring Entity Richness in Wikidata](https://arxiv.org/abs/2610.24709)

**<font color=#1a73e8>作者：</font>** Michelle Nwachukwu, Albert Meroño-Peñuela, Martim Brandão  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wikidata is a large, heterogeneous knowledge graph and applying data quality metrics requires context-specific approaches. The "richness" quality metric is currently under-researched and typically restricted to the ontology level, which fails to capture entity-specific structural depth. To address this gap, we introduce SQuIREL, a method that measures richness directly at the entity level using six dimensions: Semantic Specificity, Qualifier Density, Internal Connectivity, Reference Provenance, External Network Connectivity, and Linguistic Accessibility. These dimensions are kept disaggregated to preserve actionability for targeted editorial intervention. We apply this metric to two case studies of oil paintings (Brazilian vs. French) and writers (grouped by citizenship and gender) to demonstrate how it surfaces representational inequalities that may indicate systemic bias. Our metric successfully distinguishes between highly tailored and basic entity profiles, revealing nuances that raw counts and existing aggregate scores obscure. Specifically, it identifies structural imbalances, such as 48% of Brazilian paintings clustering as low-richness stubs against 0% in the French cohort, as well as intersectional patterns, including contrasting gender gaps between UK and Nigerian writers.

---


### 161. [Neuro-Inspired Inhibitory Message Passing for Accurate and Token-Efficient Multi-Agent Reasoning](https://arxiv.org/abs/2610.24718)

**<font color=#1a73e8>作者：</font>** Nima H. Siboni, Magdalena Springer, Vahid Rostami  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems promise to solve problems by bringing together information beyond the reach of any individual agent. Retrieval and tool use can distribute this information across agents, making communication essential to collaboration. A central challenge is keeping crucial evidence visible in each agent's context as messages accumulate. Repeated information can crowd out rare, decisive evidence. Models of cortical circuits suggest a principle for addressing this imbalance: inhibition can selectively suppress shared inputs while preserving sensitivity to weaker signals. We adapt this principle into inhibitory message passing, a training-free communication router that cancels redundant evidence separately for each evidence sentence and receiver. Each round, it forwards evidence sentences restated in agents' messages, delivering each at most once to receivers whose own evidence lacks it and excluding the senders' reasoning and answers. Against standard message passing, accuracy in peer groups rose by 39-77 percentage points across three benchmarks, and tokens per run fell by 10-46%. Gains held across seven open models spanning four to thirty-two billion parameters and two commercial models, in groups up to sixty-four agents, and across multi-agent architectures including peer-to-peer, orchestrator-worker, and multilevel hierarchical organizations. These findings support a scalable design pattern for more accurate and token-efficient multi-agent reasoning.

---


### 162. [Tensor Network Datamodels for Training Data Attribution](https://arxiv.org/abs/2610.24721)

**<font color=#1a73e8>作者：</font>** Farzaneh Heidari, Md Rifat Arefin, Louis Jaburi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Datamodels predict how a model's behavior changes when different parts of its training data are included or removed. However, linear datamodels assign fixed contributions to training units and cannot represent non-additive joint effects. We introduce Tensor Network Datamodels (TNDMs), which use low-rank tensor networks to model dependencies among training units while keeping the representation compact. TNDMs learn a map from subsets of the training data to the outcome of training on those subsets, allowing them to represent interactions among several training units. We prove that complementary and redundant training groups can induce high-degree subset functions with compact low-rank representations. A single fitted TNDM can then be used for several training data questions, including predicting the effect of removing data, measuring the importance of individual training units, identifying interactions between training units, and selecting useful subsets of the training data. We evaluate TNDMs on controlled tasks designed to contain strong interactions, as well as standard fine-tuning settings for classification and reasoning. On a controlled reasoning task, TNDMs outperform every baseline while observing only half as many training subsets, and TNDM-TT reduces prediction NMSE by $89\%$ relative to the linear datamodel after observing approximately $0.0061\%$ of all possible training subsets. In factual-association fine-tuning, a single TNDM-CP raises held-out $\mathrm{R}^2$ from $0.579$ to $0.668$ over the linear datamodel. These results demonstrate that compact low-rank models improve prediction when training data effects depend on combinations of training groups.

---


### 163. [GLOSS-MT: Controllable Low-Resource Machine Translation with an Editable Dictionary](https://arxiv.org/abs/2610.24730)

**<font color=#1a73e8>作者：</font>** Mich-Seth Owusu, Stephen E. Moore, Akwasi Asare 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting a pretrained machine translation (MT) model to new terminology usually requires new parallel data and another round of fine-tuning, which is costly for low-resource languages. We ask whether controllability can be added to MT, and the fine-tuning burden reduced, without degrading the pretrained model. GLOSS-MT looks up the source's noun phrases in an offline English-Twi dictionary, replaces every phrase found by its Twi translation in place, and fine-tunes a translation model once to translate these mixed inputs. We apply the same data and pipeline to NLLB-200 (600M, 1.3B, 3.3B), OPUS-MT en-tw and TranslateGemma 4B. On a document-level English-to-Asante Twi benchmark (84 documents, four domains), every fine-tune scores above its pretrained base in chrF2 (+2.85 to +5.48), and the three NLLB fine-tunes are the best open systems (50.12-50.80). A direct controllability test on human-translated Bible passages shows that the three fine-tunes tested write 79-97% of the dictionary terms, and that replacing every dictionary entry by a different term changes the output accordingly (70-97% of the new terms appear) with no retraining. We release the models, data and code.

---


### 164. [How Does Muon Work in Private Deep Learning? Scalable Differentially Private Training via Orthogonalization](https://arxiv.org/abs/2610.24736)

**<font color=#1a73e8>作者：</font>** Alexander Gaponov, Grigory Malinovsky, Egor Shulgin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training deep neural networks requires optimizers that balance computational efficiency with formal data privacy. While orthogonalized update rules, such as the recently introduced Muon optimizer, have shown strong empirical performance and scalability, their behavior under Differential Privacy (DP) is not yet understood. In this paper, we propose DP-Muon, a differentially private variant of the Muon optimizer. By analyzing Muon's orthogonalized updates through the lens of a Linear Minimization Oracle (LMO), we show that the leading effect of per-example clipping is a positive rescaling of the gradient, to which the LMO is blind, so that only a small directional residual controlled by the centered gradient variance enters the optimization error. This yields an $\mathcal O(K^{-1/4})$ convergence rate, up to logarithmic factors, to a clipping-dependent neighborhood at a fixed noise scale and, with noise calibrated to a fixed $(\varepsilon,\delta)$ budget, the standard $(\sqrt d/(n\varepsilon))^{1/2}$ privacy--utility bound of DP-SGD, without assuming bounded gradients. Furthermore, we investigate the hyperparameter landscape of DP-Muon and document how the optimal learning rate, momentum, and batch size change under privacy. Empirically, on image classification DP-Muon matches or improves on DP-SGD and DP-Adam, whereas on language modeling the best optimizer depends on the batch size, with DP-Muon best at small batches and DP-Adam best near the privacy-optimal batch size.

---


### 165. [Gaussian Process Bandits with Paired Auxiliary Observations](https://arxiv.org/abs/2610.24737)

**<font color=#1a73e8>作者：</font>** Weibo Huang, Qing Feng, Ruihao Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is widely used for expensive black-box optimization, yet observation noise makes each evaluation less informative and slows posterior learning. Standard BO learns from costly outcomes gathered during optimization. In many applications, however, low-cost auxiliary data are available beforehand. We introduce Auxiliary-Informed Gaussian Process Bandit (AI-GPB), a variance-reduction method that combines an offline estimate of the auxiliary mean with a correction coefficient learned from paired online observations. Notably, it exploits correlation between paired observation errors without requiring the auxiliary mean to approximate the objective. We establish finite-sample GP confidence bounds and regret guarantees, including explicit cumulative and simple regret rates for Matérn kernels. Numerical experiments across continuous BO benchmarks with varied landscapes and dimensions show consistent reductions in cumulative and simple regret relative to vanilla GP-UCB, even when within-pair correlation is moderate and the auxiliary mean is estimated from noisy offline data.

---


### 166. [Editing Images into Reusable Layers via Compositional Edit-Prior Distillation](https://arxiv.org/abs/2610.24738)

**<font color=#1a73e8>作者：</font>** Wen Xue, Yong Liu, Xueheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality image editing requires precise modification of target regions while preserving the content of unrelated regions. Existing editing models produce flattened outputs that limit precise local manipulation and layer reuse, while decomposition methods typically optimize layer recovery separately from instruction-driven editing. To this end, we introduce LayerEditor, a unified framework that couples instruction-guided image editing with controllable generation of reusable RGBA layers. At its core, In-Context RGB-Alpha Token Modeling jointly represents the edited canvas and an ordered sequence of RGB-Alpha layers within a single token sequence, enabling semantic edits and explicit control over individual layer content. To retain the pretrained model's editing capability during adaptation to layered outputs, we propose Compositional Edit-Prior Distillation, which transfers its editing prior to both the edited canvas and the image composed from the predicted layers. To support training and evaluation, we construct LayerEditor-100K, a large-scale paired image-editing dataset with ordered RGBA layer annotations, and introduce dedicated benchmarks for layered editing. Extensive experiments demonstrate that LayerEditor maintains strong editing fidelity while generating accurate RGBA layers, supporting both flexible layer-level manipulation and multi-layer decomposition.

---


### 167. [Toward Collective Model Intelligence: Characterizing and Coordinating Models](https://arxiv.org/abs/2610.24739)

**<font color=#1a73e8>作者：</font>** SinapisAI Team, Jian-Dong Liu, Qun Dai 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Independently developed AI models accumulate diverse and complementary capabilities, but a growing model collection does not automatically realize Collective AI. Addressing this gap requires understanding model capabilities with limited evaluation, organizing complementary models to collaborate on diverse tasks, and executing model calls efficiently under resource constraints. We present a systematic approach to pursuing Collective Model Intelligence through three connected components. First, Model Eval constructs evidence-based capability profiles by combining query-level performance estimation with cross-domain prediction, reducing the need for exhaustive evaluation. Second, Mio (Models in One) organizes complementary model candidates and supports task-conditioned, cost-aware selection and collaboration as task requirements evolve. Third, Mos (Model Serving OS) separates model selection from execution and provides endpoint scheduling and shared model deployment and distribution. Experiments show lower capability-estimation errors under limited evaluation. Across nine public benchmarks, Mio 1.0 Lite achieves the highest average score and lowest average cost among compared methods, with per-request costs 73.7-97.5% lower than those of the best-scoring alternatives. A prewarmed shared cache accelerates model-file retrieval by up to 23.3 times. This work lays a foundation for Collective Model Intelligence by characterizing and coordinating the diverse capabilities of an expanding model universe.

---


### 168. [SecODD: Adapting the Operational Design Domain from Driving Autonomy to Autonomous Cyber Defense](https://arxiv.org/abs/2610.24741)

**<font color=#1a73e8>作者：</font>** Jina Kang, Jeong-Han Yun, Hyesong Choi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security operations centers are beginning to delegate detection, triage, and containment to Autonomous Cyber Defense (ACD) agents at execution time. Erroneous high-impact playbooks can disrupt critical services and create accountability gaps among deployers, SOC supervisors, vendors, managed service providers, and infrastructure providers. We propose SecODD, an execution-time governance framework for ACD that adapts the Operational Design Domain concept from autonomous-vehicle regulation to cyber autonomy. It defines the authorized scope of automated defensive actions, models when meaningful human intervention must remain possible, and specifies auditable due-care conditions through a Mitigation Safe Harbor. Four engineering requirements---tamper-evident logging, human-in-the-loop orchestration, rollback playbooks, and safe-state transition controls---are evaluated through a per-scenario audit matrix that illustrates how two ACD failure modes can be translated into pass/fail audit outcomes. The result is an evidence-oriented framework that authorizes ACD only when autonomous actions are bounded, interruptible, recoverable, and reconstructable from evidence.

---


### 169. [Collaborative Hand Drawing to Conceptualize Usable Privacy and Security Research Problems: Students' Perspectives (Extended Version)](https://arxiv.org/abs/2610.24748)

**<font color=#1a73e8>作者：</font>** Eman Alashwali, Joud Alraimi, Maryam Almaghrabi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this paper, we explore students' perspectives on incorporating hand drawing to conceptualize usable privacy and security research problems. We surveyed 64 female students who participated in an in-class collaborative hand drawing activity to conceptualize usable privacy and security research problems as part of a group-based student research project on usable privacy and security in an information and computer security course for undergraduate students. Our survey responses suggest that students perceived the drawing exercise positively. That is, they found it helpful in several aspects, enjoyable, and they recommend it to other students taking the course. The students also said that they would like to have such an exercise in other courses, such as Principles of Human-Computer Interaction and Fundamentals of Data Networks. Only three students mentioned downsides of the exercise, namely doubts about their drawing skills. Our results provide useful insights for educators seeking to enhance the student learning experience.

---


### 170. [CorrFlow: Self-Correcting Flow Matching](https://arxiv.org/abs/2610.24750)

**<font color=#1a73e8>作者：</font>** Hangwei Zhang, Nathan Rouillé, Chuanxia Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-matching models generate samples through iterative velocity predictions, but typically do not revisit these predictions using the intermediate representations that produced them. We introduce CorrFlow, a self-correcting flow-matching framework that reuses this information through a lightweight refiner. Under rectified-flow interpolation, the error of the one-step clean prediction equals the realized velocity residual scaled by the noise level. Motivated by this identity, the refiner learns to predict residual corrections from the base model's clean prediction, conditioning, noise level and hidden states from the same forward pass. The correction is added to the base velocity before each sampling update, so subsequent predictions are made from the corrected state. This requires no additional base-model evaluations and only one lightweight refiner evaluation per step. Our theoretical analyses establish conditions under which feature reuse outperforms raw-input affine predictors and refiner training achieves greater residual-risk reduction than continued base-model training under a matched training compute budget. Experiments on class-conditional image generation, text-to-video generation and image-to-video generation show consistent improvements over the corresponding base models, including gains in visual quality and physical consistency. Project Page: this https URL

---


### 171. [From Overparameterised Expressions to Parsimonious Models: Fisher-Geometric Pruning for Symbolic Regression](https://arxiv.org/abs/2610.24753)

**<font color=#1a73e8>作者：</font>** Veronica Guidetti, Luca La Rocca, Fabrício Olivetti de França 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Genetic programming symbolic regression (GPSR) often returns expressions that are larger than necessary, with dormant branches and finely tuned algebraic configurations that fit sampling noise. Existing complexity-control strategies, such as multi-objective size-accuracy search or information criteria embedded in the fitness function, act on syntactic representations during model search. We introduce Fisher-Geometric pruning (FGP), a post-hoc model-reduction framework that acts on fitted models and can complement these techniques.
FGP combines local information geometry at the maximum-likelihood solution with explicit compatibility tests for interpretable parametric boundaries. A taxonomy of parametric directions separates local sensitivity from proximity to reducible boundaries, enabling the treatment of unidentifiable directions and reductions through zero constraints, asymptotic limits, and signed parameter identifications. Candidate reductions are realised by symbolic contraction and refitting, then accepted only when their cross-validated predictive risk remains within a prescribed tolerance.
We evaluate FGP on controlled diagnostic problems and Pareto fronts generated by GPSR. Across both settings, FGP substantially reduces structural complexity while preserving, and often improving, out-of-sample accuracy. Comparisons with competing pruning strategies and ablations show that, by combining geometric screening, boundary compatibility, and predictive validation, FGP yields the most consistent joint gains in parsimony and generalisation.

---


### 172. [CorrCLIPv2: Harnessing Unlabeled Images for Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2610.24757)

**<font color=#1a73e8>作者：</font>** Dengke Zhang, Fagui Liu, Quan Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation aims to classify pixels without being restricted to a fixed set of categories. Although Contrastive Language-Image Pre-training (CLIP) demonstrates remarkable potential for open-vocabulary recognition, its segmentation capability is impaired by noisy inter-class patch interactions. To this end, this work proposes a unified training-free object-centric framework, named CorrCLIPv2, from three complementary aspects of patch correlation, feature representation, and output regularization. Specifically, for patch correlation, we leverage class-agnostic mask generators to explicitly disentangle inter-class interactions. Moreover, we utilize spatially-coherent features from self-supervised models to compute attention scores to mitigate mask inaccuracies. Regarding feature representation, we devise a refinement mechanism to simultaneously strengthen spatial details and semantic representation. Within the output space, we unify predictions via voting in each mask to enhance spatial consistency. To mitigate contextual bias and enhance prediction accuracy of objects, we further extend the framework by incorporating a cross-image object retrieval paradigm, which incurs minimal computational overhead. We build a memory bank of CorrCLIP-enhanced features from unlabeled images and implement a regime of multi-CLIP ensemble. By aggregating semantically consistent object features across diverse contexts retrieved from the memory bank, CorrCLIPv2 mitigates context-induced interference and obtains more robust predictions. Extensive experiments demonstrate that our approach establishes a new state-of-the-art on 10 standard benchmarks. Remarkably, it even surpasses fully supervised open-vocabulary methods across 22 multi-domain datasets. Code is available at: this https URL.

---


### 173. [Heart Signal (ECG) as Vibration Signature for Human Authentication Using TinyML](https://arxiv.org/abs/2610.24761)

**<font color=#1a73e8>作者：</font>** Yogeswar Reddy Thota, Student Member, IEEE 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ensuring data security in the era of Artificial Intelligence (AI) and deepfake technology requires robust biometric systems. Conventional methods such as facial recognition, iris scans, fingerprints, and voice recognition are increasingly vulnerable to spoofing and provide only one-time authentication at login. This study introduces an Electrocardiogram (ECG) based authentication framework, compared with Photoplethysmography (PPG), leveraging Tiny Machine Learning (TinyML) for deployment on resource-constrained microcontroller units (MCUs). The proposed method enables continuous authentication, offering ongoing verification throughout device usage, which conventional biometrics cannot achieve. It also serves as a password-free solution, reducing risks of credential loss, theft, or reuse. However, ECG signals vary with physical activity, health conditions, age, and emotional states, requiring robust signal processing and learning algorithms. To address this, efficient TinyML models were designed to mitigate recognition errors from noisy real-time data. Experiments used single-lead ECG signals (Lead I) from UofTDB, MIT-BIH Arrhythmia, MIT-BIH Noise Stress Test, and PTB databases. Spectrograms and spectral features were extracted to train Deep Neural Network (DNN), 1D CNN, and 2D CNN models within the Edge Impulse platform, achieving 98% accuracy. The trained model was converted into TinyML format and deployed on an Espressif ESP-EYE (ESP32, 240 MHz). Support Vector Machine (SVM) models were also applied for benchmarking. By analyzing the number of heartbeats required for reliable recognition, the results show that averaging multiple signals improves tolerance to noise and enhances accuracy. Overall, ECG-based authentication demonstrates strong potential as a secure, real-time, and continuously verifiable method for personal identification on wearable and edge devices.

---


### 174. [Paired-Outcome Learning for Selective Spacecraft Attitude Capture under Torque Limits](https://arxiv.org/abs/2610.24763)

**<font color=#1a73e8>作者：</font>** Donghe Chen, Jia Deng, Zehao Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Torque-limited spacecraft attitude capture requires adapting the maneuver speed to uncertain braking authority. Faster settings can reduce average tracking error while worsening individual maneuvers, making selective modification of an existing controller a baseline-relative learning problem. A paired-outcome method combines three mechanisms: physically interpretable continuation policies with different speed envelopes, separate prediction of task failure and successful-pair tracking gains, and context-dependent rejection that executes the unchanged baseline. Complete paired simulations provide labels under common plant parameters and measurement seeds; training, validation, and calibration are separated by context. Basilisk experiments use 108 development contexts, 324 labeling rollouts, and 624 evaluation episodes across 48 test contexts, including disclosed post-freeze diagnostics. The selective controller reduces aggregate integrated attitude error by 4.67% relative to the branch baseline, with 17 improvements, 31 exact ties, and no observed regressions. Always using the fast alternative achieves a 4.81% reduction but worsens 11 cases. Gains occur in principal-axis, near-axis, braking-boundary, and selected noise/drift maneuvers; general coupled cases retain the baseline. Ablations show no additional aggregate benefit from branch commitment, active querying, or score subtraction. The evidence supports a restricted empirical trade-off between average improvement and individual regression, without establishing a closed-loop safety guarantee.

---


### 175. [ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction](https://arxiv.org/abs/2610.24766)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhou, Junyuan Shang, Tianyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing Multi-token prediction (MTP) methods are auxiliary by design: the multi-horizon loss mostly trains modules attached to the backbone, and each added horizon costs another module and another pass. We propose Efficient Causal Self-Recursion (ECHO), which removes both costs. The backbone's own final layer predicts every horizon, so the supervision lands on the parameters that generate the next token, and Dynamic Depth Sampling (DDS) keeps deeper horizons affordable by drawing the training depth with probabilities that decay along depth. Future prediction thus becomes part of the autoregressive objective rather than a task attached to it, and the gains follow on both sides of it. In pretraining, added depth converts into downstream accuracy where auxiliary modules saturate, concentrating on reasoning and code at half the MTP training overhead of training every depth. At inference, the pretrained model is its own drafter: it drafts beyond the depth it was trained for, and keeps its draft-target alignment on the open-ended, high-entropy generation where post-hoc drafters lose theirs. The advantage survives a doubled token budget, a repeated pretraining run, and supervised finetuning.

---


### 176. [DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments](https://arxiv.org/abs/2610.24767)

**<font color=#1a73e8>作者：</font>** SeongJun Jeong, Junghyun Kim, Gi-Cheon Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents in human-centered environments require memory that integrates what they observe with what humans tell them over time. However, existing embodied memories are built primarily from visual experience, leaving open how dialogue with humans can be grounded in the objects encountered throughout that experience. We introduce DialogMem, a two-phase benchmark in which agents build memory from time-aligned streams of posed RGB-D observations and dialogue, and later use it for instance-level object navigation and question answering (QA). DialogMem provides 142 episodes across 27 real-world 3D scenes, with 14,193 QA pairs and 11,890 navigation instructions. We evaluate nine memory representations within a unified framework of memory formation, evidence retrieval, and reasoning for task outputs. In experiments, appending dialogue to visual memory at evaluation time substantially improves QA but yields negligible navigation gains, suggesting that relevant dialogue is present in memory but not grounded to specific objects. Controlled diagnostics show that navigation improves with link quality but falls short of ground-truth object-level memory even under perfect linking. Retrieving the correct object entry and recovering its spatial location remain further bottlenecks. These results identify three bottlenecks for dialogue-grounded embodied memory: grounding and organizing dialogue at object-level entries during formation, retrieving the correct entry, and localizing it accurately.

---


### 177. [Global Convergence in Deep Networks via the Second Law of Thermodynamics](https://arxiv.org/abs/2610.24775)

**<font color=#1a73e8>作者：</font>** Matan Tsipory, Ofir Gaash, Itamar Harel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing convergence analyses of finite-width overparameterized deep neural networks under standard parameterization often rely on parameters remaining close to their initialization and typically neglect the role of noise, despite empirical evidence that stochasticity can improve optimization and generalization. To bridge this gap, we study $L_2$-regularized continuous-time Langevin dynamics (CLD) with isotropic noise, for training feedforward networks with smooth activations. We introduce a change-of-measure inequality, inspired by the second law of thermodynamics, that enables control of key properties of the training dynamics under the time-evolving parameter distribution. Leveraging a sharpened lower bound on the minimum eigenvalue of the Neural Tangent Kernel (NTK) at initialization, we show that injected noise helps preserve NTK stability with high probability without confining the weights to a small neighborhood of their initialization. As a result, we derive a non-asymptotic upper bound on the expected training loss. Our analysis yields explicit conditions on width and noise temperature that guarantee convergence to a finite loss floor. Finally, we experimentally show the network Jacobian can change from initialization, departing the commonly analyzed lazy regime.

---


### 178. [Process-Aware Event Log Augmentation for Process Prediction under Labeled Data Scarcity](https://arxiv.org/abs/2610.24777)

**<font color=#1a73e8>作者：</font>** Sjoerd van Straten, Alessandro Padella, Marwan Hassani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Process Monitoring (PPM) forecasts future events of ongoing business processes based on event logs. However, deep learning PPM approaches are often limited by labeled data scarcity and the low variability of real-world logs. To address this, we introduce SiamSA-PPM, a self-supervised framework combining Siamese learning with statistically grounded data augmentation. It employs novel transformation methods that leverage control-flow semantics and frequent behavioral patterns to generate realistic, semantically valid trace variants, learning generalizable prefix representations without labeled supervision. Extensive experiments on real-world event logs with a wide range of variability, incorporating exhaustive hyperparameter tuning, demonstrate the value of this process-aware augmentation. Compared to state-of-the-art baselines, SiamSA-PPM achieves competitive or superior predictive performance in both next activity and final outcome prediction tasks. An open source implementation of our method is publicly available under this https URL..

---


### 179. [IndustrialCAD-1400: Benchmarking Detailed Industrial Assemblies from Text](https://arxiv.org/abs/2610.24789)

**<font color=#1a73e8>作者：</font>** Hebao Zhu, Kang An, Zhuoke Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial assemblies require more than a recognizable shape: functional parts, interfaces, dimensions and service features must satisfy a detailed request together. We introduce IndustrialCAD-1400, a text-to-CAD benchmark for this industrial setting. Its 1,400 requests combine 400 equipment categories across 40 domains with 250 four-case design families. Family requests specify a median of 17 named component or configuration roles and six explicit numeric targets; controlled variants test whether dimensions change while shared structure is retained. Task construction draws on documented manufacturer information, owner specifications and engineering guidance. Models generate geometry programs from requests, and a common Blender environment executes them to produce scenes, optional measurements, and standardized views for evaluation. A request assessment of front, isometric, and top views measures visible component, arrangement, and interface fulfillment without requiring a single reference geometry. Five stratified panels preserve complete families while covering the benchmark exactly once, enabling balanced comparisons and separating industrial breadth from controlled numerical responsiveness. In conclusion, IndustrialCAD-1400 extends text-to-CAD from recognizable part geometry to industrial assembly synthesis under joint component, interface, spatial, and numerical specifications.

---


### 180. [UniAVC: Unified Audio-Video Creation via Progressive Training and Asymmetric Scheduling](https://arxiv.org/abs/2610.24791)

**<font color=#1a73e8>作者：</font>** Kien T. Pham, Yuhao Liu, Chong Hou Choi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified audio-video creation requires a single model capable of text-conditioned joint synthesis, bidirectional cross-modal generation, and instruction-guided editing across both modalities. Existing methods rely heavily on paired corpora, which are scarce for joint generation and even rarer for editing. Consequently, they are spent learning single-branch generative and editing capabilities that abundant unimodal data could readily teach, rather than on the cross-modal coupling. Furthermore, prevailing systems apply a single shared noise schedule to both modalities, neglecting two critical limitations. First, due to the significant discrepancy in information density, video requires prolonged high noise to organize spatial and motion structure, whereas the sparser audio signal can settle earlier during the synthesis process, the dynamics a uniform schedule might compromise. Second, lockstep denoising leaves asymmetric workflows, such as conditioning on one modality to synthesize or edit another, untrained. We present UniAVC, which addresses both obstacles. It first trains each branch on unimodal dataset to full generative and editing competence, and subsequently dedicates paired data to exploit cross-modal correspondence. Modality-decoupled schedulers meanwhile warp the noise schedule independently from a shared timestep, while subtasks with one clean modality directly supervise asymmetric configurations. These settings respectively enable intent-aware editing, which preserves one modality intact while enlisting it to constrain the other, and post-inference self-refinement, which regenerates only an unsatisfactory branch against an accepted one. UniAVC thus spans multiple creation tasks from a single set of weights without task-specific adapters.

---


### 181. [From Trust Scores to Driver Decisions: An Abstaining Evidential Decision Layer for Event Validation in VANETs](https://arxiv.org/abs/2610.24810)

**<font color=#1a73e8>作者：</font>** İpek Abasıkeleş Turgut  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trust management in vehicular ad hoc networks is highly active, yet the decision that a driver needs, whether a reported event is real, has received far less attention; the schemes that make it force every decision into two outcomes, even on thin or conflicting evidence. This paper presents CREST, a vehicle-side event-decision framework that can withhold a decision its evidence does not support. Each vehicle weights the reports it holds by the trust, proximity and freshness of their senders, fuses them with Yager's rule, and decides only when the fused margin reaches an abstention threshold. Abstention is a waiting state: a vehicle still unsure at the event is resolved by an explicit application policy, which makes the trade-off between missed hazards and unnecessary detours visible. CREST requires only a scalar trust per reporter and is built here on an evidential trust model whose consensus and revocation steps are updated to support the decision layer. A single report is shown to change the decision margin by at most its weight, which bounds the influence of an attacker coalition by its trust. In a pre-registered simulation study with fourteen attacks, including position spoofing and trust-gated camouflage, and with all unspecified parameters of all systems tuned by the same procedure, CREST reduces the decision error of two published trust-based dissemination systems from 0.162 and 0.106 to 0.051. With the best-guess policy it also lowers both missed and unnecessary reroutes and outperforms the forced binary rule on both error types in every cell.

---


### 182. [Directionally Factorized Illumination with Spherical Harmonic Rotation](https://arxiv.org/abs/2610.24811)

**<font color=#1a73e8>作者：</font>** Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many real-world capture scenarios involve an active light source rigidly attached to the camera: camera flashes for dark-environment imaging, underwater vehicle lights, and endoscopic/laparoscopic medical procedures. As the camera moves, the co-mounted light moves with it, causing the illumination direction at each surface point to change across views. Neural rendering methods (NeRF, Gaussian Splatting) encode this pose-dependent illumination as surface coloration, producing appearance inconsistencies and making it harder to recover the underlying scene. We present \textbf{DaFISH}, which can be plugged into any novel-view synthesis (NVS) pipeline such as NeRF. It factorizes per-point emitted color into surface albedo and a spherical harmonic (SH)-represented illumination factor. During training, the SH illumination is evaluated directly, enabling stable joint optimization of albedo, lighting, and geometry. \textbf{DaFISH} provides analytical generalization of illumination to arbitrary camera poses without retraining. Building on the closed-form SH-to-irradiance conversion, the training pipeline is fully differentiable from SH evaluation through volume rendering. Averaged over the held-out frames of the five scenes, \textbf{DaFISH} attains the best mean PSNR (38.91\,dB), SSIM (0.9613), and LPIPS (0.0582) among all compared methods. It improves over the strongest splatting baseline as well as the closest NeRF-based baseline, while recovering the scene consistently across views compared to prior methods.

---


### 183. [SwitchSplat: Learning Discrete Object States from Casually Captured Scenes](https://arxiv.org/abs/2610.24812)

**<font color=#1a73e8>作者：</font>** Yizheng Xie, Yalda Foroutan, George Shramko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting has made high-fidelity 3D reconstruction fast and accessible, yet existing representations assume a static world. This assumption breaks down in casual captures, where a user naturally interacts with the environment -- opening doors, toggling switches, or moving objects -- introducing discrete state changes that no current framework can model. Time-conditioned dynamic methods such as 4DGS conflate when a state was observed with what state the scene is in, limiting them to replaying seen sequences rather than composing arbitrary object configurations. We present SwitchSplat, the first 3DGS representation to address this gap via a base+slot decomposition: a shared static base captures the invariant scene, while each slot independently holds the two binary states (on/off) of one interactable object. Because the assignment of Gaussians to slots is fully differentiable, the model discovers the geometry of each state directly from video, without manual annotation. At inference, the user can freely combine slot states and render the resulting scene from any viewpoint. We validate SwitchSplat on a new casual-capture dataset and show that it outperforms static and dynamic baselines in novel-view synthesis quality, while uniquely supporting rendering of state combinations never seen during capture. Project page: this https URL

---


### 184. [SL-Ground: Sentence-Level Grounding for Fine-Grained Open-Vocabulary Object Detection](https://arxiv.org/abs/2610.24814)

**<font color=#1a73e8>作者：</font>** Yang-Syu Li, Cheng-Huan Yang, Chia-Yung Jui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding-based open-vocabulary detectors provide a widely used framework for text-conditioned localization, with a phrase-grounding formulation that aligns object queries to individual text tokens and recovers class scores through token-to-class aggregation. We observe that this token-level scoring design becomes a bottleneck for fine-grained open-vocabulary object detection, where the target category is defined by a complete compositional description rather than by isolated tokens. Based on this observation, we propose SL-Ground, a sentence-level grounding reformulation for grounding-based open-vocabulary detection. Instead of scoring queries against fragmented token evidence, SL-Ground encodes each category description as a complete sentence-level representation and directly scores object queries against these representations. To evaluate fine-grained recognition across label granularity, we construct a multi-granularity Stanford Cars benchmark spanning vehicle type, brand, and car model. At the finest car-model granularity, SL-Ground raises AP over the token-level variant from 14.5 to 70.6 under matched training candidate sampling and to 86.0 with full-vocabulary training, while better preserving open-vocabulary capability and avoiding repeated prompt chunking. Beyond Stanford Cars, SL-Ground also improves FG-OVD performance, achieving the best average AP among compared methods. These results show that sentence-level grounding provides a more suitable scoring unit for fine-grained OVOD and offers a practical path toward fine-grained grounding-based open-vocabulary detectors.

---


### 185. [Compose the Horizon: Parameter-Shared Blockwise Forecasting under a Sequential-Compute Trade-off](https://arxiv.org/abs/2610.24826)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Weiheng Li, Shengda Zhuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most long-horizon forecasters emit the complete future in one pass. We ask whether a compact operator can instead be reused to emit contiguous future blocks, trading stored parameters for sequential computation. Recursive Functional Decomposition (RFD) factorizes the horizon mapping into three parameter-shared block predictions. The blocks occupy disjoint future intervals and are concatenated, not added as trend, seasonal, or residual components, and each emitted block joins the rolling context that conditions the next application. In controlled three-seed experiments, removing forward feedback hurts all four evaluated datasets while stopping gradients through it changes little, so the useful signal is the evolving forecast state itself; reapplying the shared operator helps consistently, but by less than widening it. The model uses 0.08--0.46M parameters, yet its sequential channel-wise execution is slower and more memory-intensive than an iterative baseline at high channel count. In a frozen long-context evaluation against ten strong baseline families, RFD records lower test error in 23 of 24 cells; the comparison is cross-protocol, with RFD using 512/720-step context and the baselines using 96.

---


### 186. [Recurrent Temporal Restricted Boltzmann Machines as Unsupervised Encoders for Biomechanical Movement Sequences](https://arxiv.org/abs/2610.24829)

**<font color=#1a73e8>作者：</font>** Wafi Sharif, Nicholas LaHaye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biomechanical movement recordings are continuous, high-dimensional time series, and analyzing them without manually labeling them requires representations that capture how movements evolve over time. Most unsupervised representation-learning pipelines, however, treat each observation frame independently and discard this temporal structure, while energy-based models that could capture it have not extensively been adapted to biomechanical signals. So, this paper implements the Recurrent Temporal Restricted Boltzmann Machine (RTRBM), a recurrent energy-based model, into an unsupervised encoder that maps windows of movement data to fixed-length embeddings, and tests what its recurrent structure contributes. We adapt the model to continuous-valued signals, stack it into a deep architecture, and integrate it into the SIT-FUSE segmentation pipeline. We evaluate the embeddings on simulated musculoskeletal reaching and on two real gait datasets, using clustering, reconstruction, and walking-speed classification of unseen subjects, and compare them against non-recurrent and non-probabilistic baselines, including a control that removes the recurrent connection. Clustering the embeddings recovers movement structure tied to progress toward the target without any labels, which also transfers to unseen episodes. On gait data, the embeddings outperform PCA and autoencoder baselines under a nonlinear probe. However, removing the recurrent connection does not yield a measurable loss on the reaching task, and simple per-channel summary statistics classify walking speed at least as well as the embeddings. The model is therefore a working, verified encoder for SIT-FUSE, while the evidence for a benefit of recurrence is mixed, and the learned embeddings did not outperform simple summary statistics on gait.

---


### 187. [VTF900: A 900-Subject Visible-Thermal Face Recognition Dataset and Benchmark](https://arxiv.org/abs/2610.24832)

**<font color=#1a73e8>作者：</font>** Jacob Abaare, Bianca Ianetta, Cedric Nimpa Fondje 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advancements in visible-thermal face recognition, where thermal probe (query) face images are matched against visible enrollment templates, existing benchmarks are currently limited by small gallery sizes (N $\approx$ 100 subjects). This limitation inhibits the ability to accurately evaluate visible-thermal facial recognition at scale and to report significant recognition performance metrics, which have better operational relevance. Therefore, we introduce VTF900, a large-scale visible-thermal face recognition benchmark with 900 subjects and paired imagery that includes expression, pose, and occlusion variations. VTF900 is designed to support large-scale (i.e., large gallery) evaluations across verification (1:1 matching) and closed-set identification (1:N matching) for visible-thermal face recognition. Furthermore, VTF900 specifically addresses the challenging combination of cross-spectral and cross-dataset analysis. In this paper, after training models on the ARL-VTF dataset, we provide benchmark analyses across convolutional (baseline), vision transformers, and domain-adaptive neural network architectures to assess how these methods scale. At full gallery scale (N = 900), transformer models achieve strong discriminative performance under frontal conditions (e.g., ViT-B: 97.68% AUC, 51.10% TAR@1%FAR), while domain-adaptive methods such as DPIT-ResNet50 demonstrate greater robustness under off-pose conditions (94.68%AUC, 36.08% TAR@1%FAR). Our results show that high AUC at small scale does not translate to reliable performance at deployment scale, and that pose variation significantly amplifies performance degradation. VTF900 exposes these limitations, enabling more rigorous evaluation of cross-spectral face recognition systems.

---


### 188. [Measuring Consensus in AI Agent Networks](https://arxiv.org/abs/2610.24833)

**<font color=#1a73e8>作者：</font>** Jin Gao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As AI agents become increasingly connected through networks and take on tasks that require negotiation and joint decision-making, a systematic approach is needed to assess how their views converge and what information supports their decisions. We present an evaluation framework that treats consensus formation as the evolution of publicly stated positions toward a shared region, using accumulated communication history as context. The framework tracks position trajectories, group dispersion, and information expressed in public messages. Two case studies examine staffing decisions based on distributed facts and decisions requiring agents to reconcile duplicate information and a cancelled contract. Results from 1,872 completed runs associate sharing explanations with more accurate group decisions, while the second task reveals persistent disagreement despite accurate aggregate answers. Membership-change experiments provide a complementary evaluation. By separating convergence among agents from progress toward a task's full-information answer, the framework relates decision accuracy and bounded disagreement to the information available during the exchange.

---


### 189. [PCHMR: Empowering and Benchmarking Human Mesh Recovery in Privacy-Constrained Real-World Settings](https://arxiv.org/abs/2610.24841)

**<font color=#1a73e8>作者：</font>** Zeyu Cao, Qingxuan Wu, Zhiyang Dou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning directly on user-side data is an effective way to improve the performance of widely adopted data-driven human mesh recovery (HMR) models. However, doing so for existing HMR methods often assumes aggregating user-side data from real-world HMR-deployed devices to a central training server, posing a significant privacy risk as sensitive human images are transmitted. How can human mesh recovery be evaluated and improved in privacy-constrained real-world settings? We study this question through a benchmark in which state-of-the-art HMR models are trained with federated learning and a secure-aggregation variant, neither of which centralizes raw images, and evaluated across a wide range of client-scale and data-heterogeneity settings. We document that common HMR training pipelines are built around centralized data access and quantify how representative HMR backbones behave when that assumption is removed. Furthermore, to study the data bottleneck of privacy-constrained HMR training, we propose DePoser, a local annotation and fine-tuning pipeline enhanced with depth foundation models, with which collaboratively trained HMR models can be locally tailored to the end user's distribution. On in-the-wild data, fine-tuning on DePoser annotations improves personalization accuracy, measured against DePoser-generated pseudo-ground truth. This benchmark aims to support future work on privacy-constrained HMR models and their real-world deployment and evaluation.

---


### 190. [An Impossibility Result for ETF Target Geometry, and an Equinorm Remedy for Imbalanced Analytic Continual Learning](https://arxiv.org/abs/2610.24844)

**<font color=#1a73e8>作者：</font>** Berk Sezer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analytic continual learning (ACL) methods such as ACIL and GACL fit a ridge-regression classifier head on frozen features via the Sherman-Morrison-Woodbury identity, achieving exemplar-free, exact updates. A separate line of work, Progressive Neural Collapse (ProNC), shows standard continual classifiers benefit from a progressively expanding Simplex Equiangular Tight Frame (ETF) target. It is natural to ask whether fusing the two ideas, exact analytic updates and ETF targets, would yield a better closed-form continual learner. We show this is not the case as the fusion turns out to be identical to plain one-hot ACIL. Further, Simplex ETFs are not nested across class counts, so the literal "progressively expand the ETF" construction stops yielding an ETF as new tasks arrive, and it introduces catastrophic forgetting ($4\times$ that of a classic ACIL head). We therefore separate an ETF's two defining properties, equiangularity and equinormality, and apply each on its own to the classifier weights rather than the targets, where the invariance above does not hold. Equinorm post-processing of the fitted weights recovers both tail-class and overall average accuracy across the long-tailed regime from 5:1 to 100:1 imbalance (e.g. +32.0 tail-accuracy points and +16.0 average-accuracy points at 100:1 on CIFAR-100/ViT), transferring in sign across two backbones and two datasets, at a mild cost of 5.4 average-accuracy points on CIFAR-100/ViT on near-balanced streams (below $\approx 3{:}1$). Equiangular geometry, by contrast, is exactly inert on the target side but actively harmful on the weight side, usually losing to plain one-hot. Hence, the generally useful part of Neural Collapse geometry in Analytic Continual Learning is equinorm post-processing of the weights, becoming more useful as class imbalance grows; and equiangularity is at best a no-op and induces catastrophic forgetting at worst.

---


### 191. [Arbitrary-Scale Anisotropic 3D MRI Super-Resolution with Gaussian Prototypes](https://arxiv.org/abs/2610.24858)

**<font color=#1a73e8>作者：</font>** Aditya Rastogi, Ramon Leiser, Prateek Singh 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing MRI acquisition time improves patient comfort, reduces motion artefacts, and increases scanner throughput. Clinical protocols often shorten acquisitions by sacrificing spatial resolution, particularly along the slice axis. Super-resolution can recover higher-resolution images, but existing methods are typically specialised to one scale or acquisition geometry, limiting their use across heterogeneous clinical protocols. We present GSMR3D, a continuous volumetric model that reconstructs arbitrary isotropic and anisotropic resolutions with a single checkpoint per MRI contrast. It combines a learned dictionary of anisotropic 3D Gaussian prototypes with scale-conditioned frequency encoding and an exact measurement-consistency projection, keeping reconstructions consistent with the acquired low-resolution data. We train separate models on 3,731 contrast-enhanced T1-weighted and 30,254 T1-weighted brain MRI volumes from clinical and population-based cohorts. We evaluate GSMR3D against geometry-specific specialists for isotropic, in-plane, and through-plane super-resolution using reconstruction quality and downstream tasks: brain tumour segmentation, brain-metastasis detection, and brain parcellation. GSMR3D outperforms specialists at isotropic $2\times$ and achieves better LPIPS, DISTS, and FID across all geometries, although specialists retain higher PSNR in anisotropic settings. It more faithfully preserves glioma segmentations across all geometries, achieves the highest lesion sensitivity on an independent brain-metastasis cohort, and the highest brain-parcellation agreement for isotropic and in-plane reconstruction. Reconstruction takes about 6s per volume, adding little overhead relative to acquisition-time savings. GSMR3D offers a flexible approach to MRI scan-time reduction with one model per contrast across geometries while preserving information relevant to downstream tasks.

---


### 192. [SpriteStage: Long Horizon Animation Generation via Progressive Scene Programming and Replay](https://arxiv.org/abs/2610.24869)

**<font color=#1a73e8>作者：</font>** Zhaoqi Wang, Zijian Zhang, Jiamou Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models synthesize visual sequences from text and image inputs. Extending video generation to long animations requires actions, dialogue, camera coverage, and narrative developments to remain coordinated across scenes. Executable scene programs make these decisions available for inspection. Constructing an entire story before observing its execution can leave later scenes dependent on unrealized events. We present SpriteStage, a progressive scene programming framework that builds animation through iterative enactment and engine reorchestration. Iterative enactment generates each scene from an accepted world checkpoint and narrative snapshot, executes it on a shared spatial stage, and uses runtime and visual feedback to revise the relevant actions or story beats. The accepted outcome becomes the starting state for the next scene. Engine reorchestration maps the resulting draft to production assets and engine capabilities while retaining its events, geometry, and timing. Inspection of the assembled sequence and frozen replay carry the accepted performance into the final video. Three complete animations, ranging from approximately 9.9 to 14.3 minutes, demonstrate the framework's effectiveness in producing extended narratives through scene programming and engine execution.

---


### 193. [RAFT: Redundancy-Aware Input Filtering for Temporal Graph Neural Network Training](https://arxiv.org/abs/2610.24875)

**<font color=#1a73e8>作者：</font>** Yue Dai, Sarah Zhou, Youtao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graph neural networks (TGNNs) have shown strong performance on dynamic graph learning tasks by continuously updating node memories from evolving interactions (i.e., events) and leveraging these memories for downstream predictions. As graphs grow rapidly in modern applications, training requires processing an increasing number of events; meanwhile, each event can update node memories used by later events, creating dependencies that constrain parallel execution and limit the benefits of additional computing resources. These costs motivate an upstream question: Are all events, and the dependencies they introduce, necessary for learning? We investigate this question through two roles of temporal events: prediction targets and historical events sampled as inputs. We observe that targets involving stable node memories tend to exhibit lower prediction loss, while filtering historical events associated with stable memories can retain similar training-loss trajectories in several evaluated settings. Together, these observations suggest an opportunity to identify input redundancy through changes in node memories. Building on this opportunity, we propose RAFT, a redundancy-aware input-filtering framework for TGNN training. RAFT tracks memory changes during training and uses them to guide two filters: a root-event filter removes selected prediction targets before training, and a support-event filter excludes selected historical context during sampling. Filtering inputs before their downstream preparation and processing reduces the work they trigger. Across three TGNN models and five datasets, RAFT reduces training inputs by 35.23% on average and up to 97.11%, while reducing recorded training time by up to 52.56\% with negligible changes to model precisions.

---


### 194. [Sample-Efficient Reinforcement Learning with General Utilities via Neural Dual Critics](https://arxiv.org/abs/2610.24880)

**<font color=#1a73e8>作者：</font>** Ankur Naskar, Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with general utilities optimizes nonlinear functionals of policy-induced occupancy measures. We develop a natural actor-critic method for concave RLGU objectives admitting an exact variational dual representation, with explicit constructions for a broad class of separable occupancy utilities. Rather than estimating the occupancy measure and then forming the policy-gradient pseudo-reward, our method learns this pseudo-reward directly as a function of the state-action pair using a neural critic. The critic is trained by projected stochastic updates, while multilevel Monte Carlo combines outputs across training horizons to control its bias at logarithmic expected cost. Our analysis separates conditional actor bias from estimator second moments and accounts explicitly for dual optimization, critic approximation, and neural linearization errors. Under policy-transfer, dual-stability, and local critic-regularity conditions, the method achieves $\widetilde{O}(T^{-1/2})$ global convergence above policy, critic-class, and finite-width approximation errors using $\widetilde{O}(T)$ expected environment transitions and reference samples. For a fixed critic representation, this yields $\widetilde{O}(\epsilon^{-2})$ sampling complexity above the approximation floor, covering infinite state-action spaces and occupancy utilities beyond fixed finite vectors of returns.

---


### 195. [Measuring Data Diversity with Embeddings: A Taxonomy and Benchmark for Diversity Measures](https://arxiv.org/abs/2610.24888)

**<font color=#1a73e8>作者：</font>** Cantao Su, Anna Wegmann, Esther Ploeger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diversity is a critical property of text corpora, with direct implications for training data curation, test set design, and model generalization. However, its measurement remains fragmented and poorly understood. Existing embedding-based diversity measures vary widely in how they are computed and can yield substantially different diversity scores on the same data, yet no systematic comparison of their empirical behaviour exists. We make two contributions toward addressing this gap. First, we present a taxonomy of 21 embedding-based diversity measures, organizing them into four families based on their underlying computations. Second, we introduce EmbDivBench, a benchmark that evaluates these measures along three conceptually distinct components (variety, balance and disparity) on both simulated and natural text data. Although Mean Pairwise Distance is the most commonly used measure, our experiments show that it is outperformed by several alternatives on the three diversity components, with Graph Entropy being the best choice overall. Lastly, we distil these findings into practical recommendations for diversity measure selection.

---


### 196. [Multi-Speed Field Evaluation of a Semi-Autonomous Precision Sprayer for Weed Control in Vegetable Crops](https://arxiv.org/abs/2610.24893)

**<font color=#1a73e8>作者：</font>** Md Khairul Islam, Boyang Deng, Yuzhen Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine vision-guided precision spraying is promising for sustainable vegetable production by enabling site-specific weed targeting, reducing herbicide application while protecting crop yield and quality. However, the effects of operating speed of sprayer systems on the integrated detection-tracking-actuation pipeline remain insufficiently characterized under field conditions. This study evaluated a semi-autonomous, tractor-based spraying system for targeted weed control in radish and quantified performance across three operating speeds. A five-season dataset comprising 10,599 images and 84,311 annotated instances across seven classes was curated for model development. A YOLOv11-medium model was integrated with ByteTrack tracking and a customized 12-nozzle sprayer on a semi-autonomous electric tractor. Field trials were conducted at 0.13, 0.27, and 0.45 m/s (i.e., 0.3, 0.6, and 1.0 mph) to characterize speed-dependent changes in weed detection, targeting, actuation, and crop damage. At the lowest speed of 0.13 m/s, the system achieved 94.6% mAP@50 and 93.2% recall for weed and crop detection. However, increasing platform speed substantially reduced system performance, with weed hit rate declining from 78.3% to 35.0% and crop contact rates increasing from 20.1% to 28.7%. Consequently, the system did not meet predefined commercial-viability thresholds. These results demonstrate that practical deployment requires improvements beyond weed detection alone, particularly coordinated improvements in motion-robust plant perception, spray-timing compensation, and crop-adjacent actuation precision. The identified performance bottlenecks provide specific engineering targets for advancing vision-guided precision spraying toward practical, high-speed vegetable weed management. The software programs developed in this study have been made publicly available to support future precision weeding research.

---


### 197. [Distribution-Based Regularization for Reward Fine-Tuning Diffusion and Flow Models](https://arxiv.org/abs/2610.24897)

**<font color=#1a73e8>作者：</font>** Romeo Passaro, Jeongjae Lee, Jong Chul Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward fine-tuning is an effective way to adapt pretrained diffusion and flow-matching models to downstream objectives, but aggressive optimization often leads to mode collapse and distributional drift. Existing methods attempt to control this drift with reverse-KL regularization, implemented as an $\ell_2$ penalty on the velocity field; however, this functions by indirectly constraining sampling dynamics rather than directly acting on the generated distribution. To address this, we propose DFR (Distributional Functional Rewards), which augments the task reward with a distribution-dependent, per-sample reward that acts explicitly on the generated distribution. Formally, we generalize the KL-regularized objective from expected rewards, which are linear in the model's distribution, to convex functionals of it. The first variation of this objective defines an effective, distribution-dependent reward that directly penalizes deviation from the pretrained distribution. This formulation yields additive per-sample rewards for the Fréchet distance (FD), maximum mean discrepancy (MMD), and DreamSim diversity, recovering several recently proposed rewards as special cases. Across various text-to-image fine-tuning tasks, DFR matches the peak reward of KL-tuned baselines while increasing diversity by up to 29% at equal or lower drift.

---


### 198. [Predicting Individual Differences in Lipreading From Eye-Tracking and Pupillometry During Silent Visual Speech](https://arxiv.org/abs/2610.24898)

**<font color=#1a73e8>作者：</font>** Puneet Kumar, Satyarth Malik, Gao Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lipreading ability varies widely, including among people who are hard of hearing. Although mouth-directed attention is linked to speechreading outcomes, it remains unclear how much lipreading skill can be inferred from viewing behavior and which signals carry this information. We examine whether individual differences in lipreading ability are reflected in viewing behavior during silent speech and quantify the contributions of gaze dynamics, pupil-linked signals, and spatial viewing allocation. We introduce the Lipreading Perception Study (LiPS) dataset and a tracker-independent preprocessing pipeline that synchronizes SR Research EyeLink gaze and pupil recordings with the stimuli. Twenty-four adults (age 32 $\pm$ 10 years) completed a four-alternative forced-choice silent lipreading task. An extreme-groups protocol yielded 18 participants labeled as stronger or weaker lipreaders. Each participant-trial included four aligned views: lip-region images, frame-level gaze, pupil summaries, and spatial viewing proportions. A four-branch neural network with cross-modal attention predicted labels using participant-disjoint splits and systematic ablations. The full model reached accuracy 0.680 $\pm$ 0.040 across five folds, outperforming naive fusion baselines in accuracy. The pupil and viewing-summary branch was most informative: removing it caused the largest degradation (0.618 accuracy, 0.623 AUC), while it alone achieved 0.675 accuracy. The lip-image stream contributed little to participant-level discrimination. Individual differences in lipreading are reflected in pupil-linked and frame-level gaze signals rather than in how much time a viewer spends looking at the mouth. Synchronized gaze and pupillary measures may provide objective markers of visual speech perception, warranting investigation in larger, clinically diverse populations. LiPS provides a resource for extending this work.

---


### 199. [Same Data, Different Bytes: Serialization-Invariant Integrity Checks for Agent-Published Datasets](https://arxiv.org/abs/2610.24916)

**<font color=#1a73e8>作者：</font>** Jin Gao, Maura Clark  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent networks require reliable ways for requesting agents to verify where data is located, how it can be accessed, and whether the data received matches what the data owner made available. Checksum mismatches can reflect either altered content or serialization differences that preserve data equivalence under specified rules. Data identification mechanisms for agents, such as DataFacts, describe where data can be accessed and provide checksums for checking received data against published references. We propose a serialization-invariant identification method that assigns the same identifier to data representations equivalent under explicit rules. We use DataFacts as a case study, retaining its existing checksum alongside the proposed identifier. In a controlled agent study, we compare the proposed configuration with ordinary-tool and checksum baselines across equivalent re-encodings, altered content, and unavailable references. The study includes three model tiers from each of two providers. For equivalent re-encodings, the proposed configuration increased expected-outcome rates by 80.4 percentage points over the ordinary-tool baseline and by 70.2 percentage points over the checksum baseline. The proposed configuration also increased evidence-supported rejection of altered content by 3.5 percentage points over the checksum baseline. We contribute a serialization-invariant identification method with explicit equivalence rules, an integration approach illustrated through DataFacts, and an empirical evaluation against ordinary-tool and checksum baselines.

---


### 200. [CARTA: Self-Supervised Reusable Transaction Embeddings via Heterogeneous Tokenization and Cross-Attention](https://arxiv.org/abs/2610.24920)

**<font color=#1a73e8>作者：</font>** Shreyas K. Chandrahas, Jose Munoz, Satish Babu Bellapu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acquiring fraud labels for payment transactions is expensive and inconsistent across tasks, and high-cardinality identifiers such as merchant names make one-hot feature pipelines infeasible at scale. We present CARTA, a self-supervised encoder that learns a compact 16-dim embedding from raw transactions without labels; the frozen embedding is then reused for label-efficient fraud probing and exploratory unsupervised risk stratification without retraining the encoder. CARTA uses type-specific projections with learned embedding tables for high-cardinality identifiers, trained with token excision and InfoNCE contrastive loss. On IEEE-CIS, its linear probe at 1% of labels exceeds a raw-feature probe at 100%; on IBM TabFormer (2M rows), its frozen embedding reaches GBDT AUPRC 0.508, above frequency encoding (0.411) and the merchant-dropping baseline (0.022), though fully-supervised CatBoost is stronger. CARTA is a label-free, reusable representation that complements task-specific supervised models.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
