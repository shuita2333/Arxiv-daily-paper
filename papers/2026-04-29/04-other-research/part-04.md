# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

---

### 151. [ArguAgent: AI-Supported Real-Time Grouping for Productive Argumentation in STEM Classrooms](https://arxiv.org/abs/2604.23449)

**<font color=#1a73e8>作者：</font>** Jennifer Kleiman, Yizhu Gao, Xin Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Argumentation is a core practice in STEM education, but its productivity depends on who participates and how they interact. Higher-achieving students often dominate the talk and decision-making, while lower-achieving peers may disengage, defer, or comply without contributing substantive reasoning. Forming groups strategically based on students' stances and argumentation skills could help foster inclusive, evidence-based discourse. In practice, however, teachers are constrained in implementing this grouping strategy because it requires real-time insight into students' positions and the quality of their argumentation, information that is difficult to assess reliably and at scale during instruction. We present a generative AI-powered system, ArguAgent, that creates groups optimizing for stance heterogeneity while constraining argumentation quality differences to +/-1 level on a validated learning progression. ArguAgent uses a two-component assessment pipeline: first scoring student arguments on a 0-4 rubric, then clustering positions via semantic analysis. We validated the scoring component against human expert consensus (Krippendorff's {\alpha}\alpha {\alpha} = 0.817) using 200 expert-generated scores. Testing three OpenAI models (GPT-4o-mini, GPT-5.1, GPT-5.2) with identical calibrated prompts, we found that systematic prompt engineering informed by human disagreement analysis contributed 89% of scoring improvement (QWK: 0.531 to 0.686), while model upgrades contributed an additional 11% (QWK: 0.686 to 0.708). Simulation testing across 100 classes demonstrated that the grouping algorithm achieves 95.4% of groups that meet both design criteria, a 3.2x improvement over random assignment. These results suggest ArguAgent can enable real-time, theoretically grounded grouping that promotes productive STEM argumentation in classrooms.

---


### 152. [From Edges to Depth: Probing the Spatial Hierarchy in Vision Transformers](https://arxiv.org/abs/2604.23452)

**<font color=#1a73e8>作者：</font>** Jainum Sanghavi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers trained only on image classification routinely transfer to tasks that demand spatial understanding, yet they receive no spatial supervision during pretraining. We ask where and how robustly such structure is encoded. Probing a frozen ViT-B/16 layerwise for two complementary properties, local patch boundaries (BSDS500) and per-patch depth (NYU Depth V2), reveals a clear hierarchy: boundary structure becomes linearly decodable at layers 5-6 (AP = 0.833), while depth, which requires integrating global cues, peaks two to three layers later at layer 8 (MAE = 0.0875). Both signals collapse at the final classification layer, and random-weight controls confirm the encodings are learned rather than architectural. Causal interventions add specificity: ablating the single direction a linear depth probe reads degrades depth decoding by up to 165%, while ablating any other direction changes it by less than 1%. Targeted activation patching along that direction shows the depth signal is partially re-derived at each layer rather than passively carried in the residual stream, with mid-layer interventions persisting most strongly downstream. The result is that a classification-trained ViT develops an actively maintained spatial hierarchy that mirrors the early-to-late progression observed in the primate visual cortex.

---


### 153. [ARIstoteles -- Dissecting Apple's Baseband Interface](https://arxiv.org/abs/2604.23457)

**<font color=#1a73e8>作者：</font>** Tobias Kröll, Stephan Kleber, Frank Kargl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Wireless chips and interfaces expose a substantial remote attack surface. As of today, most cellular baseband security research is performed on the Android ecosystem, leaving a huge gap on Apple devices. With iOS jailbreaks, last-generation wireless chips become fairly accessible for performance and security research. Yet, iPhones were never intended to be used as a research platform, and chips and interfaces are undocumented. One protocol to interface with such chips is Apple Remote Invocation (ARI), which interacts with the central phone component CommCenter and multiple user-space daemons, thereby posing a Remote Code Execution (RCE) attack surface. We are the first to reverse-engineer and fuzz-test the ARI interface on iOS. Our Ghidra scripts automatically generate a Wireshark dissector, called ARIstoteles, by parsing closed-source iOS libraries for this undocumented protocol. Moreover, we compare the quality of the dissector to fully-automated approaches based on static trace analysis. Finally, we fuzz the ARI interface based on our reverse-engineering results. The fuzzing results indicate that ARI does not only lack public security research but also has not been well-tested by Apple. By releasing ARIstoteles open-source, we also aim to facilitate similar research in the future.

---


### 154. [A Benchmark Suite of Reddit-Derived Datasets for Mental Health Detection](https://arxiv.org/abs/2604.23458)

**<font color=#1a73e8>作者：</font>** Khalid Hasan, Jamil Saquer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing availability of online support groups has opened up new windows to study mental health through natural language processing (NLP). However, it is hindered by a lack of high-quality, well-validated datasets. Existing studies have a tendency to build task-specific corpora without collecting them into widely available resources, and this makes reproducibility as well as cross-task comparison challenging. In this paper, we present a uniform benchmark set of four Reddit-based datasets for disjoint but complementary tasks: (i) detection of suicidal ideation, (ii) binary general mental disorder detection, (iii) bipolar disorder detection, and (iv) multi-class mental disorder classification. All datasets were established upon diligent linguistic inspection, well-defined annotation guidelines, and human-judgmental verification. Inter-annotator agreement metrics always exceeded the baseline agreement score of 0.8, ensuring the labels' trustworthiness. Previous work's evidence of performance on both transformer and contextualized recurrent models demonstrates that these models receive excellent performances on tasks (F1 ~ 93-99%), further validating the usefulness of the datasets. By combining these resources, we establish a unifying foundation for reproducible mental health NLP studies with the ability to carry out cross-task benchmarking, multi-task learning, and fair model comparison. The presented benchmark suite provides the research community with an easy-to-access and varied resource for advancing computational approaches toward mental health research.

---


### 155. [Architecture Matters for Multi-Agent Security](https://arxiv.org/abs/2604.23459)

**<font color=#1a73e8>作者：</font>** Ben Hagag, William L. Anderson, Christian Schroeder de Witt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS), composed of networks of two or more autonomous AI agents, have become increasingly popular in production deployments, yet introduce security risks that do not arise in single-agent settings. Even if individual agents exhibit robust security, architectural decisions governing their coordination can create attack surfaces that have not been systematically characterized. In this work, we present an empirical study of how MAS design decisions shape the tradeoff between task performance and attack resistance. Across three agentic environments (browser, desktop, and code) and 13 architectural configurations, we use stagewise evaluations that distinguish planning refusal, execution-stage interception, partial harmful execution, and successful attack completion to study three key design choices: (i) agent roles, which determine how authority and responsibility are allocated; (ii) communication topology, which shapes how and when agents interact; and (iii) memory, which determines the context and state visibility accessible to each agent. We find that multi-agent architectures are more vulnerable than standalone agents in the majority of configurations, with attack success rates varying by up to 3.8x at comparable or higher benign accuracy, and that no single design is universally safer. These results motivate the development of further evaluations that move beyond the security properties of a single agent.

---


### 156. [Machine learning models for estimating counterfactuals in a single-arm inflammatory bowel disease study](https://arxiv.org/abs/2604.23465)

**<font color=#1a73e8>作者：</font>** Dan Liu, Fida K. Dankar, Jennifer C. deBruyn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-arm trials accelerate study timelines by reducing the number of patients that must be recruited for a concurrent control group. However, these designs require an alternative comparator to estimate treatment effects. One approach is to construct a virtual control arm using a machine learning (ML) model trained on external control data to predict the counterfactual outcomes of the treatment arm. Our aim in this study was to leverage virtual controls by developing and evaluating ML-based counterfactual outcome models trained on IFX-treated patients to predict 1-year steroid-free clinical remission (SFCR ) and a composite of C-reactive protein remission plus steroid-free clinical remission (CRP-SFCR) for ADA-treated pediatric Crohn's disease patients, and to compare the resulting IFX-versus-ADA treatment effect estimates with those obtained using propensity score matching to external controls. Five ML models were used to train counterfactual models on the observed IFX cohort data. The resulting models were used to predict the counterfactual outcomes for the ADA arm patients. LGBM yields the best OR closest to the propensity score matched reference, and all 95% CI results align with the conclusion from the reference study that no statistical difference in the primary and secondary outcomes has been observed between the patients treated with ADA or IFX. Our study supports virtual controls as a viable and effective substitute for expensive, lengthy or unethical patient recruitment in an inflammatory bowel disease (IBD) trial. The developed gradient boosted prediction model can be used as a pretrained model to generate IFX counterfactual predictions in future studies, pending external validation and assessment of transportability.

