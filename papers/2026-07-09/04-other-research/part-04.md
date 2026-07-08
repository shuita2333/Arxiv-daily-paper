# 📦 其他研究 | 2026年07月09日

> 本类共 **195** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-195**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-195**

---

### 151. [Token-Based Dual-view Fusion and Adaptation of Large Vision Models for Breast Cancer Classification](https://arxiv.org/abs/2607.06309)

**<font color=#1a73e8>作者：</font>** Aysan Ghayouri Pirsoltan, Shima Babakordi, Mohammad Reza Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate breast cancer classification from mammography requires effective integration of complementary information from craniocaudal (CC) and mediolateral oblique (MLO) views, which provide a more complete characterization of breast abnormalities. However, existing multi-view learning approaches typically rely on feature-level aggregation or single-stage cross-attention, which can entangle view-specific and shared representations and restrict interaction to limited network depths. To address these limitations, we propose a token-centric dual-view learning framework that unifies prompt-based adaptation and cross-view fusion within a frozen vision transformer backbone. The framework reformulates inter-view interaction as structured token-level communication, where dedicated fusion tokens explicitly encode bidirectional information exchange between CC and MLO views via cross-attention, serving as intermediate carriers of cross-view dependencies rather than relying on direct feature fusion. Unlike conventional methods that apply fusion at a single layer, fusion modules are inserted at multiple transformer depths, enabling progressive and repeated interaction across the encoder hierarchy. Fusion tokens are reintegrated into the token sequence and refined by subsequent transformer layers, facilitating hierarchical propagation of complementary information while preserving view-specific structure. Experiments on VinDr-Mammo and CMMD datasets demonstrate consistent improvements over linear probing, prompt-only adaptation, and conventional fusion baselines. On the VinDr-Mammo BI-RADS classification task, the framework achieves 50.40% F1-score and 0.8090 AUC, including a 0.10 AUC improvement over a dual-view fusion baseline in the binary setting. Ablation studies further validate the effectiveness of token-based fusion and multi-depth interaction design.

---


### 152. [Synthetic-to-Real Translation for Class-Agnostic Motion Prediction](https://arxiv.org/abs/2607.06319)

**<font color=#1a73e8>作者：</font>** Yizheng Wu, Hongwei Fan, Kewei Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion understanding is critical for ensuring safety and robustness in autonomous driving systems, driving increasing interest in motion prediction. A key challenge in this domain is the high cost associated with acquiring real-world motion labels. It is therefore ideal if we could transfer motion knowledge from synthetic data to real data. In this context, we explore the potential of synthetic-to-real translation for motion prediction (SRMP). However, the most used naive motion regression methods are notably sensitive to the synthetic-to-real domain shift, resulting in unreliable knowledge translation. To address this, we propose a novel approach integrating a motion knowledge translation framework with two key components: (1) objectness-aware motion prediction, which explicitly models the joint distribution of motion patterns and objectness priors to improve domain-invariant feature learning, and (2) objectness-aided motion enhancement, a motion label refinement mechanism that leverages learned objectness priors to filter motion noise. Furthermore, we present a physically-based pipeline for generating Motion4D, the first synthetic 4D LiDAR dataset tailored for SRMP research, addressing the lack of synthetic motion datasets. Experimental results demonstrate that our approach effectively bridges the domain gaps and yields superior performance on real scenes.

---


### 153. [Dithered Gaussian Mechanism for Randomness-Efficient Differential Privacy](https://arxiv.org/abs/2607.06320)

**<font color=#1a73e8>作者：</font>** Nikita P. Kalinin, Rasmus Pagh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present the dithered Gaussian mechanism, a novel alternative to the discrete Gaussian mechanism for differential privacy that discretizes the private output rather than the noise distribution itself. By interpreting this discretization as post-processing of the Gaussian mechanism, our construction directly inherits the privacy guarantees of the standard Gaussian mechanism while avoiding vulnerabilities caused by finite-precision floating-point outputs. We show that the mechanism is provably randomness-efficient: by sampling the discretized output values directly, the number of high-quality random bits required for privacy can be reduced significantly and made independent of the noise level. This is achieved by separating the randomness into two sources: a high-quality source used for the privacy-critical sampling step, and a high-performance public source, possibly known to the adversary, that supplies the additional randomness needed for randomized discretization. This separation enables the use of cryptographically secure randomness without substantial performance loss. As an application, we study model training with DP-SGD and show that cryptographically secure noise generation with reduced exposure to floating-point vulnerabilities can be achieved with modest practical overhead.

---


### 154. [Bridging Diffusion Pruning and Step Distillation with Teacher-Aligned Repair](https://arxiv.org/abs/2607.06335)

**<font color=#1a73e8>作者：</font>** Jincheng Ying, Li Wenlin, Minghui Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate high-quality images, but their inference cost comes from two sources: large denoising networks and repeated denoising steps. Existing compression pipelines usually attack these costs separately. Pruning reduces the network, but most pruning methods still rely on a long post-pruning retraining stage to recover a many-step sampler. Step distillation reduces the number of denoising steps, but it usually assumes a student that can already follow the teacher well enough to receive useful distillation gradients. This paper asks whether post-pruning retraining can be replaced by step distillation. We find that the direct replacement fails: after pruning an EDM2-XS teacher, starting SiDA from the pruned checkpoint produces unusable samples. We introduce a short teacher-alignment repair stage as a bridge between pruning and step distillation. The bridge matches the pruned generator to the teacher on noisy real-image latents, then hands the repaired checkpoint to one-step distillation. On ImageNet-512, the original EDM2-XS baseline uses 124.713M parameters and 63 network evaluations, reaching an FID of 3.53. With a suitable distillation objective, our 20% pruned one-step generator uses 98.826M parameters and one network evaluation, reaching an FID of 3.12. With 30% pruning, the model uses 88.029M parameters and one network evaluation, with an FID of 4.26.

---


### 155. [Physics-Informed Neural Embeddings of PDE Solution Families](https://arxiv.org/abs/2607.06348)

**<font color=#1a73e8>作者：</font>** Raul Jimenez, Svitlana Mayboroda, Pavlos Protopapas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a physics-informed framework for learning finite-dimensional embeddings of solution families of partial differential equations. The method uses a multihead Physics-Informed Neural Network in which a shared body learns a latent manifold representing the solution space, while linear heads reconstruct individual solutions associated with different initial conditions. A head-orthogonalization penalty removes degeneracies in the latent representation and stabilizes the principal-component spectrum across training realizations. Because the initial condition is built into the network output by construction, these principal components measure the additional variability the network learns on top of the initial profile, not the full solution itself. We apply the method to the one-dimensional viscous Burgers equation, with the heat and wave equations as robustness checks. For a latent dimension $n_b=20$, the learned manifolds exhibit pronounced effective dimensional reduction: for Burgers dynamics, only $2$-$4$ principal components capture about $95\%$ of the latent-space variance, while $4$-$7$ capture about $99\%$, depending on the initial-condition family; the same qualitative compression holds for the heat and wave equations. We also split the wavenumber axis into bands (``Fourier shells'') and measure how much each band contributes to every principal component. The resulting frequency profile is invariant under the change-of-basis freedom that the orthogonalization penalty leaves in the latent space, and is therefore reproducible across independent training runs. More broadly, this establishes the learned spectral profiles and principal components as robust observables of solution-manifold geometry.

---


### 156. [Generalized Synthetic Image Detection with Enhanced RGB-Noise Representation Learning](https://arxiv.org/abs/2607.06354)

**<font color=#1a73e8>作者：</font>** Zhen Li, Gang Cao, Tian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large-scale generative models has accelerated the spread of highly deceptive AI-generated images, making generalized synthetic image detection a critical imperative. Existing forensic networks often struggle with cross-model generalization and realworld degradations due to their reliance on single-domain representations and conventional binary classification optimization. To overcome these limitations, we propose RNSIDNet, a novel forensic framework that achieves robust detection through enhanced RGB-Noise representation learning. Specifically, our method employs a dual-branch architecture where global RGB semantics, extracted by an attention-refined CLIP backbone, dynamically modulate highfrequency noise artifacts captured by Bayar convolutions via a Feature-wise Linear Modulation (FiLM) module. To further enhance the learned representations, we design a Hard Sample-aware Contrastive Learning (HSCL) strategy. By explicitly penalizing challenging training samples, HSCL reshapes the latent feature space to maximize the discriminative margin between pristine and synthetic domains. Extensive experiments across eight public benchmark datasets verify that our model achieves state-of-the-art performance, delivering superior generalization ability, robustness, and computational efficiency. Code and dataset will be publicly available on this https URL.

