# 📦 其他研究 | 2026年09月17日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-219**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-219**

---

### 201. [SlotDiT: Object-Centric Representations for Diffusion Transformers](https://arxiv.org/abs/2609.17414)

**<font color=#1a73e8>作者：</font>** Gjergj Plepi, Sven Behnke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-conditioned latent diffusion models perform strongly in video generation and are promising backbones for robotic applications. However, existing approaches rely on pixel-level or VAE-based latent representations that lack explicit semantic structure, leaving the impact of the representation space largely unexplored. Slot-based object-centric representations offer a structured alternative by decomposing scenes into object-level latents, or slots. While they have shown success in dynamics modeling and planning, they have not yet been explored for diffusion-based generative modeling. We introduce SlotDiT, a text-guided Diffusion Transformer (DiT) that operates in a slot-based latent space. Given a reference image and a language instruction, SlotDiT decomposes the scene into object-centric slots representing individual entities. Conditioned on the instruction and observed scene context, the model autoregressively denoises future slot trajectories to predict scene dynamics. To systematically investigate latent-space design for diffusion transformers, we compare slot-based representations against VAE-based and semantics-aligned alternatives within a unified DiT framework. Our experiments show that using slots as DiT latents yields competitive video generation quality while consistently improving task-completion rates across four robotic datasets. Furthermore, their compact representation provides a computationally efficient alternative to VAE-based and semantics-aligned latent spaces. Overall, our results demonstrate that object-centric structure is a powerful inductive bias for diffusion-based generative modeling in robotic environments. The project page is available at this https URL.

---


### 202. [Knowledge as Orbit: Finite Collections as Phases of an Exactly Periodic Latent Generator](https://arxiv.org/abs/2609.17417)

**<font color=#1a73e8>作者：</font>** Siddharth Pal, Viktoria Rojkova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite knowledge is usually stored extensionally, one code or vector per item. We ask whether a finite collection can instead be stored intensionally, as the decoded orbit of one compact law that returns exactly to its start. For X objects, we encode item i as the i-th phase of a fixed rotation in a learned latent space and decode all phases with a shared network; the latent advances through a bank of rotations at integer harmonics of the cycle, a real discrete Fourier operator, so that R^X equals the identity and exact closure is guaranteed rather than learned. Images are a controlled carrier; looping video is the case where the phase order is the content's own temporal structure. Holding the decoder fixed and varying only the operator, a general learned operator diverges, a norm-preserving but non-periodic one degrades around the loop, and the exactly periodic operator is flat; on real images the gap widens. Capacity is then the decoder's budget: dense decoders carry a structural overhead per crisp image that no size reconciles with compression, while a small convolutional decoder on objects that share a manifold reaches crisp and compressed. A codebook control shows the generative law is free in reconstruction terms while multiplying the latent store many-fold. On seven benchmark clips, against a matched frame-index baseline, the cycle reaches equal or better fidelity at equal parameters while wrapping at machine precision, where the baseline leaves a visible seam; pinning the baseline's frequencies to loop harmonics closes its seam too, confirming that exact periodicity is the operative constraint. Finite cyclic knowledge can be stored as dynamics rather than independent instances, with exact recurrence supplied by algebra and content by a shared decoder.

---


### 203. [Transformer-Based Token Fusion and Dynamic Graph Planning for Audio-Visual Navigation](https://arxiv.org/abs/2609.17421)

**<font color=#1a73e8>作者：</font>** Shaohang Wu, Yinfeng Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Navigation (AVN) requires an agent to localize and navigate toward a continuously vocalizing target relying solely on visual observations and acoustic cues. Currently, systems lack the ability to adaptively correct and replan when faced with incomplete or misleading visual perception. Furthermore, relying on physical collisions to compensate for missing visual information results in inefficient and unsafe navigation, whereas existing methods are overly dependent on passive visual perception. To address these issues, we propose the Transformer-based Token Fusion and Dynamic Graph Planning (TDGP) model, which incorporates high-level perception layers and leverages the Transformer model to fuse multimodal cues for precise local planning. Next, a low-level planning layer is designed that uses physical collision penalties to remove edges that collide with the map in real time and apply corresponding penalties, forcing the agent to automatically re-plan to compensate for the lack of visual information. Experiments show that our TDGP model outperforms baseline models on the Replica and Matterport3D (MP3D) datasets, and that the model's sound enhancement strategy significantly improves generalization in unheard acoustic scenarios.

