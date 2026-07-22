# 📦 其他研究 | 2026年07月23日

> 本类共 **241** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-241](./part-05.md)

---

### 151. [Public perceptions of AI-driven decision-making in healthcare: A structural equation modeling approach](https://arxiv.org/abs/2607.18884)

**<font color=#1a73e8>作者：</font>** Leonie Westerbeek, Ernesto de Leon, Julia C.M. van Weert  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is increasingly integrated into healthcare to support diagnostics, decision-making, and administrative processes. However, the successful implementation of AI depends not only on technical performance but also on public perceptions of its helpfulness, riskiness, and fairness. This study examines public perceptions of automated decision-making (ADM) in healthcare. Data were drawn from the first wave of an ongoing longitudinal survey panel. The final sample consisted of 3,915 respondents and was analyzed with structural equation modeling. Perceptions of ADM in healthcare as helpful, risky, and fair were treated as the dependent variables. AI literacy, familiarity with different forms of AI, confidence in clinicians' ability to distinguish AI- from human-generated content, use of conversational agents for health information, and use of traditional digital health information sources were included as exogenous. Greater familiarity with different forms of AI, higher confidence in the clinician's ability to recognize AI-generated content, and use of conversational agents for health information were associated with greater perceived helpfulness. Use of conversational agents was associated with lower perceived risk, whereas greater familiarity with AI and greater reliance on traditional health information sources were associated with higher perceived risk. Perceptions of ADM as fair were most strongly predicted by confidence in the clinician's ability, with additional small positive associations with AI familiarity, AI literacy, and use of conversational agents. Public perceptions of ADM in healthcare are shaped by technological familiarity, use of conversational agents, and confidence in human oversight. Overall, ADM's perceived helpfulness and fairness are driven more by trust in healthcare professionals than by trust in the technology itself.

---


### 152. [NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework](https://arxiv.org/abs/2607.18887)

**<font color=#1a73e8>作者：</font>** Yuan Gui, Hongchen Luo, Liqi Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vessel trajectory prediction in complex maritime environments is essential for traffic management, collision warning, route planning, and autonomous navigation. Although AIS-based learning methods have progressed rapidly, existing datasets are often released as raw message streams or irregular time series, with inconsistent sampling rates, noisy observations, heterogeneous coordinate systems, and non-unified scenario protocols. Most public AIS resources also lack structured representations of navigational lanes, waterway geometry, and navigable-region constraints, limiting reproducible, environment-aware forecasting. To address this, we introduce NaviAIS, a standardized scenario-level AIS dataset for vessel trajectory prediction. It organizes multi-vessel historical-future trajectories within unified temporal windows and local coordinate systems, and provides rasterized navigable maps, vectorized lane priors, lane graphs, and structured map representations. Compared with existing datasets, it jointly supports vectorized lanes, multi-scenario coverage, vectorized maps, open accessibility, and processed trajectories. Built on this dataset, we propose NaviLane, a hierarchical macro-action framework for map-aware prediction. NaviLane first performs trajectory-map joint encoding for a unified scene representation, then uses a discrete macro-action codebook to generate multimodal candidates coarse-to-refined. A residual refinement module improves local geometric and dynamical consistency, and a world-model-based consequence-aware evaluator ranks candidates by interaction risk and environmental feasibility. Experiments show NaviLane outperforms representative baselines in both single-modal and multimodal settings, confirming the value of structured navigational priors, hierarchical multimodal generation, and consequence-aware evaluation.

---


### 153. [Black-Mamba: Biologically-Inspired Leaky Accumulation for Conceptual Knowledge under Distribution Drift](https://arxiv.org/abs/2607.18899)

**<font color=#1a73e8>作者：</font>** Giuseppe Soriano, Nicola Tonellotto, Alberto Gotta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting under real-world conditions is inherently non-stationary, as the conditional distribution of future observations evolves over time. Recent test-time adaptive sequence models address this challenge by updating internal states during inference, but tie adaptation to instantaneous prediction errors or surprise. This coupling can conflate persistent distribution shift with stochastic innovations, leading to unnecessary updates and inefficient adaptation. We introduce Black-Mamba, a test-time adaptive forecasting architecture that formulates online adaptation as evidence-gated state tracking under distribution drift. The model augments a base predictor with a dynamic memory updated when temporally accumulated surprisal provides sufficient evidence of a regime change. This turns adaptation into a selective, event-driven process rather than a continuous one. Across multiple forecasting benchmarks with non-stationary dynamics, Black-Mamba achieves competitive or improved predictive performance compared to existing test-time adaptation methods while significantly reducing the number of memory updates during inference. Together with mathematical analysis and biological evidence, these results suggest that accumulated surprisal provides a principled signal for distinguishing persistent drift from transient noise, yielding more efficient and robust adaptation.

---


### 154. [SynGallery: A Synthetic Gallery of Real Paintings for Instance-Level Artwork Recognition](https://arxiv.org/abs/2607.18907)

**<font color=#1a73e8>作者：</font>** Patryk Bartkowiak, Jakub Markil, Bartosz Kotrys 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance-level artwork recognition requires matching a handheld visitor photograph to a specific work in a large museum collection. This is challenging because painting datasets typically provide clean catalog images for training, while test queries are captured under oblique viewpoints, gallery lighting, reflections, frames, and other scene-level variations. We present SynGallery, a synthetic gallery dataset for artwork retrieval that addresses this gap without collecting additional real photographs. Starting from catalog images of real paintings, we place each artwork into a procedurally generated 3D gallery scene and render it from multiple viewpoints under varied geometric and appearance conditions, while preserving the exact identity of the original work. The resulting dataset contains 24,490 rendered views of 4,898 paintings from the Met benchmark. We show that these synthetic views provide a stronger training signal than the corresponding studio photographs. At the same number of training data points, training only on SynGallery improves art painting recognition from 67.18 to 73.47 GAP$^-$. When added to the full Met training set, SynGallery improves the published benchmark protocol from 35.97 to 38.48 GAP. Ablation experiments show that the gain comes primarily from geometric viewpoint variation rather than photographic realism: blur, sensor noise, and image compression consistently reduce performance.

---


### 155. [Enhancing Transformer-based Routing by Encoding Distance via Relative Positional Encoding](https://arxiv.org/abs/2607.18909)

**<font color=#1a73e8>作者：</font>** Leyre Encío, Daniel Fuertes, Carlos R. del-Blanco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper explores Relative Positional Encoding (RPE) as an additive bias in Transformer architectures to solve the Team Orienteering Problem. By embedding in the attention mechanism pairwise spatial relationships among nodes of the graph that represents the routing problem, the transformer encoder can compute a richer spatial-aware graph embedding that allows the decoder to estimate better routes. Experimental results involving instances up to 100 nodes demonstrate consistent improvements in collected rewards and optimality gaps over vanilla Transformer architectures used by other state-of-the-art works. These findings highlight that explicit relational modeling significantly enhances scalability and generalization for complex combinatorial optimization.

---


### 156. [Breaking Feedback-Blindness: Utility-Augmented Transformer for Sequential Decision Making](https://arxiv.org/abs/2607.18910)

**<font color=#1a73e8>作者：</font>** Yuyang Shen, Shan Dai, Daimin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential decision making in non-stationary and partially observable environments requires rapid adaptation to latent regime changes. However, existing Transformer decision models face a structural bottleneck in the retrieval mechanism: even when reward is used for training or exposed as an input token, attention retrieval remains primarily driven by observation-derived similarity. We formalize this limitation as feedback-blind retrieval, and formally show that, on feedback-informative tasks, observation-equivalent histories with different action-reward outcomes cannot be distinguished by any observation-only attention, resulting in suboptimal choice. To address this mismatch, we propose the Utility-Augmented Transformer (UAT), a new feedback-conditioned retrieval attention architecture in which a compact utility state modulates the query, key, and value projections, allowing action-reward history to directly alter context retrieval during the forward pass. UAT also enjoys an exact zero-gate degradation property that recovers the Vanilla Transformer when feedback is uninformative. Under finite-horizon compactness and Lipschitz assumptions, we prove that UAT strictly enlarges the observation-only Transformer class and can uniformly approximate feedback-dependent decision maps. Across four non-stationary benchmarks: synthetic navigation with hidden goal shifts, non-stationary sepsis treatment, cross-market portfolio allocation, and delayed-feedback recommendation, UAT consistently improves performance over observation-only, test-time adaptation, and input-level feedback baselines, with particularly large gains in noisier regimes that require stronger adaptation.

---