---


### 157. [Automated Compliance Mapping in Cloud Security with Domain-Adapted Sentence Transformers](https://arxiv.org/abs/2607.06364)

**<font color=#1a73e8>作者：</font>** John Bianchi, Luca Petrillo, Fabio Martinelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mapping cloud security controls to technical metrics is currently a manual process. This paper proposes domain adaptation of Sentence Transformer models to automate it. We build a training corpus of 3,499 semantic pairs from five European security standards and a set of technical metrics, then expand it via back-translation and LLM-based paraphrasing to up to 13,996 samples across four scenarios. We fine-tune five architectures and evaluate their performance on two independent tasks: control-to-metric and cross-standard controls association. All fine-tuned models outperform their zero-shot baselines. On the control-to-metric task, the best model gains up to 23 nDCG@10 points, while on the cross-standard control task, \textit{multi-qa-mpnet-dot-v1} under back-translation reaches 0.870 nDCG@10. The results show that in-domain training data is a primary driver of performance for the considered case studies.

---


### 158. [The Impact of Security and Privacy Controls on Users' Emotional Engagement with Generative AI Chatbots](https://arxiv.org/abs/2607.06371)

**<font color=#1a73e8>作者：</font>** Jabari Kwesi, Jiaxun Cao, Hailee Cunningham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chatbots powered by generative AI (e.g., OpenAI's ChatGPT and Google's Gemini) are increasingly being appropriated for emotional support and companionship. These tools offer a suite of security and privacy (S&P) controls, including model training opt-outs and memory toggles, yet how the presence of these controls influences users' attitudes toward emotionally sensitive disclosure remains understudied. We conducted a mixed-methods vignette study with 354 U.S. participants to examine how S&P controls influence users' willingness to engage with generative AI chatbots for emotional support, their perceptions of how protected they are when using these systems, and their perceptions of how effective the chatbots are for providing support. Controls enabling deletion of disclosures had the largest positive impact: these offerings outperformed technically sophisticated controls such as local-only processing and model training opt-outs, where participants expressed difficulty understanding the underlying mechanisms. Yet trust remains fragile, and participants often doubted S&P controls would function as promised. We conclude with actionable recommendations informed by our results to bridge users' comprehension gaps, build credible assurances, and properly calibrate barriers for users in distress.

---


### 159. [FADRA: Frequency-Aware Diffusion with Residual Adaptation for Video Face Restoration](https://arxiv.org/abs/2607.06389)

**<font color=#1a73e8>作者：</font>** Jin Jiang, Jia Wang, Panwen Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video face restoration (VFR) aims to recover high-quality and temporally consistent facial details from severely degraded video sequences; however, existing methods still struggle to balance spatial fidelity and temporal coherence under complex degradations. To address this, we propose FADRA, a frequency-aware diffusion framework with iterative residual adaptation specifically tailored for robust VFR. We first leverage the strong temporal consistency of a pre-trained text-to-video diffusion model and introduce lightweight LoRA adapters together with a Low-Quality (LQ) Pixel-Alignment Feature Fusion module to efficiently adapt the frozen generative prior to the VFR task. To further adapt the frozen diffusion backbone to the downstream VFR task beyond LoRA-based adaptation, we introduce a Repeated Residual Adaptation Head (RRAH) for step-wise residual refinement after the diffusion backbone. To make this refinement explicitly guided by the degraded observation, RRAH further takes the LQ latent together with the current velocity prediction as input, allowing the model to repeatedly revisit LQ cues and predict residual updates at each flow-matching step. This LQ-guided repeated residual adaptation helps recover fine facial details while preserving the inherent temporal priors of the pre-trained model. Furthermore, to ensure the structural integrity of perceptually important details, we introduce a Frequency-Aware Loss that provides explicit supervision across multiple spectral bands, emphasizing visually sensitive frequency components that are crucial for perceptual quality and prone to temporal jittering. Extensive experiments demonstrate that FADRA recovers better facial structures and produces more temporally consistent videos than state-of-the-art methods, leading to clear gains in both quantitative metrics and visual perception.

---


### 160. [ExplAIner: A Declarative Query Language for Explaining Classification Models](https://arxiv.org/abs/2607.06407)

**<font color=#1a73e8>作者：</font>** Marcelo Arenas, Pablo Barceló, Diego Bustamante 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The XAI community has studied a wide range of queries and scores for explaining predictions of ML models. From a data management perspective, this proliferation of explanation notions calls for declarative query languages in which such notions can be specified, combined, and analyzed uniformly. In this paper, we develop such a framework for Boolean models. We first revisit FOIL, an interpretability query language for black-box models, and show that it has two fundamental limitations: it cannot express central optimality-based explanation queries, and its evaluation problem over decision trees is hard for every level of the polynomial hierarchy. We then introduce ExplAIner, a query language based on FOIL with an extended vocabulary and a layered structure. We show that ExplAIner can express a broad family of explanation notions, including abductive, contrastive, feature-based, and distance-based queries. We also prove that the evaluation problem for each query in ExplAIner belongs to the Boolean hierarchy over every class of Boolean models for which some basic predicates can be evaluated in polynomial time. In particular, that property holds for deterministic and decomposable Boolean circuits. Finally, we introduce Opt-FOIL, an optimization-oriented fragment of ExplAIner for computing explanations that are minimal with respect to strict partial orders, and prove that its evaluation problem is in $\mathrm{FP}^{\mathrm{NP}}$ under the same tractability assumptions. These complexity results have a direct algorithmic consequence: a fixed ExplAIner query can be evaluated with a fixed number of calls to a SAT solver, while a notion of explanation specified in Opt-FOIL can be computed with a polynomial number of such calls. This is particularly relevant in formal XAI, where SAT solvers have been successfully used to compute explanations for several classes of ML models.

---


### 161. [Temporal Modeling of Optically Variable Devices in Identity Documents](https://arxiv.org/abs/2607.06408)

**<font color=#1a73e8>作者：</font>** Glen Pouliquen, Joseph Chazalon, Guillaume Chiron 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust remote verification of identity documents relies on analyzing faint, transparent security features like Optically Variable Devices (OVDs), or "holograms", within user-captured videos under uncontrolled conditions. Current systems, however, face critical limitations: existing methods often treat video frames in isolation, neglecting the intrinsic dynamic nature of OVDs and leaving systems vulnerable to swapping attacks, or focus on general holographic presence and lack the ability to verify specific OVD types. Moreover, the economic infeasibility of frame-by-frame video annotation makes supervised training impractical. In this work, we introduce two novel approaches for verifying the dynamic behavior of transparent OVDs protecting the holder's portrait, specifically designed for open-set scenarios where attack types are unknown during training. We demonstrate that these approaches can be trained without any attack samples in a self-supervised setting, surpassing previous state-of-the-art methods on public datasets while adhering strictly to industrial constraints. Our results confirm that modeling temporal dynamics is essential for defeating sophisticated attacks under realistic conditions, and underscores the promise of sequence modeling and anomaly detection for OVD verification. Code is available at this https URL.

---


### 162. [XRFormer: Multiscale Tokenization for XRF Representation Learning](https://arxiv.org/abs/2607.06424)