---


### 204. [Talking Head Synthesis with Facial Landmark Guidance via 3D Gaussian Splatting](https://arxiv.org/abs/2609.17422)

**<font color=#1a73e8>作者：</font>** Ziheng Yang, Yinfeng Yu, Yongming Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-driven digital human generation plays an important role in virtual communication, immersive interaction, and media production. With the development of Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), recent talking-head systems have obtained more faithful 3D facial geometry and appearance modeling. A remaining difficulty is that speech features mainly describe temporal acoustic patterns rather than explicit facial layouts. As a result, directly driving 3D facial deformation with audio may produce inaccurate mouth motion, weak expression details, and local artifacts. To address this issue, we propose a facial-keypoint-guided spatial enhancement module. The predicted landmarks provide structural cues for selecting and enriching spatial points around expression-sensitive facial regions. We further introduce a global landmark compensation mechanism, where the full set of keypoints is encoded into a conditioning vector to refine 3DGS attributes. This compensation supplies whole-face structural information to the underlying shape representation. Experiments under self-driven and cross-driven settings show that the proposed method improves visual quality, facial realism, and lip synchronization.

---


### 205. [Tracking the Unseen: An Occlusion-Robust Framework for Target Tracking Under Full and Long-Term Occlusion](https://arxiv.org/abs/2609.17427)

**<font color=#1a73e8>作者：</font>** Mais Mohammed, Sharifa Mohammed, Hanan Awadh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time multi-object tracking systems remain highly vulnerable to full and long-term occlusion, where targets temporarily or completely disappear from the camera's field of view. Conventional trackers may terminate trajectories prematurely, resulting in identity loss and reduced situational awareness in applications such as defense and surveillance. This work proposes an occlusion-robust target tracking framework that maintains target identity and trajectory continuity through the integration of YOLOv11n object detection, Kalman Filter motion prediction, and occlusion-aware appearance-based re-identification. The framework consists of three stages: object detection, position estimation during occlusion, and identity recovery after target reappearance. Six Re-Identification (Re-ID) architectures were evaluated within the same tracking framework under identical conditions, with the Occlusion-Aware Mask Network (OAMN) achieving the best overall performance and therefore selected for the final pipeline. The framework was benchmarked against OccluTrack on the public OVIS dataset, achieving relative improvements of 18.1 percent in Multiple Object Tracking Accuracy (MOTA) and 25.1 percent in Identity F1 Score (IDF1), while reducing identity switches by 12.8 percent. On a custom military dataset simulating surveillance and battlefield-like environments with long-term occlusion, the framework achieved a MOTA of 0.734 and an IDF1 of 0.729, corresponding to relative improvements of 14.2 percent and 5.8 percent over OccluTrack. The system demonstrated strong tracking continuity, robust identity preservation, and reliable trajectory estimation under challenging occlusion conditions, highlighting its effectiveness for defense-related surveillance applications requiring continuous target tracking during visibility loss.

---


### 206. [Learning-Guided Planning in Large Dynamic Action Spaces: Budgeted Tree Search for One-to-Many Mobile Charging](https://arxiv.org/abs/2609.17429)

**<font color=#1a73e8>作者：</font>** Liang-Ching Tao, Pi-Chung Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many learned sequential decision systems map the current state directly to an action. That shortcut becomes brittle when candidate actions are numerous, geometrically structured, and rebuilt with the state. One-to-many mobile charging makes this setting concrete: with N=250 sensors, the initial state induces about 1,125 candidate charging-stop actions; each chosen stop simultaneously serves its in-range sensors, and the action universe changes as sensors die. LP-BTS is a learning-guided planning architecture: a graph proposal policy concentrates a small candidate support, a learned value critic evaluates leaves, and edge-budgeted PUCT compares short simulated futures before committing an action. Because the policy scores this set without a fixed output head, a single frozen checkpoint covers every evaluated setting, spanning action universes from 736 to 2,813 stops. Matched ablations reveal complementary effects: uniform sampling costs 8.8 survival percentage points, while, with targeted support fixed, PUCT jointly retains 1.4 points (about 3.5 of 250 sensors) and direct policy selection travels 23% farther. On a prospectively specified, sealed 30-scenario confirmatory bank evaluated once, LP-BTS attains the highest observed survival (0.4545) and alive-AUC (0.8031). Its estimated survival advantage over the strongest domain-engineered comparator is +0.0066 (95% CI [-0.0037, +0.0184]), an unresolved difference, while it exceeds a deadline heuristic and two source-derived direct-policy reconstructions on every paired scenario. Both learned rows are trained, source-derived reconstructions of variants reported by Gong et al. In this setting, the results provide controlled evidence about learning-guided planning in a large, dynamic action space.