### 157. [From a Multilingual Streaming ASR Backbone to Kenyan-Language Systems: Data-Centric Adaptation of Nemotron 3.5 for Kikuyu, Dholuo, and Kalenjin](https://arxiv.org/abs/2607.18912)

**<font color=#1a73e8>作者：</font>** Mark Gatere  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) for African languages is constrained by orthographic inconsistency, annotation artifacts, missing audio, speaker and domain imbalance, and evaluation procedures that differ from deployment. We present an end-to-end engineering study adapting NVIDIA Nemotron 3.5 ASR Streaming 0.6B to Kikuyu, Dholuo, and Kalenjin. Starting from a Kenyan Swahili-adapted checkpoint, we retain its cache-aware FastConformer RNN-T, prompt conditioning, and streaming decoder during full-parameter fine-tuning. The study covers corpus auditing, Unicode normalization, split checks, duration filtering, low-rate continuation, validation-based checkpoint selection, true-streaming evaluation, artifact preservation, and isolated serving.
On internal, adaptively consulted evaluation sets excluded from gradient updates at context [56,13], selected Kikuyu and Dholuo models achieve 42.97% and 33.98% WER, respectively. Dholuo records 9.59% CER and 8.13% no-space CER under its frozen historical label policy; Kikuyu records 7.79% no-space CER. Kalenjin remains a work in progress: v1-v reaches 68.74% WER on a 2,411-row clean-v3 diagnostic subset excluding long-pause annotations, digit-bearing references, and targets shorter than three tokens. Its checkpoint selection used a mixed-source validation manifest containing test-origin rows, so the score is not an independent generalization estimate. We also report negative findings involving non-speech labels, short-utterance over-generation, boundary-sensitive WER, and cloud job-lifecycle failures. We make no state-of-the-art claim because the internal sets, repeated consultation, and normalization differ from public benchmarks. This work provides an auditable account of adapting a multilingual streaming model into language-specific systems without discarding streaming constraints.

---


### 158. [Circuit Claims Depend on What Is Extracted and How It Is Compared](https://arxiv.org/abs/2607.18921)

**<font color=#1a73e8>作者：</font>** Yang Sheng, Jie Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Circuit extraction identifies a small set of model components whose presence preserves a target behavior under ablation, and the resulting circuit is often read as the mechanism behind that behavior. We argue that this reading is under-determined: preserving behavior does not single out one circuit, because the claim it supports depends on which circuit is reported and how two circuits are compared. We make this concrete in a synthetic Lean tactic-prediction benchmark -- predicting the next step of a proof -- where fixed proof rules with randomized surface form let differences between extracted circuits be attributed to these choices rather than to the task. Across dense and weight-sparse checkpoints (most weights constrained to zero) of the same transformer, evaluated on atomic (single-rule) and compositional (multi-rule) proofs, we vary which extracted object is reported (a compact prediction-preserving circuit, a broader graph that also keeps surrounding read, write, and routing structure, or the smallest subgraph meeting a post-ablation loss threshold), and whether each attention head's query and key are represented jointly or separately. Exact component-to-component edge overlap is low and sensitive to these choices, at times dropping to a random baseline, while two coarser summaries stay stable: the set of selected attention heads, and the circuit-size ranking of conditions that differ in which supervised checkpoint initializes reinforcement learning (RL). The largest accuracy gains from RL on compositional proofs come with the most structure beyond the atomic circuits. A circuit-level claim is therefore well defined only once one states which circuit is reported, the pruning threshold used to extract it, and the level at which circuits are compared. We distill these requirements into a reporting practice for circuit-extraction studies.

---


### 159. [Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning](https://arxiv.org/abs/2607.18923)

**<font color=#1a73e8>作者：</font>** Stella Ho, Joel Villalobos, Joseph West 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ECoG-based visual semantic decoding enables inference of semantic interpretation of visual perception from complex, noisy brain activity. This study examines the feasibility of visual semantic decoding using an end-to-end deep learning framework using electrocorticography (ECoG). Specifically, the decoding task is to predict visual categories from video stimuli using time-series neural inputs. A previously collected ECoG dataset from participants ($n=17$) with drug-resistant epilepsy is used for analysis. With fewer than 50 training samples per visual category, this study evaluates multiple deep learning approaches, artificial neural network architectures, and frequency-band filtered inputs. The best-performing approach is analyzed to shed light on the discriminative information it relies on across spectral, temporal, and cortical dimensions. The selected decoding system uses mixup augmentation, a Transformer-based encoder, and high-gamma (80-150 Hz) inputs with a 900 ms post-stimulus window. Further analysis shows that early visual cortex (V2-V4), ventral stream visual cortex, MT+ complex with neighbouring visual areas, and lateral temporal cortex contributed substantially to decoding performance. This study demonstrates that an end-to-end deep learning framework can yield promising decoding performance from dynamic visual stimuli without handcrafted features, while the model behavior remains interpretable through spectral, temporal, and cortical dimensions, which are broadly consistent with established neuroscience knowledge.

---


### 160. [Learning Explicit Physical Parameter Control and Benchmarking for Video Generation](https://arxiv.org/abs/2607.18924)

**<font color=#1a73e8>作者：</font>** Yanxun Li, Hao Wen, Bingze Song 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in image-to-video generation have improved visual realism, making physically grounded and controllable dynamics an important step toward future world simulation.
Current models often generate plausible motion, but it is not reliably governed by explicit physical causes, and instance-level constraints can leak or become entangled in multi-object interactions.
We attribute this gap to two missing pieces: large-scale, fine-grained physical parameterization, and model designs that correctly bind physical attributes to instances and emphasize dynamics over appearance.
To bridge this gap, we introduce PhyParam-Dataset, an interaction-centric collection of 130K physically simulated videos with dense physical parameterization, including force vectors, object material properties, and environmental constants across five representative rigid-body motion types.
Built on this data, we present PhyParam, a physics-guided image-to-video diffusion model that conditions on object-level forces, masses, friction, restitution, and scene-level gravity via a lightweight physical-attention routing mechanism, and further improves motion learning with semantic-structural feature-space supervision.
We also establish PhyParam-Bench, a benchmark for physical-law consistency in image-to-video generation, with a multi-level protocol evaluating temporal dynamics, spatial stability, and semantic--physical alignment. Experiments show that PhyParam improves physical consistency while maintaining high visual fidelity, advancing explicit rigid-body physical-parameter control for image-to-video generation.
We will publicly release the dataset, benchmark, and code to support future research.

---


### 161. [Functional Equivalence and Geometric Diversity in Neural Network Approximations: An Empirical Characterization](https://arxiv.org/abs/2607.18930)

**<font color=#1a73e8>作者：</font>** Anuragine S A, Prem Jagadeesan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Universal Approximation Theorem states that a neural network with a single hidden layer is sufficient to approximate any continuous univariate function on a compact domain to arbitrary error. However, the uniqueness of such neural network representations is not guaranteed, raising questions about practical identifiability. In this work, we address this concern by analyzing functional equivalence and geometric diversity of neural network approximations to a few elementary mathematical functions. The analysis includes an extensive study of single-layer neural networks and multilayer perceptrons under noisy and noise-free conditions. Beyond just network capacity, we study the geometric properties through the lens of sloppiness, characterized by the eigen spectrum of the Hessian of the cost function and the effective rank to quantify the dimensionality of parameter space. The study reveals large equivalence classes of functionally indistinguishable yet geometrically diverse networks that consistently exhibit low effective rank and structural redundancy. Finally, a model select criterion is proposed for identifying optimal models based on parsimony, ease of estimation, and inference efficiency.

---


### 162. [Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing](https://arxiv.org/abs/2607.18934)

**<font color=#1a73e8>作者：</font>** Laurin Wagner, Mario Zusag, Bernhard Thallinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern ASR models trained on heterogeneously annotated data treat transcription style (verbatim vs. intended) as an uncontrolled latent variable, causing measurable decoding instability, evaluation confounding (up to 60% of reported WER attributable to style mismatch), and unreliable word-level timing. We show that models already encode both styles; the challenge is controlled activation. Using coverage-aware decoder task tokens trained on parallel verbatim/intended transcript pairs, we raise German disfluency F1 from 10% to 79% zero-shot, despite English-only training. Full English-only fine-tuning surpasses all baselines in verbatim accuracy, disfluency detection, and intended-mode quality across both languages. We further introduce supervised cross-attention fine-tuning that improves word-level timestamps on disfluent speech beyond forced-alignment baselines. Finally, we propose verbatimize, a new task enabling scalable creation and enrichment of speech corpora with high-quality canonical verbatim transcriptions.

---