**<font color=#1a73e8>作者：</font>** Sofiane Daimellah, Sylvie Le Hégarat-Mascle, Clotilde Boust  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray fluorescence (XRF) spectroscopy is a key modality for material analysis in cultural heritage. However, automated learning from XRF spectra remains challenging: XRF spectra are complex one-dimensional signals composed of sharp elemental peaks, broader structures, and background variations that are not taken into account by existing learning-based models. This paper introduces XRFormer, a transformer architecture tailored to XRF spectra through a multiscale convolutional tokenizer that injects locality and multi-resolution inductive biases before global self-attention. The tokenizer progressively reduces spectral resolution while increasing embedding dimensionality, and the resulting token sequence is processed by a standard transformer encoder. We further investigate self-supervised pretraining for XRF representation learning using Masked Spectral modeling (MSM) and a physics-informed Peak Presence Prediction (PPP) objective. Experiments on the Pigments Checker STANDARD v.5 dataset for pigment identification and unmixing show that XRFormer consistently outperforms ViT, SpectralFormer (with and without CAF), and a 1D-CNN baseline for pigment identification. For pigment unmixing, XRFormer achieves robust abundance estimation while maintaining significantly higher parameter efficiency than SpectralFormer, operating at a lower token resolution (128 vs. 512 tokens) and with less than half the number of parameters (1.5M vs. 3.37M). MSM yields consistent gains across both tasks, while PPP further enhances performance for both identification and unmixing when tuned with an appropriate peak prominence. These results highlight multiscale, modality-aware tokenization as an effective and parameter efficient foundation for transformer-based XRF modeling under data-limited conditions. A GitHub repository is provided at this https URL.

---


### 163. [TILDE: TILt-based Distributional Erasure for Concept Unlearning](https://arxiv.org/abs/2607.06432)

**<font color=#1a73e8>作者：</font>** Naveen George, Naoki Murata, Yuhta Takida 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept unlearning in text-to-image diffusion models is critical for safe and practical deployment: with rising privacy concerns, copyright disputes, trademark constraints, and safety regulations, deployed systems must be able to suppress unwanted concepts after training. Existing methods often remove the target concept effectively, but practical unlearning also requires an equally fundamental property: the unlearned model should retain quality, diversity, and semantic coverage on benign generation. The gold standard is a retain-only model trained from scratch without the unwanted data. However, common erasure objectives do not specify which post-unlearning distribution should approximate this reference, leaving retention as an implicit consequence of the update rule. We propose TILDE, TILt-based Distributional Erasure, which formulates concept unlearning as a distributional alignment problem: the desired target is the minimum-deviation conditional distribution from the pretrained model under a forgetting constraint. This energy-tilted, anchor-free target suppresses concept-expressing images while preserving benign relative mass for each prompt. We instantiate this principle with residual $\nabla$-GFlowNet training, which learns the score correction induced by the forget energy relative to the pretrained diffusion model. Across objects, artistic styles, and characters, TILDE achieves strong forgetting while improving retention and distributional fidelity over prior baselines.

---


### 164. [Finding H. pylori in the Fine Print: Evidence-Linked Multi-Agent Case Finding from Gastric Biopsy Reports](https://arxiv.org/abs/2607.06435)

**<font color=#1a73e8>作者：</font>** Yufan Wang, Anit Kumar Sahu, Yan Fei Ng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data from Singapore indicated that about 31% of the population had evidence of Helicobacter pylori infection. Persistent H. pylori infection is associated with chronic active gastritis and peptic ulcer disease, and its eradication is key to gastric cancer prevention. However, evidence supporting \textit{H. pylori} positivity and H. pylori-associated gastritis may be distributed across heterogeneous coded and free-text report fields and may require contextual interpretation of assertion and negation, limiting keyword search, and making manual review difficult to scale. We conducted a retrospective pilot evaluation of the Nimblemind Multi-Agent System (nMAS), a field-name-driven, evidence-linked extraction workflow, using 54 de-identified gastric biopsy pathology reports from a large healthcare system in Singapore. Four clinician-scoped binary fields were evaluated: gastric/stomach biopsy, biopsy status, H. pylori positivity, and H. pylori-associated gastritis. Across 216 feature-case decisions, nMAS correctly classified 213, corresponding to 98.61% overall accuracy. A separately implemented UMA-style MiniMax M2.5 comparator produced similar aggregate and per-field classification metrics. Although predictive performance was similar, nMAS maintained unified report-level outputs with supporting source sentences; the demonstrated contribution is therefore workflow integration and traceability rather than predictive superiority. Under an illustrative, unmeasured scenario, reviewing 1,000 reports at five minutes per manual review versus five seconds per evidence-linked verification would reduce review time from 83.3 to 1.4 staff-hours, corresponding to 81.9 staff-hours and about USD~6,100 in potential staff-time value. Larger multi-institutional studies should evaluate evidence-span correctness, clinician verification time, and generalizability.

---


### 165. [PIPBench: A Profile-Inclusive Framework for Personalized Image Generation Evaluation](https://arxiv.org/abs/2607.06440)

**<font color=#1a73e8>作者：</font>** Yuhang Wu, Shuxiang Zhang, Wee Hian Ching 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image models such as DALLE-3 excel at following diverse prompts yet remain blind to individual aesthetic preferences. We study personalized image generation, where models must align outputs with a user's implicit visual preferences based on a few historically preferred images and a short prompt. To this end, we introduce PIPBench, the first profile-inclusive benchmark for evaluating personalized image generation. We further propose a novel data construction pipeline that leverages psychological and demographic profiling dimensions for both real-user data collection and scalable agent-based data generation. Using PIPBench, we conduct a thorough evaluation of representative line of methods. Our experiments reveal key limitations in existing methods, suggesting new challenges and opportunities for personalized text-to-image synthesis. Project page: this https URL

---


### 166. [Analysis-by-Proxy: Localization Signals in VLMs Operating as Condition Encoders](https://arxiv.org/abs/2607.06445)

**<font color=#1a73e8>作者：</font>** Yoav Baron, Sara Dorfman, Roni Paiss 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly utilized as the conditioning backbone for diffusion-based image editing due to their remarkable multimodal reasoning capabilities. While standalone VLMs demonstrate strong localization capabilities, editing pipelines frequently struggle to maintain this accuracy, particularly in complex, multi-entity scenes. In this work, we investigate this performance gap, hypothesizing that it stems from treating the VLM as a condition encoder. In this role, the model is restricted to a single forward pass, preventing the autoregressive generation process for which it was optimized, thereby failing to fully expose its capabilities. To investigate whether this spatial understanding persists when the VLM is used as a condition encoder, we introduce Analysis-by-Proxy. In this framework, we train a lightweight, interpretable proxy model on the VLM's intermediate representations using an auxiliary localization task. By analyzing the VLM through this proxy, we uncover the specific VLM representations that encode localization information. Our findings expose a fundamental mismatch between how spatial knowledge is represented within a VLM condition encoder and how it is extracted by current editing pipelines. We reveal that under single-pass constraints, the localization signal does not reliably propagate to the predefined layer configurations commonly used for conditioning. Instead, this crucial signal remains hidden within intermediate representations, at locations that vary depending on the input prompt. Using our introduced Analysis-by-Proxy framework, we reveal the fundamental failures of existing condition extraction strategies in editing pipelines, opening the door to more principled design of conditioning architectures.

---


### 167. [Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory](https://arxiv.org/abs/2607.06447)

**<font color=#1a73e8>作者：</font>** Jihao Liu, Guoxiong Gao, Zeming Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent LLM-based mathematical reasoning agents have begun to tackle research-level problems and, in several cases, have contributed to the resolution of open problems. However, scaling and orchestrating such agents effectively remains challenging, due to the difficulty of coordinating parallel proof search while keeping intermediate claims organized and reliable. In this paper, we propose Danus, an orchestration system for research-level mathematical reasoning centered on a shared fact graph as a global memory-management mechanism. Danus consists of a main agent that performs planning and coordination, multiple worker agents that carry out proof search in parallel, and a stateless verifier that checks proposed mathematical claims before they are admitted into the fact graph. Each verified fact is stored together with its proof and logical dependencies, allowing the system to build long arguments incrementally while keeping the shared proof state organized. The main agent periodically summarizes the evolving proof state, redirects workers across promising directions, and supports interaction with human mathematicians through progress reports. We evaluate Danus through six research-level case studies in algebraic geometry, singularity theory, and combinatorics, illustrating how the fact-graph memory mechanism enables Danus to construct long, detailed mathematical proofs. Our results suggest that fact-graph-based orchestration provides an effective route toward scaling mathematical reasoning agents for long-horizon research problems. Danus is open source at this https URL.