---


### 207. [CareMirror: Bringing Caregiver Wellbeing into the Dementia Care Ecosystem](https://arxiv.org/abs/2609.17434)

**<font color=#1a73e8>作者：</font>** Jiayue Melissa Shi, Ethan Nguyen, Drishti Goel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Family caregivers of people living with dementia shoulder emotional and practical responsibilities, yet their own wellbeing often remains peripheral to dementia care. We built CareMirror, an envisioned caregiver wellbeing ecosystem with interconnected caregiver- and clinician-facing interfaces for longitudinal reflection, personalized support, and caregiver-controlled sharing with clinical care. We conducted semi-structured interviews with 14 caregivers, using CareMirror as a design probe to examine how they perceived this ecosystem and what expectations, concerns, and boundaries emerged around clinical connection. Caregivers valued attention to their wellbeing, longitudinal awareness, context-sensitive support, and clinical visibility when it could lead to meaningful follow-up. However, repeated reflection could become burdensome or emotionally difficult, automatic clinical sharing could inhibit candid disclosure, and participants wanted control over what information entered clinical care. They also expected AI to support reflection and communication without replacing caregiver voice or clinician judgment. We contribute design considerations for proactive, clinically connected caregiver wellbeing support.

---


### 208. [Reduced-Space Multi-Fidelity Bayesian Optimization of Process Simulation Models](https://arxiv.org/abs/2609.17440)

**<font color=#1a73e8>作者：</font>** Niki Triantafyllou, Andrea Bernardi, Maria M. Papathanasiou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing industrial process flowsheets is often computationally prohibitive due to the high cost of rigorous simulations and the curse of dimensionality inherent in complex design spaces. To address these challenges, we present a reduced-space multi-fidelity Bayesian optimization (RS-MFBO) framework designed for high-dimensional, expensive black-box functions. The approach integrates Global Sensitivity Analysis (GSA) for dimensionality reduction with a fidelity-augmented Gaussian process that captures correlations between low-cost approximations and expensive high-fidelity evaluations. A cost-aware acquisition strategy, augmented with cooldown and promotion mechanisms, adaptively guides the allocation of samples across fidelities. The framework is validated on two distinct industrial process simulators: a plasmid DNA bioprocess in SuperPro Designer and a green fuel synthesis plant in Aspen HYSYS. Results across diverse economic and physical objectives demonstrate that the proposed method substantially reduces the number of high-fidelity simulator evaluations while maintaining competitive optimization performance compared to single-fidelity baselines. These results highlight RS-MFBO as a scalable, simulator-agnostic approach for cost-constrained black-box optimization.

---


### 209. [ORCA: Occlusion-Aware Refinement and Completion for Novel View Synthesis](https://arxiv.org/abs/2609.17450)

**<font color=#1a73e8>作者：</font>** Weronika Jakubowska, Maciej Zięba, Przemysław Spurek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel-view synthesis from a single image is a fundamentally ambiguous problem. As the camera moves away from the input viewpoint, previously hidden regions become visible, exposing missing geometry and holes in the reconstructed scene. Existing methods often rely on generative models to complete such regions. However, many of these artifacts are small gaps near depth boundaries and do not require generating new scene content.
In order to eliminate expensive process of generating image we introduce ORCA, an occlusion-aware method for reconstructing and completing explorable 3D scenes from a single image. ORCA first introduces 3D structure into a Gaussian-anchor representation using monocular depth while preserving the original camera-ray correspondence. During scene exploration, missing regions are handled based on their size and structure. Small disocclusions are repaired using RGB-D information already available in the reconstruction, while generative inpainting is reserved for larger regions that cannot be reliably recovered from the scene. New Gaussian anchors are added and optimized locally without modifying the existing representation. By reducing unnecessary reliance on generative inpainting, ORCA limits generation-induced hallucinations and better preserves the content and structure of the original scene.
On DIV2K, ORCA improves novel-view quality over VistaDream across all reported metrics, increasing MUSIQ from 61.60 to 68.71 and CLIP-IQA from 0.474 to 0.574. These results show that many novel-view artifacts can be repaired effectively by reusing information already present in the reconstructed scene.