### 163. [What General Intelligence Requires: Non-Reducible Constraints Across Levels of Description](https://arxiv.org/abs/2607.18943)

**<font color=#1a73e8>作者：</font>** Subhomoy Bakshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General intelligence, of the kind that underwrites the full range of human cognitive achievement, is not a property of computational architecture alone. This paper advances a single thesis: the structural constraints on general intelligence occupy distinct levels of description and are mutually non-reducible, in the sense that the special-sciences tradition gives to that term. It follows that no single architectural advance, and no continuation of the scaling programme by itself, can produce artificial general intelligence (AGI), and that research programmes must be evaluated against the full constraint profile rather than against performance on any one benchmark. The thesis is developed through a method that reads general intelligence through four evidential lenses, AI systems research, anthropology, law, and economics, each anchored to a distinct level of description, supplemented by speculative fiction used as a disciplined heuristic in the context of discovery rather than the context of justification. Applying the method yields a taxonomy of twenty-three structural constraints organised into eight clusters; six are examined in depth and ordered as an ascending ladder of levels, with explicit bridges showing why progress at one level cannot carry to the next. The argument issues in five falsifiable predictions, each stated with a named benchmark family and a disconfirmation condition, converting a descriptive framework into a research programme with a longer horizon than the scaling hypothesis implies.

---


### 164. [Constrained CTC Decoding for Efficient Diacritic Restoration](https://arxiv.org/abs/2607.18946)

**<font color=#1a73e8>作者：</font>** Rufael Marew, Amr Keleg, Hanan Aldarmaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we address diacritic restoration for Arabic speech transcripts. Most speech data are undiacritized, limiting the ability of modeling fine-grained phonological distinctions. The speech modality has recently been explored as a way to complement text-based diacritic restoration efforts. We propose an efficient non-autoregressive approach for speech-to-text diacritization based on Connectionist Temporal Classification (CTC). Our method incorporates hard constraints during decoding by constructing a character-level diacritization lattice from an undiacritized transcript and restricting hypotheses to valid diacritized realizations. We evaluate on Classical Arabic and Modern Standard Arabic test sets (namely, ArVoice and ClArTTS) against a more computationally-complex multi-modal diacritic restoration baseline, and show statistically significant reductions in diacritic error rates in both, demonstrating that the proposed approach offers both performance and efficiency gains.

---


### 165. [H$^2$SD: Hybrid Hindsight Self-Distillation](https://arxiv.org/abs/2607.18955)

**<font color=#1a73e8>作者：</font>** Qiye Cai, Yichuan Ma, Linyang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning capabilities of large language models on tasks such as mathematical reasoning and code generation. However, most RLVR methods assign a scalar outcome reward to an entire trajectory, resulting in sparse supervision and limited token-level credit assignment. On-policy distillation (OPD) provides denser supervision by distilling token-level distributions from a stronger teacher model, but requires an additional teacher and typically assumes a shared vocabulary. On-policy self-distillation (OPSD) removes this dependency by conditioning the same model on privileged information to construct a teacher policy. However, directly matching the teacher distribution may cause information leakage and unstable optimization. RLSD avoids direct matching by using the teacher signal only to modulate update magnitudes, but it cannot provide an explicit correction direction when the sampled reasoning fails. To address this tradeoff, we introduce $\mathrm{H}^{2}\mathrm{SD}$, a hybrid hindsight self distillation framework that uses the teacher differently according to trajectory correctness. For successful trajectories, the teacher receives the student response confirmed as correct together with a rephrasing instruction, and its probabilities on the original response tokens are used to modulate update magnitudes without changing the direction determined by the reward. For failed trajectories, we condition the teacher on a reference hint containing key reasoning steps and a verified answer, and minimize the reverse KL divergence from the student to the teacher. Experiments on multiple challenging reasoning benchmarks show that H$^2$SD consistently outperforms representative RLVR, OPSD, and RLSD baselines while maintaining stable optimization and favorable generation efficiency.

---


### 166. [Variational meta-learning inference for low dimensional neural system identification](https://arxiv.org/abs/2607.18965)

**<font color=#1a73e8>作者：</font>** Matteo Rufolo, Dario Piga, Marco Forgione  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has proven highly effective for nonlinear system identification, but heavily parameterized neural networks are prone to overfitting in low-data regimes and lack reliable uncertainty quantification. The recently developed manifold meta-learning framework addresses the data efficiency problem by restricting the model parameters to a meta-learned low-dimensional manifold. However, that method is purely deterministic. We propose a fully probabilistic extension of the manifold meta-learning framework, based on amortized Variational Inference, where a generative prior over the low-dimensional parameter manifold is learned. During task-specific adaptation, we combine Maximum A Posteriori estimation with the Laplace approximation to yield a mathematically grounded posterior approximation. Evaluated on a static regression task and the Bouc--Wen dynamical system benchmark, the proposed approach achieves predictive accuracy comparable to its deterministic counterpart while successfully providing calibrated uncertainty bounds in severely low-data regimes.

---


### 167. [Measuring Reward-Seeking via Contrastive Belief Updates](https://arxiv.org/abs/2607.18966)

**<font color=#1a73e8>作者：</font>** Axel Højmark, Jérémy Scheurer, Evgenia Nitishinskaya 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models trained with reinforcement learning may learn to optimize the grader's judgment rather than the intended objective. This "reward-seeking" is difficult to measure because a model that pursues the grader's judgment and one that pursues the intended objective behave identically whenever the grader rewards the intended behavior. We measure reward-seeking using Contrastive Synthetic Document Finetuning to change a model's beliefs about what the grader rewards, putting those beliefs in conflict with what users or developers want, and measuring the rate at which the model adopts each party's preferred behavior. Applied to intermediate checkpoints of a capabilities-focused OpenAI o3 RL run, without safety training, we find that these checkpoints often side with grader preferences over those of users or developers on coding and alignment tasks. This tendency to side with the grader trends upward throughout RL training. For example, in an environment that forces a choice between keeping a promise to a supervisor and breaking it to complete the task, a late capabilities-focused o3 checkpoint breaks the promise 87% of the time when SDF documents say the grader rewards task completion, versus 9% when they say it rewards honesty (a choice its chain-of-thought often makes explicit). An earlier checkpoint is far less sensitive (40% vs. 24%). Our method also generalizes to reward-hacking models. A model organism trained to reward-hack (gpt-oss-120b) is more than twice as sensitive to grader preferences as the unmodified model, with the mean behavioral shift in favor of the grader rising from 33% to 86%. These results indicate that RL can increase reward-seeking over the course of training, producing models that may act against their developers' intentions when they believe that doing so leads to higher reward.

---


### 168. [Verifiable Self-Evolution for Open-Ended Dialogue Skills via Future-Feedback Prediction](https://arxiv.org/abs/2607.18973)

**<font color=#1a73e8>作者：</font>** ChaoJin Zhao, Xuan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Textual skills provide a lightweight way to improve frozen language-model agents, but their self-evolution normally requires a stable validation signal. Such signals are natural in mathematics or code, where an answer can be checked after it changes, yet are problematic in open-ended dialogue: changing the assistant response also changes the user's next reaction, so a logged reaction cannot directly evaluate a counterfactual response. We propose future-feedback skill evolution, which first redirects self-evolution from prescribing the current answer to predicting whether the observed answer will lead to a positive or negative subsequent user signal. This prediction task is verifiable on fixed logged tuples and therefore supports validation-gated textual optimization. The evolved feedback skill captures interpretable criteria for response quality and can subsequently serve as a diagnostic and optimization target for answer skills. On a proprietary, privacy-preserving sales-assistant dataset, careful quality filtering and a balanced resolved/unresolved split yield more than 75% prediction accuracy. Beyond this result, the central contribution is a formulation that converts otherwise moving conversational feedback into a fixed offline learning target, enabling reproducible skill evolution without placing every candidate skill in live traffic. We discuss the boundary between observational verification and counterfactual validity, and position the method as an offline optimization stage rather than a replacement for final human or online evaluation.

---


### 169. [Mi-Memory: A Lifecycle Memory Framework for Personal AI](https://arxiv.org/abs/2607.18975)