---


### 157. [Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs](https://arxiv.org/abs/2604.23466)

**<font color=#1a73e8>作者：</font>** Divakar Kumar Yadav, Tian Zhao, Deepak Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> NVIDIA's CUDA Tile (CuTile) introduces a Python-based, tile-centric abstraction for GPU kernel development that aims to simplify programming while retaining Tensor Core and Tensor Memory Accelerator (TMA) efficiency on modern GPUs. We present the first independent, cross-architecture evaluation of CuTile against established approaches such as cuBLAS, Triton, WMMA, and raw SIMT on three NVIDIA GPUs spanning Hopper and Blackwell: H100 NVL, B200, and RTX PRO 6000 Blackwell Server Edition. We benchmark representative AI workloads, including GEMM, fused multi-head attention, and end-to-end LLM inference in BF16/FP16 precision, to assess both performance and portability.
Our results show that CuTile effectiveness is strongly workload- and architecture-dependent. On datacenter-class Blackwell (B200), CuTile achieves up to 1007 TFLOP/s for fused attention, outperforming FlashAttention-2 by 2.5x while requiring only 60 lines of Python kernel code. For GEMM, CuTile reaches 52-79% of cuBLAS performance in 22 lines of code (versus 123 for WMMA), making it a practical replacement for hand-written CUDA kernels but not yet for vendor-optimized libraries. However, the same CuTile attention kernel achieves only 53% of FlashAttention-2 throughput on RTX PRO 6000 (sm_120), exposing significant cross-architecture optimization gaps. In contrast, Triton sustains 62-101% of cuBLAS performance across all tested platforms without architecture-specific tuning, demonstrating substantially stronger portability.

---


### 158. [Can Humans Detect AI? Mining Textual Signals of AI-Assisted Writing Under Varying Scrutiny Conditions](https://arxiv.org/abs/2604.23471)

**<font color=#1a73e8>作者：</font>** Daniel Tabach  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study asks whether the threat of AI detection changes how people write with AI, and whether other people can tell the difference. In a two-phase controlled experiment, 21 participants wrote opinion pieces on remote work using an AI chatbot. Half were randomly warned that their submission would be scanned by an AI detection tool. The other half received no warning. Both groups had access to the same chatbot. In Phase 2, 251 independent judges evaluated 1,999 paired comparisons, each time choosing which document in the pair was written by a human. Judges were not told that both writers had access to AI. Across all evaluations, judges selected the warned writer's document as human 54.13% of the time versus 45.87% for the unwarned writer. A two-sided binomial test rejects chance guessing at p = 0.000243, and the result holds across both writing stances. Yet on every measurable text feature extracted, including AI overlap scores, lexical diversity, sentence structure, and pronoun usage, the two groups were indistinguishable. The judges are picking up on something that feature-based methods do not capture.

---


### 159. [Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization](https://arxiv.org/abs/2604.23472)

**<font color=#1a73e8>作者：</font>** Ziyang Liu, Xinyan Guo, Xuchen Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While recent autonomous agents demonstrate impressive capabilities, they predominantly rely on manually scripted workflows and handcrafted heuristics, inherently limiting their potential for open-ended improvement. To address this, we propose Escher-Loop, a fully closed-loop framework that operationalizes the mutual evolution of two distinct populations: Task Agents that solve concrete problems, and Optimizer Agents that recursively refine both the task agents and themselves. To sustain this self-referential evolution, we propose a dynamic benchmarking mechanism that seamlessly reuses the empirical scores of newly generated task agents as relative win-loss signals to update optimizers' scores. This mechanism leverages the evolution of task agents as an inherent signal to drive the evaluation and refinement of optimizers without additional overhead. Empirical evaluations on mathematical optimization problems demonstrate that Escher-Loop effectively pushes past the performance ceilings of static baselines, achieving the highest absolute peak performance across all evaluated tasks under matched compute. Remarkably, we observe that the optimizer agents dynamically adapt their strategies to match the shifting demands of high-performing task agents, which explains the system's continuous improvement and superior late-stage performance.

---


### 160. [GeoCert: Certified Geometric AI for Reliable Forecasting](https://arxiv.org/abs/2604.23474)

**<font color=#1a73e8>作者：</font>** Regina Zhang, Zongru Li, Honggang Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting systems in science must be accurate, physically consistent, and certifiably reliable. Most existing models address prediction, constraint enforcement, and verification separately, limiting scalability and interpretability. We introduce GeoCert, a geometric AI framework that unifies forecasting, physical reasoning, and formal verification within a single differentiable computation. GeoCert formulates forecasting as evolution along a hyperbolic manifold, where negative curvature induces contraction dynamics, intrinsic robustness, and logarithmic-time certification. A hierarchical constraint architecture separates universal physical laws from domain-specific dynamics, enabling certified generalization across energy, climate, finance, and transportation systems. GeoCert achieves state-of-the-art accuracy while reducing computational cost by 97.5% and maintaining better certification rates. By embedding verification into the geometry of learning, GeoCert transforms forecasting from empirical approximation to formally verified inference, offering a scalable foundation for trustworthy, reproducible, and physically grounded scientific AI.

---


### 161. [Do Synthetic Trajectories Reflect Real Reward Hacking? A Systematic Study on Monitoring In-the-Wild Hacking in Code Generation](https://arxiv.org/abs/2604.23488)

**<font color=#1a73e8>作者：</font>** Lichen Li, Hengguang Zhou, Yijun Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward hacking in code generation, where models exploit evaluation loopholes to obtain full reward without correctly solving the tasks, poses a critical challenge for Reinforcement Learning (RL) and the deployment of reasoning models. Existing studies have been conducted primarily on synthetic hacking trajectories. However, whether these synthetic behaviors faithfully represent naturally emerging hacking in the wild remains unclear. In this work, we present a systematic analysis of the synthetic vs. in-the-wild discrepancy in reward hacking. We examine to what extent hacking behaviors induced by prompting resemble those emerging during RL training, and whether monitors trained on synthetic trajectories generalize to naturally arising but previously unseen hacking. To scale up the curation of in-the-wild reward hacking trajectories, we modified Group Relative Policy Optimization (GRPO) by injecting conflicting unit tests as tracers and applying a "resampling-until-hack" mechanism. Through controlled comparisons between monitors trained on synthetic versus in-the-wild data, we find that (1) synthetic-data-trained monitors fail to generalize to "in-the-wild" hacking, and (2) monitors trained on our "in-the-wild" trajectories demonstrate stronger generalizability to unseen hacking types. Our results indicate that synthetic reward hacking data may not fully reflect natural reward hacking behaviors, and that relying solely on synthetic data can lead to misleading conclusions. The codebase is available at this https URL

---


### 162. [K-SENSE: A Knowledge-Guided Self-Augmented Encoder for Neuro-Semantic Evaluation of Mental Health Conditions on Social Media](https://arxiv.org/abs/2604.23493)

**<font color=#1a73e8>作者：</font>** Vijay Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Early detection of mental health conditions, particularly stress and depression, from social media text remains a challenging open problem in computational psychiatry and natural language processing. Automated systems must contend with figurative language, implicit emotional expression, and the high noise inherent in user-generated content. Existing approaches either leverage external commonsense knowledge to model mental states explicitly, or apply self-augmentation and contrastive training to improve generalization, but seldom do both in a principled, unified framework. We propose K-SENSE (Knowledge-guided Self-augmented Encoder for Neuro-Semantic Evaluation of Mental Health), a framework that jointly exploits external psychological reasoning and internal representation robustness. K-SENSE adopts a three-stage encoding pipeline: (1) inferential commonsense knowledge is extracted from the COMET model across five mental state dimensions; (2) a semantic anchor is constructed by combining hidden representations from two parallel encoding streams, projected into a shared space before fusion; and (3) a supervised contrastive learning objective aligns same-class representations while encouraging the attention mechanism to suppress irrelevant knowledge noise. We evaluate K-SENSE on Dreaddit (stress detection) and Depression_Mixed (depression detection), achieving mean F1-scores of 86.1 (0.6%) and 94.3 (0.8%), respectively, over five independent runs. These represent improvements of approximately 2.6 and 1.5 percentage points over the strongest prior baselines. Ablation experiments confirm the contribution of each architectural component, including the temporal knowledge integration strategy and the choice to keep the knowledge encoder frozen during fine-tuning.

---


### 163. [Do Transaction-Level and Actor-Level AML Queues Agree? An Empirical Evaluation of Granularity Effects on the Elliptic++ Graph](https://arxiv.org/abs/2604.23494)