---


### 168. [Lower Bounds for PIR with Preprocessing from Blackbox Cryptography](https://arxiv.org/abs/2607.06451)

**<font color=#1a73e8>作者：</font>** Alexander Hoover, Giuseppe Persiano, Kevin Yeo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> (shortened for arXiv metadata)
We study the limits of single-server private information retrieval (PIR) with preprocessing. Prior work has shown that single-server PIR with sublinear communication requires a linear number of (public-key) server operations per query [DMO00, DH24]. Recent breakthrough works, including [CHK22, ZPZS24, LMW23], circumvent these lower bounds by critically leveraging preprocessing to construct single-server PIR with sublinear query computation.
Our work presents computation lower bounds for any single-server PIR with preprocessing that makes blackbox usage of {\em any} cryptography (such as random oracles and virtual blackbox obfuscation). For any client preprocessing scheme where the client stores $s$ bits about an $n$-bit database, we prove the online amortized computation must be $\Omega(n/s)$ across $k = \Omega(s)$ queries (even if performed in a single batch query). In more detail, we prove that they must have either $\Omega(n/s)$ amortized online communication or the server must perform $\Omega(n/s)$ cryptographic operations. Our lower bounds are optimal as there exist PIRs with client preprocessing matching exactly one of the above requirements while outperforming the other. Furthermore, our lower bounds also rule out the existence of doubly efficient PIR from blackbox cryptography with sublinear query computation. Our proof framework also supports $\Omega(n/s)$ communication lower bounds for three mildly restricted classes of single-server PIR.
We also prove lower bounds for symmetric private information retrieval (SPIR) with client preprocessing in the random oracle model and present a matching SPIR construction with client preprocessing using only OWFs during queries.

---


### 169. [Andha-Dhun: A First Look at Audio Descriptions in Hindi](https://arxiv.org/abs/2607.06457)

**<font color=#1a73e8>作者：</font>** Ritabrata Chakraborty, Divy Kala, Nisheeth Bhooshan Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio Descriptions (ADs) narrate visual content for Blind and Low Vision (BLV) audiences during gaps in audiovisual media. There is growing momentum around ADs in movies and TV shows, and with mandates from India's Central Board of Film Certification (CBFC), there is a need to expand ADs beyond English. Yet, there is no work that generates ADs for any Indian language. To address this gap, we present the first systematic study of ADs in Hindi, contributing to aspects such as data, generation, and evaluation. We introduce Andha-Dhun, the first dataset of human-authored Hindi ADs collected from 8 full-length movies. We explore two approaches for generating ADs in Hindi: (i) directly from English dense video descriptions, and (ii) translating English ADs into Hindi. We evaluate these approaches using perplexity and LLM-as-a-judge metrics to assess fluency and quality respectively. We also analyze movies that have both English and Hindi human-authored ADs and find that naive translation introduces artifacts and narrows diversity compared to original Hindi ADs. Direct machine translation fails to adapt cultural references, while human-translated ADs do better but still fall short. Our findings emphasize that the purpose of Hindi ADs is accessibility for Indian BLV audiences, and that this requires adapting content for the audience more than strict fidelity to the source.

---


### 170. [Verification of Dynamic Holographic Behavior in Identity Documents](https://arxiv.org/abs/2607.06466)

**<font color=#1a73e8>作者：</font>** Glen Pouliquen, Joseph Chazalon, Guillaume Chiron 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the remote verification of the authenticity of Optically Variable Devices (commonly known as holograms) on identity documents. Typically placed over the cardholder's photo, these devices provide strong and easily verifiable security for human inspection but pose challenges for automated verification. Existing approaches easily cover static frauds (e.g. paper photocopy) and can be evaluated for such, but their capacity to detect real, dynamic fraud cases (e.g. handcrafted hologram) has not been evaluated to date because of the lack of public datasets. Furthermore, they are usually trained to detect known attack types, and few of them can generalize to new, unseen attacks. This work features three contributions to address these limitations: 1) a new public dataset, MIDV-DynAttack, which extends the existing MIDV-Holo dataset with realistic, static and dynamic attacks against identity document specimens, tripling the number of attack samples compared to the original dataset, 2) a novel verification method which can assess the authenticity of a specific hologram thanks to the analysis of its dynamic behavior and appearance, can be trained without dynamic attack samples, and exhibits new state-of-the-art performance, 3) a benchmark of existing approaches which follows a clear evaluation protocol and emphasizes the inability of other approaches to deal with dynamic attacks, as well as new challenging attacks to deal with. Code and dataset are publicly available at this https URL.

---


### 171. [EgoPolice: A Benchmark for Egocentric Video Understanding in High-Stakes Police Body-Worn Camera Footage](https://arxiv.org/abs/2607.06468)

**<font color=#1a73e8>作者：</font>** Max Gonzalez Saez-Diez, Jihoon Chung, Adam D. Wolsky 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce EgoPolice, a carefully curated dataset of real, egocentric police-civilian interactions, sourced from publicly available body-worn camera videos. We select police-civilian action labels that are critical for police behavioral research and annotate them at a second-by-second granularity. The videos feature rapid and irregular camera motion, dense human interactions, and rare high-stakes events, making the dataset a challenging benchmark for motion-robust and context-aware egocentric perception. We provide two different tasks, classification and multiple-choice question-answering, and benchmark both open-source and closed-source models. We find that even the best video models like Gemini 2.5 Pro still struggle to accurately predict high-risk actions such as "Weapon Out". Beyond serving as a benchmark, EgoPolice provides a foundation for developing models capable of identifying events of interest in large-scale body-worn camera video repositories, enabling more efficient downstream human review.

---


### 172. [A VLM-Enhanced Framework for Comprehensive Traffic Sign Condition Assessment Integrating Daytime Visual Performance and Nighttime Retroreflectivity Evaluation](https://arxiv.org/abs/2607.06478)

**<font color=#1a73e8>作者：</font>** Linlin Zhang, Neema Jakisa Owor, Xiang Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic signs are crucial components of road safety, serving as visual tools under all lighting conditions. The Manual on Uniform Traffic Control Devices (MUTCD) specifies daytime visual factors such as legibility and color contrast, and nighttime retroreflectivity requirements. Traditional assessment methods rely on manual inspections, which the Federal Highway Administration (FHWA) notes are subjective, labor-intensive and pose safety concerns, while retroreflectometers are expensive and unaffordable for smaller agencies. Most existing studies focus on either daytime factors or nighttime retroreflectivity but rarely integrate both aspects comprehensively. This study develops a novel framework that systematically evaluates traffic signs through integrated daytime-nighttime assessment. The methodology employs three fine-tuned Vision Language Models (VLMs) for daytime visual performance assessment across four key factors: legibility, color, surface and shape integrity, and surrounding environment conditions. VLM predictions are converted to numerical scores through sentiment analysis and Contrastive Language-Image Pre-Training (CLIP) scoring, while nighttime performance is assessed using LiDAR-derived retroreflectivity following established calibration procedures. The framework integrates these components into a comprehensive Sign Condition Index (SCI) for maintenance guidance. Evaluation results demonstrated that LLaVA and Qwen outperformed InternVL, achieving bidirectional cosine similarity scores of 0.67-0.76 across all factors. Among 462 validated traffic signs, 68 were flagged by the proposed framework as requiring immediate replacement due to inadequate retroreflectivity performance. This research provides a cost-effective alternative to traditional manual inspections for comprehensive traffic sign condition assessment.

---


### 173. [A Physics-Informed Neural Network Framework for Elastodynamic Wave Propagation in Bimaterial Systems](https://arxiv.org/abs/2607.06479)