---


### 210. [How Does Title Framing Influence Pattern Identification in Line Charts?](https://arxiv.org/abs/2609.17455)

**<font color=#1a73e8>作者：</font>** Jasmine Lim, Tapendra Pandey, Arran Zeyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual data communication in digital media is increasingly characterized by short attention spans and snapshot-based viewing, often employing line charts to convey trends and patterns. Among all visual elements, titles are crucial elements that can shape how viewers interpret visual information and form chart takeaways. In this study, we examine how title characteristics, particularly title word count and intended message, influence people's pattern identification in single-class line charts. Participants viewed 50 line charts collected from online news media and identified the pattern they perceived. Our results demonstrate that both title word count and intended message significantly influence viewers' pattern identification. Our findings highlight the importance of title framing in shaping quick-view pattern takeaways and supporting effective visualization communication.

---


### 211. [Decomposition Buys Integrity, Not Yield](https://arxiv.org/abs/2609.17464)

**<font color=#1a73e8>作者：</font>** Rong He  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems split a task across a tree of agents and justify the split with folklore: smaller contexts, cleaner separation, parallelism. We ask what the split does to how much of what the leaves discover reaches the root. Model a decomposition as a tree in which an agent handed $b$ items keeps any one with probability $r(b)$. If $r(b)=1/b$, every tree delivers exactly one finding, for every task size and every shape; we verify this to $2.4 \times 10^{-15}$ on 20,000 random irregular trees. If $r(b)=Cb^{-\delta}$, a depth-$k$ tree over $N$ findings yields $C^k N^{1-\delta}$: task size and architecture separate, and architecture contributes only $C \le 1$ per level, so flat is optimal for yield and no arrangement of agents escapes the exponent $\delta$. On 600 production deep-research traces $\delta = 0.34$ [0.30, 0.38], by three identifications that do not share a failure mode. At a hop where item boundaries come from the tool rather than a text heuristic, and where $b=1$ occurs 550 times, $C = 0.571$ [0.527, 0.615] is observed rather than extrapolated, over 16,082 hops. A tier also costs alignment: on 1,012 annotated multi-agent traces one brief in sixteen goes off-target, giving $\mu = 0.939$ and a per-tier penalty $C\mu = 0.536$. Depth is bought on two other axes. The root context is the only state that persists and the only one that cannot cheaply forget, and depth cuts its exposure from $N$ items to $N^{1/k}$. Depth is also cheaper: production flat agents bill as $N^{1.39}$, not the $N^2$ an append-only context predicts, and at equal spend two tiers overtake flat at 403 findings. Across every parameter we measured the model says 0.7% to 11.3% of production sessions are worth delegating, against 7.8% that do. A hazard model on 743,819 production tool calls finds that delegation does not respond to a filling context and is instead an opening move.

---


### 212. [Det-LIME: Detector-Aware, Multi-Instance Local Interpretable Model-Agnostic Explanations for Automated Marine Mammal Detection](https://arxiv.org/abs/2609.17479)

**<font color=#1a73e8>作者：</font>** Jiayi Zhou, David W. Johnston, Brinnae Bent  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid uptake of black-box object detectors in marine mammal research and monitoring, explainability techniques are rarely integrated into conservation workflows. Furthermore, most classification-oriented explainability tools are ill-suited to detection tasks involving imagery of social organisms or those with colonial life histories, as they ignore multiple detections within a scene and produce single-instance outputs that blur evidence across individuals. These methods also generate low-resolution, often biologically irrelevant visuals, limiting their utility for debugging, targeted data augmentation, and refined data collection.
We proposed Det-LIME, a detector-aware, multi-instance adaptation of Local Interpretable Model-Agnostic Explanations (LIME) that produced instance-specific, box-aligned explanations by combining per-detection weighting, a proximity kernel that emphasizes regions near each box, and Intersection-over-Union-based matching to track the same instance across perturbations. We evaluated Det-LIME on aerial drone imagery for harbor seal detection, with an additional seabird case study to assess generality, and compared it with vanilla LIME, Stabilized LIME, Deterministic LIME, and gradient-based attribution methods.
Using the Attribution Ratio and Max Saliency Hit Rate metrics, we showed that Det-LIME consistently improved multi-instance attribution. In practice, these higher-resolution, instance-aware explanations provide insight into model outputs and support post-processing, debugging, and actionable improvements in modeling and data collection or augmentation.