**<font color=#1a73e8>作者：</font>** Xule Liu, Hanlin Teng, Chao Li 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal AI is moving beyond chat-only interaction toward continuous services that span phones, cars, homes, wearables, cameras, and tools. In this setting, memory cannot remain a cache of prior conversations. It should serve as a continuity and governance substrate: preserving durable user state, grounding answers in multimodal and device evidence, supporting correction and forgetting, bounding policy evolution, and remaining deployable under latency, cost, privacy, and edge-cloud constraints. This technical report presents Mi-Memory, a lifecycle memory framework for Personal AI organized around four roles: Structure, Expansion, Evolution, and Deployment. A shared audit contract links these roles through four recurring artifact families: typed evidence payloads preserve source identity and provenance, diagnostic traces localize evidence loss across the serving pipeline, strategy artifacts make memory-policy changes explicit, and gate/rollback records bound accepted evolution. MiMemory instantiates the roles through MemStack, MemSense/MemFuse, D$^{2}$ACCI/E$^{2}$MEND, and LiteMem. In controlled-reference Structure evaluations, MemStack reaches 93.59%, 57.24%, and 87.47% on LoCoMo, PersonaMem-V2, and LongMemEval, respectively; other tracks report module-level, preliminary/internal, transfer-feasibility, or design-only evidence with explicit boundaries. MiMemory is a step toward auditable, evidence-gated, and deployment-aware memory systems for Personal AI. Project homepage: this https URL .

---


### 170. [Disentangling Curriculum Learning in NLP: Towards a Unifying Taxonomy](https://arxiv.org/abs/2607.18984)

**<font color=#1a73e8>作者：</font>** Vanessa Toborek, Florian Seiffarth, Sebastian Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite more than a decade of curriculum learning (CL) research in NLP, the field lacks a principled account of which difficulty function or scheduler to use for a given problem. To understand what has hindered progress towards this account, we propose a fine-grained taxonomy separating difficulty evaluation from training scheduling to enable systematic analysis of CL strategies. For difficulty evaluation, we distinguish attribution source and task dependence, revealing difficulty as a perspectival concept encoding different assumptions about what makes an instance hard to learn. For scheduling, we provide the first formalisation of CL schedulers in terms of expected training contribution, enabling comparison across implementations by introducing retention regimes and monotonicity properties. Applied in a dedicated analysis of CL works in NLP, our taxonomy reveals a systematic incomparability problem: prior works conflate distinct notions of difficulty and scheduling, often pursuing different objectives under the same CL label -- hindering comparison and the accumulation of a coherent evidence base. Beyond diagnosis, the taxonomy supports the design, analysis, and comparison of CL strategies, and motivates evaluation practices that disentangle the sources of observed improvement.

---


### 171. [SWITi: Quantifying and Reducing Tiling Artifacts with Sliding Window Inner Tiling](https://arxiv.org/abs/2607.18990)

**<font color=#1a73e8>作者：</font>** Federico Carrara, Aman Kukde, Melisande Croft 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> SWITi is a test-time method for reducing artifacts in tiled predictions, particularly for neural networks that learn posterior distributions from which solutions are sampled at inference time. Tiled predictions are unavoidable for large image data, and artifacts arise whenever tiles are smaller than a network's receptive field and when tiles are independent posterior samples. SWITi averages overlapping sliding-window predictions, so discrepancies between neighboring samples are spread across shifted tile positions rather than accumulating at fixed seam coordinates. For posterior models, SWITi uses no more tile samples than an MMSE estimate requires and therefore incurs no additional forward passes. Additionally, we introduce two reference-free metrics, the Fraction of Rejected Tests (FRT) and Artifact Severity (ASV), for detecting and quantifying tiling artifacts from a per-tile permutation test that compares the distribution of pixel gradients across tile seams against the surrounding image content. On pre-trained and published image splitting models across three fluorescence microscopy datasets in 2D and 3D, we show that SWITi substantially attenuates stitching seams while also improving reconstruction fidelity and resolution. Since tiling artifacts in posterior predictions can easily be mistaken for biological structures or for boundaries between biological structures, removing or reducing them using SWITi will improve the downstream processing of large image predictions, which is particularly relevant for biomedical data.

---


### 172. [Benchmarking Deep Learning Approaches for AEC Engineering Drawing Layout Detection and Information Extraction](https://arxiv.org/abs/2607.18997)

**<font color=#1a73e8>作者：</font>** Tianyang Huang, Alessio Lombardi, Ahmed Elnagar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Information Extraction (IE) from Architecture, Engineering, and Construction (AEC) drawings remains hindered by manual inefficiency, while Layout Detection, a vital 'middleware' organizing graphical and textual hierarchies, is underexplored. General document layout models, optimized for text-centric content, lack validation on engineering drawings. This study constructs a custom AEC-specific layouts dataset and benchmarks five deep learning architectures. RF-DETR achieves state-of-the-art performance with an $mAP_{50}$ of 0.949, while the Vision-Language Model Qwen3-VL attains a leading F1-score of 0.911. Conversely, models pre-trained on general document datasets suffer from "domain interference", causing performance degradation. This establishes a robust technical foundation for automated IE in AEC.

---


### 173. [MedDDC-Eval: Diagnosis-Decoupled Evaluation of Multi-Turn Medical Consultation Agents](https://arxiv.org/abs/2607.18999)

**<font color=#1a73e8>作者：</font>** Guofeng Zhang, Yizeng Quan, Huaiyi Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn medical consultation agents must decide what to ask, adapt to patient responses, and determine when the collected evidence is sufficient. However, coupled evaluation conflates the quality of the policy-elicited history with policy-specific terminal diagnosis generation: strong generation can compensate for a thin history, while weaker generation can obscure a rich one. We introduce MedDDC-Eval, a diagnosis-decoupled testbed that treats elicited history as the comparison object and holds the history-to-diagnosis mapping constant through a shared frozen reader. Across two held-out sources, a grounded interface and an auditable diagnosis-trajectory-efficiency (D/T/E) harness measure diagnostic usefulness, information acquisition, and efficiency. Directional semantic coverage followed by deterministic one-to-one assignment yields coherent precision-recall counts for open-ended items, with at most one credited match per prediction or reference. Holding histories fixed, changing only the diagnostic reader shifts diagnosis F1 by 2.2-19.0 points and reverses 18% and 36% of pairwise policy orderings on the Record and Dialogue splits. We further apply standard Group Relative Policy Optimization (GRPO) over interactive multi-turn rollouts to post-train Qwen3-32B using diagnosis-result and trajectory feedback. On the 100-case Record and 70-case Dialogue splits, the trained policy improves over its initialization by 9.7 and 4.6 total-score points; removing either primary signal lowers held-out joint performance. These results show that MedDDC-Eval supports controlled attribution, interpretable elicited-history measurement, and evaluation-guided evidence-acquisition policy development.

---


### 174. [Learning Semantic-Robust Change Detection via Semantic-Invariant Self-Distillation](https://arxiv.org/abs/2607.19000)

**<font color=#1a73e8>作者：</font>** Jiuhe Qu, Yingping Liang, Ying Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Change detection aims to identify semantic changes between remote sensing images. However, features from models are easily disturbed by non-semantic variations, such as illumination, shadows, and atmospheric changes, leading to false alarms and limited generalization in real-world scenarios. In this paper, we propose \textbf{SCDistill}, a framework for learning semantic-robust change detection via semantic-invariant self-distillation. First, to strengthen semantic consistency, we introduce a semantic-invariant self-distillation strategy that learns semantic robustness from perturbed yet semantically consistent data, empowering the change detector to extract disturbance-resistant features and achieve more reliable and accurate semantic change identification. Second, to expand paired data with non-semantic variations, we design a diffusion-based perturbation simulation pipeline that synthesizes complex environmental changes, enabling the model to explicitly learn to distinguish semantic changes from appearance-level fluctuations and reduce false alarms caused by non-semantic disturbances. These components promote robustness from data and representation perspectives, leading to synergistic performance gains. Extensive experiments demonstrate that SCDistill achieves state-of-the-art performance on multiple semantic change detection benchmarks and exhibits strong generalization to binary change detection and change captioning tasks. Code is accessible at this https URL.

---


### 175. [Subject-Conditioned Glucose Forecasting in Type-1 Diabetes](https://arxiv.org/abs/2607.19006)

**<font color=#1a73e8>作者：</font>** Giorgia Rigamonti, Mirko Paolo Barbato, Davide Marelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of blood glucose concentration is key in the management of Type 1 Diabetes, facilitating early detection of adverse glycemic events and supporting timely therapeutic interventions. Despite recent advances in glucose prediction, most existing approaches rely on population-level representations or implicit personalization strategies that fail to deliver effective subject-specific forecasts. In this work, we propose Subject-Conditioned Glucose Prediction (SCGP), a novel multimodal deep learning architecture conceived for personalized blood glucose prediction. SCGP conditions glucose predictions based on observed glucose data and a compact subject-specific representation learned from contextual information. By explicitly separating subject characterization from glucose dynamics modeling and avoiding early fusion of heterogeneous inputs, the proposed framework effectively captures inter-subject variability while preserving robust and reliable temporal modeling. Experiments on two state-of-the-art benchmark datasets demonstrate that SCGP consistently improves forecasting performance, enabling reliable detection of adverse glycemic events across multiple prediction horizons, highlighting the benefits of explicit subject conditioning for personalized diabetes management.