**<font color=#1a73e8>作者：</font>** Ankur Malik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based anti-money laundering (AML) systems on blockchain networks can score suspicious activity at two granularity levels -- transactions or actor addresses -- yet compliance action is conducted per actor. This paper contributes an evaluation methodology for measuring how scoring granularity affects investigation queue composition under fixed review budgets. We formalize the evaluation through a projection framework mapping transaction-level scores to the actor-level action unit via four aggregation operators, and introduce budgeted investigation metrics -- yield@budget, burden decomposition, and case fragmentation. Using the public Elliptic++ Bitcoin dataset (203,769 transactions; 822,942 address occurrences), we train independent random forest classifiers at each level under a causal temporal protocol and compare review queues through Jaccard overlap, burden decomposition, and feature-matching ablations. At one-percent budget, temporal evaluation yields mean Jaccard of 0.374 (SD 0.171); static pooled evaluation yields 0.087 (95% CI [0.079, 0.094]). An enriched address model receiving all 237 features produces even lower overlap (Jaccard=0.051), with 4.3% illicit per 100 reviews versus 30.2% for the transaction-projected queue. Address-level detection value is temporally concentrated: two timesteps exceed 91% illicit per 100 reviews while the static burden is only 3.4%. A fixed hybrid policy underperforms the best single-level queue by 5.05pp (CI [-10.2pp, -0.9pp]). These findings establish that scoring granularity is a consequential design variable for AML investigation systems -- same data, same budget, different queues, different addresses investigated.

---


### 164. [Interpretable Physics-Informed Load Forecasting for U.S. Grid Resilience: SHAP-Guided Ensemble Validation in Hybrid Deep Learning Under Extreme Weather](https://arxiv.org/abs/2604.23500)

**<font color=#1a73e8>作者：</font>** Md Abubakkar, Sajib Debnath, Md. Uzzal Mia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate short-term electricity load forecasting is a cornerstone of U.S. grid reliability; however, prevailing deep learning models remain opaque, limiting operator trust during extreme weather. A unified, interpretable, physics-informed ensemble framework is proposed, integrating a Convolutional Neural Network (CNN) branch for local feature extraction and a Transformer branch for long-range dependency modeling; the branches are fused through a validation-optimized weighted ensemble and regularized by a physics-informed loss derived from the piecewise parabolic temperature-demand relationship of the Electric Reliability Council of Texas (ERCOT) system. Post-hoc interpretability is provided through SHapley Additive exPlanations (SHAP) with the DeepExplainer backend, yielding global and event-level attributions. Using eight years of ERCOT hourly load data (2018-2025) fused with Automated Surface Observing System (ASOS) records from three Texas stations, the framework achieves 713 MW MAE, 812 MW RMSE, and 1.18% MAPE on the test window. For Hampel-flagged extreme events, MAPE falls by 20.7% relative to its Transformer branch and by 40.5% relative to its CNN branch; an ablation confirms that the parabolic and ramp constraints drive a 14.7% RMSE reduction. SHAP analysis reveals a regime shift: temperature dominates under normal operation, whereas wind speed and precipitation become more influential during cold fronts and heatwaves.

---


### 165. [BurstGP: Enhancing Raw Burst Image Super Resolution with Generative Priors](https://arxiv.org/abs/2604.23508)

**<font color=#1a73e8>作者：</font>** Dong Huo, Tristan Aumentado-Armstrong, Samrudhdhi B. Rangrej 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Burst image super resolution (BISR) aims to construct a single high-resolution (HR) image by aggregating information from multiple low-resolution (LR) frames, relying on temporal redundancy and spatial coherence across the burst. While conventional methods achieve impressive results, they often struggle with complex textures and oversmoothing. Diffusion models, particularly those pretrained on high-quality data, have shown remarkable capability in generating realistic details for image and video super-resolution. However, their potential remains largely under-explored in BISR, where existing approaches typically rely on task-specific diffusion models trained from scratch and operate on single-frame reconstructions. In this work, we propose BurstGP, a novel diffusion-based solution for BISR, which leverages generative priors of recent foundation models to overcome these issues. In particular, we build a multiframe-aware diffusion model on top of a conventional BISR approach, which boosts image quality with minimal loss to fidelity. Further, we introduce (i) a novel degradation-aware conditioning mechanism, which controls synthesis of fine details based on the estimated degradation in the input, and (ii) a robust sRGB-to-lRGB inverter, enabling us to utilize generative multiframe (video) sRGB priors, while operating with raw input and lRGB output images. Empirically, we demonstrate that BurstGP outperforms the existing state of the art, both quantitatively (especially with respect to perceptual metrics, including MUSIQ and LPIPS) and qualitatively. In particular, our proposed method excels at recovering richer textures and finer structural details, highlighting the potential of video priors for BISR over traditional methods.

---


### 166. [Breaking the Secret: Economic Interventions for Combating Collusion in Embodied Multi-Agent Systems](https://arxiv.org/abs/2604.23511)

**<font color=#1a73e8>作者：</font>** Qi Liu, Xiaohui Chen, Zhihui Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Collusion among autonomous agents poses a critical security threat in embodied multi-agent systems (MAS), where coordinated behaviors can deviate from global objectives and lead to real-world consequences. Existing defenses, primarily based on identity control or post-hoc behavior analysis, are insufficient to address such threats in embodied settings due to delayed feedback and noisy observations in physical environments, which make behavioral deviations difficult to detect accurately and in a timely manner. To address this challenge, we propose a mutagenic incentive intervention approach that mitigates collusion by reshaping agents' payoff structures. By rewarding agents who report collusive behavior and penalizing identified participants, the mechanism induces strategic defection and renders collusion unstable. We further design supporting mechanisms, including reporting deposits, smart contract-based reward enforcement, and encrypted communication, to ensure robustness against misuse of the incentive mechanism and retaliation from penalized agents. We implement the proposed approach in both simulated and real-world embodied environments. Experimental results show that our method effectively suppresses collusion by inducing defection, while preserving system efficiency. It achieves performance comparable to the non-collusion baseline and outperforms representative reactive defenses, thereby fulfilling the desired security objectives. These results demonstrate the effectiveness of proactive incentive design as a practical paradigm for securing embodied multi-agent systems.

---


### 167. [Time-Delayed Publicly Verifiable Quantum Computation for Classical Verifiers](https://arxiv.org/abs/2604.23516)

**<font color=#1a73e8>作者：</font>** Ameer Mohammed, Aydin Abadi, Jaffer Mahdi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Publicly verifiable delegation is a well-known problem involving a user who wishes to outsource a resource-intensive computational task to a more powerful but potentially untrusted server such that any other party is able to efficiently check the veracity of the computation's result. This problem has been extensively studied in the classical domain where the user and server are both non-quantum machines. However, the problem becomes more challenging when the classical user wants to delegate a quantum circuit to a single prover with quantum-computing capabilities. Previous solutions have resorted to using impractical or non-standard cryptographic solutions (e.g. indistinguishability obfuscation) to achieve this requirement. In this work, we relax the requirement to have time-delayed publicly verifiable proofs, where the verification key is made known to the public only when the computation (and its proof) are guaranteed to have been completed. We propose a practical non-interactive scheme leveraging commitment schemes and time-lock puzzles, which can be efficiently realized through well-established and standard post-quantum assumptions. The main idea of our technique lies in using time-lock puzzles to compile a 2-round privately verifiable scheme into a non-interactive publicly verifiable scheme with timestamped proofs, outsourcing not only the quantum computation but the puzzle solving as well. Security is proven in the quantum random oracle model with a common reference string (CRS).

---


### 168. [Autocorrelation Reintroduces Spectral Bias in KANs for Time Series Forecasting](https://arxiv.org/abs/2604.23518)

**<font color=#1a73e8>作者：</font>** Chen Zeng, Jiahui Wang, Qiao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing theory suggests that Kolmogorov-Arnold Networks (KANs) can overcome the spectral bias commonly observed in neural networks under the assumption that inputs are statistically independent. However, this assumption does not hold in time series forecasting (TSF), where inputs are lagged observations with strong temporal autocorrelation. Through theoretical analysis and empirical validation, we obtain an unexpected finding: temporal autocorrelation reintroduces spectral bias in KANs, and the bias becomes increasingly pronounced as the degree of autocorrelation increases. This suggests that standard KANs may face substantial difficulties in TSF with strongly autocorrelated inputs. To address this problem, we introduce the Discrete Cosine Transform (DCT) to reduce the correlations among the network inputs. As expected, experimental results reveal that DCT preprocessing substantially reduces the observed low-frequency preference in TSF. This result also corroborates that the spectral bias of KANs in TSF tasks is indeed induced by the autocorrelation among input variables.