---


### 213. [Quick-View Takeaways: How Does Title Framing Influences Pattern Identification in Line Charts?](https://arxiv.org/abs/2609.17485)

**<font color=#1a73e8>作者：</font>** Jasmine Lim, Tapendra Pandey, Arran Zeyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual data communication in digital media is increasingly characterized by short attention spans and snapshot-based viewing, often employing line charts to convey trends and patterns. Among all visual elements, titles are crucial ones that can shape how viewers interpret visual information and form chart takeaways. In this study, we examine how title characteristics, particularly title word count and intended message, influence people's pattern identification in single-class line charts. Participants viewed 50 line charts collected from online news media and identified the pattern they perceived. Our results demonstrate that both title word count and intended message significantly influence viewers' pattern identification. Our findings highlight the importance of title design in shaping chart takeaways and effective visualization communication.

---


### 214. [FreqSpaNet: Frequency and Spatial Learning of SFPF for Physical Layer Hardware Integrity Detection](https://arxiv.org/abs/2609.17491)

**<font color=#1a73e8>作者：</font>** Xiaoxuan Huang, Jinlong Xu, YiZhe Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unauthorized hardware replacement can preserve a wireless device's logical identity while altering its physical implementation, posing a challenge to hardware integrity verification. Spatio-frequency polarization fingerprints (SFPFs) capture device-dependent responses across multiple frequencies and directions, but their frequency and spatial dimensions exhibit different structural dependencies. We propose FreqSpaNet, an SFPF representation learning network for open set hardware anomaly detection. A frequency branch captures local variations among neighboring frequencies, while a geometry-aware spatial branch models directional relationships using angular information. The two representations are combined through adaptive fusion, and complementary pretraining further captures shared information while preserving the distinct characteristics of the frequency and spatial representations. Experiments show that FreqSpaNet achieves a mean AUROC of 96.31\%, 9.05 points above the baseline. Results under seven hardware replacement scenarios further verify the effectiveness of FreqSpaNet.

---


### 215. [ENCP: Episode-Normalized Conformal Prediction for Vision-and-Language Navigation](https://arxiv.org/abs/2609.17499)

**<font color=#1a73e8>作者：</font>** Vicky Feliren, A. Taufiq Asyhari, Muhamad Risqi U. Saputra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation for Vision-Language-Navigation (VLN) models is a critical task since it can help identify ambiguous and unreliable predictions, enabling agents to make safer navigation decisions. As one of the most advanced uncertainty estimation frameworks, conformal prediction (CP) offers a promising approach for uncertainty estimation in VLN. However, given that VLN agent requires a sequence of steps, standard calibration in conformal prediction fails to provide coverage guarantee it promises over a dependent, variable-length VLN episode. To this end, we propose Episode-Normalized Conformal Prediction (ENCP), which rescales a nonconformity score by the policy's residual confidence and calibrates one maximum score per episode. Under exchangeable calibration and test episodes, this construction covers the ground truth at every step with probability at least $1 - \alpha$, while allowing dependence among steps within an episode. Across four VLN policies and three nonconformity scores on R2R and REVERIE dataset, ENCP meets all reported empirical step-coverage targets on the seen-to-unseen evaluation. These results demonstrate that ENCP can provide model-agnostic uncertainty estimates, which might be useful for determining when a VLN agent should defer to a more capable predictor, including human assistance.

---


### 216. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](https://arxiv.org/abs/2609.17521)

