# 🔐 大模型安全相关研究 | 2026年07月28日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents](https://arxiv.org/abs/2607.21642)

**<font color=#1a73e8>作者：</font>** Wenxiao Zhang, Yu Liu, Zhiwei Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly used for coding and terminal automation, making shell-command dispatch a high-stakes runtime control point. We study command-level pre-execution mediation for individual shell commands produced by LLM agents under bounded path context. Existing safeguards remain limited: generic guardrails do not model shell structure in sufficient detail, always-on LLM judges are relatively costly and variable, and shell parsers do not directly prevent harmful execution. We present CARE (Canonicalization, Attribution, and Resolution Engine), a shell-specific, static-first verifier for individual shell commands before execution. CARE canonicalizes generated commands into stable verification targets, derives deterministic evidence over syntax, command semantics, path context, and provenance-backed risk patterns, and escalates only underdetermined cases to an LLM judge. This design keeps the common case fast, reproducible, and auditable while reserving neural adjudication for borderline commands. On the balanced main split, CARE reaches 85.64% F1 with a 0.91% false-positive rate at 2.32 ms mean latency. When deployed in its static enforcement profile, CARE retains 84.99% F1 at 0.34 ms and reduces realised harm on RedCode-gen to 37.33%. Across external-generalization tests and controlled Docker-sandbox execution, these profiles expose a practical trade-off between benign recovery, false-positive burden, latency, and harm reduction. Overall, command-level shell mediation can reduce dispatch-boundary risk for LLM agents while preserving most benign workflows.

---


### 2. [Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense](https://arxiv.org/abs/2607.21824)

**<font color=#1a73e8>作者：</font>** Yedidel Louck  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users' behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model, through prompt injection and misalignment. We show that the more consequential risks lie one layer down, in the protocol between agents and commerce services. There, vulnerabilities are structural : exploitation is deterministic and ndependent of which model an agent runs, so no model improvement removes them. Across three leading platforms we identify 33 such vulnerabilities, each succeeding deterministically regardless of the deployed model, at a 100% attack-success rate (ASR) wherever live-measured. The same failure modes recur across independently built codebases, a systemic pattern rather than isolated bugs. Three of them chain into an end-to-end payment hijack. We contribute a taxonomy separating these structural attacks from model-dependent semantic ones. We also build two artifacts: AIP-Bench (Agent Interaction Protocol Benchmark), to our knowledge the first deterministic benchmark for agentic commerce security, and PCAT (Protocol-level Commerce Agent Trust), a platform-agnostic defense that drives the structural attack-success rate to zero for four of the five structural classes (RC-1, RC-2, RC-4, RC-5), with RC-3 (observable credential channels) reduced to warn-only, without modifying any platform. Agentic commerce must be secured at the protocol layer, not only the model.

---


### 3. [Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing](https://arxiv.org/abs/2607.21983)

**<font color=#1a73e8>作者：</font>** Deyu Yang, Rundong Wei, Xiaoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ethereum non-fungible tokens (NFTs) implement ownership, transfer, authorization, and metadata operations through smart contracts, making contract vulnerabilities a direct risk to digital assets. Existing static analyzers provide efficient rule-based screening but can struggle with application-specific logic, whereas unconstrained large language model analysis may be distracted by irrelevant code or produce inconsistent outputs. We present a vulnerability-detection method that combines vulnerability-focused code slicing, an ERC-721-oriented knowledge base, and constrained DeepSeek analysis. Regular-expression patterns locate candidate statements for reentrancy, integer overflow or underflow, and timestamp dependence. A structure-aware context-window algorithm then extracts line-numbered code slices. DeepSeek analyzes each slice using explicit decision rules and a fixed output schema, and the resulting records support automated batch processing. On 450 NFT contract samples, the full configuration produced 437 positive labels, corresponding to a reported positive-label rate of 97.1%. Removing the external knowledge base reduced this rate to 87.11%, while analyzing complete contracts without the knowledge base reduced it to 73.78%. These results indicate that focused code context and domain constraints materially affect the detector's reported output.

---


### 4. [PoCEvolve: Generating Proof-of-Concept Exploits from Security Patches with Vulnerability-Aware Prompt Evolution](https://arxiv.org/abs/2607.22076)

**<font color=#1a73e8>作者：</font>** Duc Manh Tran, Ratnadira Widyasari, Ivana Clairine Irsan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ideally, the detailed information about a vulnerability should be made available together with the fixing commit. In practice, however, such details often become available only long after the commit, even when a CVE has already been published. During this window, the patch is already public, so attackers can reverse-engineer it, yet defenders lack the details needed to assess exposure, prioritize, and validate the fix. Executable evidence, such as a proof-of-concept (PoC) exploit, could fill this gap. Prior work has automated PoC generation, but the state-of-the-art approach, PoCGen, assumes that a detailed vulnerability report is already available, which is precisely what is missing during this window. In this paper, we first present an empirical study quantifying the long delay between the fixing commit and the availability of a detailed vulnerability report. We then introduce PoCEvolve, a vulnerability-aware prompt-evolution framework that generates PoCs directly from vulnerability-fixing commits. Given a vulnerability-fixing commit, PoCEvolve synthesizes a corresponding PoC exploit. To learn from unsuccessful generation attempts, PoCEvolve assesses the usefulness of different dimensions of vulnerability-related context, including the inferred vulnerable API and code-coverage information. These assessments guide prompt evolution towards more effective exploit-generation prompts. We evaluate PoCEvolve on this http URL, where PoCEvolve achieves a PoC generation success rate of 58.4%, corresponding to relative improvements of 20.7% over PoCGen and 200.0% over the LLM baseline with GPT-4o-mini. With a recent model, Qwen3.7-Plus, PoCEvolve achieves a higher success rate of 85.3%. When detailed vulnerability reports are available, PoCEvolve achieves a success rate of 71.7%, improving over PoCGen by 11.1%.

---


### 5. [DeFiScreener: Efficient DeFi Attack Pre-screening in Smart Contracts via Historical Case Matching](https://arxiv.org/abs/2607.22184)

**<font color=#1a73e8>作者：</font>** Rui Cao, Shaojing Fan, Zhimei Sui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain and its killer applications, particularly decentralized finance (DeFi), are gaining widespread adoption, with over 5,200 DeFi projects deployed on mainstream blockchains as of January 2026. At the same time, security risks in DeFi are becoming increasingly serious. However, existing DeFi detection tools usually cover only specific attack types, exhibiting severely limited detection coverage.
In this paper, we argue that an effective way to address this gap is to pre-screen vulnerable instances from large volumes of smart contract functions and call sequences. This is motivated by a key phenomenon we term "perilous temporal asymmetry". Inspired by this, we propose DeFiScreener, the first automated pre-screening framework for DeFi attacks that uses historical exploit cases to identify potentially vulnerable functions and call sequences. Given the full source code of a target project, DeFiScreener builds Function Call Trees (FCTs) and generates semantic embeddings for each function using a large language model (LLM), allowing both program structure and function intent to be analyzed together. It then applies a dual-level screening process. At the function level, function embeddings are matched against an Attack Pattern Library of historically exploited functions. At the sequence level, the proposed Attack Pattern Oriented Monte Carlo Tree Search (APO-MCTS) efficiently explores the FCTs and screens vulnerable call sequences. The identified candidates are ultimately passed to an LLM for further interpretive and security analysis.
We empirically evaluate the DeFiScreener over datasets comprising 207 real-world DeFi attack incidents. Experimental results demonstrate that DeFiScreener achieves a remarkable 98.55% recall and 84.30% precision in attack pre-screening.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