**<font color=#1a73e8>作者：</font>** Sonal Ankush Chibire, Jenn-Terng Gau, Bo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) provide a promising framework for solving partial differential equations while embedding the underlying physical laws directly into the learning process. This study presents a PINN-based framework for modeling transient elastodynamic wave propagation in bimaterial systems governed by the axisymmetric equations of linear elasticity. A steel-aluminum specimen representative of a Split Hopkinson Pressure Bar configuration is considered, and the governing elastodynamic equations, together with the corresponding initial, boundary, and interface conditions, are incorporated directly into the network through a physics-informed loss function. High-fidelity finite-element simulations performed using ANSYS Workbench Explicit Dynamics are used for validation and as supplementary data constraints during training. The proposed framework accurately predicts wave transmission and reflection across the bimaterial interface and reproduces axial and radial displacement histories, face-averaged responses, and the dominant stress and strain evolution with close agreement to the finite-element solutions. The trained network further demonstrates the ability to predict wave responses at previously unseen time instants and for modified material properties without requiring additional finite-element simulations, providing a continuous surrogate model for elastodynamic analysis. Mesh-sensitivity studies confirm numerical robustness, while additional material combinations demonstrate the generality of the proposed methodology. The results show that integrating physics-informed neural networks with explicit finite-element analysis provides an accurate and computationally efficient framework for elastodynamic wave propagation in heterogeneous solids, offering an effective surrogate modeling approach for high-rate solid mechanics and impact engineering applications.

---


### 174. [Prompt-Adapter Context Routing for Parameter-Efficient Multi-Shot Long Video Extrapolation](https://arxiv.org/abs/2607.06481)

**<font color=#1a73e8>作者：</font>** Anna Córdoba, Adam Puente Tercero, Nerea Angulo Hijo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PACR-Video, a parameter-efficient framework for multi-shot long video extrapolation that preserves recurring entities, scene structure, visual style, and causal progression without full generator fine-tuning. PACR-Video keeps a text-to-video diffusion transformer frozen and augments it with low-rank temporal adapters conditioned by learned shot-role prompt tokens. To maintain long-horizon coherence, it builds a recursive prompt bank that stores compact entity, location, action, and style prompts from previous shots, then routes them through adapter gates according to predicted narrative dependencies. A Shot-Local/Story-Global tuning objective combines next-shot reconstruction, cross-shot identity contrast, and prompt sparsity regularization, while an adapter composition schedule balances early-shot visual consistency with later-shot event progression and viewpoint change. Across six multi-shot and long-video benchmarks, PACR-Video outperforms text-to-video, tuning-based, memory-augmented, streaming, and recursive-context baselines on distributional quality, semantic alignment, identity consistency, temporal smoothness, motion stability, transition coherence, and human preference. These results show that compact prompt routing and lightweight temporal adaptation provide sufficient controllable capacity for stable long video extrapolation.

---


### 175. [Assessing the Operational Impact of Poisoning Attacks over Augmented 3D Point Cloud Public Datasets for Connected and Autonomous Vehicles](https://arxiv.org/abs/2607.06484)

**<font color=#1a73e8>作者：</font>** Marwan Lazrag, Badis Hammi, Lorena Gonzalez-Manzano 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Poisoning attacks against public datasets lead to major concerns, such as (i) misclassification of perceived objects when the poisoned data is used for training and (ii) embedding of backdoors that may eventually be triggered later on, when specific conditions in the system apply over the learned models. Its impact over data augmentation models is unclear. While data augmentation reduces the likelihood of poisoning attack success, some valid questions remain. Is data augmentation affecting the impact of poisoning attacks? can it increase the number of poisoned samples or injected backdoors? We explore in this paper some of these questions. We assess the effects of augmenting poisoned 3D point cloud datasets and validate that poisoning is able to evade the sanitizing nature of augmentation techniques when using the concrete case of Generative Adversarial Network (GAN) techniques to exemplify the case of data augmentation processing. We also validate that poisoning propagates over the augmented datasets and perturbs the decision made by general-purpose classifiers, in the end. All the experimental material (including tools, datasets, and classifiers) is publicly available, to facilitate reproducibility and to foster further research in the topic.

---


### 176. [Multi-Agent Deep Reinforcement Learning for Multi Objective Battery Management in Dairy Farms](https://arxiv.org/abs/2607.06489)

**<font color=#1a73e8>作者：</font>** Marcos Eduardo Cruz Victorio, Karl Mason  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dairy industry in Ireland has a large potential for the integration of renewable energy and the reduction of carbon emissions. However, researchers of distributed generation control are mainly focused on residential and commercial applications. To contribute to the effective integration of renewable energy in the dairy sector, this paper presents a multi-objective optimisation control system based on differential evolution and multi agent Deep Reinforcement Learning. The proposed control is organised in two layers: the upper layer uses dynamic pricing, and the lower layer is based on multi-agent reinforcement learning for battery management. This paper also simulates the electrical response of the proposed control system in a rural distribution circuit. The simulation results show that the proposed control framework can improve profits from energy arbitrage up to 18% compared to using Rule-based models, increase the use of distributed generation without significantly increasing cost, and comply with the Irish grid code in terms of voltage variation.

---


### 177. [Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated Real-Time Monte Carlo Engine](https://arxiv.org/abs/2607.06495)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Live sports commentary is grounded generation under a deadline: statements concern real, named athletes, the grounding state changes every few seconds, and no reference text exists at generation time. We present Pitwall, a production system that generates natural-language Formula 1 strategy briefings in English, Spanish, and Portuguese, treating faithfulness as an architectural property rather than an aspiration: every published sentence is decomposed into typed factual claims (positions, gaps, tyres, pace, overtakes, race control) and each claim is verified against the probabilistic race state that prompted it. The same verifier gates the fine-tuning data: of 3,045 model-written targets, only the 81.9% whose every claim is state-supported are retained, the rest falling back to a provably faithful template, so the generator never sees an ungrounded target. Verification is meaningful because of the grounding substrate: a vectorized Monte Carlo engine (N=2,000 per-lap race continuations) calibrated on 126 races (2018-2024) and validated on fully held-out 2025-2026 seasons (winner-in-top-3 90.3% over 155 backtests; held-out Brier 0.0745). A recurring finding spans both halves of the system: virtues trade off and must be gated separately. In simulation, calibration-optimal is not decision-optimal; in generation, fine-tuning on richer targets buys vividness that collapses into hallucination when the grounding state is sparse -- a failure a four-base replication traces to base-model instruction adherence, not scale, and that sparse-context auditing removes from the production model. End-to-end operation -- live timing to verified trilingual briefings -- was confirmed at two consecutive live Grands Prix (Austria and Britain, 2026); at Silverstone a timestamped probability trace, committed to disk before the outcome was known, locked onto the eventual winner ten laps before the flag.

---


### 178. [EntroPath: Maximum Entropy Path Ensemble Embedding for Manifold Learning](https://arxiv.org/abs/2607.06497)

**<font color=#1a73e8>作者：</font>** Przemysław Rola  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce EntroPath, a manifold learning method that recovers geodesic geometry from data graphs through ensembles of diffusion paths. Many existing graph-based embeddings rely either on locally normalised random walks or on shortest-path distances. The former can concentrate diffusion in densely sampled regions, while the latter are sensitive to spurious shortcut edges in the graph. EntroPath instead builds its dissimilarities from the maximum entropy random walk (MERW), which aggregates the full ensemble of k-step paths between points rather than relying on any single trajectory. We show that the resulting free-energy dissimilarity converges to squared geodesic distance in the short-time limit, via Varadhan's heat-kernel formula. The diffusion depth k interpolates smoothly between local neighbourhood structure and global manifold geometry, and the symmetrised kernel admits an exact Gram factorisation connecting EntroPath to kernel methods. We further provide scalable extensions via landmark projection and diffusion-potential pseudotime. Across synthetic manifolds and single-cell benchmarks, EntroPath consistently matches or outperforms diffusion- and shortest-path-based methods, while remaining competitive with neighbourhood-preserving embeddings (UMAP, t-SNE) on local-structure metrics. Its gains are most pronounced on manifolds with non-uniform sampling density and well-separated branching trajectories, where path-ensemble diffusion more faithfully preserves the underlying geodesic geometry.

---


### 179. [GlassTENG: Self-Powered Triboelectric Nanogenerator based Sensing of Pulse, Jaw, and Upper Facial Activity from Everyday Glasses](https://arxiv.org/abs/2607.06509)