**<font color=#1a73e8>作者：</font>** Chuhao Chen, Peter Wonka, Chaoyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive control for video generation is moving from coarse prompts toward fine-grained, physically meaningful manipulation of dynamic scenes. Yet existing controllable methods either require the full control schedule before generation starts, or use pixel-space signals that dictate object positions rather than physical dynamics. To address these limitations, we propose PhysStream, an autoregressive model for physics-grounded image-to-video synthesis that incorporates structured scene memory---positional maps and object tracking maps derived online from previously generated frames---and supports fine-grained motion control via sparse velocity-increment signals that encode physical quantities, letting the model learn the underlying dynamics. We train our model in two stages: a bidirectional model is first finetuned with motion-control conditioning, then a causal autoregressive model is trained with additional structured scene memory, further improving physical consistency. PhysStream enables interactive, mid-generation control over multi-object tabletop rigid-body scenes---a capability not supported by prior methods---reducing motion distribution distance (FVMD) by 33% and trajectory error by 12% over the strongest baselines on synthetic benchmarks, and is preferred by human evaluators in over 85% of in-the-wild comparisons. Please check our website for more details: this https URL

---


### 217. [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](https://arxiv.org/abs/2609.17523)

**<font color=#1a73e8>作者：</font>** Shuhan Xue, Jianyuan Zhong, Ziyuan Nan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce and release ScienceBuddy, an interactive scientific research workspace that brings continually improving scientific agents into researchers' everyday workflows. ScienceBuddy supports researchers in carrying out scientific tasks while transforming their requests, feedback, and execution evidence into tasks and evaluation rubrics for continual learning. At its core is recursive-in-recursive self-improvement, a paradigm that couples harness evolution with model reinforcement learning: the inner recursion improves the harness with the model fixed, while the outer recursion trains the model under the improved harness. Harness evolution shapes training experience, and model learning creates new opportunities for harness adaptation. We present case studies of researcher interaction, harness refinement, and model learning, with the benchmark cases spanning four scientific task families. By releasing ScienceBuddy as a research product, we make this paradigm available to the scientific community and take a step toward discovery intelligence: scientific AI that advances through sustained collaboration with researchers and evolves alongside the research it supports. Website: this http URL

---


### 218. [You Shall Not Pass into Ring-0! A User Privacy-Friendly Anti-Cheat Architecture for Personal Computers](https://arxiv.org/abs/2609.17525)

**<font color=#1a73e8>作者：</font>** Santosh Gokul Narayanan, Giovanni Paladino, Chuqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Kernel-level anti-cheats are effective against malicious player behavior in competitive video games, but raise significant user privacy concerns regarding installing unverifiable components at privileged modes (i.e., ring-0 in x86). While existing research has focused on improving the effectiveness of anti-cheats, the user privacy concern has been largely ignored. Tirith is an anti-cheat architecture that addresses this problem using two key ideas. First, instead of running video games within regular processes that players (as root admins) have control over, Tirith executes video games in Protected Virtual Machines that naturally sandbox computations from untrusted admins. Second, to monitor user behavior outside the sandbox (e.g., see if they are running malicious drivers), Tirith leverages a virtualization monitor that is trusted by both players and developers. Together, these ideas remove the need to run untrusted kernel-level anti-cheats, while providing the same level of protection compared to such solutions against a wide-range of common cheating mechanisms. The main challenge we face in implementing these ideas, however, is that the existing software stack for virtual machines is not designed to run video games and creates significant security and performance problems. We address these problems by proposing a security-focused Library OS kernel for games and an efficient graphics sharing pipeline for near-native rendering and display performance. In summary, without compromising on cheating behavior detection or performance, this work makes user privacy a first-class citizen in personal computers.

---


### 219. [Agentic Societies Need a Social Harness](https://arxiv.org/abs/2609.17527)

**<font color=#1a73e8>作者：</font>** Tapan Chugh, Vidushi Singh, Krish Jain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> An agentic society is a collection of AI agents that coordinate autonomously across trust boundaries, on behalf of different principals whose objectives may only partially align. We show experimentally that in agentic societies even honest, competent agents often fail to reach satisfactory outcomes with existing harnesses and messaging primitives, and that faulty or malicious agents can stall collaboration, influence outcomes, and pursue other harmful goals by exploiting vulnerabilities in communication (``speech''). We argue that agentic societies need a \emph{social harness} for inter-agent interactions, in addition to each agent's \emph{personal harness}, which manages its private context and communication with its principal. We propose a layered architecture for social harnesses which (i) prevents classes of failures outright, (ii) enables agents to detect invalid messages at runtime, and (iii) supports post-facto investigation and consequences, and highlight directions for future research to realize these capabilities.

---


> [!TIP]
> 当前位于：**201-219**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-219**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