---


### 176. [Caring Over Computing: An Ethical and Sociotechnical Perspective on Generative AI for Social Connectedness in Dementia Care](https://arxiv.org/abs/2607.19007)

**<font color=#1a73e8>作者：</font>** Teis Arets, Giulia Perugia, Maarten Houben 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People with dementia in residential care often experience reduced social connectedness. Person-centered care approaches foreground meaningful social interactions to support well-being, but staff and time pressures increasingly constrain opportunities for such care. Generative AI (GenAI) technologies offer possibilities for helping care professionals facilitate social connectedness, despite increasing care pressures. Yet, the meaningful integration of such technologies into the complex sociotechnical setting of residential dementia care is not straightforward. To responsibly design GenAI technologies for dementia care, we need to investigate how care professionals recognize and foster social connectedness and how technologies intersect with those approaches in care contexts. We conducted five workshops with 15 care professionals from three care organizations to pursue this objective. Our findings show that fostering social connectedness involves ongoing interpretation, negotiation, and adaptation to residents' individual needs. Technology was used by care professionals to support communication, interaction, and shared activities, yet remained largely peripheral to everyday care routines and required active mediation for use in practice. Drawing on an ethics of care framework, we derive ethical and sociotechnical implications for the responsible design and positioning of GenAI in residential dementia care.

---


### 177. [Biological Amnesia in ICU Time-Series Prediction: A Drift-Adaptive Two-Stream Architecture with Temporal Retrieval](https://arxiv.org/abs/2607.19020)

**<font color=#1a73e8>作者：</font>** Fatema Ferdous Tamanna, K. M. Merajul Arefin, Md. Abdul Masud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Clinical decision support systems degrade silently as treatment protocols evolve, yet standard adaptation methods treat models as monolithic blocks, unable to distinguish stable patient physiology from shifting institutional practice. Methods: We propose an adaptive clinical intelligence architecture for ICU intervention prediction that structurally decouples physiological from treatment representations, confining parameter updates to the treatment stream upon a dual distributional and accuracy trigger. Automated audit logs record which treatment features drove each adaptation event and how their importance shifted. At inference, an attribution-driven Temporal RAG module grounds each prediction in patient-specific, era-matched PubMed evidence anchored to the patient's dominant physiological features. Experiments used 84,792 MIMIC-IV stays (2008-2022) under strict chronological split. Results: Drift localised entirely to the treatment stream, validating the structural prior. Selective adaptation improved vasopressor and septic shock discrimination and calibration over the static source model. A fully retrained baseline yielded marginally higher aggregate discrimination but missed 26 septic shock cases the framework correctly identified, with none in the reverse direction; retrieval consistency with the pre-adaptation source model was preserved by the framework but degraded substantially in the retrained baseline. Conclusions: Structurally constraining adaptation to drifting components while preserving stable physiological representations enables clinical AI to evolve with practice without distorting learned patient biology. This architecture offers a template for governable, interpretable deployment of adaptive models in high-stakes clinical environments.

---


### 178. [Unsupervised Multi-kernel Learning for Automated Algorithm Selection](https://arxiv.org/abs/2607.19031)

**<font color=#1a73e8>作者：</font>** Yihang Lu, Tome Eftimov, Carola Doerr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated algorithm selection in black-box optimization typically relies on supervised models that map landscape features to algorithm performance labels. Such models are costly to train, benchmark-dependent, and often fail to generalize to unseen problem classes. We study an unsupervised alternative: multi-kernel clustering over heterogeneous landscape representations, in which problem instances are grouped without using performance labels in the clustering stage, and the resulting clusters are mapped post hoc to solver recommendations through a strictly separated three-stage evaluation protocol. Drawing on two decades of advances in multiple kernel learning, we adopt a multi-kernel k-means formulation that jointly learns cluster assignments and kernel weights over four heterogeneous landscape views: ELA, DeepELA, DoE2Vec, and TransOptAS. On affine BBOB-derived selector tasks for Differential Evolution (DE) and Particle Swarm Optimization (PSO) at a fixed evaluation budget, we report mean plus or minus standard deviation selector profiles over 50 independent random seeds for stochastic configurations. Multi-kernel clustering obtains the strongest mean profile on the DE portfolio and remains competitive with, and nominally ahead of, the leading baselines on the more compressed PSO portfolio, where differences among the best methods are small relative to stochastic variation. In representative median-seed runs used for visualization, the learned kernel weights retain ELA and TransOptAS while assigning zero weight to DeepELA and DoE2Vec, providing a task-specific interpretation of which representations are retained by the multi-kernel model for selector-oriented grouping.

---


### 179. [Content is What Remains: Invariant Speech Tokenization from Parallel Utterances](https://arxiv.org/abs/2607.19033)

**<font color=#1a73e8>作者：</font>** Laurin Wagner, Bernhard Thallinger, Miroslav Stankovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete speech tokenizers aim to disentangle semantic from acoustic information, yet targets from self-supervised learning (SSL) models like HuBERT retain non-linguistic variation: speaker identity, prosody, and channel conditions leak into the tokens, inflating entropy. Our key insight is that when enough speakers utter the same words under varying conditions, linguistic content is the only shared factor. We propose PINT (Parallel INvariant Tokenization), which fine-tunes an SSL encoder with alignment losses across parallel utterances and augmentations to distill this shared residual. PINT collapses identical words onto consistent token sequences, drastically reducing conditional entropy. Unlike ASR text, PINT tokens preserve frame-level temporal grounding and serve as drop-in semantic targets for audio codecs. Experiments show a 98.7% relative reduction in speaker probe accuracy (93.1% to 1.2%), a 42% lower ABX error rate, and 27-30% lower LM perplexity versus baselines, confirming that the right invariance is key to efficient learning.

---


### 180. [CoGoal3D: Collaborative 3D Object Detection with 3D-Aware Fusion and Refinement](https://arxiv.org/abs/2607.19036)

**<font color=#1a73e8>作者：</font>** Zhihao Yang, Zhiyu Xiang, Peng Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> V2X collaborative object detection features overcoming the limitations of single-vehicle systems by aggregating environmental features from multiple collaborative agents. However, existing mainstream V2X perception methods mainly focus on 2D BEV object detection. When 3D detection task is concerned, inferior results are obtained because they ignore the 3D spatial misalignment caused by differing height and attitude among the collaborators. In this paper, we propose a novel collaborative 3D object detection framework called CoGoal3D, which extracts and refines the 3D feature gradually in a two-stage pipeline. In the first stage, a multiscale 3D-aware global fusion module is designed to mitigate the 3D spatial misalignment. The resulting proposals are then refined in the second stage with an auxiliary task of 3D point reconstruction. An effective multi-agent collaborative data augmentation strategy is further proposed to enrich the training data while minimizing information loss. Extensive experiments on public real-world datasets demonstrate that our CoGoal3D achieves new state-of-the-art performance, with 3D AP@0.7 improvements of 10.86%, 10.34%, and 10.18% on the DAIR-V2X, V2V4Real, and V2X-Real datasets, respectively. Code is available at this https URL.

---


### 181. [Gaze-DETR: Top-Down Guidance Through Priority Maps for Infrared Weak-Small UAV Detection with DETR](https://arxiv.org/abs/2607.19040)

**<font color=#1a73e8>作者：</font>** Nian Liu, Yuxin Yang, Shubo Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (ISTD) remains challenging because tiny, low-contrast targets are easily overwhelmed by clutter, noise, or occlusion. Conventional single-frame and multi-frame detectors rely on bounding-box supervision, which specifies final target locations but offers little explicit guidance for prioritizing candidate regions or preserving weak-target evidence before localization. Task-driven visual search offers such guidance: top-down goals and visual evidence jointly form a spatial priority map that ranks candidate locations. Building on this principle, we propose Gaze-DETR, a bio-inspired detector that learns an internal priority map before localization. First, a priority head predicts a normalized priority map from image features. Second, Residual Priority-Guided Feature Modulation (RPFM) enhances high-priority responses while retaining multi-scale features. Finally, Priority-Guided Anchor Query Injection (PAQI) converts high-priority locations into decoder anchor queries. We train the priority head using three supervision schemes: box-derived Gaussian maps; real-gaze maps constructed from fixation-density maps; and transferred pseudo-gaze maps learned from gaze--box relations in paired annotations and applied to Anti-UAV410 training boxes. To support the latter two schemes, we construct TIR-UAV120-Gaze with paired detection and task-driven eye-tracking annotations. On TIR-UAV120-Gaze, Gaze-DETR achieves 85.76 mAP$_{50}$ and 88.77 F1 with box-derived supervision, and 86.18 mAP$_{50}$ and 89.00 F1 with real-gaze supervision. On Anti-UAV410, it achieves 87.06 mAP$_{50}$ and 90.90 F1 with box-derived supervision, and 87.08 mAP$_{50}$ and 90.43 F1 with transferred pseudo-gaze supervision. These results show that explicit spatial-priority learning provides pre-localization guidance complementary to bounding-box supervision across annotation settings and costs.