---


### 169. [When PINNs Go Wrong: Pseudo-Time Stepping Against Spurious Solutions](https://arxiv.org/abs/2604.23528)

**<font color=#1a73e8>作者：</font>** Sifan Wang, Shawn Koohy, Yiping Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) provide a promising machine learning framework for solving partial differential equations, but their training often breaks down on challenging problems, sometimes converging to physically incorrect solutions despite achieving small residual losses. This failure, we argue, is not merely an optimization difficulty. Rather, it reflects a fundamental weakness of the empirical PDE residual loss, which can admit trivial or spurious solutions during training. From this perspective, we revisit pseudo-time stepping, a technique that has recently shown strong empirical success in PINNs. We show that its main benefit is not simply to ease optimization; instead, when combined with collocation-point resampling, it helps reveal and avoid spurious solutions. At the same time, we find that the effectiveness of pseudo-time stepping depends critically on the choice of step size, which cannot be tuned reliably from the training loss alone. To overcome this limitation, we propose an adaptive pseudo-time stepping strategy that selects the step size from a finite-difference surrogate of the local residual Jacobian, yielding the largest step permitted by local stability without per-problem tuning. Across a diverse set of PDE benchmarks, the proposed method consistently improves both accuracy and robustness. Together, these findings provide a clearer understanding of why PINNs fail and suggest a practical pathway toward more reliable physics-informed learning. All code and data accompanying this manuscript are available at this https URL.

---


### 170. [Analysis of Personal Data Exposure in Thailand](https://arxiv.org/abs/2604.23538)

**<font color=#1a73e8>作者：</font>** Suphannee Sivakorn, Sasawat Malaivongs, Nuttaya Rujiratanapat  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the digital era, personal data, particularly sensitive identifiers such as the Social Security Number and National Identification Number, have become a highly valuable asset, raising significant concerns regarding privacy and security. This study examines the risks associated with the online exposure of the Thai National Identification Number, a key element of identity verification in both governmental and commercial transactions. Similar to the Social Security Number in the United States, this unique identifier is crucial for various legal, financial, and welfare-related activities. However, the increasing digitization of personal records has heightened its vulnerability to unauthorized access and misuse, particularly through search engines that inadvertently index sensitive information.
This research identifies publicly exposed Thai National Identification Numbers across major search engines, assessing the potential threats to individual privacy and national security. The study reveals the exposure of over 1.2 million unique National Identification Numbers, along with other highly sensitive personal data, e.g., addresses, contact details, employment status, disability status, and health information. Notably, the analysis indicates that a significant majority of these exposures originate from the Thai government sector websites, highlighting critical vulnerabilities in public data management practices. This widespread exposure not only increases the risk of identity theft and financial fraud but also underscores the urgent need for enhanced cybersecurity measures, stricter regulatory enforcement, and improved data governance within government agencies to prevent future breaches. Addressing these issues is essential to safeguarding citizens' personal information and ensuring compliance with Thailand's data protection laws in an increasingly digitized world.

---


### 171. [MetaGAI: A Large-Scale and High-Quality Benchmark for Generative AI Model and Data Card Generation](https://arxiv.org/abs/2604.23539)

**<font color=#1a73e8>作者：</font>** Haoxuan Zhang, Ruochi Li, Yang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Generative AI necessitates rigorous documentation standards for transparency and governance. However, manual creation of Model and Data Cards is not scalable, while automated approaches lack large-scale, high-fidelity benchmarks for systematic evaluation. We introduce MetaGAI, a comprehensive benchmark comprising 2,541 verified document triplets constructed through semantic triangulation of academic papers, GitHub repositories, and Hugging Face artifacts. Unlike prior single-source datasets, MetaGAI employs a multi-agent framework with specialized Retriever, Generator, and Editor agents, validated through four-dimensional human-in-the-loop assessment, including human evaluation of editor-refined ground truth. We establish a robust evaluation protocol combining automated metrics with validated LLM-as-a-Judge frameworks. Extensive analysis reveals that sparse Mixture-of-Experts architectures achieve superior cost-quality efficiency, while a fundamental trade-off exists between faithfulness and completeness. MetaGAI provides a foundational testbed for benchmarking, training, and analyzing automated Model and Data Card generation methods at scale. Our data and code are available at: this https URL.

---


### 172. [AusSmoke meets MultiNatSmoke: a fully-labelled diverse smoke segmentation dataset](https://arxiv.org/abs/2604.23542)

**<font color=#1a73e8>作者：</font>** Weihao Li, Hongjin Zhao, Gao Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildfires are an escalating global concern due to the devastating impacts on the environment, economy, and human health, with notable incidents such as the 2019-2020 Australian bushfires and the 2025 California wildfires underscoring the severity of these events. AI-enabled camera-based smoke detection has emerged as a promising approach for the rapid detection of wildfires. However, existing wildfire smoke segmentation datasets that are used for training detection and segmentation models are limited in scale, geographically constrained, and often rely on synthetic imagery, which hinders effective training and generalization. To overcome these limitations, we present AusSmoke, a new smoke segmentation dataset collected from Australia to address the data scarcity in this region. Furthermore, we introduce a MultiNational geographically diverse and substantially larger fully-labelled benchmark, called MultiNatSmoke, that consolidates publicly available international datasets with the newly collected Australian imagery, expanding the scale by an order of magnitude over previous collections. Finally, we benchmark smoke segmentation models, demonstrating improved performance and enhanced generalization across diverse geographical contexts. The project is available at \href{this https URL}{Github}.

---


### 173. [Safeguarding Skies: Airport Cybersecurity in the Digital Age](https://arxiv.org/abs/2604.23545)

**<font color=#1a73e8>作者：</font>** Suphannee Sivakorn, Nuttaya Rujiratanapat, Yotsapat Ruangpaisarn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The aviation industry faces significant vulnerabilities from both physical and cybersecurity threats, highlighting the urgent need for enhanced cybersecurity measures amid increasingly sophisticated attacks. This paper systematically reviews emerging threats at airports, analyzing real-world incidents and relevant literature while mapping risks to the MITRE ATT&CK Matrix, a widely recognized knowledge base for categorizing cyberattack tactics, techniques, and procedures. This is the first to apply the MITRE Matrix to airport security risks, offering a novel approach to understanding and mitigating these challenges. Building on this analysis, the paper advocates for modern cybersecurity defense models, emphasizing Cybersecurity Frameworks and Zero Trust Architecture, as well as critical measures for supply chain risk management and strategies to mitigate ransomware and DoS attacks. Our analysis provides insights into vulnerabilities and actionable recommendations, serving as a comprehensive guide for aviation stakeholders to strengthen defenses against evolving cybersecurity threats.

---


### 174. [COMO: Closed-Loop Optical Molecule Recognition with Minimum Risk Training](https://arxiv.org/abs/2604.23546)

**<font color=#1a73e8>作者：</font>** Zhuoqi Lyu, Qing Ke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical chemical structure recognition (OCSR) translates molecular images into machine-readable representations like SMILES strings or molecular graphs, but remains challenging in real-world documents due to inexhaustible variations in chemical structures, shorthand conventions, and visual noise. Most existing deep-learning-based approaches rely on teacher forcing with token-level Maximum Likelihood Estimation (MLE). This training paradigm suffers from exposure bias, as models are trained under ground-truth prefixes but must condition on their own previous predictions during inference. Moreover, token-level MLE objectives hinder the optimization towards molecular-level evaluation criteria such as chemical validity and structural similarity. Here we introduce Minimum Risk Training (MRT) to OCSR and propose COMO (Closed-loop Optical Molecule recOgnition), a closed-loop framework that mitigates exposure bias by directly optimizing over molecule-level, non-differentiable objectives, by iteratively sampling and evaluating the model's own predictions. Experiments on ten benchmarks including synthetic and real-world chemical diagrams from patent and scientific literature demonstrate that COMO substantially outperforms existing rule-based and learning-based methods with less training data. Ablation studies further show that MRT is architecture-agnostic, demonstrating its potential for broad application to end-to-end OCSR systems.

---


### 175. [Spatiotemporal Degradation-Aware 3D Gaussian Splatting for Realistic Underwater Scene Reconstruction](https://arxiv.org/abs/2604.23551)