**<font color=#1a73e8>作者：</font>** Raj N. Dave, Jovanis Prodanich, Yung-ching Lai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smart glasses maintain near-continuous skin contact at multiple arterial and muscular sites, making them a promising platform for physiological sensing. In practice, though, two factors make sustained daily wear and longitudinal deployment impractical for the quantified self: the discomfort of prolonged sensor-skin contact (e.g., gels and adhesives) and the sensor power demands that increase battery size, weight, and maintenance burden. We present GlassTENG, an ultra-low-power sensor that embeds three custom-fabricated triboelectric nanogenerators (TENGs) into a glasses frame at the angular artery on the nasal bridge, the superficial temporal artery on an extended arm, and the temporalis muscle at the temple. Each GlassTENG sensor is self-powered in transducing mechanical energy to electrical energy and consumes 1.36 $\mu$W per sensor at the analog front-end. GlassTENG enables simultaneous capture of arterial pulse waveforms, jaw kinematics (e.g., clenching, tapping, eating), and upper facial activity (e.g., blinking, eyebrow movement). In a 20-participant user study, we achieve 93.8% accuracy across six jaw and upper facial activities and estimate heart rate with a mean absolute error of 1.82 beats per minute (BPM) relative to a ground-truth chest-strap sensor in 30s windows. Together, these results establish a future pathway toward a longitudinally worn, ultra-low-power, glasses-based physiological monitoring platform.

---


### 180. [FootsiesGym: A Fighting Game Benchmark for Two-Player Zero-Sum Imperfect-Information Games](https://arxiv.org/abs/2607.06514)

**<font color=#1a73e8>作者：</font>** Chase McDonald, Nathan Tsang, Wesley N. Kerr  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present FootsiesGym, an open-source environment for learning in a non-trivial two-player, zero-sum, imperfect-information game. Built on HiFight's minimalist 2D fighting game Footsies, it isolates the cyclic, non-transitive strategic interactions of fighting game neutral play while remaining simple enough for efficient analysis. We provide a vectorized simulator that enables high-throughput training on standard hardware, making the environment accessible and reproducible. We describe the design of the environment, benchmark several reinforcement learning algorithms, and discuss open research directions it enables. The code is available at this https URL.

---


### 181. [Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.06516)

**<font color=#1a73e8>作者：</font>** Songbur Wong, Xiaosong Jia, Junqi You 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating end-to-end autonomous driving (E2E-AD) remains challenging, as existing driving simulation methods often trade off closed-loop interactivity (e.g., CARLA) and real-world visual fidelity (e.g., nuScenes). We present \textbf{\emph{Point as Skeleton}}, a generative sensor simulation framework for state-updated autoregressive driving video generation, in which an autoregressive generator synthesizes visual observations from step-wise updated ego states, actor states, scene maps, and point-cloud skeleton conditions. To support closed-loop rollout, we introduce Reset-and-Roll, which adapts rolling diffusion inference to simulation by preventing future-conditioned latent states from being committed across simulation steps. To stabilize error accumulation during step-wise autoregressive rollout, we introduce point-cloud skeletons that decouple foreground and background assets and project them into camera-view painted-point and template-depth conditions, providing appearance and geometric cues. We further implement a nuPlan-based renderer-level closed-loop generative interface for evaluating generation under ego deviations from the original log. Experiments on nuScenes and nuPlan show that \textit{Point as Skeleton} improves autoregressive generation quality during closed-loop rollout, demonstrating its potential for visually faithful closed-loop driving simulation. The code is available at this https URL.

---


### 182. [DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression](https://arxiv.org/abs/2607.06523)

**<font color=#1a73e8>作者：</font>** Anna Cordoba, Adam Puente Tercero, Nerea Angulo Hijo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context language model inference is increasingly limited by the memory bandwidth and capacity required to store key-value caches, yet existing compression methods often apply uniform budgets across layers or tokens and degrade retrieval when lexical cues and semantic states require different preservation. We introduce DepthWeave-KV, a token-adaptive cache compression method that factorizes key and value states across neighboring transformer layers using shared low-rank channel bases while retaining lightweight token-specific residuals where attention behavior is sensitive. DepthWeave-KV combines cross-depth residual factorization with a token-conditional depth router that allocates higher reconstruction rank to instruction-bearing and retrieval-critical tokens, and uses calibration-free online error tracking from attention-output probes to adapt compression during generation without retraining the base model. A fused CUDA implementation jointly performs basis lookup, residual dequantization, and attention projection to reduce decode-time memory traffic. Across LongBench, Needle-in-a-Haystack, L-Eval, and long-form QA and summarization benchmarks, DepthWeave-KV achieves near-full-cache task quality with substantially lower memory use, improving average score and retrieval accuracy over prior compressed caches while reaching 8.3x KV memory reduction and 72.8 tokens per second at 64K context.

---


### 183. [Crossroads: A Smart Contract Layer for Chain-Abstracted Assets](https://arxiv.org/abs/2607.06525)

**<font color=#1a73e8>作者：</font>** James Austgen, Dani Vilardell, Ari Juels  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper introduces Crossroads, a smart contract layer for chain-abstracted assets. In Crossroads, assets from nearly any chain are represented on a single backend blockchain as ERC-20 tokens. As a result, any asset can participate in smart-contract-based exchange, lending, or privacy applications on a single unified platform. So while Crossroads offers cross-chain bridging, a common, partial approach to alleviating the fragmentation of the blockchain ecosystem today, this is just one service within Crossroads' general-purpose chain-abstraction model.
Crossroads relies on key encumbrance: a threshold signing committee holds encumbered keys controlling assets on each integrated chain, signing transactions only as authorized by smart contracts on the backend blockchain. Asset movements are fee-efficient, as ownership changes are recorded on the backend blockchain and users may set the transaction fee for withdrawals.
Crossroads enables permissionless, modular integration of new blockchains using pluggable oracles with flexible design options (zkBridge, TEE-based, hybrid). Asset deposits into Crossroads benefit from strong, chain-specific finalization guarantees, minimizing the risk of reorg attacks. Unlike existing bridges, however, third-party smart contracts in Crossroads can provide fast, optimistic access to funds before finalization completes.
We prove that Crossroads satisfies soundness: given an honest quorum of signing committee members, any user can unilaterally generate a withdrawal transaction transferring their net balance to an account on an integrated blockchain. We implement a proof of concept across multiple public blockchains: Bitcoin, Ethereum, and Solana. We catalog a range of applications enabled by Crossroads, including universal wallets, cross-chain staking and lending, privacy-preserving payments, and private management of public blockchain assets.

---


### 184. [Life Style Levels: Neighborhood Delineation using Geospatial Data](https://arxiv.org/abs/2607.06529)

**<font color=#1a73e8>作者：</font>** Srivatsa Kulkarni, Debarag Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-scale socioeconomic information is often unavailable across rapidly ur-banizing regions of the developing world, like India, limiting the ability to delineate intra-urban variations in affluence and deprivation. This study pro-poses a scalable, grid-based urban delineation framework using building morphology derived from open-source satellite imagery. Urban areas across 59 Indian cities and towns are partitioned into high-resolution spatial grids and characterized using interpretable morphological indicators, which are combined into a transparent, rule-based scoring framework to delineate areas with contrasting levels of urban affluence. The resulting classifications are validated through ground-level Google Street View observations, revealing a sharp contrast between the grid classes which are consistent with the ex-pected effects of the lifestyle affluence indicators. We further investigate density-based clustering of building footprints in Mumbai to identify dense urban settlements, demonstrating that the resulting clusters exhibit substan-tial spatial overlap with known informal settlements across the city. Finally, we conduct an exploratory analysis mapping consumer loan delinquency across the derived affluence classes. By relying entirely on publicly available geospatial data, the proposed framework provides a scalable, interpretable, and cost-effective approach for granular urban affluence mapping across In-dian cities.

---


### 185. [The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology](https://arxiv.org/abs/2607.06531)