---


### 182. [Spectral Higher-Order Neural Networks Have Sharp Expressivity Bounds](https://arxiv.org/abs/2607.19042)

**<font color=#1a73e8>作者：</font>** Gianluca Peri, Diego Febbe, Duccio Fanelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural hypergraphs are a natural generalization of neural networks, the reference models in modern machine learning. Yet, their deployment has proven demanding: the number of weighted hyperedges required leads to an intractable parameter explosion. However, a novel parametrization that leverages spectral attributes for neural hypergraphs has been recently proposed, that enables to recycle parameters via a weight sharing scheme and consequently yields a significant reduction of the associated computational cost. Preliminary tests carried out on spectral higher-order architectures pointed to meaningful improvements in both performance and interpretability. Building on these results, we advance the benchmarking efforts by evaluating the spectral higher order framework on N-bit parity tasks, a well-established testbed known to be particularly challenging. As we will convincingly argue, Spectral Higher-Order Neural Networks (SHONNs) possess a versatile and highly tunable hypothesis space.

---


### 183. [Contrastive On-Policy Distillation](https://arxiv.org/abs/2607.19046)

**<font color=#1a73e8>作者：</font>** Jiacheng Ruan, Jun Tang, Wenzhen Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy Distillation (OPD) supervises a student model on trajectories sampled from its own policy by minimizing the divergence between the output distributions of the teacher and student at each token position, thereby providing dense token-level supervision. Although existing OPD methods have demonstrated strong performance in improving the reasoning ability of student models, their objectives fundamentally rely on token-level distribution matching. Consequently, they lack an explicit signal for comparing a token's relative compatibility across reasoning modes and thus do not directly model preferences between these modes. To address this limitation, we propose COPD, a contrastive OPD framework. Specifically, for each token generated by the student model, a frozen teacher model scores the same student state under two contrasting instructions that elicit light and heavy reasoning. The difference between the resulting log probabilities serves as a token-level advantage signal to guide the OPD update. Rather than merely imitating a single teacher distribution, COPD directly encourages the student model to learn more concise and efficient reasoning strategies. We conduct experiments on nine multimodal benchmarks covering both reasoning and understanding tasks. The results show that COPD substantially reduces reasoning length without compromising model performance and consistently improves efficiency across different tasks and model scales. Furthermore, the contrastive formulation can be seamlessly integrated into the On-policy Self-distillation (OPSD) framework, where self-contrastive supervision is constructed without an additional teacher model, thereby enabling the model to distill itself toward lightweight reasoning.

---


### 184. [Chi-MERA: Defending Orbit-Based Authentication of LEO Satellites with the Space Oddity of MLAT (Long Version)](https://arxiv.org/abs/2607.19047)

**<font color=#1a73e8>作者：</font>** Sarah Jung, Eric Jedermann, Martin Strohmeier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An active research area, physical layer security can be a last resort in insecure legacy systems, a resource-efficient alternative, or a complementary backup for cryptographic techniques. In this paper, we demonstrate that previously established authentication schemes for LEO satellites are vulnerable to attackers that control multiple devices. In extensive experiments, such attackers produce false positive rates (FPR) of up to 40%.
Based on a root cause analysis, we develop a novel scheme, called Chi-MERA, that improves authentication performance and is robust against multi-device attackers. Our scheme uses two enhancements: (1) multilateration (MLAT) to clearly distinguish between attackers and legitimate satellites, and (2), a new resilient signature scheme without dependency on a single dedicated reference receiver. Our evaluation shows that exploiting MLAT characteristics such as residual analysis to classify vastly different signal source categories (orbit vs. non-orbit) is highly effective. In extensive simulations, we show that the new authentication achieves low FPR of $<$2% and false negative rates of $<$3% for accidentally rejecting valid signals. Furthermore, our scheme's defense scales linearly: $n$ receivers reliably withstand spoofing (FPR $< 1%$) from attackers with $\frac{n}{2}$ devices.

---


### 185. [Benchmarking Human and Automatic Speech Recognition of Diverse Speech: Initial Results](https://arxiv.org/abs/2607.19049)

**<font color=#1a73e8>作者：</font>** Ilse Huisman, Rares Popa, Yuanyuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans are often considered to be the best listeners and seen as the upper-bound performance of automatic speech recognition (ASR) systems. We present a preliminary comparison of the performances of state-of-the-art ASR systems and Dutch native listeners on the recognition of "diverse" speech, specifically Dutch child and older adults' speech and Flemish. Google Telephony outperformed the other ASR systems. Importantly, the ASR systems showed similar performance to the listeners, and in specific cases even outperformed them. Slight performance differences between the listeners and ASR systems were found related to speaker's age and regional accents and utterance length. Future research should focus on making ASR systems more robust to acoustic variability related to aging and regional accents. A comparison of ASR recognition performances on the test stimuli and the full Jasmin-CGN test sets showed the influence of the specific test sets on the conclusions regarding benchmarking human and ASR performance.

---


### 186. [Probabilistic Physics-Aware Machine Learning Predictions of Electric Truck Energy Consumption with Field Data](https://arxiv.org/abs/2607.19054)

**<font color=#1a73e8>作者：</font>** Hannes Nilsson, Rafael Basso, Balázs Kulcsár 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we incorporate first principle physics into the construction of data-driven methods by considering a model that accounts for the different sources of energy losses during vehicle operations. Our results show that Bayesian linear regression based on this physics-aware model can improve the reliability of the expected energy consumption, as compared with standard linear regression. Further, it is shown that more complex machine learning models such as neural networks and gradient boosted regression trees, based on the same physical model, can further improve the accuracy in energy forecasting and significantly outperform standard versions of the same machine learning models. In addition to point predictions of the energy consumption, we develop a framework for estimating the corresponding uncertainty in the form of predicted standard deviation. Our results show that all of the models learn to estimate the uncertainty reasonably well.

---


### 187. [Vector-Bench: Can Models Surgically Edit SVG Code?](https://arxiv.org/abs/2607.19056)

**<font color=#1a73e8>作者：</font>** Yug Aditi Gupta, Prannay Hebbar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instruction-based vector editing requires two capabilities: making a requested change and leaving everything else alone. The second is easy to miss when an output is judged only as a raster image. We introduce Vector-Bench, a compact, difficult benchmark of 40 SVG repair tasks. Each task pairs a corrupted SVG program with an author-written visual instruction, a hidden target program, 5.05 annotated repairs on average, and an average of 60.55 protected objects. Instructions describe visible defects without exposing element identifiers, coordinates, color codes, or path data. We define a deterministic binary specification reward: requested repairs use attribute-aware perceptual tolerances, while unrequested rendering- or application-relevant structure must remain semantically unchanged and the result must be a valid SVG. Canonical target equality and stricter source fidelity are retained as diagnostics. Validity-gated repair progress, a near-complete tier, and valid-output Unintended Change Rate (UCR) explain partial outcomes. We evaluate 34 model endpoints (25 listed as open-weight, 5 inexpensive controls, and 4 frontier closed endpoints) over 1360 requests. The strongest endpoint reaches only 15.0% full specification success, despite 43.7% mean repair progress, showing that apparent repair progress and specification-faithful editing remain substantially different. All prompts, outputs, scoring code, costs, and per-task reports are released.

---


### 188. [Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/abs/2607.19058)