**<font color=#1a73e8>作者：</font>** Shaohua Liu, Ning Gao, Zuoya Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing realistic underwater scenes from underwater video remains a meaningful yet challenging task in the multimedia domain. The inherent spatiotemporal degradations in underwater imaging, including caustics, flickering, attenuation, and backscattering, frequently result in inaccurate geometry and appearance in existing 3D reconstruction methods. While a few recent works have explored underwater degradation-aware reconstruction, they often address either spatial or temporal degradation alone, falling short in more real-world underwater scenarios where both types of degradation occur. We propose MarineSTD-GS, a novel 3D Gaussian Splatting-based framework that explicitly models both temporal and spatial degradations for realistic underwater scene reconstruction. Specifically, we introduce two paired Gaussian primitives: Intrinsic Gaussians represent the true scene, while Degraded Gaussians render the degraded observations. The color of each Degraded Gaussian is physically derived from its paired Intrinsic Gaussian via a Spatiotemporal Degradation Modeling (SDM) module, enabling self-supervised disentanglement of realistic appearance from degraded images. To ensure stable training and accurate geometry, we further propose a Depth-Guided Geometry Loss and a Multi-Stage Optimization strategy. We also construct a simulated benchmark with diverse spatial and temporal degradations and ground-truth appearances for comprehensive evaluation. Experiments on both simulated and real-world datasets show that MarineSTD-GS robustly handles spatiotemporal degradations and outperforms existing methods in novel view synthesis with realistic, water-free scene appearances.

---


### 176. [On the Memorization of Consistency Distillation for Diffusion Models](https://arxiv.org/abs/2604.23552)

**<font color=#1a73e8>作者：</font>** Bingqing Jiang, Difan Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are central to modern generative modeling, and understanding how they balance memorization and generalization is critical for reliable deployment. Recent work has shown that memorization in diffusion models is shaped by training dynamics, with generalization and memorization emerging at different stages of training. However, deployed diffusion models are often further distilled, introducing an additional training phase whose impact on memorization is not well understood. In this work, we analyze how distillation reshapes memorization behavior in diffusion models, taking consistency distillation as a representative framework. Empirically, we show that when applied to a teacher model that has memorized data, consistency distillation significantly reduces transferred memorization in the student while preserving, and sometimes improving, sample quality. To explain this behavior, we provide a theoretical analysis using a random feature neural network model [Bonnaire et al., 2025], showing that consistency distillation suppresses unstable feature directions associated with memorization while preserving stable, generalizable modes. Our findings suggest that distillation can serve not only as an acceleration tool, but also as a mechanism for improving the memorization-generalization trade-off.

---


### 177. [PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574)

**<font color=#1a73e8>作者：</font>** Tianyidan Xie, Zhentao Huang, Mingjie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing image-to-video generation methods often produce physically implausible motions and lack precise control over object dynamics. While prior approaches have incorporated physics simulators, they remain confined to 2D planar motions and fail to capture depth-aware spatial interactions. We introduce PhysLayer, a novel framework enabling language-guided, depth-aware layered animation of static images. PhysLayer consists of three key components: First, a language-guided scene understanding module that utilizes vision foundation models to decompose scenes into depth-based layers by analyzing object composition, material properties, and physical parameters. Second, a depth-aware layered physics simulation that extends 2D rigid-body dynamics with depth motion and perspective-consistent scaling, enabling more realistic object interactions without requiring full 3D reconstruction. Third, a physics-guided video synthesis module that integrates simulated trajectories with scene-aware relighting for temporally coherent results. Experimental results demonstrate improvements in CLIP-Similarity (+2.2\%), FID score (+9.3\%), and Motion-FID (+3\%), with human evaluation showing enhanced physical plausibility (+24\%) and text-video alignment (+35\%). Our approach provides a practical balance between physical realism and computational efficiency for controllable image animation.

---


### 178. [CAPSULE: Control-Theoretic Action Perturbations for Safe Uncertainty-Aware Reinforcement Learning](https://arxiv.org/abs/2604.23576)

**<font color=#1a73e8>作者：</font>** Rahul Narava, Siddharth Verma, Ojas Jain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring safe exploration in high-dimensional systems with unknown dynamics remains a significant challenge. Existing safe reinforcement learning methods often provide safety guarantees only in expectation, which can still lead to safety violations. Control-theoretic approaches, in contrast, offer hard constraint-based safety guarantees but typically assume access to known system dynamics or require accurate estimation of control-affine models. In this paper, we propose a safe reinforcement learning framework that learns a probabilistic control-affine dynamics model in an offline setting. The learned model is leveraged to explicitly construct control barrier functions (CBFs) that incorporate model uncertainty to provide conservative safety constraints. These CBF constraints are enforced through an online constraint-based action correction mechanism, enabling safe exploration without overly restricting task performance. Empirical evaluations on nonlinear, complex continuous-control benchmarks demonstrate that our approach achieves returns comparable to those of existing baselines while significantly reducing safety violations.

---


### 179. [Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586)

**<font color=#1a73e8>作者：</font>** Zhen Ye, Xu Tan, Aoxiong Yin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint audio-video generation models have shown that unified generation yields stronger cross-modal coherence than cascaded approaches. However, existing models couple modalities throughout denoising via pervasive attention, treating high-level semantics and low-level details in a fully entangled manner. This is suboptimal for talking head synthesis: while audio and facial motion are semantically correlated, their low-level realizations (acoustic signals and visual textures) follow distinct rendering processes. Enforcing joint modeling across all levels causes unnecessary entanglement and reduces efficiency. We propose Talker-T2AV, an autoregressive diffusion framework where high-level cross-modal modeling occurs in a shared backbone, while low-level refinement uses modality-specific decoders. A shared autoregressive language model jointly reasons over audio and video in a unified patch-level token space. Two lightweight diffusion transformer heads decode the hidden states into frame-level audio and video latents. Experiments on talking portrait benchmarks show Talker-T2AV outperforms dual-branch baselines in lip-sync accuracy, video quality, and audio quality, achieving stronger cross-modal consistency than cascaded pipelines.

---


### 180. [FinGround: Detecting and Grounding Financial Hallucinations via Atomic Claim Verification](https://arxiv.org/abs/2604.23588)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial AI systems must produce answers grounded in specific regulatory filings, yet current LLMs fabricate metrics, invent citations, and miscalculate derived quantities. These errors carry direct regulatory consequences as the EU AI Act's high-risk enforcement deadline approaches (August 2026). Existing hallucination detectors treat all claims uniformly, missing 43% of computational errors that require arithmetic re-verification against structured tables. We present FinGround, a three-stage verify-then-ground pipeline for financial document QA. Stage 1 performs finance-aware hybrid retrieval over text and tables. Stage 2 decomposes answers into atomic claims classified by a six-type financial taxonomy and verified with type-routed strategies including formula reconstruction. Stage 3 rewrites unsupported claims with paragraph- and table-cell-level citations. To cleanly isolate verification value from retrieval quality, we propose retrieval-equalized evaluation as standard methodology for RAG verification research: when all systems receive identical retrieval, FinGround still reduces hallucination rates by 68% over the strongest baseline ($p < 0.01$). The full pipeline achieves a 78% reduction relative to GPT-4o. An 8B distilled detector retains 91.4% F1 at 18x lower per-claim latency, enabling $0.003/query deployment, supported by qualitative signals from a four-week analyst pilot.

---


### 181. [XITE: Cross-lingual Interpolation for Transfer using Embeddings](https://arxiv.org/abs/2604.23589)

**<font color=#1a73e8>作者：</font>** Barah Fazili, Preethi Jyothi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Facilitating cross-lingual transfer in multilingual language models remains a critical challenge. Towards this goal, we propose an embedding-based data augmentation technique called XITE. We start with unlabeled text from a low-resource target language, identify an English counterpart in a task-specific training corpus using embedding-based similarities and adopt its label. Next, we perform a simple interpolation of the source and target embeddings to create synthetic data for task-specific fine-tuning. Projecting the target text into a language-rich subspace using linear discriminant analysis (LDA), prior to interpolation, further boosts performance. Our cross-lingual embedding-based augmentation technique XITE yields significant improvements of up to 35.91% for sentiment analysis and up to 81.16% for natural language inference, using XLM-R, for a diverse set of target languages including Korean, Arabic, Urdu and Hindi. Apart from boosting cross-lingual transfer, adaptation using XITE also safeguards against forgetting and maintains task performance on the high-resource language.

---


### 182. [When AI reviews science: Can we trust the referee?](https://arxiv.org/abs/2604.23593)