**<font color=#1a73e8>作者：</font>** Ghassen Marrakchi, Basarab Matei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> - Objective: Multimodal deep learning models in oncology are currently limited by monolithic designs that rigidly couple data ingestion, clinical routing, and artificial intelligence (AI) inference. To address this inflexibility, we propose the Large Cancer Assistant (LCA), a model-agnostic, post-hoc orchestration framework designed for scalable clinical decision support. - Methods: The LCA is mathematically formalized as a 7-tuple architecture grounded in the principle of Algorithmic Impermeability, ensuring the orchestration logic remains strictly independent of underlying black-box AI models. We introduce the Entry Theory, leveraging Geometric Deep Learning (GDL) to standardize multimodal patient data along distinct structural and medical axes. The system dynamically orchestrates data via a Cancer Switching Module and intentionally isolates the core AI execution from volatile hospital IT infrastructures by outputting a Standardized Intermediate Payload (SIP). - Results: A Proof of Concept (PoC) validated the orchestration logic across four technical scenarios. The framework executed a nominal flow with negligible orchestration overhead. It empirically demonstrated algorithmic impermeability by maintaining an invariant routing projection during AI model swaps, and it validated strict failure-safety by achieving a 100\% recall rate in generating targeted Supplementary Data Requests (SDR) under injected data anomalies. Multi-protocol execution capability was also successfully verified. - Conclusion: By structurally decoupling multimodal ingestion from feature inference, the LCA provides a highly adaptable and modular orchestration foundation. The SIP establishes a clear architectural boundary, natively setting the stage for downstream Electronic Medical Record (EMR) interoperability as an independent future paradigm.

---


### 186. [GraphBU: MILP Instance Generation with Graph-Native Block Units](https://arxiv.org/abs/2607.06532)

**<font color=#1a73e8>作者：</font>** Xiaolei Guo, Chenyu Zhou, Jianghao Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-integer linear programming (MILP) instances used for solver development are hard to obtain when models come from private or application-specific pipelines. A generator must keep the structure that solvers and learned policies rely on. Existing general generators usually choose their generation unit from a formulation template, summary statistics, local graph edits, or blocks found after recombination. These units do not explicitly record how a local part of the MILP is coupled to the rest of the instance. We propose GraphBU, a graph-native generator whose basic unit is a local subproblem plus its interface. The method promotes coupling nodes into master constraints or boundary variables and uses the resulting block units for compatibility-checked replacement. The analysis focuses on the properties needed by this construction: promotion separates interfaces, replacement can preserve feasibility under an interface-slack condition, and the graph construction is invariant to row-column permutations. On MILP instances generation, this unit keeps graph statistics close to the source family, preserves feasibility on most datasets, and improves downstream Predict-and-Search training. Genrated by GraphBU, The average graph-statistical similarity was approximately 0.934, the average feasibility was approximately 96.7%, and the average increase in the main index of downstream PS was approximately 8.0%.

---


### 187. [Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs](https://arxiv.org/abs/2607.06540)

**<font color=#1a73e8>作者：</font>** Zhenyu Liu, Yunxin Li, Xuanyu Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing seamless, high-performance, native intelligent full-duplex Spoken Language Models (SLMs) remains a critical challenge and long-standing goal for the speech and NLP community. Despite notable progress, recent endeavors are fundamentally constrained by severe modality interference, which causes substantial knowledge degradation and compromises semantic integrity -- ultimately making full-duplex SLMs feel unnatural and unintelligent. In this paper, through an exhaustive fine-grained analysis of model optimization dynamics, we uncover the root cause of such performance degradation, revealing that modality interference arises from inherent gradient conflicts between acoustic and semantic modeling when the two modalities are forced to share a deep parameter space. Guided by this key insight, we introduce Lychee-FD, a native end-to-end full-duplex framework designed to mitigate modality interference. Importantly, we propose a hierarchical parameter separation strategy that decouples conflicting modalities in deep layers while preserving cross-modality coherence via a dedicated semantic alignment channel. Extensive experiments on multiple full-duplex benchmarks demonstrate that our method significantly advances the state of the art, yielding substantial improvements in both speech intelligence (+7.4% on Spoken QA) and full-duplex interaction fluidity (+28.5% on FullDuplexBench 1.5) without compromising inference efficiency. To the best of our knowledge, this work is the first to achieve two key advances: 1) uncovering and elucidating the root cause of modality interference in full-duplex SLMs, and 2) designing an elegant hierarchical model together with a practical solution for seamless, high-performance, native intelligent full-duplex SLMs.

---


### 188. [On the feasibility of dependency parsing of non-human sequences without a gold standard. Is evaluation possible in other species?](https://arxiv.org/abs/2607.06542)

**<font color=#1a73e8>作者：</font>** Ramon Ferrer-i-Cancho, Catherine Hobaiter, Thore Bergman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dependency parsing consists of finding a tree representation for a sequence. Unsupervised dependency parsing aims to develop parsing methods without a gold standard during model training. In human languages, an unsupervised parser can be evaluated because some gold standard is usually available or can be created. For other species, a gold standard is unknown. Thus one may conclude that it is impossible to determine the accuracy of an unsupervised parser and, consequently, dependency parsing is unfeasible in other species. However, here we apply recent advances in network science to demonstrate that the proportion of correct edges retrieved by a parser must be high for the sequences of vocalizations or gestures that non-human primates produce due to the fast decay of the sequence length distribution. In contrast, human language sequences lack that property. Therefore, evaluation without a gold standard is feasible in non-human primates but a hard problem in humans.

---


### 189. [Rethinking Indic AI from a Lens of Cultural Heritage Preservation](https://arxiv.org/abs/2607.06544)

**<font color=#1a73e8>作者：</font>** Aparna Madva, Sharath Srivatsa, Srinath Srinivasa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Artificial Intelligence (AI) makes inroads into different parts of the Indian subcontinent, there is significant interest in studying how AI impacts the linguistic and cultural foundations of this civilization. AI is seen as a ''double-edged sword'' where on the one hand, it can enable access and inclusion for a large population, on the other, it can homogenize worldviews and exclude underrepresented languages and worldviews. In this paper, we try to characterize this problem by addressing the extensive characteristic nature of Indian linguistics and the way they closely connect to cultural practices and worldview. We then perform a longitudinal survey of how Natural Language Processing (NLP) techniques have evolved in this space, tracing the historical development of Indic NLP, covering key milestones, methodological shifts, and resource creation efforts. In addition, the paper also examines the structural and sociolinguistic characteristics of Indian languages, such as rich morphology, complex scripts and grammar rules, diglossia, and large dialectal variation, and explains how these create unique challenges for building AI foundation models. We then discuss the growing role of Indic foundation models and analyze how these models address these long-standing resource and representation gaps. Finally, we propose a research direction called 'Culture Sensing', which re-imagines AI based on hermeneutic reasoning. Culture Sensing aims to address open problems such as ensuring equitable performance across low-resource languages and producing outputs that are culturally meaningful. By bringing together past work, current techniques, and emerging trends, this paper outlines research directions that can guide the next phase of Indic NLP and contribute to the development of more robust and inclusive Indic foundation models.

---


### 190. [Graph Convolutional Attention: A Spectral Perspective on Graph Denoising and Diffusion](https://arxiv.org/abs/2607.06546)

**<font color=#1a73e8>作者：</font>** Shervin Khalafi, Igor Krawczuk, Sergio Rozada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Denoising graphs is a fundamental problem in graph learning and the core operation of graph diffusion models. Attention-based architectures like graph transformers have recently shown promise in denoising graphs. However, our principled understanding of attention-based graph denoising remains limited, making it unclear whether standard attention is the right mechanism for this task. Here we show that, under a denoising objective, linear attention is suboptimal and can only learn an average spectral denoising filter over the training distribution. This creates a fundamental limitation as graphs often vary spectrally across the distribution. To overcome this limitation, we introduce Spectral Attention, which directly utilizes the input graph spectrum and provably outperforms linear attention by a margin governed by the spectral diversity of the distribution. We then derive Graph Convolutional Attention (GCA), a practical and permutation-equivariant realization of this idea that implements spectral denoising through graph-filtered queries and keys. For stochastic block models, GCA provably matches the idealized Spectral Attention mechanism. We further show that the softmax operation, that follows the attention, provides additional denoising by approximately projecting noisy eigenvectors onto the clean eigenspace. Empirically, replacing linear attention with GCA consistently improves graph denoising and diffusion on synthetic and real datasets, with gains strongly correlated with spectral diversity. In DiGress, GCA matches standard graph-transformer performance without computing expensive structural features, and when combined with the recently proposed PEARL positional encodings, avoids explicit eigendecomposition computations resulting in faster inference without degrading quality. The code can be found here: this http URL