**<font color=#1a73e8>作者：</font>** Nuemaan Malik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizer state is the largest single line item in the memory budget of mixture-of-experts (MoE) training: on a 6.78B-parameter MoE language model, AdamW keeps 50.6 GB of first and second moments to update 12.6 GB of bfloat16 weights. We study SkewAdam, an optimizer built on the observation that the three parameter populations of an MoE - the dense backbone, the experts, and the router - differ enough in size and gradient statistics that they should not receive the same state. SkewAdam keeps float32 momentum plus a factored second moment for the backbone (5% of parameters), a factored second moment alone for the experts (95%), and an exact second moment for the router (<0.01%). The resulting state occupies 1.29 GB, 2.6% of AdamW's, and peak training memory falls from 81.4 GB to 31.3 GB, within the budget of a 40 GB accelerator. In a controlled comparison from identical initializations over 82M tokens, SkewAdam reaches validation perplexity 108.4, ahead of AdamW (126.8), Muon (120.2), and Lion (393.7), and settles router load balance to within 1% of its uniform floor. The allocation is not what earns that perplexity: a tier ablation matches it with twenty times the state, and Adafactor, which shares the factored estimator but drops momentum, plateaus 40 points behind. The tiers buy memory at no cost to accuracy; the accuracy comes from keeping momentum, which a uniform optimizer shares too. Sweeping the baselines' learning rates narrows but does not close the gap: the best tuned AdamW reaches 118.5, tuned Adafactor 139.7. Where optimizer state lives, these results suggest, matters at least as much as how much of it there is.

---


### 189. [Deep learning-based prediction of time-resolved adhesive forces in viscoelastic Hertzian contacts](https://arxiv.org/abs/2607.19060)

**<font color=#1a73e8>作者：</font>** Ali Maghami, Merten Stender, Michele Ciavarella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast prediction of the response of adhesive soft viscoelastic contacts represents a current challenge in soft robotics and for gripping and manipulation tasks. Determining the complete time-resolved force trajectory requires full numerical simulations, whose computational cost is strongly parameter-dependent, making them impractical for real-time application or design-optimization loops. In this work, we overcome this limitation by training a scalar-conditioned, stateful, sequence-to-sequence deep learning model to predict the full force evolution from a prescribed displacement history for both short- and long-range adhesion regimes. The data set spans four orders of magnitude in loading and unloading rates and includes varied dwell times, with the Tabor parameter ranging from $0.2$ to $3.2$. To enable learning across these heterogeneous time scales, we introduce a fixed-measurement-step (FMS) representation that converts variable-length trajectories into fixed-length sequences while preserving their physical-time information. Different architectures were trained, including long short-term memory (LSTM) networks, temporal convolutional neural (TCN) networks, and time-distributed dense layers with three different Tabor-conditioning mechanisms. The models were compared using global waveform and error metrics. We found that the best-performing model has an LSTM architecture with concatenated conditioning, which achieves a held-out mean-squared error of $5.0\times10^{-4}$, a median pull-off-force error of $\approx2.2\%$, and a median hysteresis error of $\approx1.1\%$. For the held-out protocols, the model predicts a complete force trajectory with a median inference time of $0.16$ s. The model is tested across unseen parameter combinations and against analytical limiting cases, providing a rapid surrogate for repeated numerical evaluations with potential use in control-oriented applications.

---


### 190. [Now You See the Hate: Adaptive View Retrieval for Hidden Hateful Illusions](https://arxiv.org/abs/2607.19061)

**<font color=#1a73e8>作者：</font>** Qianpu Chen, Derya Soydaner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hateful optical illusions expose a serious gap in current multimodal safety systems. On original-view hateful illusions, previous work shows that six moderation classifiers achieve at most 20.9 to 24.5% accuracy and nine state-of-the-art VLMs remain at or below 10.2% with illusion-aware prompting, leaving most hidden hate undetected. We formulate hidden hateful illusion detection as a perceptual retrieval problem and propose Adaptive View Retrieval. This retrieve-and-calibrate framework assembles a complementary view bank for the image and hidden-message templates, adaptively selects which views to trust, retrieves hidden-message identities, and calibrates whether the recovered evidence is harmful. On HatefulIllusion with a frozen CLIP encoder, Adaptive View Retrieval reaches 93.2% balanced accuracy on the held-out test split. It substantially outperforms original-view baselines and fixed single-transform filters across hate slangs, hate symbols, and visibility levels. The same design also surpasses official fine-tuned CLIP baselines, matches or exceeds human performance on IllusionMNIST, IllusionFashionMNIST, and IllusionAnimals, and outperforms zoom-out preprocessing on HC-Bench under the SemVink protocol. Together, these results show that robust multimodal moderation requires recovering hidden meaning before deciding whether it is harmful.

---


### 191. [On the Effectiveness of Pretraining for Graph Combinatorial Optimization](https://arxiv.org/abs/2607.19072)

**<font color=#1a73e8>作者：</font>** David Aguado, Daniel Fuertes, Carlos R. del-Blanco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces a self-supervised pretraining framework for graph combinatorial optimization specifically designed to address the nature of routing problems like the Traveling Salesman Problem. By utilizing graph contrastive learning with geometric augmentations (specifically, rotations and axial reflections) the model is forced to learn invariant structural representations and global relative distance distributions. Results demonstrate that this pretraining strategy outperforms non-pretrained models across various problem scales. Notably, the hybrid strategy (combining rotation and reflection) achieved a 6.57% improvement in tour length for TSP1000, proving that geometric pretraining is an important inductive bias for effectively scaling neural solvers to high-dimensional instances.

---


### 192. [GEqTrain: A Configuration-Driven Framework for Retargeting Equivariant Graph Neural Networks Across 3D Scientific Tasks](https://arxiv.org/abs/2607.19083)

**<font color=#1a73e8>作者：</font>** Daniele Angioletti, Marco Nobile, Vittorio Limongelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant graph neural networks provide a powerful modeling language for three-dimensional scientific data, but their reuse is often limited by implementations tied to specific tasks, outputs, and training regimes. We present GEqTrain, a configuration-driven framework that separates dataset semantics, model composition, and training objectives. Raw data are mapped to typed node-, edge-, and graph-level fields, while model stacks, losses, and training workflows are assembled declaratively through Hydra configurations. A shared equivariant backbone and training infrastructure can therefore be retargeted to a new task primarily through configuration. We demonstrate this flexibility on three different problems handled within one software stack: coarse-grained-to-atomistic backmapping of biomolecular systems, prediction of NMR chemical shifts in molecular solids, and equivariant generative modeling. Our aim is not to surpass individually optimized task-specific systems, but to show that a shared representation and training infrastructure can achieve competitive accuracy across qualitatively different tasks at the cost of a configuration change. We further introduce GEqDiff, a generative extension based on equivariant flow matching. GEqDiff treats user-defined equivariant fields as first-class generation targets, jointly transporting Cartesian positions and non-scalar node fields spanning representations up to l=3 within a single equivariant flow. We validate this capability on a controlled synthetic benchmark inspired by protein secondary-structure motifs, showing that fields with heterogeneous transformation properties can be reconstructed jointly and with high fidelity. By reducing the software overhead of moving between predictive and generative, scalar and tensorial settings, GEqTrain aims to make equivariant modeling more reproducible, extensible, and reusable.

---


### 193. [DAIS: Dependency-Aware Intermediate QA Supervision for Complex Reasoning](https://arxiv.org/abs/2607.19088)

**<font color=#1a73e8>作者：</font>** Yu Wang, Ming Fan, Xicheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) supervision exposes intermediate rationales, but flat rationale targets usually optimize a single reasoning sequence and provide limited supervision on how local conclusions should support later decisions. We introduce Dependency-Aware Intermediate QA Supervision (DAIS), a training-time framework that converts filtered teacher rationales into stage-level QA records. Each intermediate record predicts a local answer conditioned on the previous states needed for that decision, while the final-answer record keeps the original task format; evaluation therefore uses only the original input and optional context. Across GDPR, AIACT, MedQA, and FOLIO with multiple Qwen backbones, DAIS improves average final-answer accuracy over answer-only, flat chain-of-thought, and independent-QA baselines. On policy-compliance benchmarks, it achieves a largest gain of 5.6% and an average gain of 4.2% over the strongest non-DAIS baseline. Controlled ablations show that valid previous-state conditioning contributes beyond longer targets or additional intermediate text, supporting dependency-conditioned intermediate QA as a lightweight auxiliary supervision signal for standard final-answer inference.

---


### 194. [An unsupervised clustering analysis of breast cancer data derived from electronic health records enhanced through UMAP dimensionality reduction](https://arxiv.org/abs/2607.19089)