**<font color=#1a73e8>作者：</font>** Jialiang Wang, Yuchen Liu, Hang Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The volume of scientific submissions continues to climb, outpacing the capacity of qualified human referees and stretching editorial timelines. At the same time, modern large language models (LLMs) offer impressive capabilities in summarization, fact checking, and literature triage, making the integration of AI into peer review increasingly attractive -- and, in practice, unavoidable. Yet early deployments and informal adoption have exposed acute failure modes. Recent incidents have revealed that hidden prompt injections embedded in manuscripts can steer LLM-generated reviews toward unjustifiably positive judgments. Complementary studies have also demonstrated brittleness to adversarial phrasing, authority and length biases, and hallucinated claims. These episodes raise a central question for scholarly communication: when AI reviews science, can we trust the AI referee? This paper provides a security- and reliability-centered analysis of AI peer review. We map attacks across the review lifecycle -- training and data retrieval, desk review, deep review, rebuttal, and system-level. We instantiate this taxonomy with four treatment-control probes on a stratified set of ICLR 2025 submissions, using two advanced LLM-based referees to isolate the causal effects of prestige framing, assertion strength, rebuttal sycophancy, and contextual poisoning on review scores. Together, this taxonomy and experimental audit provide an evidence-based baseline for assessing and tracking the reliability of AI peer review and highlight concrete failure points to guide targeted, testable mitigations.

---


### 183. [Learning to Identify Out-of-Distribution Objects for 3D LiDAR Anomaly Segmentation](https://arxiv.org/abs/2604.23604)

**<font color=#1a73e8>作者：</font>** Simone Mosco, Daniel Fusaro, Alberto Pretto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the surrounding environment is fundamental in autonomous driving and robotic perception. Distinguishing between known classes and previously unseen objects is crucial in real-world environments, as done in Anomaly Segmentation. However, research in the 3D field remains limited, with most existing approaches applying post-processing techniques from 2D vision. To cover this lack, we propose a new efficient approach that directly operates in the feature space, modeling the feature distribution of inlier classes to constrain anomalous samples. Moreover, the only publicly available 3D LiDAR anomaly segmentation dataset contains simple scenarios, with few anomaly instances, and exhibits a severe domain gap due to its sensor resolution. To bridge this gap, we introduce a set of mixed real-synthetic datasets for 3D LiDAR anomaly segmentation, built upon established semantic segmentation benchmarks, with multiple out-of-distribution objects and diverse, complex environments. Extensive experiments demonstrate that our approach achieves state-of-the-art and competitive results on the existing real-world dataset and the newly introduced mixed datasets, respectively, validating the effectiveness of our method and the utility of the proposed datasets. Code and datasets are available at this https URL.

---


### 184. [Thinking Like a Clinician: A Cognitive AI Agent for Clinical Diagnosis via Panoramic Profiling and Adversarial Debate](https://arxiv.org/abs/2604.23605)

**<font color=#1a73e8>作者：</font>** Zhiqi Lv, Duofan Tu, Jun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The application of large language models (LLMs) in clinical decision support faces significant challenges of "tunnel vision" and diagnostic hallucinations present in their processing unstructured electronic health records (EHRs). To address these challenges, we propose a novel chain-based clinical reasoning framework, called DxChain, which transforms the diagnostic workflow into an iterative process by mirroring a clinician's cognitive trajectory that consists of "Memory Anchoring", "Navigation" and "Verification" phases. DxChain introduces three key methodological innovations to elicit the potential of LLM: (i) a Profile-Then-Plan paradigm to mitigate cold-start hallucinations by establishing a panoramic patient baseline, (ii) a Medical Tree-of-Thoughts (Med-ToT) algorithm for strategic look ahead planning and resource aware navigation, and (iii) a Dialectical Diagnostic Verification procedure utilizing "Angel-Devil" adversarial debates to resolve complex evidence conflicts. Evaluated on two real world benchmarks, MIMIC-IV-Ext Cardiac Disease and MIMIC-IV-Ext CDM, DxChain achieves state-of-the-art performances in both diagnostic accuracy and logical consistency, offering a modular and reliable architecture for next-generation clinical AI. The code is at this https URL.

---


### 185. [Hamiltonian Graph Inference Networks: Joint structure discovery and dynamics prediction for lattice Hamiltonian systems from trajectory data](https://arxiv.org/abs/2604.23606)

**<font color=#1a73e8>作者：</font>** Ru Geng, Panayotis Kevrekidis, Yixian Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lattice Hamiltonian systems underpin models across condensed matter, nonlinear optics, and biophysics, yet learning their dynamics from data is obstructed by two unknowns: the interaction topology and whether node dynamics are homogeneous. Existing graph-based approaches either assume the graph is given or, as in $\alpha$-separable graph Hamiltonian network, infer it only for separable Hamiltonians with homogeneous node dynamics. We introduce the Hamiltonian Graph Inference Network (HGIN), which jointly recovers the interaction graph and predicts long-time trajectories from state data alone, for both separable and non-separable Hamiltonians and under heterogeneous node dynamics. HGIN couples a structure-learning module -- a learnable weighted adjacency matrix trained under a Hamilton's-equations loss -- with a trajectory-prediction module that partitions edges into physically distinct subgraphs via $k$-means clustering, assigning each subgraph its own encoder and thereby breaking the parameter-sharing bottleneck of conventional GNNs. On three benchmarks -- a Klein--Gordon lattice with long-range interactions and two discrete nonlinear Schrödinger lattices (homogeneous and heterogeneous) -- HGIN reduces long-time energy prediction error and trajectory prediction error by six to thirteen orders of magnitude relative to baselines. A symmetry argument on the Hamiltonian loss further shows that the learned weights encode the parity of the underlying pair potential, yielding an interpretable readout of the system's interaction structure.

---


### 186. [Comparative Study of Weighted and Coupled Second- and Fourth-Order PDEs for Image Despeckling in Grayscale, Color, SAR, and Ultrasound](https://arxiv.org/abs/2604.23612)

**<font color=#1a73e8>作者：</font>** Manish Kumar, Rajendra K. Ray  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partial Differential Equation (PDE)-based approaches have gained significant attention in image despeckling due to their strong capability to preserve structural details while suppressing noise. However, conventional second-order PDE models tend to generate blocky artifacts, whereas higher-order models often introduce speckle patterns. To resolve it, this paper proposes and comparatively analyzes two advanced PDE-based frameworks designed for speckle noise suppression while preserving the fine edges. The first model introduces a novel weighted formulation that combines second and fourth-order PDEs through a weighting parameter. The second-order diffusion coefficient employs grayscale and gradient-based indicators, while the fourth-order term is guided solely by a Laplacian-based indicator. The second model constructs a coupled PDE framework, where independent fourth and second-order components are explicitly solved in an iterative manner. In this coupled structure, each diffusion coefficient is defined separately to enhance adaptability in varying image regions. Both models are implemented using the explicit finite difference method. The proposed techniques are extensively evaluated on a variety of datasets, including standard grayscale, color, Synthetic Aperture Radar (SAR), and ultrasound images. Comparative experiments with the existing Telegraph Diffusion Model (TDM) and Fourth-Order Telegraph Diffusion Model (TDFM) demonstrate the superiority of the proposed approaches in reducing speckle noise while effectively preserving fine image structures and edges. Quantitative evaluations using PSNR, SSIM and Speckle Index metrics confirm that the proposed models produce higher image quality and enhanced visual perception. Overall, the presented PDE-based formulations provide a reliable and efficient framework for image despeckling in both natural and medical imaging.

---


### 187. [Applications of the Transformer Architecture in AI-Assisted English Reading Comprehension](https://arxiv.org/abs/2604.23615)

**<font color=#1a73e8>作者：</font>** Ping Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper studies interpretable and fair artificial intelligence architectures for understanding English reading. Introduced transformer-based models, integrating advanced attention mechanisms and gradient-based feature attribution. The model's lack of interpretability, reduction of algorithmic bias, and unreliable performance in learning environments are the current issues faced in natural language teaching. A unified technical pipeline has been constructed, including adversarial bias correction methods, token-level attribution analysis, and multi-head attention heatmap visualization. Experimental validation was conducted using a large-scale labeled English reading comprehension dataset, and the data partitioning scheme and parameter optimization procedures have been determined. The method significantly outperforms the state-of-the-art models for this task in terms of accuracy and macro-average F1 score; in some aspects, it even surpasses or closely matches the results of human evaluations. In multi-week user experiments, the explainable transformer improved teachers' trust and operability in feedback-based assessments within the scoring system. The proposed method aims to ensure high prediction accuracy and fairness for different learners. This indicates that it is a real-world educational application based on artificial intelligence with a focus on interpretation. Improve the user experience in AI-assisted reading comprehension systems, counteract biases, and enhance the details explained by transformers.

---