---


### 191. [Unsupervised Domain Adaptation for Calcification Classification in Mammography Across Multi-Site Datasets](https://arxiv.org/abs/2607.06549)

**<font color=#1a73e8>作者：</font>** Xuan Liu, Derek L. Nguyen, Emily C. Barre 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based computer-aided diagnosis (CAD) systems have shown strong performance in breast cancer diagnosis, particularly for classification tasks in mammography. However, domain shifts across multi-site datasets remain a challenge, especially when models are applied to unseen domains. In this work, we proposed a calcification classification framework to improve malignant versus benign breast disease classification across multi-site mammography datasets. The framework consisted of two components: (1) an unsupervised domain adaptation module based on style transfer models (AdaIN and CycleGAN) to generate vendor-specific and technique-specific training samples without additional annotations, and (2) a supervised classification module using Swin Transformer V2 as the backbone. We evaluated the proposed method on three datasets: cross-validation on OPTIMAM (National Health Service, United Kingdom; n=2994), followed by external validation on EMBED (Emory University; n=125), and Duke Calcification Dataset v1 (n=788). These datasets cover multiple vendors and include both full-field digital mammography and synthetic 2D images derived from digital breast tomosynthesis. The proposed framework improved cross-site performance for both EMBED (AUC 0.68 to 0.72) and the Duke Calcification Dataset (AUC 0.68 to 0.73). These findings indicate that domain adaptation can reduce domain shifts and improve the generalization for calcification classification across multi-site datasets.

---


### 192. [MonoIR-RS: Infrared Remote Sensing Vision-Language Learning with CLIP and VLM Adaptation](https://arxiv.org/abs/2607.06552)

**<font color=#1a73e8>作者：</font>** Jiaju Han, Ma Yaqi, Yahui Chai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared remote-sensing imagery captures intensity structure, object-background contrast, and illumination-invariant cues often invisible in RGB imagery. Yet, most remote-sensing vision-language resources and models focus on visible-band semantics, leaving infrared vision-language understanding underexplored. We introduce MonoIR-RS, a large-scale infrared remote-sensing vision-language dataset and benchmark that couples IR-aware data construction with CLIP-style contrastive adaptation and VLM instruction tuning. Built from the same source pool and split as FusionRS, MonoIR-RS retains the infrared image as the model-facing modality, yielding 600,000 synthesized infrared images and 59,032 retained IR-aware caption records. The model experiments use this retained language-supervision subset, whose captions rewrite supervision around grayscale structure and infrared-style contrast instead of RGB appearance. We show that the synthesized infrared imagery is markedly closer to real thermal imagery than a grayscale conversion on the AVIID benchmark. We fine-tune five CLIP backbones and six VLM backbones, and calibrate them against zero-shot behavior: IR-aware adaptation lifts CLIP mean recall by up to 12.8 points and drives VLM captioning IR-cue coverage to 100% while reducing residual RGB-color leakage to near zero. By isolating the infrared modality from RGB-IR dual-modal learning, MonoIR-RS offers a controlled, reproducible testbed for aligning infrared remote-sensing evidence with language.

---


### 193. [From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with Text-to-Image Models](https://arxiv.org/abs/2607.06553)

**<font color=#1a73e8>作者：</font>** Zanyi Wang, Xin Lin, Haodong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale text-to-image models are attractive backbones for dense prediction because RGB generation pretraining learns rich semantic, structural, and geometric priors. Existing generative and editing approaches reuse these priors by casting dense prediction as target generation: annotations such as depth, normals, alpha mattes, masks, and heatmaps are encoded into an RGB-trained VAE latent space and decoded back as image-like targets. We argue this inherits more of the generative output interface than dense prediction requires: unlike RGB synthesis, dense prediction asks for pixel-correct, task-native fields on the same image plane, not new RGB content to be rendered. Our key observation is that a pretrained DiT already organizes RGB inputs through a patch-to-token-to-patch lattice on the image plane, so each token indexes a fixed output patch whose channels can carry task-native quantities instead of RGB appearance. We instantiate this as ReChannel: we keep the VAE encoder for the DiT's input distribution but drop the target-side decoder, adapt the frozen DiT with task LoRA, and map each token to its p x p x K_t pixel-space patch through a shared token-local linear head--about 33K parameters, no spatial mixing. Using FLUX-Klein, we evaluate on six dense prediction tasks and over a dozen benchmarks. This minimal interface sets new state-of-the-art on trimap-free matting, KITTI depth, and referring segmentation, and stays competitive on normals, saliency, and pose. In a matched 4B setting it is more accurate and 2.48x faster than an edit-plus-latent-decode counterpart--dense perception can benefit from generative pretraining without inheriting its output interface.

---


### 194. [ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation](https://arxiv.org/abs/2607.06555)

**<font color=#1a73e8>作者：</font>** Ruihang Zhang, Felix Taubner, Pooja Ravi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking the six-degree-of-freedom (6-DoF) pose of objects and surfaces from monocular video is a long-standing problem in computer vision. To tackle this problem, existing methods require inputs beyond the video itself-such as 3D models, depth maps, object masks, or task-specific learned features-and they struggle with textureless, transparent, reflective, or deformable surfaces. Here, we introduce ProxyPose, which recasts 6-DoF pose tracking as video-to-video translation. Given only a video and a single marked pixel in the first frame, a fine-tuned video diffusion model translates the input into a proxy video-a synthetic video depicting a colored polyhedron undergoing the same local rigid-body motion as the surface region at the marked pixel. Because the proxy's geometry and appearance are known by construction, recovering its full 6-DoF trajectory reduces to classical pose estimation with off-the-shelf solvers. This formulation leverages large-scale video pre-training to absorb the hardest aspects of pose tracking-handling challenging materials, occlusions, and deformations-into the translation step, while operating at the pixel level with no assumptions about object identity, boundaries, or global rigidity. ProxyPose achieves state-of-the-art 6-DoF pose tracking accuracy without the additional inputs required by competing methods and after fine-tuning the video model only on synthetic data. We further demonstrate that ProxyPose extends to face tracking, camera pose estimation, and challenging in-the-wild scenes that are beyond the reach of existing approaches. Project page: this https URL.

---


### 195. [ELSA3D: Elastic Semantic Anchoring for Unified 3D Understanding and Generation](https://arxiv.org/abs/2607.06565)

**<font color=#1a73e8>作者：</font>** Tianjiao Yu, Xinzhuo Li, Yifan Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified 3D foundation models aspire to generate 3D assets and reason about them in language within a single backbone, but their text-3D interaction remains largely implicit. Existing methods concatenate text and 3D tokens into a flat sequence and rely on self-attention, collapsing coarse structural cues and fine geometric details into one undifferentiated representation. We introduce ELSA3D, a unified 3D model that addresses this with elastic semantic anchoring, structuring language and geometric reasoning jointly along matched abstraction scales. ELSA3D represents geometry with a scale-aware octree tokenizer and introduces Anchor Tokens, sparse cross-modal units that select semantic cues, route them to the most relevant 3D scale, retrieve scale-specific geometric evidence, and write the fused signal back into the unified representation, keeping interaction sparse yet precise. A lightweight per-block router makes both computation and reasoning elastic, choosing which text tokens instantiate anchors at which geometric scale so that cross-modal capacity concentrates where alignment is most needed. ELSA3D achieves state-of-the-art performance across image-to-3D generation, text-to-3D generation, and 3D captioning, outperforming the strongest unified baseline while roughly halving FLOPs and inference latency relative to the non-elastic version of the same model.

---


> [!TIP]
> 当前位于：**151-195**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-195**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