**<font color=#1a73e8>作者：</font>** Davide Chicco, Nicoletta Benvenuto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Breast cancer is one of the most widespread types of cancer, affecting approximately 8 million women worldwide. Electronic health records of patients diagnosed with this disease can serve as valuable datasets for computational analyses, enabling the discovery of new insights about the pathology. Unsupervised clustering, in particular, can identify groups of patients with medically significant features, revealing data trends that might otherwise go unnoticed by medical doctors. In this study, we first applied the DBSCAN density-based clustering method to three independent datasets derived from electronic medical records of patients with mammary carcinoma. Subsequently, to enhance our results, we preceded the DBSCAN application with a dimensionality reduction phase using UMAP. We evaluated our clustering outcomes using three statistical indices (DBCV, DCSI, and DISCO). Our results confirm the effectiveness of combining UMAP with DBSCAN for clustering data derived from electronic health records, paving the way for the medical interpretation of the patient groups identified by our approach.

---


### 195. [Supra Cognitive Modes: A Routed Architecture for Agent Memory](https://arxiv.org/abs/2607.19096)

**<font color=#1a73e8>作者：</font>** Joshua Tobkin, David Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories. We describe Supra Cognitive Modes (SCM), an architecture that maps explicit or automatically selected per-query modes to retrieval and synthesis payloads over one shared ingest substrate. A frozen semantic classifier and runtime gates dispatch queries among fused lexical and dense lookup, graph or iterative multi-hop handling, and stratified long-form synthesis. The substrate combines multi-granularity embeddings, extracted triples, fact-version metadata, and optional asynchronous enrichments. We characterize the deployed configuration on three benchmarks: Long-term Conversational Memory (LoCoMo; n = 1,986), MemoryAgentBench (MAB; n = 3,671), and LongMemEval (n = 500). The reference run records 84.87% on LoCoMo factoid categories and 68.61% on adversarial abstention, 61.49% on MAB across two repetitions, and 86.00% on LongMemEval. A repository-backed reproduction produces similar aggregate scores and supports task- and mode-conditioned failure analysis. Raw baseline outputs, aligned end-to-end timing for LoCoMo and LongMemEval, and complete token ledgers are unavailable; stored rows also omit some final runtime decisions. The results characterize one implemented routed configuration and its diagnostic failure patterns, while source inspection verifies the per-query control interface and shared-substrate design. Causal routing effects, efficiency gains, and statistical significance remain outside the available evidence.

---


### 196. [FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility](https://arxiv.org/abs/2607.19100)

**<font color=#1a73e8>作者：</font>** Yihalem Yimolal Tiruneh, Muhammad Salman Ali, Uyoung Jeong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing animatable 3D human avatars from monocular video is a fundamental problem in computer vision with broad applications in AR/VR and digital content creation. Existing approaches typically couple parametric body models with neural rendering or 3D Gaussian splatting and optimize all body regions jointly from short videos, which often degrades fidelity in the visible areas. To overcome this limitation, we introduce FlexiAvatar, a unified framework that explicitly optimizes only the visible body regions, effectively eliminating artifacts arising from unobserved limbs. Our method integrates occlusion-robust SMPL-X tracking with part-specific residual refinement to capture high-frequency geometric and appearance details. To complete entirely unseen regions (e.g., back views), we leverage a diffusion-based approach to generate texture consistent with the observed appearance. Experiments on full-body (NeuMan, ZJU-MoCap, WildAvatar), upper/half-body (talk-show clips), and head-only (INSTA) inputs show that FlexiAvatar delivers consistently higher reconstruction quality, outperforming state-of-the-art methods by an average PSNR improvement of approximately 3% across datasets. Finally, by restricting optimization to observed regions, our method reduces the effective number of Gaussians that must be optimized and rendered, leading to reduced runtime and memory overhead in partial-visibility scenarios.

---


### 197. [Translation as Augmentation: Effect of Translated Data on Assessment of Difficulty](https://arxiv.org/abs/2607.19101)

**<font color=#1a73e8>作者：</font>** Yiheng Wu, Jue Hou, Roman Yangarber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable Text Difficulty Assessment is a prerequisite for valid text simplification workflows and personalized learning applications. However, the development of robust assessment models is severely hindered by a critical bottleneck: the scarcity of expert-annotated corpora containing fine-grained difficulty levels (e.g., CEFR), particularly for lower-resource languages. This paper addresses this data scarcity problem in the context of a low-resource European language. We propose a cross-lingual data augmentation strategy that leverages machine translation to transfer labeled resources from high-resource languages to the target low-resource language. We train BERT-based regression models to predict difficulty scores and investigate whether synthetic, translated data can effectively supplement native training sets. Our experiments demonstrate that augmenting scarce native data with machine-translated corpora significantly improves the accuracy of difficulty estimation, offering a viable solution for languages lacking extensive expert annotations.

---


### 198. [OpenRTAG: A Comprehensive Benchmark for Robust Text-Attributed Graph Learning under Data Quality Degradation](https://arxiv.org/abs/2607.19108)

**<font color=#1a73e8>作者：</font>** Yuze Dai, Zhihan Zhang, Yan Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-attributed graphs (TAGs) are an important graph data form that combine relational structure with rich node text. However, real-world TAGs are often imperfect, with quality issues arising from text, structure, and labels, and typically manifesting as sparsity, noise, and imbalance. These dimensions define nine representative degradation scenarios that can substantially affect TAG learning. Although prior studies have explored specific mitigation strategies, existing evidence remains fragmented across degradation types, datasets, tasks, and model families, leaving TAG robustness insufficiently understood. To address this gap, we present OpenRTAG, a robustness benchmark for text-attributed graph learning. OpenRTAG organizes TAG quality issues into a unified 3 * 3 taxonomy and supports standardized evaluation across nine TAG datasets and three downstream tasks. It systematically evaluates scenario validity and model sensitivity, compares traditional GNNs, LLM-GNNs, and a representative GFM, investigates the effectiveness, efficiency, and robustness of scenario-matched baselines, and further examines model behavior under composite degradation scenarios. OpenRTAG provides a standardized testbed for understanding robustness in TAG learning under realistic low-quality settings.

---


### 199. [Exploiting Load/Store Leakage of Sparse Vectors for Key Recovery in HQC](https://arxiv.org/abs/2607.19109)

**<font color=#1a73e8>作者：</font>** Gustavo Banegas, Benjamin Smith, Jad Zahreddine  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hamming Quasi-Cyclic (HQC) is a code-based key encapsulation mechanism selected by NIST for standardization, making its resistance to implementation attacks critically important. We present a side-channel attack that exploits load/store leakage in the manipulation of HQC's sparse secret vectors. Analysing Cortex-M4 assembly generated from the reference implementation, we identify a leakage surface in which the low and high 32-bit halves of each 64-bit word leak with different strengths, due to compiler-generated register spilling. We exploit this leakage to construct a simple zero-word distinguisher classifying machine words of the secret vector as zero or nonzero from electromagnetic measurements. The recovered zero positions are then translated into decoding hints, reducing HQC key recovery to a shortened syndrome-decoding problem. We analyse the resulting decoding complexity for all HQC parameter sets: at 32-bit granularity an expected 88.7% of the machine words of y are zero for HQC-1, cutting the decoding to $\approx$ 2 46 bit operations. Experiments on a Cortex-M4 validate the predicted low/high-half asymmetry-approximately 500 traces for the stronger low-half channel and 5,000 for the weaker high-half channeland recover the zero words of an HQC-1 key at 32-bit granularity. Finally, we discuss practical countermeasures that eliminate the sparsity exploited by the attack.

---


### 200. [GATE-3D: Geometry-Aware Test-time Adaptive Reranking for Open-Set 3D Shape Retrieval](https://arxiv.org/abs/2607.19111)

**<font color=#1a73e8>作者：</font>** Hao Wu, Heyi Lin, Zilin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large pretrained vision models have substantially improved appearance-based 3D shape retrieval, but they still confuse shapes that look similar while differing in geometry. Although geometry-aware features can reduce these errors, naive fusion of geometry and appearance may hurt retrieval when the two modalities are already well aligned. We propose GATE-3D, a lightweight query-adaptive reranking method that incorporates geometry without retraining the retrieval backbone. For each query, GATE-3D predicts how much a geometry-aware score should adjust the appearance-based ranking using features that capture disagreement between the two modalities. This selective design lets geometry contribute where it helps and stay silent where it would hurt. Experiments on three open-set 3D retrieval benchmarks show that GATE-3D improves over appearance-only retrieval and is more robust than always-on fusion. On the primary benchmark, it improves mAP@10 by 2.00 points over appearance-only retrieval (p=0.041); it also improves leave-one-category-out generalization and reduces geometric false positives by 10.8%. GATE-3D achieves competitive zero-shot results against DAC-based baselines. We further find that simple linear routing is more effective than a small MLP in the low-data regime, suggesting that cross-modal disagreement features matter more than model capacity for adaptive routing.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