### 188. [The Vehicle May Be Sick: Denial of Diagnostic Services by Exploiting the CAN Transport Protocol](https://arxiv.org/abs/2604.23617)

**<font color=#1a73e8>作者：</font>** Seungjin Baek, Seonghoon Jeong, Huy Kang Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vehicle diagnostics has become essential for detecting in-vehicle errors and ensuring safety. While the Unified Diagnostic Services (UDS) protocol is widely adopted for diagnostic operations, it relies on the ISO 15765-2 standard as the transport protocol over the Controller Area Network (CAN), which was designed without inherent security considerations. In this paper, we identify eight novel attack scenarios that exploit specific transport layer mechanisms in the ISO 15765-2 standard, including Flow Control manipulation, Sequence Number violations, and error handling abuses. We evaluate these attacks on a real passenger vehicle using two distinct diagnostic tools to demonstrate their practical impact. Our results confirm that three of these attack scenarios successfully induce denial of diagnostic services, leading to abnormal diagnostic results such as concealed faults and manipulated sensor readings. These findings highlight critical vulnerabilities that can deceive technicians and drivers, potentially exposing vehicles to significant safety risks.

---


### 189. [A Synergistic CNN-Transformer Network with Pooling Attention Fusion for Hyperspectral Image Classification](https://arxiv.org/abs/2604.23622)

**<font color=#1a73e8>作者：</font>** Peng Chen, Wenxuan He, Feng Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the hyperspectral image (HSI) classification task, each pixel is categorized into a specific land-cover category or material. Convolutional neural networks (CNNs) and transformers have been widely used to extract local and non-local features in HSI classification. Recent works have utilized a multi-scale vision transformer (ViT) to enhance spectral feature capture and yield promising results. However, most existing methods still face challenges in the effective joint use of spatial-spectral information and in preserving information across layers during the propagation process. To address these issues, we propose a synergistic CNN-Transformer network with pooling attention fusion for HSI classification, which collaboratively utilizes CNNs and ViT to process spatial and spectral features separately. Specifically, we propose a Twin-Branch Feature Extraction (TBFE) module, which employs 3D and 2D convolution in parallel to comprehensively extract spectral and spatial features from HSI. A hybrid pooling attention (HPA) module is designed to aggregate spatial attention. Moreover, a cascade transformer encoder is employed for global spectral feature extraction, and a simple yet efficient cross-layer feature fusion (CFF) module is designed to reduce the loss of crucial information in the previous network layers. Extensive experiments are conducted on several representative datasets to demonstrate the superior performance of our proposed method compared to the state-of-the-art works. Code is available at this https URL.

---


### 190. [Neural Grammatical Error Correction for Romanian](https://arxiv.org/abs/2604.23627)

**<font color=#1a73e8>作者：</font>** Teodor-Mihai Cotet, Stefan Ruseti, Mihai Dascalu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Resources for Grammatical Error Correction (GEC) in non-English languages are scarce, while available spellcheckers in these languages are mostly limited to simple corrections and rules. In this paper we introduce a first GEC corpus for Romanian consisting of 10k pairs of sentences. In addition, the German version of ERRANT (ERRor ANnotation Toolkit) scorer was adapted for Romanian to analyze this corpus and extract edits needed for evaluation. Multiple neural models were experimented, together with pretraining strategies, which proved effective for GEC in low-resource settings. Our baseline consists of a small Transformer model trained only on the GEC dataset (F0.5 of 44.38), whereas the best performing model is produced by pretraining a larger Transformer model on artificially generated data, followed by finetuning on the actual corpus (F0.5 of 53.76). The proposed method for generating additional training examples is easily extensible and can be applied to any language, as it requires only a POS tagger

---


### 191. [Hallo-Live: Real-Time Streaming Joint Audio-Video Avatar Generation with Asynchronous Dual-Stream and Human-Centric Preference Distillation](https://arxiv.org/abs/2604.23632)

**<font color=#1a73e8>作者：</font>** Chunyu Li, Jiaye Li, Ruiqiao Mei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time text-driven joint audio-video avatar generation requires jointly synthesizing portrait video and speech with high fidelity and precise synchronization, yet existing audio-visual diffusion models remain too slow for interactive use and often degrade noticeably after aggressive acceleration. We present Hallo-Live, a streaming framework for joint audio-visual avatar generation that combines asynchronous dual-stream diffusion with human-centric preference-guided distillation. To reduce articulation lag in causal generation, we introduce Future-Expanding Attention, which allows each video block to access synchronous audio together with a short horizon of future phonetic cues. To mitigate the quality loss of few-step distillation, we further propose Human-Centric Preference-Guided DMD (HP-DMD), which reweights training samples using rewards from visual fidelity, speech naturalness, and audio-visual synchronization. On two NVIDIA H200 GPUs, Hallo-Live runs at 20.38 FPS with 0.94 seconds latency, yielding 16.0x higher throughput and 99.3x lower latency than the teacher model Ovi. Despite this speedup, it retains strong generation quality, reaching comparable VideoAlign overall score and Sync Confidence score while outperforming other accelerated baselines in the overall quality-efficiency trade-off. Qualitative results further show robust generalization across photorealistic, multi-speaker, and stylized scenarios. To the best of our knowledge, Hallo-Live is the first framework to combine streaming dual-stream diffusion with preference-guided distillation for real-time, text-driven audio-visual generation.

---


### 192. [Causal Discovery as Dialectical Aggregation: A Quantitative Argumentation Framework](https://arxiv.org/abs/2604.23633)

**<font color=#1a73e8>作者：</font>** Sheng Wei, Yulin Chen, Beishui Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraint-based causal discovery is brittle in finite-sample regimes because erroneous conditional-independence (CI) decisions can cascade into substantial structural errors. We propose Quantitative Argumentation for Causal Discovery (QACD), a semantics-driven framework that represents CI outcomes as graded, defeasible arguments rather than irreversible constraints. QACD maps statistical test outcomes to argument strengths and aggregates conflicting evidence through connectivity-mediated witness propagation, producing a fixed-point acceptability labeling over candidate adjacencies. Experiments on standard benchmark Bayesian networks suggest that QACD improves structural coherence and interventional reliability in several noisy or inconsistent CI regimes, while remaining competitive with classical constraint-based, hybrid, and prior argumentation-based baselines.

---


### 193. [From Rights to Rites: Expectations Management in Smart-Home AI](https://arxiv.org/abs/2604.23635)

**<font color=#1a73e8>作者：</font>** Varad Vishwarupe, Ivan Flechais, Marina Jirotka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Domestic voice assistants and smart-home devices are increasingly embedded in everyday routines, yet their ethics are often treated as an afterthought or delegated to compliance teams. To explore how expectations about smart-home AI are constructed and managed, we conducted 33 semi-structured interviews with designers, developers, and researchers from major smart-home platforms (Amazon Alexa, Microsoft Azure IoT, and Google Nest). Using a constructivist grounded theory approach, we develop Expectations Management (EM): a culturally embedded model describing how practitioners shape, calibrate, and repair expectations by balancing organisational rights with culturally situated rites. We show that EM differs from expectation-confirmation theory and trust-calibration by foregrounding moral judgement, situated action, and cross-cultural variation. Our analysis reveals four recurring design tensions: automation vs. autonomy, helpfulness vs. intrusiveness, personalisation vs. predictability, and transparency vs. obscurity and distils them into a five-phase EM Design Playbook that supports moral prudence. We discuss implications for responsible smart-home design and offer guidance for human-centred AI.

---


### 194. [Discriminator-Guided Adaptive Diffusion for Source-Free Test-Time Adaptation under Image Corruptions](https://arxiv.org/abs/2604.23636)

**<font color=#1a73e8>作者：</font>** Francesco Olivato, Cigdem Beyan, Vittorio Murino  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we study Source-Free Unsupervised Domain Adaptation under corruption-induced domain shifts, where performance degradation is caused by natural image corruptions that go beyond additive noise, including blur, weather effects, and digital artifacts. We propose a diffusion-based, input-level adaptation framework that operates entirely at test time and keeps all source-trained models frozen, explicitly targeting robustness to corrupted target inputs. Our method leverages a source-trained diffusion model as a generative prior and introduces a discriminator-guided adaptive diffusion strategy that dynamically controls the amount of perturbation applied to each test sample. Rather than relying on a fixed diffusion depth, the discriminator determines, on a per-image basis, when sufficient forward diffusion has been applied to suppress corruption-specific artifacts, with each corruption type effectively defining a distinct target domain. This adaptive stopping mechanism applies only the necessary amount of noise to remove domainspecific corruption while preserving class-discriminative structure. The reverse diffusion process then reconstructs a source-aligned image, optionally stabilized through structural guidance, which is classified using a frozen source-trained classifier. We evaluate the proposed approach across a broad spectrum of corruption-induced target domains, covering 15 diverse corruption types, and demonstrate more balanced robustness with competitive or improved performance across non-noise corruptions. Additional analyses reveal how the adaptive diffusion schedule responds to different corruption characteristics, highlighting the practicality, generality, and robustness of the proposed framework. The code is publicly available at this https URL.

---


### 195. [Quantifying the Persistence of Daily Routines](https://arxiv.org/abs/2604.23638)

**<font color=#1a73e8>作者：</font>** Nguyen Luong, Talayeh Aledavood  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Daily life is structured by recurring routines that coordinate biological rhythms with social and occupational demands. Individual differences in work schedules, family obligations, and social commitments produce distinctive ways of organizing activities throughout the day. Do people have typical days with certain arrangement of activities? How often do these typical days or routines occur and does this differ from person to person? We introduce a framework for quantifying such recurring routines, their persistence over time and their distinctiveness for different people. We model consecutive days in one's life as a sequence of different types of typical days, i.e. routines. Characterizing each day through patterns of activities common among all people - sleep, movement, and device use - we identify a small set of routine types that capture the dominant structure of everyday behavior. We then test whether individuals maintain stable, person-specific distributions over these types and transition between them in characteristic ways. Validating this framework with passive sensing data from 1,086 participants across 153,000 person-days in three longitudinal studies, we find that daily life typically resolves into approximately eight routine types and each person maintains a characteristic distribution over these types. Both the time allocation across routine types and the day-to-day transition dynamics are substantially more similar within individuals than between them, remaining stable across observation windows spanning weeks to months and across populations differing in age, occupation, and health status. Routine persistence shows modest associations with personality traits such as conscientiousness, but is broadly similar across age and gender. Our findings establish routine patterns as stable, person-specific behavioral fingerprints with applications in personalized health monitoring.

---


### 196. [VDLF-Net: Variational Feature Fusion for Adaptive and Few-Shot Visual Learning](https://arxiv.org/abs/2604.23641)

**<font color=#1a73e8>作者：</font>** Jiawei Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces VDLF-Net, which attaches a compact VAE to a multi-scale CNN backbone. Latent vectors and softmax-gate support the backbone feature maps, while $\ell_2$-normalized embeddings from the gated maps contribute toward supervised classification or episodic few-shot prediction. Under standard CIFAR-100 and Mini-ImageNet protocols, VDLF-Net demonstrates an improved performance over ResNet-50 Enhanced, VGG-16, Prototypical Networks, and Matching Networks. Extensive ablations show that removing the fine-resolution scale has the greatest impact on VDLF-Net's performance. At the same time, KL and reconstruction at the chosen $\alpha$ pose a minor performance reduction, demonstrating that performance gains over classical episodic baselines mainly originate from the full VDLF-Net architecture and training strategy.

---


### 197. [RaV-IDP: A Reconstruction-as-Validation Framework for Faithful Intelligent Document Processing](https://arxiv.org/abs/2604.23644)

**<font color=#1a73e8>作者：</font>** Pritesh Jha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent document processing pipelines extract structured entities (tables, images, and text) from documents for use in downstream systems such as knowledge bases, retrieval-augmented generation, and analytics. A persistent limitation of existing pipelines is that extraction output is produced without any intrinsic mechanism to verify whether it faithfully represents the source. Model-internal confidence scores measure inference certainty, not correspondence to the document, and extraction errors pass silently into downstream consumers.
We present Reconstruction as Validation (RaV-IDP), a document processing pipeline that introduces reconstruction as a first-class architectural component. After each entity is extracted, a dedicated reconstructor renders the extracted representation back into a form comparable to the original document region, and a comparator scores fidelity between the reconstruction and the unmodified source crop. This fidelity score is a grounded, label-free quality signal. When fidelity falls below a per-entity-type threshold, a structured GPT-4.1 vision fallback is triggered and the validation loop repeats. We enforce a bootstrap constraint: the comparator always anchors against the original document region, never against the extraction, preventing the validation from becoming circular.
We further propose a per-stage evaluation framework pairing each pipeline component with an appropriate benchmark. The code pipeline is publicly available at this https URL for experimentation and use.

---


### 198. [Structural Enforcement of Goal Integrity in AI Agents via Separation-of-Powers Architecture](https://arxiv.org/abs/2604.23646)

**<font color=#1a73e8>作者：</font>** Rong Xiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent evidence suggests that frontier AI systems can exhibit agentic misalignment, generating and executing harmful actions derived from internally constructed goals, even without explicit user requests. Existing mitigation methods, such as Reinforcement Learning from Human Feedback (RLHF) and constitutional prompting, operate primarily at the model level and provide only probabilistic safety guarantees. We propose the Policy-Execution-Authorization (PEA) architecture, a "separation-of-powers" design that enforces safety at the system level. PEA decouples intent generation, authorization, and execution into independent, isolated layers connected via cryptographically constrained capability tokens. We present five core contributions: (C1) an Intent Verification Layer (IVL) for ensuring capability-intent consistency; (C2) Intent Lineage Tracking (ILT), which binds all executable intents to the originating user request via cryptographic anchors; (C3) Goal Drift Detection, which rejects semantically divergent intents below a configurable threshold; (C4) an Output Semantic Gate (OSG) that detects implicit coercion using a structured $K \times I \times P$ threat calculus (Knowledge, Influence, Policy); and (C5) a formal verification framework proving that goal integrity is maintained even under adversarial model compromise. By shifting agent alignment from a behavioral property to a structurally enforced system constraint, PEA provides a robust foundation for the governance of autonomous agents.

---


### 199. [Rényi Pufferfish Privacy with Gaussian-based Priors: From Single Gaussian to Mixture Model](https://arxiv.org/abs/2604.23649)

**<font color=#1a73e8>作者：</font>** Wenjin Yang, Ni Ding, Zijian Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rényi Pufferfish Privacy (RPP) provides a Rényi divergence-based privacy framework for correlated data, but existing $\infty$-Wasserstein mechanisms are often conservative and sacrifice data utility. We study Gaussian mechanisms for RPP under Gaussian and Gaussian-mixture priors. For single Gaussian priors, we derive the exact Rényi divergence after Gaussian perturbation, obtain a relaxed closed-form sufficient condition for $(\alpha,\epsilon)$-RPP, and characterize the monotonicity of the calibrated noise with respect to the privacy budget $\epsilon$ and the Rényi order $\alpha$. To handle more general non-Gaussian and multimodal priors, we approximate secret-conditioned outputs with Gaussian mixture models and introduce an optimal-transport-based sufficient condition for RPP. Experiments on three UCI datasets with statistical (\textsc{RAW}, \textsc{MEAN}) and model-output (\textsc{BNN}, \textsc{GP}) queries show that our prior-aware mechanisms consistently require less noise than a recent RPP additive-noise baseline, achieving an average noise reduction of 48.9\%. These results show that our mechanisms can substantially improve the privacy-utility trade-off under RPP.

---


### 200. [Geometry-Conditioned Diffusion for Occlusion-Robust In-Bed Pose Estimation](https://arxiv.org/abs/2604.23651)

**<font color=#1a73e8>作者：</font>** Navid Aslankhani Khameneh, Marco Carletti, Cigdem Beyan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust in-bed human pose estimation under blanket occlusion remains challenging due to the scarcity of reliable labeled training data for heavily covered poses. Existing approaches rely on multi-modal sensing or image-to-image translation frameworks that remain conditioned on visible source imagery, limiting scalability and pose diversity. In this work, we reformulate occlusion-aware augmentation as a geometry-conditioned generative modeling task. We conduct a systematic comparison of deterministic masking, unpaired translation, paired diffusion-based translation, and a proposed pose-conditioned Latent Diffusion Model (Pose-LDM). Unlike image-guided methods, Pose-LDM synthesizes blanket-covered images directly from skeletal keypoints, eliminating dependence on paired supervision and pixel-level source-image conditioning while enabling generation from arbitrary pose inputs. All augmentation strategies are evaluated through their impact on downstream pose estimation under a fixed backbone. Pose- LDM achieves the highest strict localization accuracy under severe occlusion while maintaining overall detection performance comparable to paired diffusion models, approaching the performance of fully supervised training. These results demonstrate that geometry-conditioned diffusion provides an effective and supervision-efficient pathway toward occlusion-robust inbed pose estimation without modifying the sensing pipeline. The code is available at: this http URL GeoDiffPose.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
